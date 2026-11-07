# Plan de proyecto: Gestión y Huellitas UdeA

## 1. Actividades y presupuesto

La guía solicita valorar 50 horas de trabajo del equipo a razón de un salario mínimo legal mensual vigente (SMLMV). Para esta estimación académica se toma como referencia el SMLMV 2026 de **$1.750.905 COP** y el divisor mensual de **210 horas**, aplicable desde el 15 de julio de 2026 con la jornada máxima semanal de 42 horas.

- Valor hora sin redondear: $1.750.905 / 210 = **$8.337,64 COP**.
- Valor hora redondeado para la tabla: **$8.338 COP**.
- Valor estimado de las 50 horas: 50 × $8.338 = **$416.900 COP**.

Este cálculo es una valoración académica del tiempo de práctica del equipo, no un registro de pagos ni de horas efectivamente ejecutadas. Las referencias normativas se enlazan al final de este apartado.

| ID | Actividad | Horas | Costo (COP) |
|---|---|---:|---:|
| A1 | Acta combinada del equipo (entendimiento, colaboración y responsabilidades) | 3 | $25.014 |
| A2 | Reporte de visión | 3 | $25.014 |
| A3 | Especificación de requisitos | 4 | $33.352 |
| A4 | Plan de proyecto y plan de versionado | 3 | $25.014 |
| A5 | README, logo y estructura del repositorio | 4 | $33.352 |
| A6 | Diseño del algoritmo y de las clases | 5 | $41.690 |
| A7 | Módulo validaciones.py | 5 | $41.690 |
| A8 | Módulo archivos.py | 5 | $41.690 |
| A9 | Menú, registro y radicado de 120 caracteres | 5 | $41.690 |
| A10 | Módulo reportes.py (6 estadísticas) | 5 | $41.690 |
| A11 | Pruebas y corrección de errores | 4 | $33.352 |
| A12 | Manual de usuario | 2 | $16.676 |
| A13 | Revisión final y preparación de la sustentación | 2 | $16.676 |
| | **Total** | **50** | **$416.900** |

**Fuentes para la estimación:** [Decreto 1469 de 2025 — SMLMV 2026](https://www.presidencia.gov.co/Documents/251230-Decreto-1469-MinTrabajo.pdf); [Circular 0101 de 2025 — divisor mensual de horas y jornada de 42 horas desde el 15 de julio de 2026](https://normativa.colpensiones.gov.co/compilacion/docs/circular_mintra_0101_2025.htm). El Consejo de Estado revocó el 9 de julio de 2026 la suspensión provisional del Decreto 1469 de 2025; por ello se conserva como referencia el valor de $1.750.905.

## 2. Cronograma (Diagrama de Gantt)

~~~mermaid
gantt
    title Gestión y Huellitas UdeA (15 oct - 22 nov 2026)
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    section Documentación
    Acta combinada (A1)             :a1, 2026-10-15, 2d
    Reporte de visión (A2)          :a2, 2026-10-15, 2d
    README, logo y repo (A5)        :a5, 2026-10-15, 4d
    Requisitos (A3)                 :a3, 2026-10-16, 3d
    Plan de proyecto y versionado (A4) :a4, 2026-10-19, 2d
    section Desarrollo
    Diseño del algoritmo (A6)       :a6, 2026-10-20, 5d
    validaciones.py (A7)            :a7, 2026-10-26, 6d
    archivos.py (A8)                :a8, 2026-10-26, 6d
    Menú y radicado (A9)            :a9, 2026-11-02, 6d
    reportes.py (A10)               :a10, 2026-11-02, 6d
    Pruebas y correcciones (A11)    :a11, 2026-11-09, 6d
    section Cierre
    Manual de usuario (A12)         :a12, 2026-11-12, 4d
    Revisión final y sustentación (A13) :a13, 2026-11-16, 4d
    Entrega 2                       :milestone, 2026-11-22, 0d
~~~

## 3. Hitos

| Fecha | Hito |
|---|---|
| 21 oct | Documentos de la Entrega 1 corregidos y subidos |
| 25 oct | Diseño del algoritmo terminado |
| 14 nov | Programa completo y probado |
| 19 nov | Manual y revisión final listos |
| 22 nov | Entrega 2 |

## 4. Seguimiento del avance real (corte: 7 de noviembre de 2026)

Este seguimiento diferencia los documentos y módulos que ya están incorporados en la rama desarrollo de las actividades que aún requieren revisión del equipo. No equivale a un porcentaje de horas ejecutadas: las horas reales deben registrarse con el equipo.

| Actividad | Evidencia actual | Estado al 7 nov |
|---|---|---|
| A1. Acta única del equipo | Acta combinada recibida; copia pública PDF en docs/actas/Acta_de_entendimiento_publica.pdf; la copia pública omite firmas e identificaciones. Reúne entendimiento, colaboración y responsabilidades en un solo archivo | Parcial: confirmar con el docente si acepta un único documento combinado, pues la rúbrica enumera tres entregables |
| A2. Reporte de visión | docs/reporte_vision.md | Revisado y corregido; pendiente validación del equipo |
| A3. Especificación de requisitos | docs/especificacion_requisitos.md | Revisada; alineada con el comportamiento documentado del sistema |
| A4. Plan de proyecto y versionado | docs/plan_proyecto.md y docs/plan_versionado.md | Elaborados; horas reales pendientes de registrar |
| A5. README, logo y estructura | README con roles, expectativas y aportes del acta; logo vectorial en images/logo_huellitas.svg; falta confirmar fortalezas concretas y nombres que difieren entre README y acta | Parcial |
| A6. Diseño del algoritmo y clases | docs/algoritmo.md y clases c_main, c_validaciones, c_archivos, c_reportes | Implementado; pendiente explicación y revisión del equipo |
| A7. Validaciones | src/validaciones.py y pruebas de datos válidos e inválidos | Implementado; pruebas automatizadas aprobadas |
| A8. Archivos | src/archivos.py; prueba de los cuatro archivos y consecutivos independientes | Implementado; pruebas automatizadas aprobadas |
| A9. Menú, registro y radicado | src/main.py y generación de TXT de 120 caracteres | Implementado; pendiente prueba de aceptación con el equipo |
| A10. Reportes | src/reportes.py y pruebas de las seis estadísticas con varios registros; mensaje de ausencia de datos para el promedio | Implementado; pruebas automatizadas en verificación |
| A11. Pruebas y correcciones | tests/test_core.py y GitHub Actions | En verificación después de las últimas correcciones |
| A12. Manual de usuario | docs/manual_de_usuario.md | Borrador revisado; pendiente prueba paso a paso |
| A13. Revisión final y sustentación | Aún no hay evidencia de revisión final o ensayo de sustentación | Pendiente |

### Control de horas

Registrar las horas reales por integrante y actividad en las reuniones del equipo. La estimación total de 50 horas es la referencia del proyecto y no debe confundirse con horas ya ejecutadas.

| Integrante | Horas estimadas según distribución del equipo | Horas reales registradas |
|---|---:|---:|
| José Miguel López Doria | [Acordar] | [Registrar] |
| Juliana Rivera Sarge | [Acordar] | [Registrar] |
| Víctor José Salgado Romero | [Acordar] | [Registrar] |
| Juan Pablo Quintero Gómez | [Acordar] | [Registrar] |
| Sebastián Cardona | [Acordar] | [Registrar] |

## 5. Riesgos

| Riesgo | Mitigación |
|---|---|
| Un integrante no entrega su parte | Seguimiento semanal según los acuerdos del acta combinada |
| Errores en validaciones o archivos | Pruebas con datos válidos e inválidos antes del 14 nov |
| Algún integrante no entiende el código | Cada uno explica su módulo al grupo antes de la sustentación |
