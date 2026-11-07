# Manual de usuario — Gestión y Huellitas UdeA

> **Versión:** borrador de la rama `desarrollo`. Debe comprobarse en el equipo antes de considerarse manual definitivo.

## 1. Propósito

Gestión y Huellitas UdeA es un programa de consola para registrar y hacer seguimiento a Peticiones, Quejas, Reclamos y Sugerencias (PQRS) relacionadas con la atención de perros y gatos en la Universidad de Antioquia.

## 2. Requisitos

- Python 3 instalado.
- Una copia local del repositorio.
- No se requieren paquetes externos: el programa utiliza módulos de la biblioteca estándar de Python.

## 3. Ejecutar pruebas y abrir el programa

Desde la carpeta raíz del repositorio, ejecute primero las pruebas:

```bash
python -m unittest discover -s tests -v
```

Para abrir el sistema:

```bash
python src/main.py
```

## 4. Menú principal

El menú contiene cinco opciones:

1. Registrar PQRS.
2. Consultar PQRS.
3. Registrar cambio en PQRS.
4. Estadísticas.
5. Salir.

Escriba el número de la opción y presione Enter.

## 5. Registrar una PQRS

Seleccione la opción 1. El programa solicitará los datos del solicitante y de la solicitud. Si un dato no cumple las reglas, mostrará un mensaje y volverá a pedirlo.

| Dato | Regla principal |
|---|---|
| Nombre completo | 3 a 100 caracteres; letras, tildes, espacios, apóstrofes y guiones |
| Tipo de documento | CC, TI, CE, PP o NIT |
| Número de documento | 3 a 15 dígitos |
| Tipo de teléfono | Celular, Fijo, Corporativo u Otro |
| Teléfono | Exactamente 10 dígitos |
| Correo electrónico | Máximo 254 caracteres; estructura usuario@dominio.com |
| Dirección | Opcional; de 5 a 200 caracteres si se ingresa |
| Tipo de solicitud | Petición, Queja, Reclamo o Sugerencia |
| Fecha de radicación | AAAA-MM-DD; no puede ser futura |
| Canal de recepción | Presencial, Correo electrónico, Página web, Teléfono, Redes sociales u Otro |
| Asunto | 5 a 150 caracteres |
| Descripción | 20 a 2.000 caracteres |
| Tipo de mascota | Perro o Gato |
| Campus | Uno de los nueve campus definidos en la especificación |

Al guardar, el sistema asigna el consecutivo propio del archivo correspondiente, define el estado inicial como Registrada y calcula la fecha máxima de respuesta sumando 30 días calendario a la fecha de radicación.

## 6. Consultar PQRS

Seleccione la opción 2. Puede escoger un tipo de solicitud para ver su listado o elegir Todas para consultar el resumen general. Para abrir un comprobante específico, indique el tipo y el consecutivo correspondiente.

## 7. Cambiar el estado

Seleccione la opción 3, indique el tipo de solicitud y su consecutivo. Los únicos cambios permitidos son:

`Registrada → En proceso → Solucionada`

No se puede pasar directamente de Registrada a Solucionada ni retroceder un estado. Cuando la PQRS cambia a Solucionada, el sistema guarda la fecha de respuesta.

## 8. Radicado TXT

Al registrar o consultar una solicitud, el programa genera un comprobante dentro de `data/radicados/`. Cada línea tiene exactamente 120 caracteres. El comprobante incluye los datos del radicado, solicitante, clasificación y asunto; no incluye la descripción detallada. Si no hay dirección, aparece N/A.

## 9. Estadísticas

Seleccione la opción 4. Se muestran seis indicadores:

1. Promedio entero de días de respuesta de las PQRS solucionadas.
2. Cantidad por tipo de solicitud.
3. Cantidad por tipo de mascota.
4. Distribución por estado.
5. PQRS activa más antigua.
6. PQRS vencidas o próximas a vencer en cinco días calendario o menos.

## 10. Archivos de datos y privacidad

Los registros se guardan en archivos de texto UTF-8 dentro de `data/`, uno por tipo:

- `Peticion.txt`
- `Queja.txt`
- `Reclamo.txt`
- `Sugerencia.txt`

Cada archivo contiene registros JSON, uno por línea, y mantiene un consecutivo independiente. Los radicados se guardan en `data/radicados/`.

Los archivos generados se excluyen del control de versiones mediante `.gitignore`. No se deben subir al repositorio público datos personales reales de solicitantes.

## 11. Cerrar el programa

Seleccione la opción 5 para salir de forma normal.
