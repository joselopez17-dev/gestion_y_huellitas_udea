# Manejo de los archivos de PQRS.

import json
import os
import textwrap
from datetime import date, datetime, timedelta
from pathlib import Path

from .validaciones import c_validaciones

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
Normaliza el tipo de solicitud y evita nombres de archivo arbitrarios."""
        opcion = c_validaciones.obtener_opcion(tipo, self.ARCHIVOS.keys())
        if opcion is None:
            raise ValueError("Tipo de solicitud no válido.")
        return opcion

    def _ruta_archivo(self, tipo):
Lee registros JSON por línea y señala datos dañados con ubicación precisa."""
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
Entrega una lista ordenada y completa de un tipo de solicitud."""
        return sorted(self._leer_archivo(tipo), key=lambda registro: int(registro.get("id", 0)))

    def obtener_todos(self):
Asigna un consecutivo independiente y guarda una PQRS validada."""
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
Permite únicamente la transición consecutiva y registra la fecha de solución."""
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
Ajusta campos largos en líneas legibles sin romper el marco ASCII."""
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
Guarda el radicado TXT en una carpeta dedicada dentro de data/."""
        self.carpeta_radicados.mkdir(parents=True, exist_ok=True)
        tipo = self._tipo_oficial(registro.get("tipo_solicitud", ""))
        nombre = f"{self.ARCHIVOS[tipo][:-4]}_{int(registro.get('id', 0)):06d}.txt"
        ruta = self.carpeta_radicados / nombre
        contenido = self.construir_radicado(registro)
        ruta.write_text(contenido, encoding="utf-8")
        return ruta
