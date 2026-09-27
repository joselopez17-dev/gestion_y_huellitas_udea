# MÓDULO DE VALIDACIONES - GESTIÓN Y HUELLITAS UDEA

from datetime import datetime
def validar_nombre(nombre):
    longitud = len(nombre)
    if longitud < 3 or longitud > 100:
        return False
    for caracter in nombre:
        if caracter.isdigit():
            return False
    return True
def validar_tipo_documento(tipo_doc):
    tipo_doc = tipo_doc.upper()
    if tipo_doc in ["CC", "TI", "CE", "PP", "NIT"]:
        return True
    else:
        return False
def validar_numero_documento(num_doc):
    if num_doc.isdigit():
        longitud = len(num_doc)
        if 3 <= longitud <= 15:
            return True
    return False
def validar_tipo_telefono(tipo_tel):
    opciones = ["celular", "fijo", "corporativo", "otro"]
    if tipo_tel.lower() in opciones:
        return True
    else:
        return False
def validar_telefono(telefono, tipo_tel="celular"):
    if not telefono.isdigit():
        return False
    if tipo_tel.lower() == "fijo":
        return 7 <= len(telefono) <= 10
    else:
        return len(telefono) == 10
def validar_correo(correo):
    if len(correo) > 254:
        return False
    if correo.count("@") == 1:
        partes = correo.split("@")
        usuario = partes[0]
        dominio = partes[1]

        if len(usuario) > 0 and "." in dominio and len(dominio) > 3:
            return True
    return False
def validar_tipo_solicitud(tipo):
    opciones = ["peticion", "queja", "reclamo", "sugerencia"]
    if tipo.lower() in opciones:
        return True
    else:
        return False
def validar_tipo_mascota(mascota):
    if mascota.capitalize() in ["Perro", "Gato"]:
        return True
    else:
        return False
def validar_fecha_radicacion(fecha_texto):
    try:
        fecha_ingresada = datetime.strptime(fecha_texto, "%Y-%m-%d")
        fecha_actual = datetime.now()

        if fecha_ingresada <= fecha_actual:
            return True
        else:
            return False
    except ValueError:
        return False

            


     

    


    
    
    
  
   
  
  
  
  
