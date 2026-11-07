# Pruebas de aceptación — Gestión y Huellitas UdeA

## 1. Datos de la sesión

Completar esta información durante la ejecución real. Utilizar únicamente datos ficticios.

- **Fecha:** [Registrar]
- **Persona que prueba:** [Registrar]
- **Versión de Python:** [Registrar]
- **Rama y commit:** [Registrar]
- **Sistema operativo:** [Registrar]
- **Resultado general:** [Pendiente / Aprobado / Requiere correcciones]

## 2. Evidencia de aceptación automatizada

**Resultado: aprobada en GitHub Actions.**

- **Fecha:** 7 de noviembre de 2026.
- **Rama:** `desarrollo`.
- **Commit con la suite de aceptación:** `e759cdeb67a6181d927da703a377863c86be9f79`.
- **Entornos:** Ubuntu y Windows (`ubuntu-latest` y `windows-latest`).
- **Python:** 3.12.
- **Resultado total:** 24/24 pruebas aprobadas (16 pruebas generales y 8 pruebas automatizadas de aceptación).
- **Ejecución:** [GitHub Actions — 24 pruebas aprobadas](https://github.com/joselopez17-dev/gestion_y_huellitas_udea/actions/runs/42411265362).

Las pruebas automatizadas utilizan entradas simuladas y una carpeta temporal; no crean ni modifican registros dentro de `data/` del proyecto. Cubren el registro de los cuatro tipos, reintento tras datos inválidos, persistencia al reabrir el gestor, consulta general, comprobantes, transiciones de estado, estadísticas y presentación de las cinco opciones del menú.

**Alcance de esta evidencia:** las pruebas automáticas fueron aprobadas. Esto no equivale a una revisión visual y manual realizada por los integrantes en su computador. Los pasos manuales siguientes deben completarse y registrarse antes de declarar la aceptación final.

## 3. Preparación

- [ ] Descargar o actualizar la rama desarrollo.
- [ ] Abrir una terminal en la carpeta raíz del repositorio.
- [ ] Ejecutar `python -m unittest discover -s tests -v`.
- [ ] Confirmar que las pruebas automatizadas terminan sin errores.
- [ ] Comprobar que la carpeta data no contiene datos reales o registros antiguos que puedan alterar el ejercicio.

## 4. Prueba de registro

Registrar una solicitud ficticia de cada tipo: Petición, Queja, Reclamo y Sugerencia.

- [ ] El menú presenta las cinco opciones solicitadas.
- [ ] Un nombre con números es rechazado y vuelve a solicitarse.
- [ ] Un documento con letras o caracteres especiales es rechazado.
- [ ] Un teléfono que no contiene exactamente 10 dígitos es rechazado.
- [ ] Un correo sin estructura válida es rechazado.
- [ ] Una fecha futura o con formato incorrecto es rechazada.
- [ ] La dirección se puede dejar vacía.
- [ ] Se acepta un asunto y una descripción que cumplen las longitudes requeridas.
- [ ] El sistema asigna el ID 1 a la primera solicitud de cada tipo.
- [ ] La fecha máxima de respuesta corresponde a 30 días calendario después de la fecha de radicación.
- [ ] El estado inicial se registra como Registrada.

## 5. Prueba de almacenamiento y persistencia

- [ ] Se crean Peticion.txt, Queja.txt, Reclamo.txt y Sugerencia.txt dentro de data.
- [ ] Cada archivo conserva sus propios consecutivos.
- [ ] Los registros se conservan después de cerrar y volver a ejecutar el programa.
- [ ] La consulta general reúne las solicitudes almacenadas.
- [ ] Los registros se pueden consultar indicando tipo y consecutivo.

## 6. Prueba de radicado

Abrir el comprobante generado para cada tipo de solicitud.

- [ ] El comprobante se guarda dentro de data/radicados.
- [ ] Cada línea del comprobante tiene exactamente 120 caracteres.
- [ ] El documento muestra el consecutivo, fechas, estado y datos del solicitante.
- [ ] La dirección vacía aparece como N/A.
- [ ] La descripción detallada no aparece en el comprobante.

## 7. Prueba de cambio de estado

- [ ] Una solicitud nueva aparece como Registrada.
- [ ] Se permite cambiar de Registrada a En proceso.
- [ ] Se permite cambiar de En proceso a Solucionada.
- [ ] Se rechaza pasar directamente de Registrada a Solucionada.
- [ ] Se rechaza retroceder de estado.
- [ ] Al quedar Solucionada, se registra la fecha de respuesta.

## 8. Prueba de estadísticas

- [ ] El promedio se calcula con solicitudes solucionadas que tengan fecha de respuesta.
- [ ] Cuando no hay solicitudes solucionadas, el sistema muestra Sin datos y no un promedio de cero días.
- [ ] El conteo por tipo de solicitud coincide con los registros.
- [ ] El conteo por tipo de mascota coincide con los registros.
- [ ] La distribución por estado coincide con los registros.
- [ ] La PQRS activa más antigua corresponde a la fecha de radicación más antigua entre las no solucionadas.
- [ ] Las solicitudes vencidas o próximas a vencer se identifican de acuerdo con la fecha máxima de respuesta.

## 9. Resultado y evidencias

| Prueba | Resultado (Aprobada / Fallida / No ejecutada) | Observaciones o evidencia |
|---|---|---|
| Pruebas automatizadas (CI) | Aprobada | 24/24; Ubuntu y Windows; Python 3.12; commit `e759cde` |\n| Preparación manual | [Registrar] | [Registrar] |
| Registro | [Registrar] | [Registrar] |
| Almacenamiento y persistencia | [Registrar] | [Registrar] |
| Radicado | [Registrar] | [Registrar] |
| Cambio de estado | [Registrar] | [Registrar] |
| Estadísticas | [Registrar] | [Registrar] |

### Incidentes encontrados

| N.º | Descripción del problema | Pasos para reproducirlo | Responsable | Estado |
|---:|---|---|---|---|
| 1 | [Registrar si ocurre] | [Registrar] | [Registrar] | [Pendiente / Corregido] |

### Aprobación del equipo

- **Conclusión:** [Aprobado / Aprobado con observaciones / Requiere correcciones]
- **Integrantes que participaron:** [Registrar]
- **Fecha de aprobación:** [Registrar]

**Importante:** no marcar la prueba como aprobada hasta ejecutarla en el computador del equipo. No adjuntar capturas que expongan documentos, teléfonos, correos o datos personales reales.
