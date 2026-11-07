"""Persistencia en archivos planos para Gestión y Huellitas UdeA.

La clase c_archivos administra cuatro repositorios de texto independientes,
con consecutivos propios, escritura robusta y radicados ASCII alineados.
"""

import json
import os
import textwrap
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    from .validaciones import c_validaciones
except ImportError:  # Ejecución directa de python src/main.py
    from validaciones import c_validaciones


class c_archivos:
    """Administra la lectura, escritura, búsqueda y actualización de las PQRS."""

    ARCHIVOS = {
        "Petición": "Peticion.txt",
        "Queja": "Queja.txt",
        "Reclamo": "Reclamo.txt",
        "Sugerencia": "Sugerencia.txt",
    }
    TRANSICIONES = {
        "Registrada": "En proceso",
        "En proceso": "Solucionada",
    }
    ANCHO_RADICADO = 120

    def __init__(self, carpeta_datos=None):
        """Prepara una ruta de datos clara y configurable para pruebas y ejecución."""
        raiz = Path(__file__).resolve().parent.parent
        self.carpeta_datos = Path(carpeta_datos) if carpeta_datos else raiz / "data"
        self.carpeta_radicados = self.carpeta_datos / "radicados"

    def _tipo_oficial(self, tipo):
        """Normaliza el tipo de solicitud y evita nombres de archivo arbitrarios."""
        opcion = c_validaciones.obtener_opcion(tipo, self.ARCHIVOS.keys())
        if opcion is None:
            raise ValueError("Tipo de solicitud no válido.")
        return opcion

    def _ruta_archivo(self, tipo):
        """Devuelve la ruta segura del archivo plano correspondiente."""
        tipo = self._tipo_oficial(tipo)
        self.carpeta_datos.mkdir(parents=True, exist_ok=True)
        ruta = self.carpeta_datos / self.ARCHIVOS[tipo]
        ruta.touch(exist_ok=True)
        return ruta

    def _leer_archivo(self, tipo):
        """Lee registros JSON por línea y señala datos dañados con ubicación precisa."""
        ruta = self._ruta_archivo(tipo)
        registros = []
        with ruta.open("r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                if not linea.strip():
                    continue
                try:
                    registro = json.loads(linea)
                except json.JSONDecodeError as error:
                    raise ValueError(
                        f"Registro inválido en {ruta.name}, línea {numero_linea}: {error.msg}"
                    ) from error
                if not isinstance(registro, dict):
                    raise ValueError(f"El registro de {ruta.name}, línea {numero_linea}, no es un objeto.")
                registros.append(registro)
        return registros

    def _guardar_archivo(self, tipo, registros):
        """Reescribe el archivo completo mediante un reemplazo temporal seguro."""
        ruta = self._ruta_archivo(tipo)
        temporal = ruta.with_name(ruta.name + ".tmp")
        with temporal.open("w", encoding="utf-8", newline="\n") as archivo:
            for registro in registros:
                archivo.write(json.dumps(registro, ensure_ascii=False) + "\n")
        os.replace(temporal, ruta)

    def listar_por_tipo(self, tipo):
        """Entrega una lista ordenada y completa de un tipo de solicitud."""
        return sorted(self._leer_archivo(tipo), key=lambda registro: int(registro.get("id", 0)))

    def obtener_todos(self):
        """Combina los cuatro archivos y conserva el tipo original de cada registro."""
        registros = [
            registro
            for tipo in self.ARCHIVOS
            for registro in self._leer_archivo(tipo)
        ]
        return sorted(
            registros,
            key=lambda registro: (
                registro.get("fecha_radicacion", ""),
                registro.get("tipo_solicitud", ""),
                int(registro.get("id", 0)),
            ),
        )

    def guardar_pqrs(self, datos):
        """Asigna un consecutivo independiente y guarda una PQRS validada."""
        registro = dict(datos)
        tipo = self._tipo_oficial(registro.get("tipo_solicitud", ""))
        fecha_texto = str(registro.get("fecha_radicacion", "")).strip()
        try:
            fecha_rad = date.fromisoformat(fecha_texto)
        except ValueError as error:
            raise ValueError("La fecha de radicación debe tener formato AAAA-MM-DD.") from error
        if fecha_rad > date.today():
            raise ValueError("La fecha de radicación no puede ser futura.")

        existentes = self._leer_archivo(tipo)
        nuevo_id = max((int(item.get("id", 0)) for item in existentes), default=0) + 1
        registro["id"] = nuevo_id
        registro["tipo_solicitud"] = tipo
        registro["fecha_radicacion"] = fecha_rad.isoformat()
        registro["fecha_maxima_respuesta"] = (fecha_rad + timedelta(days=30)).isoformat()
        registro["estado_peticion"] = "Registrada"
        registro["fecha_respuesta"] = None
        registro.setdefault("fecha_registro_sistema", datetime.now().isoformat(timespec="seconds"))
        existentes.append(registro)
        self._guardar_archivo(tipo, existentes)
        return nuevo_id

    def buscar_pqrs(self, identificador, tipo=None):
        """Busca por consecutivo dentro de su archivo o en todos cuando no se indica tipo."""
        try:
            identificador = int(identificador)
        except (TypeError, ValueError):
            return None

        tipos = [self._tipo_oficial(tipo)] if tipo else list(self.ARCHIVOS)
        for tipo_actual in tipos:
            encontrado = next(
                (registro for registro in self._leer_archivo(tipo_actual)
                 if int(registro.get("id", -1)) == identificador),
                None,
            )
            if encontrado is not None:
                return encontrado
        return None

    def cambiar_estado(self, tipo, identificador, nuevo_estado):
        """Permite únicamente la transición consecutiva y registra la fecha de solución."""
        tipo = self._tipo_oficial(tipo)
        estado_oficial = c_validaciones.obtener_opcion(
            nuevo_estado, c_validaciones.ESTADOS
        )
        if estado_oficial is None:
            raise ValueError("El estado indicado no es válido.")

        registros = self._leer_archivo(tipo)
        registro = next(
            (item for item in registros if int(item.get("id", -1)) == int(identificador)),
            None,
        )
        if registro is None:
            raise ValueError("No se encontró una PQRS con ese consecutivo y tipo.")

        estado_actual = c_validaciones.obtener_opcion(
            registro.get("estado_peticion", "Registrada"), c_validaciones.ESTADOS
        ) or "Registrada"
        estado_siguiente = self.TRANSICIONES.get(estado_actual)
        if estado_siguiente != estado_oficial:
            raise ValueError(
                f"Transición no permitida: {estado_actual} solo puede cambiar a "
                f"{estado_siguiente or 'ningún otro estado'}."
            )

        registro["estado_peticion"] = estado_oficial
        if estado_oficial == "Solucionada":
            registro["fecha_respuesta"] = date.today().isoformat()
        self._guardar_archivo(tipo, registros)
        return registro

    @classmethod
    def _linea_centrada(cls, texto=""):
        """Construye una línea centrada con ancho exterior exacto de 120 columnas."""
        interior = str(texto)[: cls.ANCHO_RADICADO - 2].center(cls.ANCHO_RADICADO - 2)
        return "|" + interior + "|"

    @classmethod
    def _lineas_campo(cls, etiqueta, valor):
        """Ajusta campos largos en líneas legibles sin romper el marco ASCII."""
        texto = f"{etiqueta}: {valor if valor not in (None, '') else 'N/A'}"
        fragmentos = textwrap.wrap(
            texto,
            width=116,
            break_long_words=True,
            break_on_hyphens=False,
        ) or [""]
        return ["| " + fragmento.ljust(116) + " |" for fragmento in fragmentos]

    @classmethod
    def construir_radicado(cls, registro):
        """Genera un comprobante completo, claro y de 120 caracteres por línea."""
        borde = "+" + "-" * (cls.ANCHO_RADICADO - 2) + "+"
        lineas = [
            borde,
            cls._linea_centrada("GESTIÓN Y HUELLITAS UDEA"),
            cls._linea_centrada("COMPROBANTE DE RADICACIÓN DE PQRS"),
            borde,
            cls._linea_centrada("DATOS DEL RADICADO"),
        ]

        campos_radicado = [
            ("Consecutivo", f"#{int(registro.get('id', 0)):06d}"),
            ("Tipo de solicitud", registro.get("tipo_solicitud")),
            ("Fecha de radicación", registro.get("fecha_radicacion")),
            ("Fecha/hora de registro en sistema", registro.get("fecha_registro_sistema")),
            ("Fecha máxima de respuesta", registro.get("fecha_maxima_respuesta")),
            ("Estado", registro.get("estado_peticion", "Registrada")),
        ]
        for etiqueta, valor in campos_radicado:
            lineas.extend(cls._lineas_campo(etiqueta, valor))

        lineas.extend([borde, cls._linea_centrada("DATOS DEL SOLICITANTE")])
        campos_solicitante = [
            ("Nombre completo", registro.get("nombre_completo")),
            ("Documento", f"{registro.get('tipo_documento', '')} {registro.get('numero_documento', '')}".strip()),
            ("Teléfono", f"{registro.get('telefono_contacto', '')} ({registro.get('tipo_telefono', '')})".strip()),
            ("Correo electrónico", registro.get("correo_electronico")),
            ("Dirección", registro.get("direccion") or "N/A"),
        ]
        for etiqueta, valor in campos_solicitante:
            lineas.extend(cls._lineas_campo(etiqueta, valor))

        lineas.extend([borde, cls._linea_centrada("CLASIFICACIÓN DE LA SOLICITUD")])
        campos_clasificacion = [
            ("Canal de recepción", registro.get("canal_recepcion")),
            ("Tipo de mascota", registro.get("tipo_mascota")),
            ("Campus relacionado", registro.get("campus_relacionado")),
            ("Asunto", registro.get("asunto_titulo")),
        ]
        for etiqueta, valor in campos_clasificacion:
            lineas.extend(cls._lineas_campo(etiqueta, valor))

        lineas.extend([
            borde,
            cls._linea_centrada("Conserve este comprobante para consultar el estado de su solicitud."),
            borde,
        ])
        if any(len(linea) != cls.ANCHO_RADICADO for linea in lineas):
            raise AssertionError("El radicado contiene una línea con ancho diferente de 120.")
        return "\n".join(lineas) + "\n"

    def generar_radicado(self, registro):
        """Guarda el radicado TXT en una carpeta dedicada dentro de data/."""
        self.carpeta_radicados.mkdir(parents=True, exist_ok=True)
        tipo = self._tipo_oficial(registro.get("tipo_solicitud", ""))
        nombre = f"{self.ARCHIVOS[tipo][:-4]}_{int(registro.get('id', 0)):06d}.txt"
        ruta = self.carpeta_radicados / nombre
        contenido = self.construir_radicado(registro)
        ruta.write_text(contenido, encoding="utf-8")
        return ruta
