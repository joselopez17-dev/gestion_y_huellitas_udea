# Especificación de requisitos: Gestión y Huellitas UdeA

## 1. Requisitos funcionales (RF)

### Menú y navegación
| ID | Requisito |
|---|---|
| RF-01 | El sistema debe mostrar un menú de consola con las opciones: 1. Registrar PQRS, 2. Consultar PQRS, 3. Registrar cambio en PQRS, 4. Estadísticas, 5. Salir. |
| RF-02 | El sistema debe repetir el menú hasta que el administrador elija Salir. |

### Registro de PQRS
| ID | Requisito |
|---|---|
| RF-03 | El sistema debe asignar un ID entero auto-incremental que inicia en 1, sin repetidos. |
| RF-04 | Cada archivo plano debe tener su propia secuencia de ID, independiente de los otros. |
| RF-05 | El sistema debe validar el nombre completo: de 3 a 100 caracteres, solo letras, espacios, tildes, ñ, apóstrofes y guiones, sin números. Es obligatorio. |
| RF-06 | El sistema debe validar el tipo de documento (CC, TI, CE, PP, NIT) y el número de documento (3 a 15 dígitos, solo números). Ambos son obligatorios. |
| RF-07 | El sistema debe validar el tipo de teléfono (Celular, Fijo, Corporativo, Otro) y el teléfono de contacto (10 dígitos, solo números). Ambos son obligatorios. |
| RF-08 | El sistema debe validar el correo electrónico: máximo 254 caracteres, un único @ y un dominio válido. Es obligatorio. |
| RF-09 | El sistema debe aceptar la dirección como campo opcional, de 5 a 200 caracteres, con letras, números y los caracteres #, -, . y /. |
| RF-10 | El sistema debe validar el tipo de solicitud (Petición, Queja, Reclamo, Sugerencia) y guardar el registro en el archivo correspondiente. |
| RF-11 | El sistema debe validar la fecha de radicación en formato datetime de Python y rechazar fechas futuras. |
| RF-12 | El sistema debe validar el canal de recepción (Presencial, Correo electrónico, Página web, Teléfono, Redes sociales, Otro). |
| RF-13 | El sistema debe validar el asunto (5 a 150 caracteres) y la descripción detallada (20 a 2000 caracteres, sin ser solo espacios). |
| RF-14 | El sistema debe validar el tipo de mascota (Perro o Gato) y el campus relacionado (los 9 campus de la lista oficial). |
| RF-15 | El sistema debe calcular la fecha máxima de respuesta como fecha de registro + 30 días. |
| RF-16 | El estado inicial de toda PQRS debe ser "Registrada". |

### Consulta, cambios y radicado
| ID | Requisito |
|---|---|
| RF-17 | El sistema debe permitir consultar las PQRS registradas y mostrarlas con el formato del radicado. |
| RF-18 | El sistema debe permitir cambiar el estado solo en el orden Registrada → En proceso → Solucionada. |
| RF-19 | El sistema debe imprimir un radicado en TXT con marco ASCII (+, -, \|) de exactamente 120 caracteres de ancho. |
| RF-20 | El radicado debe mostrar encabezado, datos del radicado, datos del solicitante, clasificación y asunto, sin la descripción detallada. |
| RF-21 | Si la dirección no se ingresó, el radicado debe mostrar "N/A". |

### Estadísticas
| ID | Requisito |
|---|---|
| RF-22 | El sistema debe calcular el promedio de días de respuesta, en valores enteros (obligatoria). |
| RF-23 | El sistema debe mostrar cinco estadísticas adicionales: **[definirlas]**. |

## 2. Requisitos no funcionales (RNF)

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | Usabilidad | La consola debe ser clara y amigable, con mensajes de error que indiquen qué dato corregir. |
| RNF-02 | Fiabilidad | Los datos guardados no deben perderse ni corromperse al cerrar el programa. |
| RNF-03 | Integridad | Ningún registro puede guardarse si no pasa todas las validaciones. |
| RNF-04 | Rendimiento | Registrar o consultar una PQRS debe tardar menos de 2 segundos con hasta 1000 registros. |
| RNF-05 | Compatibilidad | El programa debe ejecutarse en Python 3.x en Windows, sin librerías externas. |
| RNF-06 | Mantenibilidad | El código debe estar modularizado en `validaciones.py`, `archivos.py` y `reportes.py`. |
| RNF-07 | Seguridad | Los datos personales solo deben quedar en los archivos de la carpeta `data/`, sin enviarse a otros sistemas. |
| RNF-08 | Portabilidad | Los archivos de datos deben ser texto plano (.txt). |
