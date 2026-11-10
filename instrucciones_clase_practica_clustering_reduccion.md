# Clase práctica: clustering y reducción de dimensionalidad

**Ruta de trabajo:** datos → preparación → K-means → clustering jerárquico → comparación → PCA para visualizar los grupos.

Al terminar podrás explicar por qué se escalan las variables, explorar el número de grupos, comparar dos particiones y representar sus resultados en dos dimensiones. Ejecuta las celdas en orden y responde las preguntas durante la práctica.

**Duración sugerida:** 90–120 minutos. **Requisitos:** Python con `numpy`, `pandas`, `matplotlib`, `scipy` y `scikit-learn`. Si faltan paquetes, instálalos en el entorno del cuaderno con `%pip install numpy pandas matplotlib scipy scikit-learn`.

El clustering es no supervisado: no usaremos etiquetas de referencia para ajustar los modelos ni para elegir el número de grupos.

## 1. Datos y pregunta

Usaremos Wine, incluido en scikit-learn: 178 vinos descritos mediante 13 mediciones químicas. La pregunta es: **¿qué agrupamientos sugieren estas mediciones y en qué se parecen los resultados de ambos métodos?**

La clase conocida del vino se reserva para una comparación externa posterior. No es una característica de entrada ni una verdad absoluta sobre cómo deberían agruparse las mediciones.

**Pregunta:** ¿qué variables tienen escalas muy diferentes? ¿Por qué podría ser un problema al usar distancias euclidianas?

## 2. Preparación y estandarización

Revisamos datos faltantes y variables constantes antes de calcular distancias. Estandarizamos cada variable a media cero y desviación estándar uno. Esto no elimina los valores extremos y supone que todas las variables elegidas merecen participar en la distancia. En un problema con datos de entrenamiento y prueba, el escalador se ajusta solo con entrenamiento.

## 3. K-means: exploración de k

K-means asigna cada observación al centroide más cercano y busca reducir la **inercia**, suma de distancias euclidianas cuadradas a los centroides. Exploraremos el codo de la curva y el coeficiente **silueta** en el espacio de 13 variables estandarizadas.

La inercia tiende a disminuir al aumentar k; no se elige simplemente su valor mínimo. La silueta va de −1 a 1: valores mayores suelen indicar grupos más compactos y separados. Ambas son ayudas, no pruebas de un número verdadero de grupos.

**Discusión:** ¿dónde se observa un posible codo? ¿Qué valor de k tiene la mayor silueta? ¿Coinciden los criterios?

Para esta práctica utilizamos **k = 3 como elección didáctica**, no como conclusión demostrada. Cambia el valor y vuelve a ejecutar las celdas siguientes para evaluar otras opciones.

## 4. Clustering jerárquico aglomerativo

Partimos de una observación por grupo y fusionamos grupos sucesivamente. Con **Ward** y distancia euclidiana, cada fusión busca el menor incremento de la variación dentro de los grupos. El dendrograma muestra las fusiones; su eje vertical representa la distancia de enlace, no el número de observaciones.

Construimos el árbol con las mismas variables estandarizadas y después lo cortamos para obtener el mismo número de grupos usado por K-means. La línea horizontal marca una distancia entre las dos fusiones que rodean ese corte. Si ambas fusiones ocurren a la misma altura, no existe una línea horizontal que produzca exactamente ese número de grupos. Esta elección facilita la comparación, pero no implica que sea el único corte razonable.

**Pregunta:** ¿qué fusiones aparecen a distancias grandes? ¿Cómo cambiaría tu interpretación al cortar el árbol en otro nivel?

## 5. Comparar e interpretar los grupos

Comparamos tamaños y asignaciones, y calculamos el **índice Rand ajustado (ARI)**: 1 indica particiones idénticas y valores cercanos a 0 sugieren un acuerdo similar al esperado por azar; puede ser negativo. Los números de grupo son identificadores arbitrarios: el grupo 0 de un método no tiene por qué corresponder al grupo 0 del otro.

La silueta se calcula con las 13 variables estandarizadas, no con la proyección PCA. Para interpretar qué caracteriza a cada grupo, también examinamos las medias en las unidades originales.

### Comparación opcional con una referencia externa

La clase conocida se usa **únicamente después** del agrupamiento. Una concordancia baja no demuestra por sí sola que el clustering sea incorrecto: las clases conocidas y las similitudes de las variables pueden reflejar criterios diferentes.

## 6. Reducción a dos dimensiones para visualizar los clusters

**PCA** construye componentes lineales que capturan direcciones de variación de los datos. Ajustamos PCA sobre las mismas 13 variables estandarizadas **después** del clustering: solo proyectamos las observaciones y coloreamos con las etiquetas ya calculadas. No estamos agrupando de nuevo en el plano.

La varianza explicada indica cuánta variación conserva cada componente. Una proyección 2D pierde información: grupos solapados o separados en la gráfica pueden comportarse de otra manera en las 13 dimensiones. El tercer panel muestra las clases conocidas como referencia, sin haberlas usado para agrupar. Los colores identifican grupos o clases dentro de cada panel; no establecen correspondencia entre ellos.

## 7. Actividades y cierre

1. Justifica un valor de k usando la gráfica de inercia, la silueta y el dendrograma. Repite el análisis con otro valor y compara tamaños, siluetas y ARI.
2. Identifica dos variables que diferencien algunos grupos usando las tablas de medias. Explica sus unidades y evita interpretar el identificador de grupo como una jerarquía.
3. Compara los dos agrupamientos con las clases conocidas en los paneles PCA y explica qué se conserva y qué información puede perderse. ¿Coincide la impresión visual con la silueta calculada en el espacio original?
4. Prueba otro criterio jerárquico, por ejemplo `method='complete'`, manteniendo la distancia euclidiana. Compara dendrograma, silueta y ARI con Ward. Explica por qué cambiar el enlace puede cambiar los grupos.
5. **Conclusión:** redacta un párrafo sobre coincidencias, diferencias y limitaciones. No presentes los grupos como categorías naturales ni como relaciones causales.

**Para llevar:** el escalamiento y las decisiones de distancia afectan los grupos; las métricas y el dendrograma ayudan, pero no deciden solos; PCA facilita la visualización sin reemplazar la evaluación en el espacio utilizado para agrupar.
