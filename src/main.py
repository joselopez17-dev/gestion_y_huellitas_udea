"""Punto de entrada del programa Gestión y Huellitas UdeA.

La clase c_main organiza un menú de consola claro, sencillo y consistente
para registrar, consultar, actualizar y analizar las solicitudes PQRS.
"""

import sys

from .archivos import c_archivos
from .reportes import c_reportes
from .reglas import c_reglas


class c_main:
    """Coordina la interacción del usuario con los módulos del sistema."""

    def __init__(self):
        self.archivos = c_archivos()
        self.reportes = c_reportes(self.archivos)

    @staticmethod
    def _pedir_validado(mensaje, validador, error, transformar=None):
        """Solicita un dato hasta obtener una entrada válida y limpia."""
        while True:
            valor = input(mensaje).strip()
            if validador(valor):
                return transformar(valor) if transformar else valor
            print(f"⚠️ {error}")

    @staticmethod
    def _pedir_opcion(mensaje, opciones, error="Seleccione una opción de la lista."):
        """Convierte entradas flexibles en opciones oficiales y uniformes."""
        while True:
            valor = input(mensaje).strip()
            opcion = c_reglas.obtener_opcion(valor, opciones)
            if opcion is not None:
                return opcion
            print(f"⚠️ {error}")

    def _capturar_datos_pqrs(self):
        """Recopila datos personales y datos completos de la solicitud."""
        print("\n📝 REGISTRO DE NUEVA PQRS")
        print("-" * 48)

        nombre = self._pedir_validado(
            "Nombre completo: ",
            c_reglas.validar_nombre,
            "Use de 3 a 100 letras; se permiten tildes, espacios, apóstrofes y guiones.",
        )
        tipo_documento = self._pedir_validado(
            "Tipo de documento (CC, TI, CE, PP, NIT): ",
            c_reglas.validar_tipo_documento,
            "Tipo de documento no válido.",
            transformar=lambda valor: valor.upper(),
        )
        numero_documento = self._pedir_validado(
            "Número de documento (3 a 15 dígitos): ",
            c_reglas.validar_numero_documento,
            "Ingrese únicamente entre 3 y 15 dígitos.",
        )
        tipo_telefono = self._pedir_opcion(
            "Tipo de teléfono (Celular, Fijo, Corporativo, Otro): ",
            c_reglas.TIPOS_TELEFONO,
        )
        telefono = self._pedir_validado(
            "Teléfono de contacto (10 dígitos): ",
            c_reglas.validar_telefono,
            "Ingrese exactamente 10 dígitos numéricos.",
        )
        correo = self._pedir_validado(
            "Correo electrónico: ",
            c_reglas.validar_correo,
            "Ingrese un correo válido, por ejemplo usuario@correo.com.",
        )

        while True:
            direccion = input("Dirección (opcional, Enter para omitir): ").strip()
            if c_reglas.validar_direccion(direccion):
                break
            print("⚠️ La dirección debe tener entre 5 y 200 caracteres permitidos.")

        tipo_solicitud = self._pedir_opcion(
            "Tipo de solicitud (Petición, Queja, Reclamo, Sugerencia): ",
            c_reglas.TIPOS_SOLICITUD,
        )
        fecha_radicacion = self._pedir_validado(
            "Fecha de radicación (AAAA-MM-DD): ",
            c_reglas.validar_fecha_radicacion,
            "Use una fecha válida en formato AAAA-MM-DD que no sea futura.",
        )
        canal = self._pedir_opcion(
            "Canal (Presencial, Correo electrónico, Página web, Teléfono, Redes sociales, Otro): ",
            c_reglas.CANALES_RECEPCION,
        )
        asunto = self._pedir_validado(
            "Asunto (5 a 150 caracteres): ",
            c_reglas.validar_asunto,
            "El asunto debe tener entre 5 y 150 caracteres.",
        )
        descripcion = self._pedir_validado(
            "Descripción detallada (20 a 2000 caracteres): ",
            c_reglas.validar_descripcion,
            "La descripción debe tener entre 20 y 2000 caracteres.",
        )
        mascota = self._pedir_opcion(
            "Tipo de mascota (Perro o Gato): ",
            c_reglas.TIPOS_MASCOTA,
        )
        campus = self._pedir_opcion(
            "Campus relacionado (escriba el nombre completo): ",
            c_reglas.CAMPUS,
            "El campus debe coincidir con uno de los nueve campus permitidos.",
        )

        return {
            "nombre_completo": nombre,
            "tipo_documento": tipo_documento,
            "numero_documento": numero_documento,
            "tipo_telefono": tipo_telefono,
            "telefono_contacto": telefono,
            "correo_electronico": correo,
            "direccion": direccion,
            "tipo_solicitud": tipo_solicitud,
            "fecha_radicacion": fecha_radicacion,
            "canal_recepcion": canal,
            "asunto_titulo": asunto,
            "descripcion_detallada": descripcion,
            "tipo_mascota": mascota,
            "campus_relacionado": campus,
        }

    def registrar_pqrs(self):
        """Guarda una solicitud nueva y genera su comprobante TXT."""
        try:
            datos = self._capturar_datos_pqrs()
            nuevo_id = self.archivos.guardar_pqrs(datos)
            registro = self.archivos.buscar_pqrs(nuevo_id, datos["tipo_solicitud"])
            if registro is None:
                raise ValueError("El registro se guardó, pero no fue posible recuperarlo.")
        except (OSError, ValueError) as error:
            print(f"❌ No fue posible guardar la PQRS: {error}")
            return

        # El comprobante se genera después de guardar. Un fallo aquí no debe
        # hacer creer al usuario que el registro se perdió ni inducir duplicados.
        try:
            ruta = self.archivos.generar_radicado(registro)
        except OSError as error:
            print("\n✅ La PQRS quedó registrada correctamente.")
            print(f"Consecutivo asignado: {nuevo_id:06d}")
            print(f"Fecha máxima de respuesta: {registro['fecha_maxima_respuesta']}")
            print(f"⚠️ No se pudo guardar el comprobante TXT: {error}")
            return

        print("\n✅ PQRS registrada correctamente.")
        print(f"Consecutivo asignado: {nuevo_id:06d}")
        print(f"Fecha máxima de respuesta: {registro['fecha_maxima_respuesta']}")
        print(f"Radicado guardado en: {ruta}")
        print("\n" + self.archivos.construir_radicado(registro))

    @staticmethod
    def _mostrar_resumen_registros(registros):
        """Presenta una lista compacta y legible de las solicitudes existentes."""
        if not registros:
            print("No hay PQRS registradas.")
            return
        print("\nREGISTROS ENCONTRADOS")
        print("-" * 96)
        for registro in registros:
            print(
                f"ID {int(registro.get('id', 0)):06d} | "
                f"{registro.get('tipo_solicitud', 'N/A'):<12} | "
                f"{registro.get('estado_peticion', 'N/A'):<12} | "
                f"{registro.get('fecha_radicacion', 'N/A')} | "
                f"{registro.get('asunto_titulo', 'Sin asunto')}"
            )

    def consultar_pqrs(self):
        """Lista registros o localiza un radicado individual por tipo e ID."""
        opciones = (*c_archivos.ARCHIVOS.keys(), "Todas")
        tipo = self._pedir_opcion(
            "\nTipo de PQRS (Petición, Queja, Reclamo, Sugerencia o Todas): ",
            opciones,
        )

        if tipo == "Todas":
            registros = self.archivos.obtener_todos()
            self._mostrar_resumen_registros(registros)
            if not registros:
                return
            tipo = self._pedir_opcion(
                "Tipo de la PQRS que desea abrir: ",
                c_archivos.ARCHIVOS.keys(),
            )
        else:
            self._mostrar_resumen_registros(self.archivos.listar_por_tipo(tipo))

        identificador = self._pedir_validado(
            "Ingrese el consecutivo que desea consultar: ",
            lambda valor: valor.isdigit() and int(valor) > 0,
            "Ingrese un consecutivo entero positivo.",
            transformar=int,
        )
        registro = self.archivos.buscar_pqrs(identificador, tipo)
        if registro is None:
            print("⚠️ No se encontró una PQRS con ese tipo y consecutivo.")
            return

        try:
            ruta = self.archivos.generar_radicado(registro)
            print("\n" + self.archivos.construir_radicado(registro))
            print(f"Comprobante disponible en: {ruta}")
        except OSError as error:
            print(f"❌ No fue posible generar el radicado: {error}")

    def cambiar_estado_pqrs(self):
        """Actualiza el estado y diferencia el cambio del refresco del radicado."""
        tipo = self._pedir_opcion(
            "\nTipo de PQRS (Petición, Queja, Reclamo, Sugerencia): ",
            c_archivos.ARCHIVOS.keys(),
        )
        identificador = self._pedir_validado(
            "Consecutivo de la PQRS: ",
            lambda valor: valor.isdigit() and int(valor) > 0,
            "Ingrese un consecutivo entero positivo.",
            transformar=int,
        )
        registro = self.archivos.buscar_pqrs(identificador, tipo)
        if registro is None:
            print("⚠️ No se encontró una PQRS con ese consecutivo.")
            return

        print(f"Estado actual: {registro.get('estado_peticion', 'Registrada')}")
        nuevo_estado = self._pedir_opcion(
            "Nuevo estado (En proceso o Solucionada): ",
            ("En proceso", "Solucionada"),
        )
        try:
            actualizado = self.archivos.cambiar_estado(tipo, identificador, nuevo_estado)
        except (OSError, ValueError) as error:
            print(f"⚠️ No se pudo cambiar el estado: {error}")
            return

        print(f"✅ Estado actualizado a: {actualizado['estado_peticion']}")
        if actualizado.get("fecha_respuesta"):
            print(f"Fecha de respuesta registrada: {actualizado['fecha_respuesta']}")

        # Si no se puede regenerar el comprobante, el cambio de estado ya quedó guardado.
        try:
            ruta = self.archivos.generar_radicado(actualizado)
            print(f"Radicado actualizado: {ruta}")
        except OSError as error:
            print(f"⚠️ El estado sí se actualizó, pero no se pudo actualizar el radicado: {error}")

    def mostrar_estadisticas(self):
        """Muestra el indicador obligatorio y cinco estadísticas complementarias."""
        print("\n📊 ESTADÍSTICAS DE GESTIÓN")
        print("=" * 56)

        promedio = self.reportes.calcular_promedio_dias_respuesta()
        if promedio is None:
            print("1. Promedio de días de respuesta: Sin datos de PQRS solucionadas.")
        else:
            print(f"1. Promedio de días de respuesta: {promedio} días")
        print("   (Se calcula con PQRS solucionadas que tienen fecha de respuesta.)")

        print("\n2. Cantidad por tipo de solicitud:")
        for tipo, cantidad in self.reportes.cantidad_por_tipo_solicitud().items():
            print(f"   - {tipo}: {cantidad}")

        print("\n3. Cantidad por tipo de mascota:")
        for mascota, cantidad in self.reportes.cantidad_por_tipo_mascota().items():
            print(f"   - {mascota}: {cantidad}")

        print("\n4. Distribución por estado:")
        for estado, cantidad in self.reportes.cantidad_por_estado().items():
            print(f"   - {estado}: {cantidad}")

        antigua = self.reportes.pqrs_mas_antigua_activa()
        print("\n5. PQRS activa más antigua:")
        if antigua:
            print(
                f"   - {antigua.get('tipo_solicitud')} #{int(antigua.get('id', 0)):06d}, "
                f"radicada el {antigua.get('fecha_radicacion')}: "
                f"{antigua.get('asunto_titulo', 'Sin asunto')}"
            )
        else:
            print("   - No hay PQRS activas.")

        proximas = self.reportes.pqrs_proximas_a_vencer()
        print("\n6. PQRS vencidas o próximas a vencer (5 días o menos):")
        if proximas:
            for registro in proximas:
                restantes = registro["dias_restantes"]
                detalle = "vencida" if restantes < 0 else (
                    "vence hoy" if restantes == 0 else f"vence en {restantes} día(s)"
                )
                print(
                    f"   - {registro.get('tipo_solicitud')} "
                    f"#{int(registro.get('id', 0)):06d}: {detalle} "
                    f"(límite {registro.get('fecha_maxima_respuesta')})"
                )
        else:
            print("   - No hay PQRS vencidas ni próximas a vencer.")

    def ejecutar(self):
        """Mantiene el menú principal activo hasta que el usuario decida salir."""
        while True:
            print("\n" + "=" * 56)
            print("🐾  GESTIÓN Y HUELLITAS UDEA  🐾".center(56))
            print("Sistema de gestión de PQRS".center(56))
            print("=" * 56)
            print("1. Registrar PQRS")
            print("2. Consultar PQRS")
            print("3. Registrar cambio en PQRS")
            print("4. Estadísticas")
            print("5. Salir")

            opcion = input("\nSeleccione una opción (1-5): ").strip()
            if opcion == "1":
                self.registrar_pqrs()
            elif opcion == "2":
                try:
                    self.consultar_pqrs()
                except (OSError, ValueError, KeyError) as error:
                    print(f"❌ No fue posible consultar los registros: {error}")
            elif opcion == "3":
                self.cambiar_estado_pqrs()
            elif opcion == "4":
                try:
                    self.mostrar_estadisticas()
                except (OSError, ValueError, KeyError) as error:
                    print(f"❌ No fue posible calcular los reportes: {error}")
            elif opcion == "5":
                print("\n¡Gracias por utilizar Gestión y Huellitas UdeA! 🐾")
                break
            else:
                print("⚠️ Opción inválida. Ingrese un número entre 1 y 5.")


def main():
    """Construye y ejecuta el gestor principal de la aplicación."""
    # La salida UTF-8 evita errores al mostrar tildes y símbolos en Windows.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    try:
        c_main().ejecutar()
    except KeyboardInterrupt:
        print("\n\nEjecución interrumpida por el usuario.")


if __name__ == "__main__":
    main()
