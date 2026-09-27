# MODULO DE VALIDACIONES - GESTION Y HUELLITAS UDEA
from datetime import datetime 
def validar_nombre(nombre):
     valida el nombre que tenga entre 3 y 100 caracteres, no tenga numeros y solo use letras o espacios.
    longitud = len(nombre)
    if longitud < 3 os longitud > 100:
return False 
# comprobar si hay numeros dentro del texto
for caracter in nombre:
    if caracter.isdigit():
        return False # si encuentra un nemero, es invalido
return True
def validar_tipo_documento(tipo_doc):
    Validar los tipos de documentos permitidos.
    Valores: CC, TI, CE, PP, NIT
    tipo_doc = tipo_doc.upper()
    if tipo_doc in ["CC", "TI", "CE", "PP", "NIT"]:
        return True
    else:
        return False
        def validar_numero_documento(num_doc):
            Validad que el documento contenga entre 3 a 15 digitos y solo numeros.
            if num_doc.isdigit():
            longitud = len(num_doc)
            if 3 <= longitud <= 15:
                return True
            return False
def validar_tipo_telefono(tipo_cel):
    Validar los tipos de telefono permitodos.
    opciones = ["celular", "fijo", "corporativo", "otro",]
    if tipo_tel.lower() in opciones:
        return True
    else:
        return False
def validar_telefono(telefono):
    Valida que el telefono de contacto tenga exactamente 10 digitos numericos.
    if telefono.isdigit() and len(telefono) == 10:
       return True
    else:
        return False
def validar_correo(correo):
    Valida que el correo tenga formato basico usuario@dominio.com, un solo 
    '@' y no exceda los 254 caracteres.
    if len(correo) > 254:
       return False
if correo.count('@') == 1:
    partes = correo.split('@')
    usuario = partes[0]
    dominio = partes[1]
    # debe tener texto amtes y despues del '@', y al menos un punto en el dominio
    if len(usuario) > 0 and "." in dominio and len(dominio) > 3:
        return True
    return False
def validar_tipo_solicitud(tipo):
    Valida que la salicitud corresponda a una de las 4 opciones oficiales.
    opciones = ["peticion", "queja", "reclamo", "sugerencia"`]
    if tipo.lower() in opcion:
        return True
    else:
        return False 
def validar_tipo_mascota(mascota):
    Valida que la mascota sea perro o gato.
    if mascota.capitalize() in ["perro", "gato"]:
        return True
    else:
        return False 
def validar_fecha_radicacion(fecha_texto):
    Valida que la fecha tenga fromato YYYY-MM-DD y no sea fecha futura.
    try:
        fecha_ingresada = datatime.striptime(fecha_texto, "%Y-%m-%d")
        fecha_actual = datatime.now()
        #verificar que la fecha ingresada no sea poeterior a la actual
        if fecha_ingresada <= fecha_actual:
            returm True
         else:
             return False 
except ValueError:
    return False

            


     

    


    
    
    
  
   
  
  
  
  
