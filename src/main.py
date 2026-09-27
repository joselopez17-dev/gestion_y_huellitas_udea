# PROGRAMA PRINCIPAL - GESTIÓN Y HUELLITAS UDEA
import os
import sys
# Conectar la carpeta 'src' para importar los módulos de lógica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
import archivos
import reportes
import validaciones
def menu_registrar_pqrs():
    print("\n")
    print("REGISTRO DE NUEVA PQRS")
    print("-")

    # 1. Nombre completo
    while True:
        nombre = input("Ingrese nombre completo: ").strip()
        if validaciones.validar_nombre(nombre):
            break
        print("X Nombre inválido. Debe tener entre 3 y 100 caracteres sin números.")
    #  Tipo de documento
    while True:
        tipo_doc = input("Tipo de documento (CC, TI, CE, PP, NIT): ").strip().upper()
        if validaciones.validar_tipo_documento(tipo_doc):
            break
        print("X Tipo no válido. Opciones permitidas: CC, TI, CE, PP, NIT.")

    #  Número de documento
    while True:
        num_doc = input("Número de documento: ").strip()
        if validaciones.validar_numero_documento(num_doc):
            break
        print("X Documento inválido. Ingrese solo números (entre 3 y 15 dígitos).")

    # Tipo de teléfono
    while True:
        tipo_tel = input("Tipo de teléfono (celular, fijo, corporativo, otro): ").strip().lower()
        if validaciones.validar_tipo_telefono(tipo_tel):
            break
        print("X Opción inválida. Elija: celular, fijo, corporativo u otro.")

    #  Teléfono de contacto
    while True:
        tel = input("Número de teléfono: ").strip()
        if validaciones.validar_telefono(tel, tipo_tel):
            break
        print("X Teléfono inválido (10 dígitos para celular, 7 a 10 para fijo).")
    # 6. Correo electrónico
    while True:
        correo = input("Correo electrónico: ").strip()
        if validaciones.validar_correo(correo):
            break
        print("X Correo no válido. Debe tener formato usuario@dominio.com.")

    #  Dirección
    direccion = input("Dirección de contacto: ").strip()

    #  Tipo de solicitud
    while True:
        tipo_sol = input("Tipo de solicitud (Peticion, Queja, Reclamo, Sugerencia): ").strip().capitalize()
        if validaciones.validar_tipo_solicitud(tipo_sol):
            break
        print("X Opción inválida. Elija: Peticion, Queja, Reclamo o Sugerencia.")

    # 9. Fecha de radicación
    while True:
        fecha_rad = input("Fecha de radicación (YYYY-MM-DD): ").strip()
        if validaciones.validar_fecha_radicacion(fecha_rad):
            break
        print("X Fecha inválida. Debe ser AAAA-MM-DD y no una fecha futura.")

    # 10. Canal de recepción
    canal = input("Canal de recepción (Web, Presencial, Correo): ").strip()
    # 11. Asunto / Título
    asunto = input("Asunto o título de la solicitud: ").strip()
    # 12. Descripción detallada
    descripcion = input("Descripción detallada del caso: ").strip()
    # 13. Tipo de mascota
    while True:
        mascota = input("Tipo de mascota (Perro / Gato): ").strip().capitalize()
        if validaciones.validar_tipo_mascota(mascota):
            break
        print("X Opción inválida. Ingrese 'Perro' o 'Gato'.")
    # 14. Campus relacionado
    campus = input("Campus relacionado (ej: Ciudad Universitaria, Robledo): ").strip()
    # 15. Estado por defecto
    estado = "Registrada"
    # Construir diccionario
    datos = {
        "nombre_completo": nombre,
        "tipo_documento": tipo_doc,
        "numero_documento": num_doc,
        "tipo_telefono": tipo_tel,
        "telefono_contacto": tel,
        "correo_electronico": correo,
        "direccion": direccion,
        "tipo_solicitud": tipo_sol,
        "fecha_radicacion": fecha_rad,
        "canal_recepcion": canal,
        "asunto_titulo": asunto,
        "descripcion_detallada": descripcion,
        "tipo_mascota": mascota,
        "campus_relacionado": campus,
        "estado_peticion": estado
    }

    # Guardar en archivo plano
    nuevo_id = archivos.guardar_pqrs(datos)
    print("\n PQRS registrada correctamente!")
    print(f" Se le asignó el consecutivo ID #{nuevo_id} en data/{tipo_sol}.txt.")
def menu_ver_reportes():
    print("\n")
    print("ESTADÍSTICAS Y REPORTES DEL SISTEMA")
    print("=")
    prom = reportes.calcular_promedio_dias_respuesta()
    print(f"Promedio de días para respuesta: {prom} días")
    tipos = reportes.cantidad_por_tipo_solicitud()
    print("\n Cantidad por tipo de solicitud:")
    for t, cant in tipos.items():
        print(f"   - {t}: {cant}")
    mascotas = reportes.cantidad_por_tipo_mascota()
    print("\n Distribución por tipo de mascota:")
    for m, cant in mascotas.items():
        print(f"   - {m}: {cant}")
    estados = reportes.cantidad_por_estado()
    print("\n Cantidad por estado:")
    for e, cant in estados.items():
        print(f"   - {e}: {cant}")

    campus_top, cant_c = reportes.campus_con_mas_pqrs()
    print(f"\n Campus con mayor volumen: {campus_top} ({cant_c} solicitudes)")
    vencer = reportes.pqrs_proximas_a_vencer()
    print(f"\n  PQRS activas próximas a vencer (≤ 5 días): {vencer}")
    print("\n")
def main():
    while True:
        print("\n")
        print("  GESTIÓN Y HUELLITAS UDEA - SISTEMA PQRS ")
        print("")
        print("1. Registrar nueva PQRS")
        print("2. Ver estadísticas y reportes")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ").strip()
        if opcion == "1":
            menu_registrar_pqrs()
        elif opcion == "2":
            menu_ver_reportes()
        elif opcion == "3":
            print("\n¡Gracias por usar Gestión y Huellitas UdeA! Hasta luego.")
            break
        else:
            print("X Opción inválida. Ingrese 1, 2 o 3.")
if name == "main":
    main()
