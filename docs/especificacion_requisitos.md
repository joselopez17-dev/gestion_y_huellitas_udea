# Especificación de requisitos — Gestión y Huellitas UdeA

## 1. Requisitos funcionales (RF)

### 1.1 Menú y navegación

| ID | Requisito |
|---|---|
| RF-01 | El sistema debe mostrar un menú de consola con las opciones: Registrar PQRS, Consultar PQRS, Registrar cambio en PQRS, Estadísticas y Salir. |
| RF-02 | El menú debe repetirse hasta que el administrador seleccione la opción Salir. |

### 1.2 Registro y validación de PQRS

| ID | Requisito |
|---|---|
| RF-03 | Cada registro debe recibir un ID entero, automático y consecutivo, que inicia en 1. |
| RF-04 | Cada archivo plano debe manejar una secuencia de ID propia e independiente de los demás archivos. |
| RF-05 | El nombre completo es obligatorio, debe tener entre 3 y 100 caracteres y solo admite letras, espacios, tildes, ñ, apóstrofes y guiones. No admite números. |
| RF-06 | El tipo de documento es obligatorio y debe ser CC, TI, CE, PP o NIT. El número de documento es obligatorio, admite entre 3 y 15 dígitos y no permite letras ni caracteres especiales. |
| RF-07 | El tipo de teléfono es obligatorio y debe ser Celular, Fijo, Corporativo u Otro. El teléfono es obligatorio y debe contener exactamente 10 dígitos numéricos, según la rúbrica. |
| RF-08 | El correo electrónico es obligatorio, tiene máximo 254 caracteres, contiene un único símbolo @ y debe presentar un dominio válido. |
| RF-09 | La dirección es opcional. Cuando se ingresa, debe tener entre 5 y 200 caracteres y admite letras, números y los caracteres #, -, . y /. |
| RF-10 | El tipo de solicitud es obligatorio y debe ser Petición, Queja, Reclamo o Sugerencia. El registro se almacena en el archivo correspondiente. |
| RF-11 | La fecha de radicación es obligatoria, se captura en formato AAAA-MM-DD y no puede ser futura. |
| RF-12 | El canal de recepción es obligatorio y debe ser Presencial, Correo electrónico, Página web, Teléfono, Redes sociales u Otro. |
| RF-13 | El asunto es obligatorio, debe tener entre 5 y 150 caracteres y admite letras, números y signos de puntuación básicos. La descripción es obligatoria, admite texto libre y debe tener entre 20 y 2.000 caracteres. |
| RF-14 | El tipo de mascota es obligatorio y debe ser Perro o Gato. El campus es obligatorio y debe corresponder a uno de los nueve campus definidos en la guía. |
| RF-15 | La fecha máxima de respuesta se calcula sumando 30 días calendario a la fecha de radicación. |
| RF-16 | El estado inicial de cada PQRS debe ser Registrada. El sistema también conserva la fecha y hora en que se incorpora al sistema. |

### 1.3 Archivos de almacenamiento

El sistema debe administrar cuatro archivos planos independientes, todos con la misma estructura de registro:

| Archivo | Contenido |
|---|---|
| Peticion.txt | Registros de peticiones |
| Queja.txt | Registros de quejas |
| Reclamo.txt | Registros de reclamos |
| Sugerencia.txt | Registros de sugerencias |

Los registros se almacenan como objetos JSON, uno por línea, en archivos de texto UTF-8. Este formato permite conservar descripciones con tildes y signos sin confundir separadores. Cada archivo conserva su propio consecutivo.

### 1.4 Consulta, cambio de estado y radicado

| ID | Requisito |
|---|---|
| RF-17 | El sistema debe permitir listar las PQRS registradas, consultar el listado general y abrir un comprobante indicando el tipo y el consecutivo de la solicitud. |
| RF-18 | Los cambios de estado deben respetar exclusivamente el flujo Registrada → En proceso → Solucionada. |
| RF-19 | El sistema debe generar un comprobante TXT delimitado por un marco ASCII. Cada línea debe tener exactamente 120 caracteres horizontales. |
| RF-20 | El radicado debe mostrar encabezado, consecutivo, fecha y hora de incorporación al sistema, fecha de radicación, estado, fecha máxima de respuesta, datos del solicitante, clasificación y asunto. |
| RF-21 | El radicado no debe incluir la descripción detallada. Si la dirección está vacía, debe mostrar N/A. |

### 1.5 Estadísticas

El sistema debe calcular el indicador obligatorio y cinco estadísticas adicionales:

| ID | Estadística | Descripción |
|---|---|---|
| RF-22 | Promedio de días de respuesta | Promedio entero de días entre la fecha de radicación y la fecha en que la PQRS pasa a Solucionada. Se calcula solo con solicitudes que tengan fecha de respuesta; se redondea al entero más cercano. Si no hay solicitudes solucionadas con fecha de respuesta, el sistema informa que no hay datos, en vez de presentar un promedio de cero días. |
| RF-23.1 | Cantidad por tipo de solicitud | Número de peticiones, quejas, reclamos y sugerencias. |
| RF-23.2 | Cantidad por tipo de mascota | Número de registros asociados a perros y gatos. |
| RF-23.3 | Distribución por estado | Cantidad de PQRS Registradas, En proceso y Solucionadas. |
| RF-23.4 | PQRS activa más antigua | Solicitud no solucionada con la fecha de radicación más antigua. |
| RF-23.5 | PQRS vencidas o próximas a vencer | Solicitudes activas cuya fecha límite ya pasó o vence en cinco días calendario o menos. |

## 2. Requisitos no funcionales (RNF)

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | Usabilidad | La consola debe ser clara y amigable, con mensajes que indiquen qué dato corregir. |
| RNF-02 | Fiabilidad | Los registros deben conservarse al cerrar el programa y actualizarse mediante un archivo temporal antes de reemplazar el archivo de datos. |
| RNF-03 | Integridad | El registro no debe guardarse si los datos obligatorios no pasan las validaciones. |
| RNF-04 | Rendimiento | El programa está orientado al volumen académico previsto y utiliza archivos locales; no se ha definido ni medido un umbral de rendimiento para grandes volúmenes. |
| RNF-05 | Compatibilidad | El programa debe ejecutarse con Python 3 y librerías de la biblioteca estándar. |
| RNF-06 | Mantenibilidad | El código debe estar separado en módulos para validaciones, archivos y reportes, utilizando clases y objetos. |
| RNF-07 | Privacidad | Los datos personales de prueba no deben publicarse en el repositorio compartido. Los archivos locales no cuentan con cifrado ni autenticación dentro de esta versión. |
| RNF-08 | Portabilidad | La información debe almacenarse en archivos de texto plano UTF-8 dentro de data/. |
| RNF-09 | Formato | Cada línea del comprobante de radicación debe tener exactamente 120 caracteres. |

## 3. Organización del código

- src/main.py: menú y coordinación de las opciones del programa.
- src/validaciones.py: validación de nombres, documentos, teléfonos, correos, fechas y demás campos.
- src/archivos.py: lectura y escritura de los cuatro archivos, consecutivos, consulta, cambios de estado y radicados.
- src/reportes.py: cálculo del promedio obligatorio y las cinco estadísticas complementarias.
- Las clases principales utilizan el prefijo c_ según la indicación de la guía.

## 4. Verificación

Los requisitos se considerarán completos después de ejecutar las pruebas automatizadas y verificar manualmente el flujo de registro, consulta, cambio de estado, generación del radicado y estadísticas.
