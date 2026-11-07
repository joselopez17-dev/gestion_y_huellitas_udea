# Matriz de cumplimiento de la rúbrica

Esta matriz compara la rúbrica del proyecto integrador con los archivos y funcionalidades presentes en la rama `desarrollo`. Un requisito funcional solo se marca completo cuando se ejecutan las pruebas y se comprueba su funcionamiento.

**Estados:** Existe = evidencia presente; Parcial = falta información o pruebas; Pendiente = sin evidencia suficiente; Por validar = el documento o código existe, pero requiere ejecución o revisión.

## 1. Entregables documentales

| N.º | Requisito | Evidencia actual | Estado |
|---:|---|---|---|
| 1 | Integrantes | Tabla en `README.md` | Parcial |
| 2 | Programa académico, habilidades y fortalezas | README con programas, roles y responsabilidades según el acta; faltan habilidades y fortalezas confirmadas por cada integrante | Parcial |
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

## 2. Acta única del equipo

El equipo decidió conservar un solo documento combinado: `docs/actas/Acta_de_entendimiento_publica.pdf`. El acta, fechada el 22/08/2026, reúne los objetivos comunes, expectativas individuales, acuerdos de colaboración y comunicación, resolución de conflictos y plan de trabajo con responsabilidades.

La copia pública omite firmas manuscritas y números de identificación personal. El original firmado debe mantenerse en un medio privado y remitirse al docente por un canal privado si lo solicita.

| Componente incluido | Evidencia | Estado |
|---|---|---|
| Entendimiento | Objetivos comunes y expectativas de los cinco integrantes | Incluido |
| Colaboración | Canales de comunicación, normas de trabajo y resolución de conflictos | Incluido |
| Responsabilidad | Tabla de ocupaciones y tareas asignadas a los cinco integrantes | Incluido; el acta no especifica plazos ni criterios de evaluación detallados |
| Firmas y aceptación | Se encuentran en el original recibido, omitidas de la copia pública | Original privado; entregar al docente si lo solicita |
| Reuniones de seguimiento | El acta registra la reunión del 22/08/2026 | Falta evidencia de reuniones posteriores si se realizaron |

**Observación de cumplimiento:** la rúbrica define las tres actas como entregables distintos. El equipo decidió conservar un único documento combinado. Esta decisión debe confirmarse con el docente, ya que el archivo único puede no satisfacer literalmente la exigencia de tres entregables.

## 3. Funcionalidades del programa

| Requisito | Implementación en `desarrollo` | Estado |
|---|---|---|
| Menú principal de cinco opciones | `src/main.py` | Por validar |
| Registro con validaciones | `src/main.py` y `src/validaciones.py`; cubierto parcialmente por pruebas automatizadas | Pruebas automatizadas aprobadas; falta prueba de aceptación |
| ID independiente por tipo | `src/archivos.py`; prueba de consecutivos independientes | Pruebas automatizadas aprobadas |
| Cuatro archivos planos | Prueba automatizada de Petición, Queja, Reclamo y Sugerencia; verifica creación y consecutivos independientes | Pruebas automatizadas aprobadas |
| Fecha máxima de 30 días | `src/archivos.py`; prueba de cálculo de fecha límite | Pruebas automatizadas aprobadas |
| Estado inicial y flujo de estados | `src/archivos.py`; prueba de transiciones | Pruebas automatizadas aprobadas |
| Consulta de PQRS y radicado | `src/main.py` y `src/archivos.py`; prueba desde el menú que genera el radicado | Pruebas automatizadas aprobadas; falta aceptación manual del equipo |
| Cambio de estado | `src/archivos.py`; prueba de transiciones | Pruebas automatizadas aprobadas |
| Radicado TXT de 120 caracteres | `src/archivos.py`; prueba de ancho, N/A y exclusión de descripción | Pruebas automatizadas aprobadas |
| Estadística obligatoria y cinco adicionales | `src/reportes.py` y `src/main.py`; pruebas con distintos tipos, estados y fechas; promedio sin datos se presenta como “Sin datos” | Pruebas automatizadas aprobadas; falta validación de aceptación |

## 4. Programación y pruebas

| Criterio | Evidencia | Estado |
|---|---|---|
| Clases y objetos | Clases `c_main`, `c_validaciones`, `c_archivos`, `c_reportes` | Existe |
| Comprensión de listas | Utilizada en almacenamiento y reportes | Existe |
| Modularización | Archivos separados para menú, validaciones, persistencia y reportes | Existe |
| Comentarios y documentación | Docstrings y comentarios de módulos y métodos | Por validar |
| Pruebas automatizadas | `tests/test_core.py` y GitHub Actions | 15/15 aprobadas en Ubuntu y Windows, Python 3.12 |
| Protección de datos generados | `.gitignore` excluye datos y radicados locales | Existe |

## 5. Evidencia de integración continua

La ejecución del 7 de noviembre de 2026 completó correctamente los quince casos de prueba en los entornos `ubuntu-latest` y `windows-latest`, utilizando Python 3.12. Esto valida los casos automatizados incluidos, pero no sustituye la prueba de aceptación ni la revisión funcional por parte de los integrantes.

## 6. Criterio para el cierre

No se marcará como completo un requisito funcional hasta ejecutar las pruebas automatizadas y verificar manualmente el registro, consulta, actualización del estado, radicado y estadísticas con datos de prueba. Los documentos deben revisarse con el equipo antes de la entrega.
