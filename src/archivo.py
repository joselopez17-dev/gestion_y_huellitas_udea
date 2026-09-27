# MÓDULO DE ARCHIVOS - GESTIÓN Y HUELLITAS UDEA
import os
from datetime import datetime, timedelta
# Ruta donde se almacenarán los archivos planos
RUTA_DATA = "data/"
def obtener_nombre_archivo(tipo_solicitud):
    Retorna la ruta del archivo plano según el tipo de solicitud.
    tipo = tipo_solicitud.capitalize()
    return f"{RUTA_DATA}{tipo}.txt"
def obtener_siguiente_id(ruta_archivo):
  Lee el archivo plano y calcula el siguiente ID auto-incremental (comenzando en 1).
    if not os.path.exists(ruta_archivo):
        return 1
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                return 1
            # Tomar la última línea guardada y extraer el primer dato (ID)
            ultima_linea = lineas[-1].strip()
            if ultima_linea:
                datos = ultima_linea.split("|")
                siguiente_id = int(datos[0]) + 1
                return siguiente_id
            return 1
    except Exception:
        return 1
def guardar_pqrs(datos):
    Guarda una nueva PQRS en su archivo plano correspondiente.
    Calcula de forma automática la fecha máxima de respuesta (+30 días).
    ruta_archivo = obtener_nombre_archivo(datos["tipo_solicitud"])
    # Generar ID consecutivo independiente
    nuevo_id = obtener_siguiente_id(ruta_archivo)
    datos["id"] = nuevo_id
    # Calcular Fecha Máxima de Respuesta (Fecha de radicación + 30 días)
    fecha_rad = datetime.strptime(datos["fecha_radicacion"], "%Y-%m-%d")
    fecha_max = fecha_rad + timedelta(days=30)
    datos["fecha_maxima_respuesta"] = fecha_max.strftime("%Y-%m-%d")
    # Formatear todos los campos delimitados por el carácter "|"
    linea = (
        f"{datos['id']}|{datos['nombre_completo']}|{datos['tipo_documento']}|"
        f"{datos['numero_documento']}|{datos['tipo_telefono']}|{datos['telefono_contacto']}|"
        f"{datos['correo_electronico']}|{datos['direccion']}|{datos['tipo_solicitud']}|"
        f"{datos['fecha_radicacion']}|{datos['canal_recepcion']}|{datos['asunto_titulo']}|"
        f"{datos['descripcion_detallada']}|{datos['tipo_mascota']}|{datos['campus_relacionado']}|"
        f"{datos['fecha_maxima_respuesta']}|{datos['estado_peticion']}\n"
    )
    # Crear la carpeta data si no existe
    if not os.path.exists(RUTA_DATA):
        os.makedirs(RUTA_DATA)
    # Añadir el registro al final del archivo plano
    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(linea)
    return nuevo_id
