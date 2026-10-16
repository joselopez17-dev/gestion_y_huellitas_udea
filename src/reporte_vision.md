# Reporte de visión: Gestión y Huellitas UdeA

## 1. Descripción general

Gestión y Huellitas UdeA es un programa de consola, hecho en Python, que
permite al administrador del Movimiento Estudiantil de Perritos y Gaticos
(MEPEGA) registrar, consultar, actualizar y analizar las PQRS
(Peticiones, Quejas, Reclamos y Sugerencias) relacionadas con la atención
veterinaria de perros y gatos en la Universidad de Antioquia.

## 2. Problema que resuelve

Hoy las PQRS llegan por redes sociales, correo, papel y de voz a voz, y se
procesan a mano con papel y lápiz. Esto genera:

- Números de radicado repetidos o mal asignados.
- Dificultad para saber cuáles PQRS están por vencerse (plazo máximo de 30
  días calendario).
- Ausencia de estadísticas para tomar decisiones.

## 3. Objetivo general

Crear un programa de consola amigable que permita gestionar documentos PQRS
mediante archivos planos y exportar los resultados.

## 4. Objetivos específicos

1. Registrar PQRS con validación de datos y radicado consecutivo, sin
   repetidos.
2. Guardar cada tipo de solicitud en su propio archivo
   (`Peticion.txt`, `Queja.txt`, `Reclamo.txt`, `Sugerencia.txt`).
3. Imprimir un radicado en TXT de 120 caracteres de ancho.
4. Controlar el estado (Registrada → En proceso → Solucionada) y la fecha
   máxima de respuesta.
5. Generar el promedio de días de respuesta y cinco estadísticas adicionales.

## 5. Alcance

**Incluye:** menú de consola, registro, consulta, cambio de estado,
radicado en TXT y estadísticas.
**No incluye:** interfaz gráfica, base de datos, envío automático de
correos ni acceso de múltiples usuarios.

## 6. Usuarios y partes interesadas

| Parte interesada | Rol |
|---|---|
| Administrador de MEPEGA | Usuario principal del programa |
| Solicitantes de PQRS | Personas cuyos datos se registran |
| Profesor Julián Andrés Castillo | Product Owner (PO) |
| Equipo de desarrollo | Diseño, código y documentación |

## 7. Beneficios

- Radicados consecutivos y sin duplicados.
- Menos errores gracias a las validaciones.
- Seguimiento de plazos: se ve qué PQRS están por vencer.
- Estadísticas para mejorar la atención de perros y gatos.
- Comprobante impreso que certifica la información registrada.

## 8. Restricciones

- Lenguaje: Python, ejecución en consola.
- Almacenamiento: solo archivos planos.
- Repositorio organizado en `src/`, `docs/`, `images/` y `data/`.
- Plazo: Entrega 2 en la semana 16.
