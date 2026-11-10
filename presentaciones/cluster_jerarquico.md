# Clustering jerárquico aglomerativo

- **Materia:** Ciencia de Datos
- **Audiencia:** Licenciatura en Nanotecnología (séptimo semestre)
- **Duración:** 60 minutos
**Idea central:** el clustering jerárquico construye una secuencia de fusiones entre grupos. El dendrograma permite explorar esa estructura a distintos niveles, pero no determina por sí solo cuántos grupos son útiles.

> **Guion para quien expone:** los tiempos y las notas en cursiva son sugerencias para la clase; el resto puede presentarse como contenido de las diapositivas.

---

## Diapositiva 1 — ¿Cómo se forman los grupos?

Imagina que tienes mediciones de varias muestras y no conoces sus categorías.

- ¿Qué muestras se parecen entre sí?
- ¿Cómo cambiaría la respuesta si usamos otra definición de «parecido»?
- ¿Podemos ver grupos grandes y subgrupos dentro de ellos?

**Hoy:** responderemos estas preguntas con clustering jerárquico aglomerativo.

*Tiempo: 2 min. Inicia con las preguntas; no es necesario resolverlas todavía.*

---

## Diapositiva 2 — Objetivos

Al final de la sesión podrás:

1. Explicar cómo funciona el método aglomerativo.
2. Describir cómo la distancia y el criterio de enlace cambian las fusiones.
3. Leer un dendrograma y proponer un corte razonado.
4. Identificar decisiones y límites al interpretar los grupos.

*Tiempo: 2 min.*

---

## Diapositiva 3 — ¿Qué significa «jerárquico»?

- Cada fila representa una observación; las columnas, sus características.
- El método construye grupos anidados: grupos pequeños pueden unirse para formar grupos mayores.
- El dendrograma representa la secuencia y la altura de esas fusiones.
- No necesita que indiquemos de antemano un único número de grupos para construir la jerarquía.

**Importante:** el algoritmo descubre una estructura según los datos y las decisiones de análisis; los grupos no son etiquetas verdaderas automáticamente.

*Tiempo: 3 min. Relaciónalo con el objetivo científico: «parecido» siempre depende de qué se midió.*

---

## Diapositiva 4 — Dos estrategias jerárquicas

| Aglomerativo | Divisivo |
| --- | --- |
| Empieza con cada observación como un grupo. | Empieza con todas las observaciones en un grupo. |
| Fusiona grupos paso a paso. | Divide grupos paso a paso. |
| Es la estrategia que veremos en esta clase. | Puede ser más costosa y se usa menos en flujos introductorios. |

**Regla de hoy:** una vez que dos grupos se fusionan, el método aglomerativo no los separa después.

*Tiempo: 2 min.*

---

## Diapositiva 5 — El algoritmo aglomerativo

1. Comienza con \(n\) grupos, uno por observación.
2. Calcula qué grupos están más cerca según una distancia y un enlace.
3. Fusiona la pareja más cercana.
4. Actualiza las distancias entre los grupos resultantes.
5. Repite hasta que quede un solo grupo.

El resultado es una jerarquía de \(n-1\) fusiones.

*Tiempo: 4 min. Señala que «distancia entre grupos» aún requiere una definición: ese será el papel del enlace.*

---

## Diapositiva 6 — Antes de agrupar: preparar los datos

- Selecciona características relevantes; excluye identificadores y etiquetas que no deberían guiar el agrupamiento.
- Revisa faltantes, valores extremos, unidades y variables constantes.
- Elige una distancia coherente con el tipo de datos y la pregunta.
- Escala las variables numéricas cuando sus unidades o magnitudes sean incompatibles.
- La codificación de categorías también puede cambiar qué significa «cerca».

**La jerarquía depende de la representación.** Cambiar las variables, la escala o la distancia puede cambiar el dendrograma.

*Tiempo: 4 min. Ejemplo: una variable en micrómetros y otra en nanómetros pueden dominar de manera distinta si no se consideran sus escalas.*

---

## Diapositiva 7 — ¿Cómo medimos la distancia entre grupos?

Supongamos observaciones en una dimensión:

| Observación | Valor |
| --- | ---: |
| A | 1 |
| B | 2 |
| C | 5 |
| D | 10 |

Distancias entre observaciones: \(d(A,B)=1\), \(d(B,C)=3\), \(d(A,C)=4\), \(d(C,D)=5\), \(d(B,D)=8\), \(d(A,D)=9\).

Cuando un grupo contiene varias observaciones, hay que definir cómo resumimos todas sus distancias al otro grupo.

*Tiempo: 3 min. Pide al grupo que identifique la pareja inicial más cercana: A y B.*

---

## Diapositiva 8 — Criterios de enlace (*linkage*)

Después de las primeras fusiones, cada grupo contiene varias observaciones. El **criterio de enlace** define cómo resumir las distancias entre dos grupos y permite al algoritmo decidir cuál pareja fusionar en el siguiente paso. Elegir otro enlace puede cambiar la forma de los grupos y el dendrograma.

| Criterio | Regla | Cuándo considerarlo |
| --- | --- | --- |
| **Simple (*single*)** | Distancia del par más cercano. | Puede encontrar estructuras alargadas; vigila el encadenamiento por puntos intermedios. |
| **Completo (*complete*)** | Distancia del par más lejano. | Tiende a favorecer grupos compactos; puede ser sensible a puntos alejados. |
| **Promedio (*average*)** | Promedio de todas las distancias entre pares. | Considera todos los pares, no solo el más cercano o lejano. |
| **Ward** | Menor aumento de la variación interna al fusionar. | Para variables numéricas y distancia euclidiana; tiende a grupos compactos. |

Los tres primeros resumen distancias entre pares de observaciones; Ward se basa en el aumento de la variación interna. La distancia, las características y su escala también deben justificarse.

Para dos grupos \(G_1\) y \(G_2\):

- **Simple (*single*):** la menor distancia entre una observación de cada grupo.
- **Completo (*complete*):** la mayor distancia entre una observación de cada grupo.
- **Promedio (*average*):** el promedio de todas las distancias entre pares de los grupos.
- **Ward:** fusiona los grupos que producen el menor aumento en la variación interna; se usa con distancia euclidiana.

El enlace no es un detalle cosmético: define qué significa que dos grupos sean cercanos.

*Tiempo: 4 min. Evita presentar Ward como otra forma de promediar distancias; su criterio se basa en el aumento de variación interna.*

---

## Diapositiva 9 — El mismo conjunto, distintos enlaces

Con los valores A=1, B=2, C=5 y D=10, las fusiones son:

| Enlace | Primera fusión | Segunda fusión | Fusión final |
| --- | --- | --- | --- |
| Simple | A–B a 1 | (A,B)–C a 3 | (A,B,C)–D a 5 |
| Completo | A–B a 1 | (A,B)–C a 4 | (A,B,C)–D a 9 |
| Promedio | A–B a 1 | (A,B)–C a 3.5 | (A,B,C)–D a 7.33 |

**La primera fusión coincide; las siguientes dependen del enlace.** La altura indica el valor del criterio de fusión, no una probabilidad de pertenencia.

*Tiempo: 5 min. Recorre una fila a la vez y pregunta cómo cada regla mide la distancia de (A,B) a C.*

---

## Diapositiva 10 — Leer un dendrograma

```text
Altura 1:  (A, B)
Altura 4:  ((A, B), C)
Altura 9:  (((A, B), C), D)
```

- Las hojas son observaciones.
- Cada unión representa una fusión.
- La altura de la unión representa la distancia o criterio al fusionar.
- Una unión a mayor altura indica que el enlace necesitó un valor mayor para fusionar esos grupos.

*Tiempo: 4 min. Este esquema resume el dendrograma para enlace completo del ejemplo anterior; el código de la diapositiva 12 genera una visualización gráfica.*

---

## Diapositiva 11 — ¿Dónde cortamos el dendrograma?

Un corte horizontal separa las ramas que aún no se han unido por encima de esa altura.

- Cortar a una altura baja suele dar más grupos.
- Cortar a una altura alta suele dar menos grupos.
- Saltos grandes entre alturas de fusión pueden sugerir cortes candidatos.
- La decisión final debe considerar la pregunta, la estabilidad y la interpretación de los grupos.

**El dendrograma no elige automáticamente el número «correcto» de clusters.**

*Tiempo: 4 min. Pregunta: ¿qué corte sugerirías en el dendrograma y qué evidencia usarías?*

---

## Diapositiva 12 — Ejemplo en Python

Con SciPy se puede calcular la jerarquía y visualizarla:

```python
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(
    n_samples=30,
    centers=3,
    cluster_std=1.0,
    random_state=42,
)

X_escalado = StandardScaler().fit_transform(X)
Z = linkage(X_escalado, method="ward")

plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Clustering jerárquico aglomerativo (Ward)")
plt.xlabel("Observaciones")
plt.ylabel("Distancia")
plt.tight_layout()
plt.show()
```

`Z` guarda las fusiones de la jerarquía; `dendrogram` las representa. En datos reales, sustituye `X` por las características seleccionadas y revisadas.

*Tiempo: 5 min. Si es posible, ejecuta el código y relaciona una unión visible con el eje vertical.*

---

## Diapositiva 13 — Ventajas y límites

**Ventajas**

- Permite explorar la estructura a varios niveles en un solo dendrograma.
- No exige fijar un número de grupos antes de construir la jerarquía.
- Puede ayudar a comunicar relaciones entre observaciones.

**Límites**

- La distancia, el enlace y el preprocesamiento influyen en el resultado.
- Las fusiones son irreversibles; una decisión temprana afecta las posteriores.
- Puede requerir mucha memoria y tiempo al crecer el número de observaciones.
- La altura del dendrograma no demuestra que los grupos sean naturales o útiles.

*Tiempo: 4 min.*

---

## Diapositiva 14 — Actividad en parejas: interpreta y decide

**Tiempo: 6 minutos**

1. Para A=1, B=2, C=5 y D=10, ¿qué pareja se fusiona primero?
2. ¿Por qué las alturas de la fusión final son distintas para enlace simple y completo?
3. Si un dendrograma presenta un salto grande entre dos alturas de fusión, ¿qué corte investigarías?
4. Menciona una comprobación necesaria antes de interpretar científicamente los grupos.

*Después de 4 minutos, pide respuestas breves y usa los 2 minutos restantes para comentar que un salto es evidencia exploratoria, no una regla universal.*

---

## Diapositiva 15 — Ideas para llevar

- El método aglomerativo empieza con observaciones individuales y fusiona grupos.
- La distancia y el enlace definen qué significa «cercanía».
- El dendrograma muestra una jerarquía; un corte propone una partición.
- Escala, selección de características y distancia pueden cambiar el resultado.
- Los clusters son patrones bajo decisiones concretas: hay que evaluar su estabilidad, utilidad e interpretación.

**Pregunta de salida:** ¿qué decisión explicarías primero para que otra persona pueda reproducir tu agrupamiento?

*Tiempo: 8 min. Reserva los últimos 4 minutos para preguntas, una respuesta individual a la pregunta de salida y cierre.*

---

## Referencia y material complementario

- Guía de clustering del curso: [Clusters](../manuales/Clusters.md).
- Documentación de SciPy para `linkage` y `dendrogram`: <https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html>
- Documentación de scikit-learn sobre clustering jerárquico: <https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering>
