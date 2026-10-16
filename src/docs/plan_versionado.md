# Plan de versionado: Gestión y Huellitas UdeA

## 1. Convención

Se usa versionado semántico `vMAYOR.MENOR.PARCHE`:

- **MAYOR:** versión final entregable (v1.0.0).
- **MENOR:** se completa un módulo o grupo de documentos.
- **PARCHE:** correcciones sin funcionalidad nueva.

Cada versión se marca con una etiqueta (tag) en GitHub. Los commits se
escriben en español y en infinitivo, por ejemplo: `Agregar validación de correo`.

## 2. Versiones y avance

Inicio: 15 oct 2026 (día 0). Entrega final: 22 nov 2026 (día 38).
El avance es el porcentaje de las 50 horas del plan de proyecto.

| Versión | Día | Fecha | Procedimiento relevante | Avance |
|---|---|---|---|---|
| v0.1.0 | 6 | 21 oct | Documentación de la Entrega 1: README, reporte de visión, requisitos, plan de proyecto, plan de versionado y estructura `src/`, `docs/`, `images/`, `data/` | 34 % |
| v0.2.0 | 10 | 25 oct | Diseño del algoritmo: diagrama de flujo y clases | 44 % |
| v0.3.0 | 16 | 31 oct | `validaciones.py` y `archivos.py` | 64 % |
| v0.4.0 | 23 | 7 nov | Menú, registro, radicado de 120 caracteres y `reportes.py` | 84 % |
| v0.9.0 | 30 | 14 nov | Pruebas y correcciones: programa completo y probado | 92 % |
| v0.9.1 | 31 | 15 nov | Manual de usuario en `docs/` | 96 % |
| v1.0.0 | 35 | 19 nov | Revisión final y preparación de la sustentación | 100 % |
| Entrega 2 | 38 | 22 nov | Entrega oficial | 100 % |

## 3. Ramas

- `main`: versión estable, solo recibe código revisado.
- `desarrollo`: integración del trabajo del equipo.
- `modulo/<nombre>`: una rama por módulo (por ejemplo `modulo/validaciones`).

## 4. Procedimiento para publicar una versión

1. Fusionar la rama del módulo en `desarrollo` y probar.
2. Fusionar `desarrollo` en `main`.
3. Crear la etiqueta: `git tag v0.3.0` y luego `git push --tags`.
4. Registrar la versión y la fecha en este documento.

## 5. Control de cambios

Cualquier cambio de alcance se acuerda con todo el equipo, queda
registrado en las actas y se refleja en una nueva versión.
