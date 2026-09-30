# Tarea independiente: acceso a servidores científicos y uso de APIs

**Asignatura:** Ciencia de Datos para Nanociencias  
**Modalidad:** trabajo individual  


## Objetivo

Investigar cómo se accede a los datos o herramientas de un servidor científico, identificar si ofrece una API y demostrar un ejemplo de uso. Explicar si existe un cliente o biblioteca de Python y, cuando no exista, mostrar otra forma de acceder al servicio.

La actividad debe permitir que un compañero con conocimientos básicos de Python comprenda el recurso y pueda repetir el ejemplo.

## Servidores propuestos

Cada estudiante analizará **uno** de los siguientes recursos, según la asignación del docente.

| Número | Recurso | Sitio web | Área del análisis |
|---|---|---|---|
| 1 | PubChem | https://pubchem.ncbi.nlm.nih.gov/ | Información de compuestos y propiedades moleculares |
| 2 | CAS Common Chemistry | https://commonchemistry.cas.org/ | Información de sustancias e identificadores CAS Registry Number |
| 3 | RCSB Protein Data Bank (RCSB PDB) | https://www.rcsb.org/ | Estructuras de macromoléculas y sus datos asociados |
| 4 | EMBL-EBI Job Dispatcher | https://www.ebi.ac.uk/jdispatcher/ | Herramientas de análisis que reciben secuencias de nucleótidos o aminoácidos |

**Delimitación de CAS:** para esta tarea se analizará **CAS Common Chemistry**. 

**Delimitación del cuarto recurso:** Job Dispatcher reúne varias herramientas. Selecciona una que acepte el tipo de secuencia de tu ejemplo, como una búsqueda con NCBI BLAST+ o un alineamiento. Indica la herramienta, el tipo de secuencia y la base de datos de destino, cuando corresponda. No todas las herramientas aceptan las mismas entradas.

# Realiza una presentación que responda:

## 1. Descripción general del servidor

- ¿Qué institución u organización mantiene el recurso?
- ¿Para qué sirve y qué pregunta científica puede ayudar a responder?
- ¿Contiene una base de datos, ofrece herramientas de análisis o ambas cosas?
- ¿Qué tipos de datos admite y cuáles devuelve?
- ¿Cuáles son sus principales funciones? Describe al menos tres, si el servicio las ofrece.
- ¿Cómo podría utilizarse en nanociencias? Propón una aplicación concreta.

Distingue lo que el servidor proporciona de lo que tendrías que calcular después. Por ejemplo, una propiedad molecular no caracteriza por sí sola el tamaño o la morfología de una nanopartícula.

## 2. ¿Tiene API?

Investiga en la **documentación oficial** y explica:

1. Si existe una API y cómo se llama.
2. Dónde se encuentra su documentación.
3. Qué operaciones permite: búsqueda, consulta de registros, descarga, envío de secuencias o ejecución de análisis, según el recurso.
4. Qué tecnología utiliza, cuando la documentación lo indique: REST, GraphQL u otra. Explica su significado en una o dos frases.
5. Qué métodos HTTP requiere la operación elegida, por ejemplo `GET` o `POST`.
6. Qué parámetros o datos de entrada necesita.
7. Qué formatos devuelve: JSON, XML, FASTA, archivos estructurales u otros, según corresponda.
8. Si requiere registro, clave de acceso, correo electrónico, suscripción o acceso institucional.
9. Qué límites o condiciones de uso señala el proveedor.
10. Si entrega el resultado inmediatamente o devuelve un identificador de trabajo que debe consultarse después.

Incluye **un endpoint de ejemplo**, si está documentado. Un endpoint es una dirección de la API que permite realizar una operación específica.

Si el recurso ofrece varias APIs, menciona las principales y explica cuál utilizarás. No es necesario probarlas todas.

**Si no encuentras una API:** indica qué documentación revisaste y escribe «no se identificó una API pública documentada». No concluyas que no existe ninguna API solamente porque no aparece en la página principal.

**Si la API requiere acceso que no tienes:** distingue «existe, pero no tengo acceso» de «no existe». Documenta el requisito y realiza la demostración mediante la interfaz web disponible. No se exige contratar servicios para esta tarea.

## 3. Acceso desde Python

Comprueba si existe una biblioteca, cliente o script que facilite el acceso al recurso desde Python.

### Si existe un cliente de Python

Describe:

- Nombre del paquete o script y enlace a su documentación o repositorio.
- Si lo mantiene el proveedor del servidor o una comunidad externa.
- Cómo se instala y qué dependencias necesita.
- Qué funciones ofrece y cuáles usarás en tu ejemplo.
- Cómo se relaciona con la API web del servidor.

No basta con escribir el nombre del paquete: muestra una llamada y explica sus entradas y resultados.

### Si hay API web, pero no identificas un cliente específico de Python

Muestra cómo acceder directamente con una biblioteca HTTP, como `requests`. Explica la URL, el método, los parámetros y cómo lees la respuesta.

**Una API web puede utilizarse desde Python aunque no exista un paquete específico para ese servidor.** La biblioteca `requests` es una herramienta general para hacer peticiones HTTP, no un cliente exclusivo del recurso.

### Si no hay API pública documentada o no puedes utilizarla

Demuestra el acceso mediante la interfaz web o una descarga autorizada:

1. Página a la que ingresas.
2. Consulta o archivo de entrada.
3. Opciones seleccionadas.
4. Resultado obtenido.
5. Forma de guardar o descargar los datos, si está disponible.

Si descargas un archivo, muestra cómo lo abres en Python cuando sea viable. Diferencia claramente la descarga manual del acceso automatizado mediante API.

## 4. Demostración de uso

Diseña y ejecuta **un ejemplo pequeño y reproducible**. Elige una de estas posibilidades o una equivalente:

| Recurso | Posible ejemplo |
|---|---|
| PubChem | Buscar un compuesto y obtener su identificador y dos propiedades disponibles |
| CAS Common Chemistry | Consultar una sustancia por nombre o CAS Registry Number y describir la información que devuelve |
| RCSB PDB | Buscar o consultar una estructura, describir sus metadatos y descargar un archivo disponible |
| EMBL-EBI Job Dispatcher | Enviar una secuencia de nucleótidos o aminoácidos a una herramienta y recuperar e interpretar el resultado |

El ejemplo debe contener:

1. **Pregunta:** qué deseas consultar o analizar.
2. **Entrada:** nombre, identificador, secuencia o archivo utilizado y su procedencia.
3. **Procedimiento:** código comentado o pasos de la interfaz web.
4. **Ejecución:** evidencia del resultado real, como una salida del cuaderno, archivo o captura de pantalla.
5. **Interpretación:** qué significa el resultado y cómo responde a la pregunta.
6. **Limitación:** qué no puedes concluir a partir de ese resultado.
7. **Reproducibilidad:** URL, parámetros, fecha de consulta y versiones de las bibliotecas utilizadas, cuando corresponda.

No entregues únicamente código copiado. Debes ejecutarlo y explicar lo que hace. Si una restricción de acceso impide ejecutar la API, identifica esa restricción y demuestra la alternativa web. No presentes datos simulados como resultados del servidor.

### Requisitos adicionales para secuencias

Para Job Dispatcher:

- Indica si tu entrada corresponde a ADN, ARN o proteína y comprueba que la herramienta la admita.
- Conserva la secuencia y su identificador de origen. Si usas FASTA, explica el encabezado y el cuerpo de la secuencia.
- Justifica la herramienta elegida y la base de datos consultada, si aplica.
- Si el servicio devuelve un identificador de trabajo, muestra cómo verificas el estado y recuperas el resultado al finalizar.
- Interpreta al menos dos campos del resultado. En una búsqueda de similitud pueden ser identidad, cobertura o valor E, si están disponibles.
- Explica que una coincidencia de secuencia no demuestra por sí sola una función biológica.

## 5. Ficha de síntesis

Incluye esta tabla completada al final del informe. Usa «no aplica» o «no se identificó» cuando corresponda y justifica esa respuesta.

| Aspecto | Respuesta |
|---|---|
| Nombre y URL del recurso | |
| Institución responsable | |
| Tipo de datos o análisis | |
| Funciones principales | |
| API y enlace a documentación | |
| Operación y endpoint del ejemplo | |
| Método y parámetros de entrada | |
| Formato de salida | |
| Requisitos de acceso | |
| Límites o condiciones relevantes | |
| Cliente de Python y quién lo mantiene | |
| Alternativa de acceso, si corresponde | |
| Aplicación propuesta en nanociencias | |
| Fecha de consulta | |

## Entregables

- **Presentación**, 20 minutos, con los apartados anteriores, la ficha y las referencias.
- **Cuaderno `.ipynb` o script `.py`**, cuando el ejemplo utilice Python. Incluye instrucciones para ejecutarlo.
- **Evidencia del ejemplo:** archivos obtenidos o capturas suficientes para comprobar la consulta y su resultado.

Cuando el ejemplo sea exclusivamente web, el informe debe contener los pasos y las capturas necesarios para repetirlo. No es obligatorio inventar código para un servicio sin acceso programático disponible.

## Criterios de evaluación

| Criterio | Puntos |
|---|---:|
| Descripción del recurso y aplicación en nanociencias | 20 |
| Investigación de la API y condiciones de acceso, respaldada por documentación | 25 |
| Descripción del cliente de Python o explicación de la alternativa de acceso | 20 |
| Ejemplo ejecutado, reproducible e interpretado | 25 |
| Claridad, ficha de síntesis y referencias | 10 |
| **Total** | **100** |

Se evalúa la calidad de la investigación y de la demostración. La inexistencia de una API pública o la falta de acceso a una API restringida no penalizan por sí solas, si se justifican y se demuestra una alternativa disponible.

## Fuentes iniciales

Estas fuentes sirven como punto de partida. Consulta la documentación específica de la operación que elijas y registra la fecha de consulta.

- [PubChem PUG REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)
- [Tutorial de PubChem PUG REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial)
- [CAS Common Chemistry](https://commonchemistry.cas.org/)
- [Solicitud de acceso a la API de CAS Common Chemistry](https://www.cas.org/services/commonchemistry-api)
- [RCSB PDB: descripción de APIs web](https://www.rcsb.org/docs/programmatic-access/web-apis-overview)
- [RCSB PDB: herramientas de código abierto](https://www.rcsb.org/docs/programmatic-access/open-source-tools)
- [EMBL-EBI Job Dispatcher: documentación](https://www.ebi.ac.uk/jdispatcher/docs/)
- [Job Dispatcher: acceso programático y clientes](https://www.ebi.ac.uk/jdispatcher/docs/webservices/)
- [Job Dispatcher: clientes de ejemplo en Python](https://github.com/ebi-jdispatcher/webservice-clients)

**Referencia temporal de estas indicaciones:** 30 de septiembre de 2026. Verifica las condiciones vigentes al realizar la tarea.
