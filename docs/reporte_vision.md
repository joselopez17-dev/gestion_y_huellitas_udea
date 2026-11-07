# Reporte de visión — Gestión y Huellitas UdeA

## 1. Descripción general

Gestión y Huellitas UdeA es un programa académico de consola desarrollado en Python para registrar, consultar y hacer seguimiento a Peticiones, Quejas, Reclamos y Sugerencias (PQRS) relacionadas con la atención de perros y gatos en el contexto de la Universidad de Antioquia.

El sistema está dirigido a una persona administradora u operadora encargada de registrar las solicitudes y consultar su evolución. Utiliza cuatro archivos de texto independientes —uno por cada tipo de PQRS— y genera un comprobante de radicación en formato TXT.

**Aclaración sobre el nombre MEPEGA:** la guía del curso presenta “MEPEGA” como una denominación ficticia y humorística, usada únicamente con fines académicos e ilustrativos. Por eso, este reporte no la presenta como una dependencia, organización ni servicio oficial de la Universidad de Antioquia.

## 2. Necesidad que aborda

El proyecto parte de la necesidad académica de organizar en un solo programa la información de las PQRS recibidas por distintos canales. Cuando el registro y el seguimiento se hacen de forma dispersa o manual, pueden aparecer dificultades como:

- Asignar consecutivos y localizar solicitudes.
- Identificar solicitudes que están próximas a cumplir el plazo de respuesta.
- Consultar el estado de una solicitud sin revisar varios registros por separado.
- Obtener estadísticas que ayuden a describir el volumen y el estado de las PQRS.

Estos puntos describen la necesidad que el proyecto busca atender; no constituyen una afirmación de que la Universidad de Antioquia tenga actualmente un procedimiento institucional específico con esas deficiencias.

## 3. Objetivo general

Desarrollar un programa de consola en Python que permita registrar, consultar y actualizar PQRS relacionadas con la atención de perros y gatos, almacenando cada tipo de solicitud en su propio archivo plano y generando comprobantes y estadísticas de seguimiento.

## 4. Objetivos específicos

1. Capturar y validar los datos del solicitante y de la PQRS.
2. Asignar consecutivos independientes para Peticiones, Quejas, Reclamos y Sugerencias.
3. Guardar los registros en cuatro archivos de texto UTF-8, uno por cada tipo de solicitud.
4. Calcular la fecha máxima de respuesta sumando 30 días calendario a la fecha de radicación.
5. Controlar el estado de cada solicitud con el flujo Registrada → En proceso → Solucionada.
6. Generar un comprobante TXT con un ancho exacto de 120 caracteres por línea, sin incluir la descripción detallada.
7. Calcular el promedio entero de días de respuesta y cinco estadísticas adicionales de gestión.

## 5. Alcance

**Incluye:**

- Menú de consola.
- Registro y validación de PQRS.
- Almacenamiento en cuatro archivos planos independientes.
- Consulta por tipo y consecutivo.
- Actualización secuencial del estado.
- Generación de radicados TXT.
- Consulta de seis indicadores estadísticos.

**No incluye:**

- Interfaz gráfica o aplicación móvil.
- Base de datos relacional o servicio en la nube.
- Envío automático de correos o notificaciones.
- Acceso simultáneo de varios operadores.
- Autenticación de usuarios ni administración de permisos dentro del programa.

## 6. Usuarios y partes interesadas

| Parte interesada | Participación |
|---|---|
| Administrador u operador | Registra, consulta y actualiza las PQRS. |
| Solicitantes | Proporcionan la información que se registra en las solicitudes. |
| Profesor Julián Andrés Castillo | Cumple el rol académico de Product Owner (PO) descrito en la guía del curso. |
| Equipo de desarrollo | Analiza requisitos, implementa, prueba y documenta el programa. |

## 7. Beneficios esperados

- Tener un consecutivo independiente para cada tipo de PQRS.
- Reducir errores de digitación mediante validaciones.
- Facilitar la consulta del estado de las solicitudes.
- Identificar solicitudes vencidas o próximas a vencer.
- Disponer de indicadores básicos para describir la gestión.
- Entregar un comprobante TXT con los datos esenciales de cada radicación.

Estos son beneficios esperados del diseño; no se presentan como resultados medidos de una implementación institucional.

## 8. Restricciones y supuestos

- Lenguaje de programación: Python 3.
- Interacción: consola.
- Almacenamiento: archivos planos UTF-8 dentro de data/.
- El programa se ejecuta localmente y no requiere paquetes externos.
- Los archivos generados pueden contener datos personales; por eso se excluyen del control de versiones y no deben publicarse.
- El plazo académico indicado para la Entrega 2 corresponde a la semana 16.
