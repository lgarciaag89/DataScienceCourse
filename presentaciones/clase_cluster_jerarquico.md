# Clase: clustering jerárquico aglomerativo

- **Curso:** Ciencia de Datos
- **Audiencia:** Licenciatura en Nanotecnología (séptimo semestre)
- **Duración:** 60 minutos
**Material relacionado:** [Guion de diapositivas](./cluster_jerarquico.md)

## Propósito de la clase

El clustering jerárquico agrupa observaciones según su similitud y representa las fusiones en un dendrograma. En esta clase construiremos la intuición del método aglomerativo, veremos por qué las reglas de enlace producen jerarquías distintas y practicaremos cómo leer un dendrograma sin asumir que existe un número de grupos universalmente correcto.

Al terminar, el estudiante podrá:

1. Describir los pasos del algoritmo aglomerativo.
2. Explicar la diferencia entre enlace simple, completo, promedio y Ward.
3. Interpretar las ramas y alturas de un dendrograma.
4. Proponer un corte y justificarlo con la pregunta y los datos.
5. Identificar decisiones de preparación que afectan los resultados.

## Distribución del tiempo

| Bloque | Minutos |
| --- | ---: |
| Motivación, conceptos y algoritmo | 13 |
| Preparación de datos y distancias | 7 |
| Enlaces y ejemplo resuelto | 13 |
| Dendrograma y decisión del corte | 8 |
| Demostración en Python | 7 |
| Actividad, respuestas y cierre | 12 |
| **Total** | **60** |

---

## 1. Motivación: ¿qué significa que dos muestras se parezcan?

Imaginemos que medimos tamaño y densidad de varias nanopartículas, pero no tenemos una categoría para cada muestra. Una pregunta posible es: **¿qué muestras presentan perfiles parecidos?**

La respuesta depende de cómo representamos las muestras. Si solo usamos tamaño, dos partículas con tamaños similares quedarán cerca aunque sus densidades sean muy distintas. Si usamos tamaño y densidad, ambas características participan en la comparación. Si una se expresa en nanómetros y otra en una escala numérica mucho menor, la primera puede dominar una distancia euclidiana sin que eso refleje su importancia científica.

Por lo tanto, un algoritmo de clustering no descubre automáticamente categorías verdaderas. Encuentra una estructura con base en:

- las observaciones incluidas;
- las características elegidas y su codificación;
- el preprocesamiento y la escala;
- la distancia y el algoritmo;
- la interpretación y el propósito del análisis.

El clustering es **no supervisado**: no necesita etiquetas correctas para construir el agrupamiento. Las etiquetas disponibles, si las hay, pueden servir después para comparar o interpretar, pero no deberían incorporarse inadvertidamente como características.

### Pregunta para el grupo

Si dos muestras tienen el mismo tamaño, pero densidades muy diferentes, ¿deberían considerarse parecidas? No hay una respuesta puramente matemática: depende de la pregunta que se quiera estudiar.

---

## 2. ¿Qué significa que el método sea jerárquico?

Un método jerárquico crea grupos anidados. Una jerarquía puede mostrar primero observaciones muy parecidas, después grupos mayores y finalmente un grupo que contiene todas las observaciones.

Hay dos estrategias generales:

- **Aglomerativa:** comienza con cada observación como un grupo individual y va fusionando grupos. Es la estrategia de esta clase.
- **Divisiva:** comienza con todas las observaciones juntas y las va separando.

El método aglomerativo no requiere que se indique un único número de clusters al principio para construir toda la secuencia de fusiones. Sin embargo, para obtener una partición concreta —por ejemplo, asignar cada observación a uno de tres grupos— hay que decidir dónde cortar la jerarquía.

Una propiedad importante es que las fusiones aglomerativas son **irreversibles**: una vez que dos grupos se unen, las etapas siguientes no vuelven a separarlos.

---

## 3. Algoritmo aglomerativo paso a paso

Con $n$ observaciones, el procedimiento es:

1. Iniciar con $n$ grupos, uno por observación.
2. Calcular las distancias entre los grupos actuales.
3. Elegir los dos grupos más cercanos según el criterio de enlace.
4. Fusionarlos.
5. Actualizar las distancias entre el nuevo grupo y los demás.
6. Repetir hasta que todas las observaciones pertenezcan a un solo grupo.

Se realizan $n-1$ fusiones. El algoritmo produce una jerarquía; el dendrograma es una forma de visualizarla.

La distancia entre dos observaciones no basta para decidir qué tan cerca están dos grupos que contienen varias observaciones. Para eso se define el **enlace** (*linkage*).

---

## 4. Preparación: las decisiones que cambian el resultado

Antes de calcular distancias:

1. **Define la pregunta.** ¿Qué similitud es relevante para el problema?
2. **Selecciona características.** Incluye variables útiles; excluye identificadores y etiquetas que producirían una comparación circular.
3. **Revisa los datos.** Inspecciona faltantes, extremos, unidades, variables constantes y errores de medición.
4. **Codifica las variables correctamente.** Una codificación numérica de categorías puede introducir distancias u órdenes que no existen.
5. **Considera la escala.** Si las magnitudes o unidades son incompatibles, evalúa una transformación o escalamiento coherente con la pregunta.
6. **Elige una distancia.** La euclidiana es habitual para variables numéricas; otras distancias pueden tener más sentido según el tipo de datos.

La estandarización suele poner variables numéricas en escalas comparables, pero **no es neutral**: cambia las distancias, asigna influencia a cada variable y no elimina necesariamente el efecto de valores extremos. No se debe escalar mecánicamente sin explicar por qué.

Si se evalúa el desempeño con datos reservados, los parámetros de las transformaciones deben ajustarse únicamente con los datos de entrenamiento para evitar fuga de información.

---

## 5. Criterios de enlace

Al inicio, cada grupo contiene una sola observación y la distancia entre grupos coincide con la distancia entre dos puntos. Después de una fusión, cada grupo puede contener varias observaciones; por eso ya no hay una única distancia entre dos grupos. El **criterio de enlace** (*linkage*) es la regla que resume las distancias entre sus observaciones.

En cada paso, el algoritmo usa esa regla para comparar los grupos actuales y fusiona la pareja con el menor valor de enlace. Por tanto, el enlace se utiliza para decidir **qué grupos se unen a continuación** y qué forma de agrupamiento tiende a favorecer el método. Elegir otro enlace puede cambiar tanto las alturas como el orden de las fusiones y, en consecuencia, el dendrograma.

Sean $G_1$ y $G_2$ dos grupos, y $d(x,y)$ la distancia entre las observaciones $x$ e $y$.

### Enlace simple (*single*)

Define la distancia entre grupos como la menor distancia entre cualquiera de sus pares de observaciones:

$$
d_{\text{simple}}(G_1,G_2)
= \min_{x \in G_1,\; y \in G_2} d(x,y)
$$

Puede conectar grupos mediante una cadena de observaciones cercanas. Esto permite encontrar estructuras alargadas, pero también puede producir el **efecto de encadenamiento**: grupos distintos pueden terminar conectados a través de puntos intermedios.

**¿Cuándo considerarlo?** Cuando sea importante detectar estructuras alargadas o conectadas por puntos vecinos. Si se esperan grupos compactos y separados, revisa si el encadenamiento está juntando grupos que preferirías mantener separados.

### Enlace completo (*complete*)

Define la distancia entre grupos como la mayor distancia entre cualquiera de sus pares de observaciones:

$$
d_{\text{completo}}(G_1,G_2)
= \max_{x \in G_1,\; y \in G_2} d(x,y)
$$

Tiende a favorecer grupos más compactos. Un punto alejado puede influir bastante porque la regla considera la mayor distancia entre pares.

**¿Cuándo considerarlo?** Cuando se prefiera que todas las observaciones de un grupo queden relativamente próximas entre sí. Ten presente que los puntos extremos pueden aumentar mucho la distancia de enlace.

### Enlace promedio (*average*)

Define la distancia entre grupos como el promedio de las distancias entre todos los pares que cruzan de un grupo al otro:

$$
d_{\text{promedio}}(G_1,G_2)
= \frac{1}{|G_1||G_2|}
\sum_{x \in G_1}\sum_{y \in G_2} d(x,y)
$$

Su valor queda entre el mínimo y el máximo para los mismos pares, pero eso no implica que siempre sea el método más adecuado. La decisión depende del problema.

**¿Cuándo considerarlo?** Cuando se quiera usar la información de todos los pares entre grupos, sin basar la decisión solo en el par más cercano o el más lejano. Sigue dependiendo de la distancia elegida y de la escala de las características.

### Método de Ward

Ward es un criterio de fusión basado en la variación de los datos dentro de los grupos. En cada paso une la pareja cuya fusión produce el menor aumento en la suma de cuadrados dentro de los grupos. Para dos grupos de datos euclidianos, ese aumento puede expresarse como:

$$
\Delta(G_1,G_2)
= \frac{|G_1||G_2|}{|G_1|+|G_2|}
\left\|\bar{x}_{G_1}-\bar{x}_{G_2}\right\|^2
$$

Aquí $\bar{x}_{G_i}$ es el centroide del grupo. Ward no es otro promedio de distancias por pares: su criterio se basa en el cambio de la variación dentro de los grupos.

**¿Cuándo considerarlo?** Cuando las características sean numéricas, tenga sentido comparar distancias euclidianas y se busquen grupos relativamente compactos. Ward suele depender de la escala, así que hay que justificar si se estandarizan las variables. No lo combines con una métrica arbitraria: el criterio estándar se formula con distancia euclidiana. Sus alturas tampoco son directamente comparables con las de los otros enlaces porque miden criterios de fusión diferentes.

### Comparación rápida

| Criterio | ¿Qué resume? | Tendencia o uso orientativo | Precaución principal |
| --- | --- | --- | --- |
| Simple | El par más cercano | Puede conectar grupos alargados | Encadenamiento por puntos intermedios |
| Completo | El par más lejano | Favorece grupos compactos | Sensibilidad a puntos alejados |
| Promedio | El promedio de todos los pares | Considera todas las distancias entre grupos | La escala y la métrica siguen importando |
| Ward | Aumento de variación interna al fusionar | Grupos compactos con variables numéricas euclidianas | No es una distancia por pares; requiere uso compatible con euclidiana |

Esta tabla orienta la elección, pero no sustituye la evaluación. Conviene comparar opciones razonables y revisar si la estructura, los perfiles y las conclusiones son útiles para la pregunta del análisis.

---

## 6. Ejemplo resuelto: cuatro observaciones

Consideremos puntos en una dimensión:

| Observación | Valor |
| --- | ---: |
| A | 1 |
| B | 2 |
| C | 5 |
| D | 10 |

Las distancias entre pares son:

| Par | Distancia |
| --- | ---: |
| A–B | 1 |
| A–C | 4 |
| A–D | 9 |
| B–C | 3 |
| B–D | 8 |
| C–D | 5 |

La pareja inicial más cercana es A–B, con distancia 1, para los tres enlaces.

### Ejemplo resuelto: distancia entre dos grupos

Ahora supongamos que en una etapa del algoritmo ya tenemos los grupos:

$G_1=\{A,B\}$ y $G_2=\{C,D\}$.

Las distancias entre sus observaciones son:

| Par entre grupos | Distancia |
| --- | ---: |
| A–C | 4 |
| A–D | 9 |
| B–C | 3 |
| B–D | 8 |

Cada enlace resume estos cuatro valores de manera diferente:

- **Simple:** toma la menor, $\min(4,9,3,8)=3$.
- **Completo:** toma la mayor, $\max(4,9,3,8)=9$.
- **Promedio:** calcula la media, $(4+9+3+8)/4=6$.

Para **Ward**, calculamos los centroides: $\bar{x}_{G_1}=(1+2)/2=1.5$ y $\bar{x}_{G_2}=(5+10)/2=7.5$. El aumento de la suma de cuadrados dentro de los grupos al fusionarlos es:

$$
\Delta(G_1,G_2)
= \frac{2\cdot2}{2+2}(7.5-1.5)^2
= 36
$$

Unir estos grupos aumentaría en 36 la variación interna total. Ward compara ese aumento con el de otras fusiones posibles y elige el menor; **no** selecciona el mínimo, máximo o promedio de las distancias entre pares.

> **Nota sobre SciPy:** con `linkage(..., method="ward")`, la altura de fusión es $\sqrt{2\Delta}$. Aquí sería $\sqrt{72}\approx8.49$; $\Delta=36$ es el aumento de suma de cuadrados. Son cantidades relacionadas, pero no idénticas.

### Enlace simple

1. Fusionar A y B a distancia 1.
2. De $\{A,B\}$ a C: $\min(4,3)=3$. Se fusiona C a altura 3.
3. De $\{A,B,C\}$ a D: $\min(9,8,5)=5$. D se une a altura 5.

### Enlace completo

1. Fusionar A y B a distancia 1.
2. De $\{A,B\}$ a C: $\max(4,3)=4$. Se fusiona C a altura 4.
3. De $\{A,B,C\}$ a D: $\max(9,8,5)=9$. D se une a altura 9.

### Enlace promedio

1. Fusionar A y B a distancia 1.
2. De $\{A,B\}$ a C: $(4+3)/2=3.5$. Se fusiona C a altura 3.5.
3. De $\{A,B,C\}$ a D: $(9+8+5)/3=22/3\approx7.33$. D se une a esa altura.

| Enlace | Primera fusión | Segunda fusión | Fusión final |
| --- | --- | --- | --- |
| Simple | A–B, altura 1 | (A,B)–C, altura 3 | (A,B,C)–D, altura 5 |
| Completo | A–B, altura 1 | (A,B)–C, altura 4 | (A,B,C)–D, altura 9 |
| Promedio | A–B, altura 1 | (A,B)–C, altura 3.5 | (A,B,C)–D, altura 7.33 |

El orden inicial de fusiones coincide, pero las alturas posteriores cambian. En conjuntos de datos más grandes también puede cambiar qué pareja se fusiona a continuación.

---

## 7. Leer y cortar un dendrograma

Un dendrograma representa la historia de fusiones:

- **Hojas:** observaciones individuales.
- **Ramas:** las observaciones o grupos que se unen.
- **Altura de la unión:** valor del criterio de fusión en esa etapa.
- **Corte horizontal:** partición de las hojas que intercepta el corte.

Para el ejemplo anterior con enlace completo:

```text
Altura 1:  (A, B)
Altura 4:  ((A, B), C)
Altura 9:  (((A, B), C), D)
```

Un corte entre las alturas 4 y 9 dejaría dos grupos: $\{A,B,C\}$ y $\{D\}$. Un corte entre 1 y 4 dejaría tres: $\{A,B\}$, $\{C\}$ y $\{D\}$.

En un dendrograma real, busca saltos entre alturas de fusión como **candidatos** a cortes. Un salto puede sugerir que se están uniendo grupos bastante distintos, pero no demuestra que la partición resultante sea científicamente correcta. La elección también depende de:

- la pregunta que originó el análisis;
- el tamaño y el perfil de los grupos;
- la estabilidad al cambiar razonablemente las variables, la escala o la muestra;
- la interpretación y utilidad dentro del dominio.

Algunos programas reordenan visualmente ramas que ya se fusionaron para mejorar la presentación. La posición izquierda-derecha de las hojas no representa una cantidad; importa la estructura de las uniones y sus alturas.

---

## 8. Demostración reproducible en Python

Este ejemplo genera mediciones sintéticas en dos dimensiones, las estandariza, construye una jerarquía con Ward y muestra el dendrograma. Los datos se generan únicamente para ilustrar el procedimiento; en un análisis real se deben justificar las características y el preprocesamiento.

```python
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Datos de ejemplo: 30 observaciones con dos características.
X, _ = make_blobs(
    n_samples=30,
    centers=3,
    cluster_std=1.0,
    random_state=42,
)

# Se ajusta el escalador a estas observaciones de ejemplo.
X_escalado = StandardScaler().fit_transform(X)

# Ward utiliza el aumento de variación interna con distancia euclidiana.
Z = linkage(X_escalado, method="ward")

plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Clustering jerárquico aglomerativo (Ward)")
plt.xlabel("Observaciones")
plt.ylabel("Distancia de fusión")
plt.tight_layout()
plt.show()

# Para ilustrar una partición concreta, solicitamos tres grupos.
etiquetas = fcluster(Z, t=3, criterion="maxclust")
print(etiquetas)
```

### Cómo leer el resultado

- `linkage` calcula las fusiones; `Z` almacena la jerarquía codificada.
- `dendrogram` representa las fusiones y sus alturas.
- `fcluster` extrae una partición de la jerarquía según el criterio elegido.
- Los números impresos por `fcluster` son identificadores, no rangos ni categorías con significado intrínseco.

Cambiar `method="ward"` por `"single"`, `"complete"` o `"average"` permite comparar otros criterios de enlace. Para comparar, observa cómo cambian las fusiones y pregunta cuál estructura es razonable para el problema; no selecciones un método solo porque produzca un dibujo más atractivo.

En aplicaciones reales, no se debe usar una variable objetivo para formar los grupos si después se quiere afirmar que estos explican o recuperan esa misma variable. Además, una proyección a dos dimensiones puede facilitar la visualización, pero puede ocultar la geometría del espacio de características original.

---

## 9. Actividad en parejas

**Duración: 6 minutos.** Consideren de nuevo A=1, B=2, C=5 y D=10.

1. ¿Qué pareja se fusiona primero para los tres enlaces del ejemplo?
2. Después de fusionar A y B, ¿cuál es la distancia de $\{A,B\}$ a C para cada uno de los enlaces simple, completo y promedio?
3. ¿Qué dos grupos se obtienen al cortar el dendrograma de enlace completo entre las alturas 4 y 9?
4. Menciona dos decisiones de preparación que podrían cambiar un dendrograma con mediciones reales.
5. ¿Qué comprobarías antes de dar una interpretación científica a los grupos?

### Respuestas para discusión

1. A y B, a distancia 1.
2. Simple: 3; completo: 4; promedio: 3.5.
3. $\{A,B,C\}$ y $\{D\}$.
4. Por ejemplo: selección de características, escala, tratamiento de extremos, codificación de categorías o distancia.
5. Justificaría el propósito y las variables, describiría los perfiles, revisaría los tamaños de grupo y comprobaría si los patrones se mantienen ante decisiones razonables. Ninguna métrica aislada demuestra que los grupos sean categorías naturales.

---

## 10. Cierre: qué debemos recordar

1. El método aglomerativo empieza con grupos individuales y los fusiona sucesivamente.
2. La definición de distancia y el criterio de enlace determinan qué significa «cercanía» entre grupos.
3. El dendrograma muestra una jerarquía; cortar el árbol produce una partición concreta.
4. El número de grupos no se decide automáticamente por una altura ni por un salto visual.
5. Las conclusiones deben acompañarse de las decisiones de análisis y sus limitaciones.

**Pregunta de salida:** si otra persona tuviera que reproducir tu análisis, ¿qué decisión explicarías primero y por qué?

## Referencias

- Guía de clustering del curso: [Clusters](../manuales/Clusters.md).
- SciPy, jerarquía de clusters: <https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html>
- scikit-learn, clustering jerárquico: <https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering>
