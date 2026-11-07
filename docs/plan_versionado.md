# Plan de versionado — Gestión y Huellitas UdeA

## 1. Convención

Se utiliza versionado semántico MAYOR.MENOR.PARCHE:

- **MAYOR:** versión estable de entrega final.
- **MENOR:** incorporación de una funcionalidad o módulo completo.
- **PARCHE:** corrección puntual sin ampliar el alcance.

Los nombres de versión de esta tabla identifican hitos de trabajo. La etiqueta formal de Git (tag) se creará cuando el equipo apruebe cada versión estable.

## 2. Base para contar los días

La versión anterior de este documento consignaba el **15 de octubre de 2026** como día 0. Esa fecha se conserva como base provisional y debe ser confirmada por el equipo, porque el historial de GitHub solo demuestra actividad del repositorio desde el **20 de octubre de 2026**, no necesariamente el inicio real del proyecto.

Tomando provisionalmente el 15 de octubre como día 0, el 7 de noviembre corresponde al día 23.

## 3. Hitos y avances comprobables

| Versión propuesta | Fecha | Día estimado | Procedimiento o avance verificable | Estado |
|---|---|---:|---|---|
| v0.0.1 | 20 oct 2026 | 5 | Primeros ajustes registrados en GitHub sobre el README del proyecto | Evidencia en historial |
| v0.1.0 | 7 nov 2026 | 23 | Organización documental, matriz de rúbrica, acta combinada pública y estructura de carpetas | Incorporado en desarrollo |
| v0.2.0 | 7 nov 2026 | 23 | Implementación de validaciones.py, archivos.py, reportes.py y menú principal | Incorporado en desarrollo |
| v0.2.1 | 7 nov 2026 | 23 | Pruebas de validaciones, almacenamiento, consulta, cambio de estado, estadísticas y radicado | 13 pruebas aprobadas antes de los últimos ajustes |
| v0.2.2 | 7 nov 2026 | 23 | Corrección de registro y cambio de estado cuando falla la generación del radicado; promedio muestra “Sin datos” cuando corresponde | 16 pruebas aprobadas en Ubuntu y Windows con Python 3.12 |
| v1.0.0 | Por definir | — | Versión de entrega después de revisión completa, pruebas en el equipo y aprobación grupal | Pendiente |

No se asignan porcentajes de avance sin un registro real de horas. Cuando el equipo lleve el control de tiempo, el avance porcentual podrá calcularse respecto de las 50 horas estimadas en el plan de proyecto.

## 4. Ramas de trabajo

- main: rama principal que conserva la versión original y estable.
- desarrollo: rama de integración donde se están incorporando y probando los cambios de la entrega final.
- modulo/nombre: ramas opcionales para trabajar de forma aislada en módulos específicos, por ejemplo modulo/validaciones.

## 5. Procedimiento para publicar una versión

1. Integrar el módulo o documento en desarrollo.
2. Ejecutar las pruebas automatizadas y revisar manualmente los cambios.
3. Corregir los errores encontrados.
4. Actualizar esta tabla con la fecha y el avance real.
5. Cuando el equipo apruebe la versión, integrar los cambios a main y crear la etiqueta correspondiente.

## 6. Control de cambios

Los cambios de alcance deben ser acordados por el equipo, registrados en el acta combinada y reflejados en una nueva versión. Ningún avance futuro se marcará como realizado hasta que exista evidencia en el repositorio.
