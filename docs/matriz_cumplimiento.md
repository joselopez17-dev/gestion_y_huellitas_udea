# Matriz de cumplimiento de la rúbrica

Esta matriz compara los requisitos del proyecto integrador con la evidencia disponible en el repositorio. Los estados se actualizarán cuando exista evidencia comprobable y, para las funciones del programa, cuando hayan sido probadas.

**Estados:** Existe = evidencia presente; Parcial = borrador o información incompleta; Pendiente = sin evidencia suficiente; Por validar = existe un documento o código que requiere revisión.

## 1. Entregables documentales

| N.º | Requisito | Evidencia actual | Estado |
|---:|---|---|---|
| 1 | Integrantes | Tabla en `README.md` | Parcial |
| 2 | Programa académico, habilidades y fortalezas | Programas académicos registrados; faltan perfiles individuales | Parcial |
| 3 | Nombre, descripción e imagen representativa | Nombre y descripción presentes; logo pendiente en `images/` | Parcial |
| 4 | Licencia del software | Archivo `LICENSE` con licencia MIT | Existe |
| 5 | Reporte de visión | `docs/reporte_vision.md` | Por validar |
| 6 | Requisitos funcionales y no funcionales | `docs/especificacion_requisitos.md` | Por validar |
| 7 | Plan, cronograma/Gantt y presupuesto | `docs/plan_proyecto.md` | Por validar |
| 8 | Plan de versionado y avance en días | `docs/plan_versionado.md` | Por validar |
| 9 | Código fuente en `src/` | Actualmente solo se encuentra `src/main.py` | Parcial |
| 10 | Manual de usuario en `docs/` | `docs/manual_de_usuario.md`, aún provisional | Parcial |
| 11 | Estructura GitHub `src/`, `docs/`, `images/`, `data/` | `src/` y `docs/` existen; se están incorporando las otras carpetas | Parcial |
| 12 | Sustentación con software ejecutable y dominio del código | Se prepara cuando el programa esté terminado y probado | Pendiente |
| 13 | Fechas y documentos de las entregas | Requiere actualizar fechas reales y guardar evidencias | Pendiente |

## 2. Actas de entendimiento y compromiso

La guía solicita acta de entendimiento, acta de colaboración y acta de responsabilidad. Se incorporó una plantilla en `docs/actas/plantillas_actas.md`; debe diligenciarse con acuerdos reales, revisarse y firmarse por el equipo.

| Documento | Estado |
|---|---|
| Acta de entendimiento | Plantilla creada; falta diligenciar y firmar |
| Acta de colaboración | Plantilla creada; falta acordar normas y firmar |
| Acta de responsabilidad | Plantilla creada; falta acordar responsables, entregables, plazos y firmas |
| Reuniones de seguimiento | Pendiente registrar reuniones reales |

## 3. Requisitos funcionales del programa

| Requisito | Evidencia esperada | Estado |
|---|---|---|
| Menú principal | Registro, consulta, cambio de estado, estadísticas y salida | Parcial |
| Registro de PQRS | Captura de datos y validaciones completas | Parcial |
| Consecutivo independiente | ID automático separado por tipo de solicitud | Pendiente |
| Cuatro archivos planos | `Peticion.txt`, `Queja.txt`, `Reclamo.txt`, `Sugerencia.txt` | Pendiente |
| Validaciones | Módulo `validaciones.py` | Pendiente |
| Gestión de archivos | Módulo `archivos.py` | Pendiente |
| Fecha límite | Fecha de radicación + 30 días calendario | Pendiente |
| Estado | Flujo Registrada → En proceso → Solucionada | Pendiente |
| Consulta de PQRS | Búsqueda y visualización del radicado | Pendiente |
| Cambio de estado | Actualización con control del flujo | Pendiente |
| Radicado TXT | Marco ASCII; líneas de exactamente 120 caracteres; sin descripción detallada; dirección N/A si falta | Pendiente |
| Estadísticas | Promedio entero de días de respuesta y cinco adicionales | Parcial |
| Reportes | Módulo `reportes.py` | Pendiente |

## 4. Requisitos de programación y organización

- [ ] Usar clases y objetos.
- [ ] Nombrar las clases con el prefijo `c_`, según la convención de la guía.
- [ ] Incorporar comprensión de listas donde resulte apropiado.
- [ ] Documentar el código según la indicación de la guía.
- [ ] Separar validaciones, persistencia y reportes en módulos.
- [ ] Mantener el código Python dentro de `src/`.
- [ ] Guardar los archivos planos dentro de `data/`.
- [ ] Guardar documentos y manual dentro de `docs/`.
- [ ] Guardar logo y recursos gráficos dentro de `images/`.

## 5. Criterio para marcar un requisito como completo

Un requisito funcional se marcará como completo únicamente después de implementarlo y probarlo con datos válidos, inválidos y casos límite. La existencia de un archivo o una función no demuestra por sí sola que funcione.
