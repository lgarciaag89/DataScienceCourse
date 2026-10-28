# Clase — Métricas de similitud y distancia

**Materia:** Ciencia de Datos  
**Duración:** 2 horas  
**Tema:** comparación de observaciones mediante distancias y similitudes

Este material está diseñado para desarrollarse en un notebook de Jupyter,
Google Colab o VS Code.

> **Idea central:** una distancia o similitud no es una propiedad absoluta de
> dos observaciones. Su significado depende de cómo representamos los datos,
> de la métrica elegida y, en muchos casos, del escalamiento de las variables.

---

## 1. Propósito de la clase

Al terminar la sesión, el estudiante podrá:

- distinguir una medida de distancia de una medida de similitud;
- calcular e interpretar las métricas de Minkowski, coseno, Jaccard y Hamming;
- elegir una métrica apropiada para variables numéricas, vectores binarios y
  datos codificados como conjuntos;
- calcular distancias entre vectores y matrices de observaciones en Python;
- explicar cómo afectan el escalamiento, la representación y la dimensión a
  las comparaciones.

## 2. Ruta de la sesión

| Tiempo | Tema | Actividad |
| ---: | --- | --- |
| 0–10 min | Motivación | ¿Qué significa que dos observaciones sean parecidas? |
| 10–25 min | Distancia y similitud | Propiedades y ejemplos |
| 25–50 min | Minkowski | Euclidiana, Manhattan y Chebyshev |
| 50–70 min | Coseno | Dirección, magnitud y vectores dispersos |
| 70–85 min | Jaccard y Hamming | Conjuntos y atributos binarios |
| 85–100 min | Otras medidas | Distancia de correlación y Mahalanobis |
| 100–115 min | Práctica | Comparación de perfiles con Python |
| 115–120 min | Cierre | Elección y limitaciones de las métricas |

---

## 3. ¿Qué significa comparar dos observaciones?

Representamos dos observaciones con vectores de características:

$$
x=(x_1,x_2,\ldots,x_p), \qquad y=(y_1,y_2,\ldots,y_p)
$$

Una **distancia** expresa cuán separadas están: valores menores indican mayor
cercanía. Una **similitud** expresa cuán parecidas son: valores mayores suelen
indicar mayor semejanza. El rango depende de la definición: por ejemplo, la
similitud coseno va de -1 a 1, mientras que la similitud de Jaccard va de 0 a 1.

No existe una conversión universal entre similitud y distancia. En algunos
casos se define una disimilitud como `1 - similitud`; hay que comprobar si esa
disimilitud satisface las propiedades matemáticas de una métrica.

### ¿Qué propiedades tiene una métrica?

Una distancia matemática suele cumplir, para cualesquiera $x,y,z$:

1. **No negatividad:** $d(x,y)\geq 0$.
2. **Identidad:** $d(x,y)=0$ si y solo si $x=y$.
3. **Simetría:** $d(x,y)=d(y,x)$.
4. **Desigualdad triangular:** $d(x,z)\leq d(x,y)+d(y,z)$.

Algunas medidas útiles para comparar datos no cumplen todas estas propiedades.
Por ello, en aplicaciones es común llamarlas también **disimilitudes**.

### La representación importa

Una distancia numérica presupone que las coordenadas se pueden restar y que
sus diferencias tienen sentido. No se debe calcular una distancia euclidiana
directamente sobre identificadores, códigos arbitrarios de categorías o
variables con unidades incompatibles sin justificar la decisión.

---

## 4. Métricas de Minkowski

La familia de Minkowski para vectores numéricos es:

$$
d_p(x,y)=\left(\sum_{i=1}^{n}|x_i-y_i|^p\right)^{1/p},
\qquad p\geq 1
$$

El parámetro $p$ determina cómo se acumulan las diferencias.

### 4.1 Distancia Euclidiana: $p=2$

Es la distancia en línea recta. Para $x=(1,2)$ e $y=(4,6)$:

$$
d_2(x,y)=\sqrt{(1-4)^2+(2-6)^2}=5
$$

Es sensible a diferencias grandes porque las eleva al cuadrado.

### 4.2 Distancia Manhattan: $p=1$

También se conoce como distancia de ciudad o norma $L_1$:

$$
d_1(x,y)=\sum_{i=1}^{n}|x_i-y_i|
$$

Para los mismos vectores, $d_1=3+4=7$. Suma los cambios absolutos por
coordenada y puede ser una alternativa cuando se desea reducir el efecto de
diferencias grandes respecto a la distancia euclidiana.

### 4.3 Distancia Chebyshev: límite de Minkowski

$$
d_\infty(x,y)=\max_i |x_i-y_i|
$$

Solo considera la mayor diferencia por coordenada. En el ejemplo anterior,
$d_\infty=4$. Es útil cuando la discrepancia máxima es lo que determina si dos
observaciones son suficientemente parecidas.

### Cálculo con Python

```python
import numpy as np
from sklearn.metrics import pairwise_distances

x = np.array([[1, 2]])
y = np.array([[4, 6]])

for p, nombre in [(1, "Manhattan"), (2, "Euclidiana"), (3, "Minkowski p=3")]:
    d = pairwise_distances(x, y, metric="minkowski", p=p)[0, 0]
    print(f"{nombre}: {d:.2f}")

d_chebyshev = pairwise_distances(x, y, metric="chebyshev")[0, 0]
print(f"Chebyshev: {d_chebyshev:.2f}")
```

Se puede calcular la distancia euclidiana directamente con NumPy:

```python
distancia = np.linalg.norm(x - y)
print(distancia)  # 5.0
```

---

## 5. Similitud y distancia coseno

La similitud coseno compara el **ángulo** entre vectores, no su longitud:

$$
\operatorname{coseno}(x,y)=
\frac{x\cdot y}{\|x\|_2\|y\|_2}
$$

Para vectores no nulos, sus valores están entre -1 y 1:

- cercano a 1: apuntan en direcciones similares;
- cercano a 0: son ortogonales;
- cercano a -1: apuntan en direcciones opuestas.

La distancia coseno suele definirse como:

$$
d_{\text{cos}}(x,y)=1-\operatorname{coseno}(x,y)
$$

Se usa mucho con documentos representados por frecuencias de palabras, vectores
dispersos y perfiles donde importa el patrón relativo más que la magnitud total.
Por ejemplo, multiplicar un vector por un escalar positivo no cambia su
similitud coseno.

```python
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances

documento_a = np.array([[1, 1, 0, 1]])
documento_b = np.array([[2, 2, 0, 2]])
documento_c = np.array([[0, 0, 1, 0]])

print(cosine_similarity(documento_a, documento_b)[0, 0])  # 1.0
print(cosine_distances(documento_a, documento_c)[0, 0])   # 1.0
```

**Precaución:** la similitud coseno no está definida matemáticamente para un
vector cero. Además, la distancia `1 - similitud coseno` no siempre cumple la
desigualdad triangular; es una disimilitud práctica, no necesariamente una
métrica en sentido estricto.

---

## 6. Jaccard: similitud de conjuntos y datos binarios

Para dos conjuntos $A$ y $B$, la similitud de Jaccard es la proporción de
elementos compartidos respecto al total de elementos presentes en al menos uno:

$$
J(A,B)=\frac{|A\cap B|}{|A\cup B|}
$$

Su distancia asociada es:

$$
d_J(A,B)=1-J(A,B)
$$

Ejemplo: si $A=\{perro, gato, pez\}$ y $B=\{gato, pez, ave\}$, la intersección
tiene dos elementos y la unión cuatro; por tanto, $J=2/4=0.5$.

Para vectores binarios, Jaccard compara las posiciones con valor 1. Los ceros
compartidos no aumentan la similitud, lo que suele ser deseable para atributos
de presencia/ausencia dispersos, como palabras en documentos o especies
detectadas.

```python
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import pairwise_distances

A = {"perro", "gato", "pez"}
B = {"gato", "pez", "ave"}

similitud_conjuntos = len(A & B) / len(A | B)
print(similitud_conjuntos)  # 0.5

presencias = np.array([
    [1, 1, 0, 1],
    [0, 1, 1, 0],
], dtype=bool)

distancia = pairwise_distances(
    presencias,
    metric="jaccard",
)[0, 1]
similitud = 1 - distancia
print(f"Jaccard: {similitud:.2f}")

# Para etiquetas multilabel, jaccard_score calcula la similitud entre
# conjuntos de etiquetas; average='samples' promedia por observación.
y_real = np.array([[1, 1, 0], [0, 1, 1]])
y_pred = np.array([[1, 0, 0], [0, 1, 1]])
print(jaccard_score(y_real, y_pred, average="samples"))
```

Si ambos conjuntos están vacíos, la fórmula tiene denominador cero. La
convención usada puede depender de la biblioteca; conviene definir cómo tratar
ese caso en el problema concreto.

---

## 7. Distancia de Hamming

Hamming cuenta en cuántas posiciones difieren dos vectores de igual longitud:

$$
d_H(x,y)=\sum_{i=1}^{n}\mathbb{1}(x_i\neq y_i)
$$

La versión normalizada divide por el número de posiciones y queda entre 0 y 1.
Es apropiada para cadenas, categorías codificadas y atributos binarios cuando
cada posición tiene el mismo peso.

```python
cadena_a = np.array(["A", "C", "G", "T"])
cadena_b = np.array(["A", "G", "G", "A"])

distancia_hamming = np.mean(cadena_a != cadena_b)
print(distancia_hamming)  # 0.5: difieren en 2 de 4 posiciones
```

Hamming trata cualquier discrepancia como igual. No expresa, por ejemplo, que
dos categorías puedan ser más parecidas entre sí que a una tercera.

---

## 8. Distancia basada en correlación

Cuando interesa comparar la forma de dos perfiles, sin importar tanto su nivel
o escala, se puede usar la correlación de Pearson $r$ y definir la
disimilitud:

$$
d_{\text{corr}}(x,y)=1-r(x,y)
$$

```python
perfil_a = np.array([10, 20, 30, 40])
perfil_b = np.array([1, 2, 3, 4])
perfil_c = np.array([4, 3, 2, 1])

sim_ab = np.corrcoef(perfil_a, perfil_b)[0, 1]
sim_ac = np.corrcoef(perfil_a, perfil_c)[0, 1]
print(sim_ab, 1 - sim_ab)  # correlación 1; disimilitud 0
print(sim_ac, 1 - sim_ac)  # correlación -1; disimilitud 2
```

Esta opción compara patrones lineales, pero no es una distancia métrica en
general. Si un vector es constante, su correlación no está definida. La
correlación mide asociación y no debe confundirse con cercanía en unidades
originales.

---

## 9. Distancia de Mahalanobis

La distancia de Mahalanobis considera la escala y la correlación entre
variables:

$$
d_M(x,y)=\sqrt{(x-y)^\mathsf{T}\Sigma^{-1}(x-y)}
$$

Aquí $\Sigma$ es la matriz de covarianza. A diferencia de la euclidiana, puede
reducir el peso de diferencias en variables muy correlacionadas y ajustar por
la variabilidad observada.

```python
from scipy.spatial.distance import mahalanobis

datos = np.array([
    [1.0, 2.0],
    [2.0, 3.1],
    [3.0, 3.9],
    [4.0, 5.2],
])
x = datos[0]
y = datos[3]

covarianza = np.cov(datos, rowvar=False)
inversa_covarianza = np.linalg.pinv(covarianza)
distancia_m = mahalanobis(x, y, inversa_covarianza)
print(distancia_m)
```

La estimación de covarianza necesita suficientes observaciones y puede ser
inestable con variables redundantes o muchas dimensiones. La pseudoinversa
permite calcular en ciertos casos singulares, pero no corrige una mala
representación ni reemplaza la revisión estadística.

---

## 10. Comparación rápida

| Métrica | Tipo de datos habitual | Qué compara | Consideración principal |
| --- | --- | --- | --- |
| Euclidiana ($L_2$) | Numéricos | Separación en línea recta | Sensible a escala y valores extremos |
| Manhattan ($L_1$) | Numéricos | Suma de diferencias absolutas | También depende de la escala |
| Chebyshev ($L_\infty$) | Numéricos | Mayor diferencia por variable | Una sola coordenada puede dominar |
| Coseno | Vectores numéricos, texto | Dirección de los vectores | Ignora magnitud; cuidado con vector cero |
| Jaccard | Conjuntos, binarios dispersos | Presencias compartidas | Ignora los ceros compartidos |
| Hamming | Cadenas, categorías, binarios | Posiciones distintas | Requiere vectores de igual longitud |
| Correlación | Perfiles numéricos | Patrón lineal conjunto | No mide diferencia en unidades originales |
| Mahalanobis | Numéricos correlacionados | Diferencia ajustada por covarianza | Requiere estimar covarianza fiable |

---

## 11. Distancias entre muchas observaciones

Con `pairwise_distances` se calcula una matriz donde la posición `(i, j)`
contiene la distancia entre la observación `i` y la observación `j`.

```python
from sklearn.metrics import pairwise_distances

X = np.array([
    [1.0, 10.0],
    [2.0, 12.0],
    [8.0, 40.0],
])

D_euclidiana = pairwise_distances(X, metric="euclidean")
D_manhattan = pairwise_distances(X, metric="manhattan")

print(D_euclidiana.round(2))
print(D_manhattan.round(2))
```

La matriz es simétrica y tiene ceros en la diagonal si se usa una distancia
simétrica. Para conjuntos grandes, una matriz completa puede consumir mucha
memoria; se debe considerar calcular solo los vecinos necesarios.

### Escala y unidades

La primera columna del ejemplo varía en unidades y rango distintos de la
segunda. Con la distancia euclidiana sin escalar, la variable de mayor rango
puede dominar. Antes de calcular distancias numéricas, se debe decidir si
conviene estandarizar, usar otro escalamiento o asignar pesos con justificación.

En un flujo predictivo, se ajusta el escalador con los datos de entrenamiento y
se aplica a validación y prueba; no se ajusta con el conjunto de prueba.

```python
from sklearn.preprocessing import StandardScaler

escalador = StandardScaler()
X_estandarizado = escalador.fit_transform(X)
D_estandarizada = pairwise_distances(
    X_estandarizado,
    metric="euclidean",
)
print(D_estandarizada.round(2))
```

El escalamiento no es neutral: altera la geometría y por tanto qué pares se
consideran cercanos. Estandarizar cada variable equivale a modificar su peso
relativo; esa decisión debe relacionarse con el dominio.

---

## 12. Actividad en parejas

Consideren tres observaciones binarias que indican si cada documento contiene
cuatro términos:

```python
documentos = np.array([
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
])
```

1. Calculen a mano la similitud Jaccard entre el primer y segundo documento.
2. Calculen su distancia Hamming normalizada.
3. Comparen esos valores con los pares primero-tercero.
4. Expliquen por qué dos documentos pueden tener Jaccard cero aunque compartan
   varios términos ausentes.
5. Repitan la comparación con similitud coseno. ¿Qué cambia?

Después, con tres perfiles numéricos elegidos por el grupo:

1. calculen distancias euclidiana y Manhattan;
2. escalen las columnas y vuelvan a calcularlas;
3. expliquen qué variable influye más antes y después del escalamiento.

---

## 13. Guía para elegir una métrica

Antes de calcular, responde:

1. **¿Qué representa cada coordenada?** ¿Es numérica, binaria, categórica o un
   conjunto?
2. **¿Qué significa una diferencia?** ¿Las diferencias tienen unidades y
   magnitudes comparables?
3. **¿Importa la magnitud o solo la dirección/patrón?** Considera coseno o
   correlación si interesa el patrón relativo.
4. **¿Los ceros compartidos son evidencia de semejanza?** Si no, Jaccard puede
   ser más apropiada que una medida que los cuente.
5. **¿Hay variables correlacionadas o escalas distintas?** Evalúa escalamiento
   y, si se justifica, Mahalanobis.
6. **¿Qué algoritmo consumirá el resultado?** Algunos algoritmos requieren una
   métrica específica o se comportan de forma distinta con disimilitudes.

No hay una métrica universalmente mejor. Es recomendable comparar alternativas
justificadas y verificar si las conclusiones cambian.

## 14. Cierre

- Euclidiana, Manhattan y Chebyshev son casos de la familia de Minkowski.
- Coseno compara orientación; Jaccard compara presencias; Hamming cuenta
  posiciones distintas.
- La métrica y el escalamiento definen qué significa “cerca”.
- Una similitud alta o distancia baja no implica que dos observaciones sean
  equivalentes en el contexto científico.

### Referencias

- Documentación de scikit-learn, métricas por pares:
  https://scikit-learn.org/stable/modules/metrics.html#pairwise-metrics-affinities-and-kernels
- Documentación de scikit-learn, `pairwise_distances`:
  https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html
- Documentación de SciPy, distancias espaciales:
  https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
