"""Validaciones centralizadas para Gestión y Huellitas UdeA.

La clase c_validaciones reúne reglas claras, estrictas y reutilizables para
los datos del solicitante, la PQRS, la mascota y el campus relacionado.
"""

import re
import unicodedata
from datetime import date, datetime


class c_validaciones:
    """Conjunto organizado de validaciones sencillas y consistentes."""

    TIPOS_DOCUMENTO = ("CC", "TI", "CE", "PP", "NIT")
    TIPOS_TELEFONO = ("Celular", "Fijo", "Corporativo", "Otro")
    TIPOS_SOLICITUD = ("Petición", "Queja", "Reclamo", "Sugerencia")
    CANALES_RECEPCION = (
        "Presencial",
        "Correo electrónico",
        "Página web",
        "Teléfono",
        "Redes sociales",
        "Otro",
    )
    TIPOS_MASCOTA = ("Perro", "Gato")
    ESTADOS = ("Registrada", "En proceso", "Solucionada")
    CAMPUS = (
        "Campus Medellín - Ciudad Universitaria",
        "Campus Medellín - Ciudadela Robledo",
        "Campus en el Área de la salud",
        "Campus Medellín - Sede de Posgrado",
        "Campus Medellín - Edificio San Ignacio",
        "Campus Medellín - Antigua Escuela de Derecho",
        "Campus Medellín - Edificio Antioquia",
        "Campus Medellín - Casas Patrimoniales",
        "Campus Medellín - Edificio de Extensión",
    )

    @staticmethod
    def _clave(valor):
        """Genera una clave uniforme, legible y sin tildes para comparar opciones."""
        texto = unicodedata.normalize("NFD", str(valor or "").strip())
        sin_tildes = "".join(caracter for caracter in texto if unicodedata.category(caracter) != "Mn")
        return " ".join(sin_tildes.casefold().split())

    @classmethod
    def obtener_opcion(cls, valor, opciones):
        """Devuelve la opción oficial equivalente o None cuando no existe."""
        clave = cls._clave(valor)
        return next((opcion for opcion in opciones if cls._clave(opcion) == clave), None)

    @classmethod
    def validar_nombre(cls, nombre):
        """Comprueba un nombre completo obligatorio, claro y sin dígitos."""
        if not isinstance(nombre, str):
            return False
        nombre = nombre.strip()
        patron = r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:[ '\-][A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*"
        return 3 <= len(nombre) <= 100 and re.fullmatch(patron, nombre) is not None

    @classmethod
    def validar_tipo_documento(cls, tipo):
        return cls.obtener_opcion(str(tipo).upper(), cls.TIPOS_DOCUMENTO) is not None

    @staticmethod
    def validar_numero_documento(numero):
        numero = str(numero or "").strip()
        return re.fullmatch(r"[0-9]{3,15}", numero) is not None

    @classmethod
    def validar_tipo_telefono(cls, tipo):
        return cls.obtener_opcion(tipo, cls.TIPOS_TELEFONO) is not None

    @staticmethod
    def validar_telefono(telefono, tipo=None):
        """Exige diez dígitos para todos los tipos, de acuerdo con la rúbrica."""
        telefono = str(telefono or "").strip()
        return re.fullmatch(r"[0-9]{10}", telefono) is not None

    @staticmethod
    def validar_correo(correo):
        """Verifica una dirección de correo sencilla, completa y de longitud válida."""
        if not isinstance(correo, str):
            return False
        correo = correo.strip()
        if len(correo) > 254 or correo.count("@") != 1 or " " in correo:
            return False
        local, dominio = correo.split("@")
        if not local or len(local) > 64 or not dominio or "." not in dominio:
            return False
        if local.startswith(".") or local.endswith(".") or ".." in correo:
            return False
        patron_local = r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
        if re.fullmatch(patron_local, local) is None:
            return False
        etiquetas = dominio.split(".")
        if len(etiquetas) < 2:
            return False
        patron_etiqueta = r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
        return all(re.fullmatch(patron_etiqueta, etiqueta) for etiqueta in etiquetas) and len(etiquetas[-1]) >= 2

    @classmethod
    def validar_direccion(cls, direccion):
        """Permite dirección opcional y comprueba longitud y caracteres permitidos."""
        if direccion is None or not str(direccion).strip():
            return True
        direccion = str(direccion).strip()
        patron = r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 #./\-]+"
        return 5 <= len(direccion) <= 200 and re.fullmatch(patron, direccion) is not None

    @classmethod
    def validar_tipo_solicitud(cls, tipo):
        return cls.obtener_opcion(tipo, cls.TIPOS_SOLICITUD) is not None

    @classmethod
    def validar_fecha_radicacion(cls, fecha):
        """Acepta ISO AAAA-MM-DD y rechaza fechas futuras o imposibles."""
        if isinstance(fecha, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha.strip()) is None:
            return False
        try:
            fecha_valida = fecha.date() if isinstance(fecha, datetime) else (
                fecha if isinstance(fecha, date) else date.fromisoformat(str(fecha).strip())
            )
            return fecha_valida <= date.today()
        except (TypeError, ValueError):
            return False

    @classmethod
    def validar_canal(cls, canal):
        return cls.obtener_opcion(canal, cls.CANALES_RECEPCION) is not None

    @staticmethod
    def validar_asunto(asunto):
        """Acepta un asunto breve y descriptivo con puntuación básica."""
        if not isinstance(asunto, str):
            return False
        asunto = asunto.strip()
        patron = r"""[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 .,;:!?¡¿()'"#/-]+"""
        return 5 <= len(asunto) <= 150 and re.fullmatch(patron, asunto) is not None

    @staticmethod
    def validar_descripcion(descripcion):
        descripcion = str(descripcion or "").strip()
        return 20 <= len(descripcion) <= 2000

    @classmethod
    def validar_tipo_mascota(cls, mascota):
        return cls.obtener_opcion(mascota, cls.TIPOS_MASCOTA) is not None

    @classmethod
    def validar_campus(cls, campus):
        return cls.obtener_opcion(campus, cls.CAMPUS) is not None

    @classmethod
    def validar_estado(cls, estado):
        return cls.obtener_opcion(estado, cls.ESTADOS) is not None


# Funciones públicas de compatibilidad para módulos que prefieran importar funciones.
validar_nombre = c_validaciones.validar_nombre
validar_tipo_documento = c_validaciones.validar_tipo_documento
validar_numero_documento = c_validaciones.validar_numero_documento
validar_tipo_telefono = c_validaciones.validar_tipo_telefono
validar_telefono = c_validaciones.validar_telefono
validar_correo = c_validaciones.validar_correo
validar_direccion = c_validaciones.validar_direccion
validar_tipo_solicitud = c_validaciones.validar_tipo_solicitud
validar_fecha_radicacion = c_validaciones.validar_fecha_radicacion
validar_canal = c_validaciones.validar_canal
validar_asunto = c_validaciones.validar_asunto
validar_descripcion = c_validaciones.validar_descripcion
validar_tipo_mascota = c_validaciones.validar_tipo_mascota
validar_campus = c_validaciones.validar_campus
validar_estado = c_validaciones.validar_estado
