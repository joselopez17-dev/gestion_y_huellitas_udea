# Manual de usuario — Gestión y Huellitas UdeA

> **Estado:** borrador provisional. Este manual se actualizará y verificará cuando se complete la implementación. No se debe considerar disponible una opción hasta que haya sido probada en el programa.

## 1. Propósito

Gestión y Huellitas UdeA es un programa de consola para apoyar el registro y seguimiento de Peticiones, Quejas, Reclamos y Sugerencias (PQRS) relacionadas con la atención veterinaria de perros y gatos en la Universidad de Antioquia.

## 2. Requisitos para utilizar el programa

- Tener Python 3 instalado.
- Descargar o clonar el repositorio.
- Ejecutar el programa desde la carpeta raíz, una vez estén integrados y probados los módulos requeridos.

## 3. Ejecución prevista

El punto de entrada del programa es:

```bash
python src/main.py
```

**Importante:** la versión actual de `src/main.py` importa los módulos `archivos.py`, `reportes.py` y `validaciones.py`, que todavía deben incorporarse y probarse. Por tanto, la ejecución completa aún no está disponible.

## 4. Funcionalidades previstas

1. Registrar una PQRS.
2. Consultar las PQRS registradas.
3. Cambiar el estado de una PQRS siguiendo el flujo autorizado.
4. Consultar las estadísticas de gestión.
5. Salir del programa.

## 5. Datos del registro

El registro contempla los datos del solicitante, la información de la solicitud, el tipo de mascota, el campus, las fechas de gestión y el estado. Las reglas detalladas se encuentran en [la especificación de requisitos](especificacion_requisitos.md).

## 6. Archivos de almacenamiento

Cada tipo de solicitud se guardará en un archivo independiente dentro de `data/`:

- `Peticion.txt`
- `Queja.txt`
- `Reclamo.txt`
- `Sugerencia.txt`

Cada archivo manejará su propio consecutivo de radicación.

## 7. Radicado

El sistema deberá generar un comprobante TXT con marco ASCII, ancho de 120 caracteres por línea y los datos esenciales de la solicitud. La descripción detallada no se incluirá. Si no se registra dirección, se mostrará `N/A`.

## 8. Seguimiento del estado

Los estados permitidos son:

`Registrada → En proceso → Solucionada`

No se deben omitir etapas ni retroceder el estado.

## 9. Estadísticas

El sistema deberá calcular el promedio entero de días de respuesta y cinco estadísticas adicionales de gestión. Las opciones definitivas se documentarán después de implementarlas.

## 10. Mensajes de ayuda y errores

La versión final incorporará mensajes claros para indicar al usuario qué dato debe corregir cuando ingrese información inválida o seleccione una opción inexistente.
