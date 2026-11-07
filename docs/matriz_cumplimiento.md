# Matriz de cumplimiento de la rúbrica

Esta matriz compara la rúbrica del proyecto integrador con los archivos y funcionalidades presentes en la rama `desarrollo`. Un requisito funcional solo se marca completo cuando se ejecutan las pruebas y se comprueba su funcionamiento.

**Estados:** Existe = evidencia presente; Parcial = falta información o pruebas; Pendiente = sin evidencia suficiente; Por validar = el documento o código existe, pero requiere ejecución o revisión.

## 1. Entregables documentales

| N.º | Requisito | Evidencia actual | Estado |
|---:|---|---|---|
| 1 | Integrantes | Tabla en `README.md` con los cinco nombres, programas y roles | Existe |
| 2 | Programa académico, habilidades y fortalezas | README con programas académicos y roles; por decisión del equipo no se publican fortalezas individuales. La rúbrica sí solicita habilidades y fortalezas, por lo que este criterio queda parcial. | Parcial |
| 3 | Nombre, descripción e imagen representativa | Nombre y descripción en README; logo vectorial e imagen representativa del proyecto en `images/` | Existe |
| 4 | Licencia del software | Archivo `LICENSE` con licencia MIT | Existe |
| 5 | Reporte de visión | `docs/reporte_vision.md` | Por validar |
| 6 | Requisitos funcionales y no funcionales | `docs/especificacion_requisitos.md` | Por validar |
| 7 | Plan, cronograma/Gantt y presupuesto | `docs/plan_proyecto.md` | Por validar |
| 8 | Plan de versionado y avance en días | `docs/plan_versionado.md` | Por validar |
| 9 | Código del algoritmo dentro de `src/` | `main.py`, `validaciones.py`, `archivos.py`, `reportes.py` | Por validar |
| 10 | Manual de usuario dentro de `docs/` | `docs/manual_de_usuario.md` y checklist `docs/pruebas_aceptacion.md` | Parcial; falta ejecutar la revisión paso a paso |
| 11 | Estructura GitHub | `src/`, `docs/`, `images/`, `data/` y `tests/` | Existe |
| 12 | Sustentación con programa ejecutable y dominio del código | Requiere ejecución final y preparación del equipo | Pendiente |
| 13 | Fechas y documentos de las entregas | Se debe confirmar el cronograma real y conservar evidencias | Pendiente |

## 2. Acta única del equipo

El equipo conserva un solo documento combinado: `docs/actas/Acta_de_entendimiento_publica.pdf`. El profesor confirmó que debe entregarse una sola acta que integre entendimiento, colaboración y responsabilidad. El documento, fechado el 22/08/2026, reúne los objetivos comunes, expectativas individuales, acuerdos de trabajo y comunicación, resolución de conflictos y distribución de responsabilidades. Los nombres indicados por el equipo para el README son Víctor Silgado y Sebastián Cardona.

La copia pública omite firmas manuscritas y números de identificación personal. El original firmado debe mantenerse en un medio privado y remitirse al docente por un canal privado si lo solicita.

| Componente incluido | Evidencia | Estado |
|---|---|---|
| Entendimiento | Objetivos comunes y expectativas de los cinco integrantes | Incluido |
| Colaboración | Canales de comunicación, normas de trabajo y resolución de conflictos | Incluido |
| Responsabilidad | Plan de trabajo con ocupación y tarea asignada a cada uno de los cinco integrantes; acuerdos generales de cumplimiento de plazos | Incluido en el acta combinada |
| Firmas y aceptación | Se encuentran en el original recibido, omitidas de la copia pública | Original privado; entregar al docente si lo solicita |
| Reuniones de seguimiento | El acta registra la reunión del 22/08/2026 | Falta evidencia de reuniones posteriores si se realizaron |

**Confirmación del docente:** el profesor indicó que se debe presentar una sola acta que integre las tres dimensiones. Por tanto, el documento combinado es el formato acordado para esta entrega; se conserva un PDF público sin firmas ni números de identificación y el original firmado se mantiene en privado.

## 3. Funcionalidades del programa

| Requisito | Implementación en `desarrollo` | Estado |
|---|---|---|
| Menú principal de cinco opciones | `src/main.py` y prueba de ejecución del menú | Prueba automatizada aprobada; revisión visual manual pendiente |
| Registro con validaciones | `src/main.py`, `src/validaciones.py` y pruebas de aceptación con entradas simuladas | Pruebas automatizadas aprobadas; falta recorrido manual del equipo |
| ID independiente por tipo | `src/archivos.py`; prueba de consecutivos independientes | Pruebas automatizadas aprobadas |
| Cuatro archivos planos | Prueba automatizada de Petición, Queja, Reclamo y Sugerencia; verifica creación y consecutivos independientes | Pruebas automatizadas aprobadas |
| Fecha máxima de 30 días | `src/archivos.py`; prueba de cálculo de fecha límite | Pruebas automatizadas aprobadas |
| Estado inicial y flujo de estados | `src/archivos.py`; prueba de transiciones | Pruebas automatizadas aprobadas |
| Consulta de PQRS y radicado | `src/main.py`, `src/archivos.py` y prueba de consulta general desde el menú | Pruebas automatizadas aprobadas; falta aceptación manual del equipo |
| Cambio de estado | `src/archivos.py`; prueba de transición desde el menú y de persistencia si falla el TXT actualizado | Pruebas automatizadas aprobadas |
| Radicado TXT de 120 caracteres | `src/archivos.py`; prueba de ancho, N/A y exclusión de descripción | Pruebas automatizadas aprobadas |
| Estadística obligatoria y cinco adicionales | `src/reportes.py` y `src/main.py`; prueba de los seis indicadores y del caso sin datos | Pruebas automatizadas aprobadas; falta revisión manual del equipo |

## 4. Programación y pruebas

| Criterio | Evidencia | Estado |
|---|---|---|
| Clases y objetos | Clases `c_main`, `c_validaciones`, `c_archivos`, `c_reportes` | Existe |
| Comprensión de listas | Utilizada en almacenamiento y reportes | Existe |
| Modularización | Archivos separados para menú, validaciones, persistencia y reportes | Existe |
| Comentarios y documentación | Docstrings y comentarios de módulos y métodos | Por validar |
| Pruebas automatizadas | `tests/test_core.py`, `tests/test_aceptacion.py` y GitHub Actions | 24/24 aprobadas en Ubuntu y Windows, Python 3.12; incluye 7 pruebas automatizadas de aceptación |
| Protección de datos generados | `.gitignore` excluye datos y radicados locales | Existe |

## 5. Evidencia de integración continua

La ejecución del 7 de noviembre de 2026 (commit `31686c6027e831cfc87d10fe6642c32f1c087e79`) completó correctamente las 23 pruebas en `ubuntu-latest` y `windows-latest`, con Python 3.12. La suite incluye ocho pruebas de aceptación con entradas simuladas y almacenamiento temporal: registro de los cuatro tipos, rechazo y reintento de datos inválidos, persistencia al reabrir el gestor, consulta general, radicados, transiciones de estado y estadísticas. [Ver ejecución de GitHub Actions](https://github.com/joselopez17-dev/gestion_y_huellitas_udea/actions/runs/42411052950). Esta evidencia automatizada no sustituye la revisión manual en el computador del equipo.

## 6. Prueba de aceptación pendiente

Se creó `tests/test_aceptacion.py` y sus siete pruebas automatizadas pasaron en Ubuntu y Windows. El checklist `docs/pruebas_aceptacion.md` conserva los pasos de revisión manual para el equipo; deben ejecutarse con datos ficticios en su computador, registrar fecha, versión y resultado, y documentar cualquier incidencia antes de marcar la aceptación manual como aprobada.

## 7. Criterio para el cierre

No se marcará como completo un requisito funcional hasta ejecutar las pruebas automatizadas y verificar manualmente el registro, consulta, actualización del estado, radicado y estadísticas con datos de prueba. Los documentos deben revisarse con el equipo antes de la entrega.
