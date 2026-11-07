# Matriz de cumplimiento de la rúbrica

Esta matriz compara la rúbrica del proyecto integrador con los archivos y funcionalidades presentes en la rama `desarrollo`. Un requisito funcional solo se marca completo cuando se ejecutan las pruebas y se comprueba su funcionamiento.

**Estados:** Existe = evidencia presente; Parcial = falta información o pruebas; Pendiente = sin evidencia suficiente; Por validar = el documento o código existe, pero requiere ejecución o revisión.

## 1. Entregables documentales

| N.º | Requisito | Evidencia actual | Estado |
|---:|---|---|---|
| 1 | Integrantes | Tabla en `README.md` | Parcial |
| 2 | Programa académico, habilidades y fortalezas | Programas registrados; faltan descripciones individuales | Parcial |
| 3 | Nombre, descripción e imagen representativa | Nombre y descripción presentes; logo vectorial en `images/logo_huellitas.svg`, pendiente de aprobación del equipo | Parcial |
| 4 | Licencia del software | Archivo `LICENSE` con licencia MIT | Existe |
| 5 | Reporte de visión | `docs/reporte_vision.md` | Por validar |
| 6 | Requisitos funcionales y no funcionales | `docs/especificacion_requisitos.md` | Por validar |
| 7 | Plan, cronograma/Gantt y presupuesto | `docs/plan_proyecto.md` | Por validar |
| 8 | Plan de versionado y avance en días | `docs/plan_versionado.md` | Por validar |
| 9 | Código del algoritmo dentro de `src/` | `main.py`, `validaciones.py`, `archivos.py`, `reportes.py` | Por validar |
| 10 | Manual de usuario dentro de `docs/` | `docs/manual_de_usuario.md` | Parcial; requiere prueba de uso |
| 11 | Estructura GitHub | `src/`, `docs/`, `images/`, `data/` y `tests/` | Existe |
| 12 | Sustentación con programa ejecutable y dominio del código | Requiere ejecución final y preparación del equipo | Pendiente |
| 13 | Fechas y documentos de las entregas | Se debe confirmar el cronograma real y conservar evidencias | Pendiente |

## 2. Actas de entendimiento y compromiso

El equipo entregó un acta combinada fechada el 22/08/2026. El documento incluye los objetivos comunes, las expectativas individuales de los cinco integrantes, los acuerdos de colaboración y comunicación, la resolución de conflictos y el plan de trabajo con responsabilidades.

Se incorporó una **copia pública en PDF** en `docs/actas/Acta_de_entendimiento_publica.pdf` y una transcripción en Markdown. La copia pública omite las firmas manuscritas y los números de identificación personal. El documento original firmado debe conservarse en un medio privado y entregarse al docente por el canal indicado si se requiere verificar las firmas.

| Documento o componente | Evidencia | Estado |
|---|---|---|
| Acta de entendimiento | PDF público y transcripción en `docs/actas/` | Existe copia pública; firma original se conserva fuera del repositorio público |
| Acta de colaboración | Acuerdos de comunicación, trabajo y resolución de conflictos incluidos en el acta combinada | Incluida en documento combinado; confirmar si la rúbrica exige archivo independiente |
| Acta de responsabilidad | Plan de trabajo con ocupación y tareas para los cinco integrantes | Incluida en documento combinado; confirmar si la rúbrica exige archivo independiente |
| Firmas y aceptación | Están en el original recibido, pero se omitieron de la copia pública | Validar entrega privada al docente |
| Reuniones de seguimiento | El acta registra la reunión del 22/08/2026; faltan actas posteriores si hubo más reuniones | Parcial |

Las plantillas en `docs/actas/plantillas_actas.md` quedan como apoyo por si el docente solicita separar las actas o registrar reuniones y acuerdos posteriores.

## 3. Funcionalidades del programa

| Requisito | Implementación en `desarrollo` | Estado |
|---|---|---|
| Menú principal de cinco opciones | `src/main.py` | Por validar |
| Registro con validaciones | `src/main.py` y `src/validaciones.py`; cubierto parcialmente por pruebas automatizadas | Pruebas automatizadas aprobadas; falta prueba de aceptación |
| ID independiente por tipo | `src/archivos.py`; prueba de consecutivos independientes | Pruebas automatizadas aprobadas |
| Cuatro archivos planos | Se crean al usar cada tipo de solicitud dentro de `data/` | Por validar |
| Fecha máxima de 30 días | `src/archivos.py`; prueba de cálculo de fecha límite | Pruebas automatizadas aprobadas |
| Estado inicial y flujo de estados | `src/archivos.py`; prueba de transiciones | Pruebas automatizadas aprobadas |
| Consulta de PQRS y radicado | `src/main.py` y `src/archivos.py` | Implementada; falta prueba manual de aceptación |
| Cambio de estado | `src/archivos.py`; prueba de transiciones | Pruebas automatizadas aprobadas |
| Radicado TXT de 120 caracteres | `src/archivos.py`; prueba de ancho, N/A y exclusión de descripción | Pruebas automatizadas aprobadas |
| Estadística obligatoria y cinco adicionales | `src/reportes.py` y `src/main.py`; pruebas con distintos tipos, estados y fechas | Pruebas automatizadas aprobadas; falta validación de aceptación |

## 4. Programación y pruebas

| Criterio | Evidencia | Estado |
|---|---|---|
| Clases y objetos | Clases `c_main`, `c_validaciones`, `c_archivos`, `c_reportes` | Existe |
| Comprensión de listas | Utilizada en almacenamiento y reportes | Existe |
| Modularización | Archivos separados para menú, validaciones, persistencia y reportes | Existe |
| Comentarios y documentación | Docstrings y comentarios de módulos y métodos | Por validar |
| Pruebas automatizadas | `tests/test_core.py` y GitHub Actions | 11/11 aprobadas en Ubuntu y Windows, Python 3.12 |
| Protección de datos generados | `.gitignore` excluye datos y radicados locales | Existe |

## 5. Evidencia de integración continua

La ejecución del 7 de noviembre de 2026 completó correctamente los once casos de prueba en los entornos `ubuntu-latest` y `windows-latest`, utilizando Python 3.12. Esto valida los casos automatizados incluidos, pero no sustituye la prueba de aceptación ni la revisión funcional por parte de los integrantes.

## 6. Criterio para el cierre

No se marcará como completo un requisito funcional hasta ejecutar las pruebas automatizadas y verificar manualmente el registro, consulta, actualización del estado, radicado y estadísticas con datos de prueba. Los documentos deben revisarse con el equipo antes de la entrega.
