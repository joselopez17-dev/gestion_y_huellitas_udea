# Validaciones de los datos.

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
Devuelve la opción oficial equivalente o None cuando no existe."""
        clave = cls._clave(valor)
        coincidencia = next((opcion for opcion in opciones if cls._clave(opcion) == clave), None)
        if coincidencia is not None:
            return coincidencia

        if tuple(opciones) == cls.CAMPUS:
            alias_campus = {
                "campus central": cls.CAMPUS[0],
                "campus principal": cls.CAMPUS[0],
                "ciudad universitaria": cls.CAMPUS[0],
                "medellin ciudad universitaria": cls.CAMPUS[0],
                "campus medellin ciudad universitaria": cls.CAMPUS[0],
                "robledo": cls.CAMPUS[1],
                "ciudadela robledo": cls.CAMPUS[1],
                "campus robledo": cls.CAMPUS[1],
                "area de la salud": cls.CAMPUS[2],
                "campus area de la salud": cls.CAMPUS[2],
                "sede de posgrado": cls.CAMPUS[3],
                "san ignacio": cls.CAMPUS[4],
                "edificio san ignacio": cls.CAMPUS[4],
                "antigua escuela de derecho": cls.CAMPUS[5],
                "edificio antioquia": cls.CAMPUS[6],
                "casas patrimoniales": cls.CAMPUS[7],
                "edificio de extension": cls.CAMPUS[8],
            }
            return alias_campus.get(clave)
        return None

    @classmethod
    def validar_nombre(cls, nombre):
Exige diez dígitos para todos los tipos, de acuerdo con la rúbrica."""
        telefono = str(telefono or "").strip()
        return re.fullmatch(r"[0-9]{10}", telefono) is not None

    @staticmethod
    def validar_correo(correo):
Permite dirección opcional y comprueba longitud y caracteres permitidos."""
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
Acepta un asunto breve y descriptivo con puntuación básica."""
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
