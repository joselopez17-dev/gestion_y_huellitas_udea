# MÓDULO DE REPORTES Y ESTADÍSTICAS - GESTIÓN Y HUELLITAS UDEA
import os
from datetime import datetime

RUTA_DATA = "data/"
ARCHIVOS_PQRS = ["Peticion.txt", "Queja.txt", "Reclamo.txt", "Sugerencia.txt"]
def cargar_todas_las_pqrs():
    Lee todos los archivos planos y retorna una lista con todos los registros formateados.
    todas_pqrs = []
    for archivo_nombre in ARCHIVOS_PQRS:
        ruta = os.path.join(RUTA_DATA, archivo_nombre)
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                lineas = f.readlines()
                for linea in lineas:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split("|")
                        if len(datos) >= 17:
                            registro = {
                                "id": datos[0],
                                "nombre": datos[1],
                                "tipo_doc": datos[2],
                                "num_doc": datos[3],
                                "tipo_tel": datos[4],
                                "telefono": datos[5],
                                "correo": datos[6],
                                "direccion": datos[7],
                                "tipo_solicitud": datos[8],
                                "fecha_radicacion": datos[9],
                                "canal": datos[10],
                                "asunto": datos[11],
                                "descripcion": datos[12],
                                "tipo_mascota": datos[13],
                                "campus": datos[14],
                                "fecha_maxima": datos[15],
                                "estado": datos[16]
                            }
                            todas_pqrs.append(registro)
    return todas_pqrs
# 1. ESTADÍSTICA OBLIGATORIA
def calcular_promedio_dias_respuesta():
    Calcula el tiempo promedio en días asignados para la respuesta (30 días estándar).
    registros = cargar_todas_las_pqrs()
    if not registros:
        return 0
    suma_dias = 0
    total_registros = len(registros)
    for reg in registros:
        f_inicio = datetime.strptime(reg["fecha_radicacion"], "%Y-%m-%d")
        f_max = datetime.strptime(reg["fecha_maxima"], "%Y-%m-%d")
        diferencia = (f_max - f_inicio).days
        suma_dias += diferencia
    promedio = suma_dias // total_registros  # Valor entero
    return promedio
# 5 ESTADÍSTICAS ADICIONALES
def cantidad_por_tipo_solicitud():
    Estadística Adicional 1: Cantidad de PQRS registradas por cada tipo.
    registros = cargar_todas_las_pqrs()
    conteo = {"Peticion": 0, "Queja": 0, "Reclamo": 0, "Sugerencia": 0} 
    for reg in registros:
        tipo = reg["tipo_solicitud"].capitalize()
        if tipo in conteo:
            conteo[tipo] += 1 
    return conteo
def cantidad_por_tipo_mascota():
    Estadística Adicional 2: Conteo de solicitudes para Perro vs Gato.
    registros = cargar_todas_las_pqrs()
    conteo = {"Perro": 0, "Gato": 0}
    for reg in registros:
        mascota = reg["tipo_mascota"].capitalize()
        if mascota in conteo:
            conteo[mascota] += 1
    return conteo
def cantidad_por_estado():
    Estadística Adicional 3: Distribución de solicitudes según su estado.
    registros = cargar_todas_las_pqrs()
    conteo = {"Registrada": 0, "En proceso": 0, "Solucionada": 0}
    for reg in registros:
        estado = reg["estado"]
        if estado in conteo:
            conteo[estado] += 1        
    return conteo
def campus_con_mas_pqrs():
    Estadística Adicional 4: Determina el campus con mayor número de reportes.
    registros = cargar_todas_las_pqrs()
    if not registros:
        return "Sin registros", 0
    conteo_campus = {}
    for reg in registros:
        campus = reg["campus"]
        if campus in conteo_campus:
            conteo_campus[campus] += 1
        else:
            conteo_campus[campus] = 1
    campus_max = max(conteo_campus, key=conteo_campus.get)
    return campus_max, conteo_campus[campus_max]
def pqrs_proximas_a_vencer():
    Estadística Adicional 5: Cantidad de PQRS activas que vencen en 5 días o menos.
    registros = cargar_todas_las_pqrs()
    fecha_actual = datetime.now()
    proximas_a_vencer = 0
    for reg in registros:
        if reg["estado"] != "Solucionada":
            f_max = datetime.strptime(reg["fecha_maxima"], "%Y-%m-%d")
            dias_restantes = (f_max - fecha_actual).days
            if 0 <= dias_restantes <= 5:
                proximas_a_vencer += 1
    return proximas_a_vencer
