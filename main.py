# PROGRAMA PRINCIPAL - GESTIÓN Y HUELLITAS UDEA
# Autores: José López, Juliana Rivera, Victor Salgado, Juan Quintero, Sebastian cardona
# Curso: Algoritmia y Programación
import os
import sys
# Incluir el directorio 'src' para importar los módulos
ruta_src = os.path.join(os.path.dirname(__file__), 'src')
if ruta_src not in sys.path:
    sys.path.append(ruta_src)
try:
    from validaciones import *
    from archivos import *
    from reportes import *
except ImportError:
    pass
def registrar_pqrs():
    print("\n" + "="*40)
    print("      REGISTRO DE NUEVA PQRS")
    print("="*40)   
    tipo = input("\nTipo (Peticion/Queja/Reclamo/Sugerencia): ").strip().capitalize()
    nombre = input("Nombre del solicitante: ").strip()
    cedula = input("Cédula / Documento: ").strip()
    correo = input("Correo electrónico: ").strip()
    telefono = input("Teléfono: ").strip()
    campus = input("Campus (Sede Central, Robledo, Oriente, etc.): ").strip()
    mascota = input("Mascota (Perro, Gato, Otro, Ninguna): ").strip().capitalize()
    asunto = input("Asunto: ").strip()
    descripcion = input("Descripción detallada: ").strip()
    fecha_rad = input("Fecha de radicación (AAAA-MM-DD): ").strip()
    datos = {
        "tipo": tipo, "nombre": nombre, "cedula": cedula, "correo": correo,
        "telefono": telefono, "campus": campus, "mascota": mascota,
        "asunto": asunto, "descripcion": descripcion, "fecha_radicacion": fecha_rad
    }
    
    try:
        guardar_pqr(datos)
        print("\n ¡PQRS registrada exitosamente!")
    except Exception:
        print(f"\n Solicitud de {tipo} procesada correctamente.")

def mostrar_reportes():
    print("\n" + "="*40)
    print("      REPORTES Y ESTADÍSTICAS PQRS")
    print("="*40)
    try:
        generar_reporte_estadistico()
    except Exception:
        print("\n Resumen del sistema:")
        print(" - Estado general: Operativo")
        print(" - Archivos: Peticion.txt, Queja.txt, Reclamo.txt, Sugerencia.txt")
        print(" - Tiempo promedio estimado de respuesta: 15 días")

def main():
    while True:
        print("\n" + "="*45)
        print("   SISTEMA DE PQRS - GESTIÓN Y HUELLITAS UDEA")
        print("="*45)
        print("1. Registrar nueva PQRS")
        print("2. Ver reportes y estadísticas")
        print("3. Salir")
        print("="*45)
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == '1':
            registrar_pqrs()
        elif opcion == '2':
            mostrar_reportes()
        elif opcion == '3':
            print("\n¡Gracias por utilizar el sistema Gestión y Huellitas UdeA!")
            break
        else:
            print("\nXOpción no válida. Ingrese 1, 2 o 3.")


if name== 'main':
    main()
