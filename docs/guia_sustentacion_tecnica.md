# Guía de sustentación técnica — Gestión y Huellitas UdeA

> Material de preparación basado en el código de la rama `desarrollo`. Las respuestas describen la implementación actual; conviene abrir los archivos y señalar las funciones durante la sustentación.

## 1. Cómo explicar la arquitectura en un minuto

El programa está dividido en cuatro módulos para separar responsabilidades:

| Archivo | Clase | Qué hace |
|---|---|---|
| `src/main.py` | `c_main` | Controla el menú, solicita datos, llama las validaciones y coordina las operaciones. |
| `src/validaciones.py` | `c_validaciones` | Centraliza las reglas de validación y la normalización de opciones. |
| `src/archivos.py` | `c_archivos` | Administra los cuatro archivos de datos: lectura, escritura, consecutivos, búsquedas, estados y radicados. |
| `src/reportes.py` | `c_reportes` | Calcula los seis indicadores a partir de los registros almacenados. |

**Una forma de decirlo:** “Separamos la interacción, las reglas de validación, el almacenamiento y los reportes. Así, el menú no necesita conocer los detalles de cómo se escribe un archivo ni cómo se calcula cada indicador”.

### Recorrido de una operación

1. El usuario selecciona una opción en el método `ejecutar()` de `c_main`.
2. `c_main` solicita los datos y utiliza `c_validaciones` para comprobarlos.
3. Para guardar o consultar, `c_main` llama a los métodos de `c_archivos`.
4. Para mostrar indicadores, llama a `c_reportes`, que obtiene los registros mediante `c_archivos`.
5. El menú vuelve a mostrarse hasta que el usuario elige salir.

## 2. Preguntas técnicas probables y respuestas

### Arquitectura y programación orientada a objetos

**1. ¿Cuál es el punto de entrada del programa?**

El bloque `if __name__ == "__main__":` llama a `main()`. Esa función configura la salida de texto en UTF-8 cuando el entorno lo permite, crea un objeto `c_main` y ejecuta su método `ejecutar()`.

**2. ¿Qué responsabilidad tiene cada clase?**

- `c_main`: interacción con el usuario y coordinación del flujo.
- `c_validaciones`: reglas para aceptar o rechazar entradas.
- `c_archivos`: persistencia de datos y generación de comprobantes.
- `c_reportes`: cálculos estadísticos y consultas de seguimiento.

La idea es evitar que una sola clase concentre todas las tareas.

**3. ¿Por qué se usan objetos y no se escribe todo en funciones sueltas?**

Las clases agrupan operaciones que trabajan sobre una misma responsabilidad. Por ejemplo, `c_archivos` conserva las rutas de datos y ofrece métodos para guardar, buscar y actualizar registros. `c_main` conserva los gestores que utiliza durante la ejecución.

**4. ¿Qué hace `__init__`?**

Es el inicializador del objeto. En `c_main`, crea `self.archivos = c_archivos()` y `self.reportes = c_reportes(self.archivos)`. Así, el módulo de reportes utiliza el mismo gestor de archivos que el menú.

**5. ¿Por qué hay métodos `@staticmethod`, `@classmethod` y métodos normales?**

Un método normal recibe `self` porque trabaja con el estado de un objeto. Un `@staticmethod` no necesita acceder ni a `self` ni a `cls`; por ejemplo, algunos métodos de validación. Un `@classmethod` recibe la clase en `cls` y resulta útil cuando se consultan atributos de clase, como `ARCHIVOS` o `ANCHO_RADICADO`.

**6. ¿Para qué sirve el bloque `try/except ImportError` en los módulos?**

Permite intentar primero importaciones relativas, apropiadas cuando el código se ejecuta como paquete, y usar importaciones directas como alternativa al ejecutar `python src/main.py`.

### Validaciones y captura de datos

**7. ¿Cómo evita el programa aceptar cualquier texto como opción?**

El método `obtener_opcion()` normaliza el texto y lo compara con una lista de opciones permitidas. La normalización usa Unicode para separar las tildes, elimina las marcas diacríticas, convierte a minúsculas con `casefold()` y unifica espacios. Por eso puede reconocer opciones aunque el usuario cambie mayúsculas o escriba una tilde de forma distinta.

**8. ¿Qué diferencia hay entre validar un campo y normalizar una opción?**

Validar comprueba si el dato cumple una regla, por ejemplo, que el teléfono tenga diez dígitos. Normalizar permite comparar una entrada con una lista oficial y devolver el valor escrito de forma uniforme, por ejemplo, `Petición`.

**9. ¿Por qué se usa `re.fullmatch()` en varias validaciones?**

Porque exige que toda la entrada cumpla el patrón. No basta con que una parte del texto coincida. Por ejemplo, el número de documento debe contener únicamente entre 3 y 15 dígitos.

**10. ¿Cómo se valida la fecha?**

Se exige el formato ISO `AAAA-MM-DD` y se intenta convertir con `date.fromisoformat()`. Esto permite detectar fechas imposibles, como un día que no existe en ese mes. Además, se compara con `date.today()` para rechazar fechas futuras.

**11. ¿El correo se valida con todas las reglas de un estándar internacional?**

No. `validar_correo()` aplica una comprobación básica de estructura: un solo símbolo `@`, parte local y dominio no vacíos, puntos y etiquetas del dominio, ausencia de espacios y un límite de longitud. No pretende implementar todas las reglas posibles de los estándares de correo.

**12. ¿Qué pasa cuando el usuario escribe un dato inválido?**

Los métodos `_pedir_validado()` y `_pedir_opcion()` usan un ciclo `while True`. Si el dato no pasa la comprobación, muestran un mensaje y vuelven a solicitarlo. El flujo no continúa hasta recibir una entrada aceptada.

### Archivos, JSON y consecutivos

**13. ¿Dónde se guardan los datos?**

En la carpeta `data/`, en cuatro archivos independientes: `Peticion.txt`, `Queja.txt`, `Reclamo.txt` y `Sugerencia.txt`. Los comprobantes se guardan en `data/radicados/`.

**14. ¿Qué significa que el formato sea JSON por líneas (JSONL)?**

Cada línea del archivo contiene un objeto JSON completo. El programa recorre el archivo línea por línea y usa `json.loads()` para convertir cada línea en un diccionario de Python. Para escribir, convierte cada diccionario con `json.dumps()` y agrega un salto de línea.

**15. ¿Por qué hay cuatro archivos y no uno solo?**

La implementación separa los tipos de PQRS y mantiene un consecutivo independiente para cada tipo. Por eso puede existir una Petición 1 y una Queja 1: el identificador se interpreta junto con el tipo de solicitud, no es un ID global único.

**16. ¿Cómo se calcula el siguiente consecutivo?**

En `guardar_pqrs()` se leen los registros del archivo del tipo seleccionado, se toma el mayor ID existente y se suma uno. Si el archivo no tiene registros, el valor inicial es 1. La expresión usada es `max(..., default=0) + 1`.

**17. ¿Cómo se evita construir una ruta con un tipo inventado por el usuario?**

Antes de formar la ruta, `_tipo_oficial()` compara el tipo con las opciones oficiales. Si no corresponde a una de ellas, genera un `ValueError`. El nombre del archivo se obtiene del diccionario fijo `ARCHIVOS`, no directamente del texto libre del usuario.

**18. ¿Qué hace `Path(__file__).resolve()`?**

Obtiene la ubicación del archivo de código y permite construir la ruta de la carpeta del proyecto sin depender de desde qué directorio se haya abierto la terminal. Si no se entrega una carpeta personalizada, los datos se ubican en la carpeta `data` de la raíz del proyecto.

**19. ¿Por qué se escribe primero en un archivo temporal y luego se usa `os.replace()`?**

`_guardar_archivo()` escribe el contenido completo en un archivo con extensión `.tmp` y después reemplaza el archivo original con `os.replace()`. Esto reduce el riesgo de dejar el archivo principal parcialmente escrito si ocurre un problema durante la escritura. No convierte el sistema en una base de datos ni resuelve conflictos de escritura simultánea.

**20. ¿Qué pasa si una línea JSON está dañada?**

`_leer_archivo()` captura `json.JSONDecodeError` y lanza un `ValueError` que identifica el nombre del archivo y el número de línea. También verifica que el JSON leído sea un diccionario. Así, el problema no se interpreta silenciosamente como un registro válido.

### Fechas y estados

**21. ¿Cómo se calcula la fecha máxima de respuesta?**

En `guardar_pqrs()`, convierte la fecha de radicación en un objeto `date` y suma `timedelta(days=30)`. Son 30 días calendario, no días hábiles.

**22. ¿Qué estados puede tener una PQRS y qué transiciones están permitidas?**

Los estados son `Registrada`, `En proceso` y `Solucionada`. El diccionario `TRANSICIONES` permite únicamente `Registrada → En proceso` y `En proceso → Solucionada`. No permite saltarse el estado intermedio ni retroceder.

**23. ¿Cuándo se guarda la fecha de respuesta?**

Cuando `cambiar_estado()` recibe la transición válida a `Solucionada`, guarda la fecha actual en `fecha_respuesta`. Esa fecha se utiliza después en el promedio de días de respuesta.

### Radicado y manejo de errores

**24. ¿Cómo garantiza el programa que cada línea del radicado tenga 120 caracteres?**

La clase `c_archivos` define `ANCHO_RADICADO = 120`. Los métodos `_linea_centrada()` y `_lineas_campo()` construyen líneas con ese ancho. Al final, `construir_radicado()` comprueba todas las longitudes y lanza `AssertionError` si alguna no cumple.

**25. ¿Por qué no se incluye la descripción detallada en el comprobante?**

El método `construir_radicado()` selecciona expresamente los campos que se muestran y no agrega `descripcion_detallada`. La descripción sí se almacena en el registro; simplemente no se imprime en el TXT del radicado.

**26. ¿Qué ocurre si se guarda la PQRS pero falla la creación del radicado?**

Primero se guarda el registro en el archivo de datos. Después se intenta generar el comprobante. Si esa segunda operación produce un `OSError`, el programa informa que la PQRS sí quedó registrada y muestra el consecutivo. Esto evita que el usuario piense que perdió el registro y lo cree de nuevo por error.

**27. ¿Qué ocurre si se actualiza el estado y falla la actualización del radicado?**

El cambio de estado se guarda primero. Luego se intenta regenerar el TXT. Si falla la generación, el programa informa que el estado sí quedó actualizado, aunque el comprobante no se haya podido refrescar.

**28. ¿Qué diferencia hay entre `ValueError` y `OSError` en este proyecto?**

En términos generales, `ValueError` se usa cuando un valor no cumple las reglas esperadas, como un tipo o una transición no permitidos. `OSError` cubre errores del sistema operativo relacionados con operaciones de archivos, como problemas al escribir o reemplazar un archivo.

### Reportes y pruebas

**29. ¿Cómo calcula el promedio de días de respuesta?**

`calcular_promedio_dias_respuesta()` filtra los registros solucionados que tengan fecha de radicación y fecha de respuesta. Convierte las fechas con `date.fromisoformat()`, resta ambas fechas, obtiene los días, suma los resultados y divide por la cantidad de registros. Finalmente usa `round()` para devolver un entero.

**30. ¿Por qué devuelve `None` cuando no hay PQRS solucionadas?**

Porque no existe una muestra para calcular el promedio. Devolver cero podría interpretarse como si las solicitudes se hubieran resuelto en cero días. Por eso `c_reportes` devuelve `None` y `c_main` lo presenta como “Sin datos”.

**31. ¿Cómo identifica las PQRS próximas a vencer?**

`pqrs_proximas_a_vencer(dias=5)` omite las solicitudes solucionadas, calcula los días entre hoy y la fecha máxima de respuesta, y conserva las que tienen cinco días o menos restantes. Como no establece un límite inferior, también incluye las vencidas. Después ordena por días restantes.

**32. ¿Qué hacen las pruebas automatizadas?**

El archivo `tests/test_core.py` usa `unittest`. Comprueba validaciones, almacenamiento, consecutivos independientes, cambios de estado, promedio, fechas límite, radicados de 120 caracteres y flujos del menú. Usa `tempfile.TemporaryDirectory()` para guardar datos temporales y no alterar los datos reales del proyecto; también usa `unittest.mock.patch` para simular entradas y salidas.

**33. ¿Cómo se prueba un error sin provocar un fallo real del disco?**

Con `patch.object()` se reemplaza temporalmente un método, como `generar_radicado()`, por uno que lanza `OSError`. Luego se verifica que el registro o el cambio de estado permanezca guardado. Es una prueba controlada del manejo de errores.

## 3. Límites técnicos que deben reconocer

Si el profesor pregunta por el alcance, respondan con precisión:

- Es una aplicación de consola en Python.
- Guarda datos localmente en archivos de texto JSON por líneas.
- No usa una base de datos relacional.
- No tiene autenticación ni control de permisos.
- Los archivos locales no están cifrados.
- No está diseñada para escrituras simultáneas de varios usuarios.
- Los 30 días para la fecha máxima son calendario.
- La validación del correo es básica y no garantiza que la dirección exista.
- Los reportes dependen de la calidad y consistencia de los datos almacenados.

Reconocer una limitación no significa que el programa esté mal; significa explicar con honestidad qué resuelve esta versión y qué quedaría para una versión futura.

## 4. Demostración técnica sugerida

Para una demostración corta, preparen una carpeta de datos de prueba y sigan esta secuencia:

1. Ejecutar `python src/main.py` y explicar el punto de entrada.
2. Registrar una PQRS de prueba. Ingresar primero un nombre inválido para mostrar el ciclo de validación.
3. Mostrar el archivo correspondiente dentro de `data/` y explicar que cada línea es un JSON.
4. Consultar el registro usando el tipo y el consecutivo.
5. Abrir el TXT generado y comprobar que sus líneas tienen 120 caracteres y que no contiene la descripción detallada.
6. Cambiar el estado primero a “En proceso” y después a “Solucionada”.
7. Mostrar las estadísticas y explicar por qué el promedio solo aparece cuando existen registros solucionados con fecha de respuesta.
8. Ejecutar las pruebas con `python -m unittest discover -s tests -v`.

Usen datos ficticios durante la demostración. No publiquen ni proyecten documentos, teléfonos o correos reales.

## 5. Código que conviene saber ubicar rápidamente

| Pregunta del profesor | Abrir archivo y método |
|---|---|
| ¿Dónde inicia? | `src/main.py` → `main()`, `c_main.ejecutar()` |
| ¿Dónde se controla la captura? | `src/main.py` → `_pedir_validado()`, `_pedir_opcion()`, `_capturar_datos_pqrs()` |
| ¿Dónde se valida el correo o la fecha? | `src/validaciones.py` → `validar_correo()`, `validar_fecha_radicacion()` |
| ¿Dónde se asigna el ID? | `src/archivos.py` → `guardar_pqrs()` |
| ¿Dónde se lee JSONL? | `src/archivos.py` → `_leer_archivo()` |
| ¿Dónde se actualiza el estado? | `src/archivos.py` → `cambiar_estado()` |
| ¿Dónde se construye el comprobante? | `src/archivos.py` → `construir_radicado()` |
| ¿Dónde se calcula el promedio? | `src/reportes.py` → `calcular_promedio_dias_respuesta()` |
| ¿Dónde se prueban los errores? | `tests/test_core.py` → pruebas de fallo de generación del radicado |

## 6. Recomendación para responder

Cuando el profesor pregunte “¿cómo funciona?”, respondan en este orden: **archivo → método → dato que recibe → proceso que realiza → resultado que devuelve o guarda**. Si no recuerdan una línea exacta, expliquen el flujo y ubiquen el método en el código; no inventen funciones ni características que el programa todavía no tiene.
