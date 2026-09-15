# Evaluación práctica de Estadística con Python
## Descriptores moleculares de péptidos


## Contexto

El archivo `peptides.csv` contiene **9,816 péptidos** y **128 variables**:

- `Class`: clase del péptido (`ABP` o `NoNABP`);
- 127 variables numéricas correspondientes a descriptores moleculares.

El objetivo es utilizar Python para **describir, comparar e interpretar estadísticamente** los datos.

> **Importante:** no basta con obtener los valores mediante Python. Cada resultado deberá acompañarse de una interpretación.

---

# Instrucciones generales

Utiliza Python y las siguientes bibliotecas:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

Carga los datos:

```python
df = pd.read_csv("peptides.csv")
```

No es necesario modificar los datos originales.

Cuando se solicite seleccionar un descriptor, utiliza exactamente el nombre de la columna correspondiente.

---

# Ejercicio 1 — Correlación entre descriptores
**15 puntos — 20 minutos**

Calcula la matriz de correlación de Pearson para todos los descriptores numéricos.

```python
numeric = df.select_dtypes(include="number")
corr = numeric.corr()
```

Después identifica:

- el par de descriptores con **mayor correlación positiva**;
- el par de descriptores con **mayor correlación negativa**.

Para evitar seleccionar la diagonal de la matriz, puedes utilizar:

```python
mask = np.triu(np.ones(corr.shape), k=1).astype(bool)

pairs = corr.where(mask).stack()
```

Ordena los resultados:

```python
pairs.sort_values(ascending=False).head()
```

y

```python
pairs.sort_values().head()
```

### Para el par con mayor correlación positiva

Calcula el coeficiente de Pearson y construye un gráfico de dispersión.

### Para el par con mayor correlación negativa

Haz lo mismo.

### Preguntas

**a)** ¿Cuál es el valor de la mayor correlación positiva?

**b)** ¿Cuál es el valor de la mayor correlación negativa?

**c)** ¿Qué significa que el coeficiente sea cercano a +1?

**d)** ¿Qué significa que sea cercano a -1?

**e)** ¿La magnitud del coeficiente de correlación es suficiente para afirmar que existe una relación causal?

---

# Ejercicio 2 — Correlación y causalidad
**15 puntos — 15 minutos**

Supongamos que dos descriptores presentan una correlación de:

```text
r = 0.95
```

Un investigador afirma:

> "El primer descriptor provoca el aumento del segundo descriptor."

### Responde

**a)** ¿Es válida esta conclusión únicamente a partir de `r = 0.95`?

**b)** Explica con tus propias palabras la diferencia entre **correlación** y **causalidad**.

**c)** Propón una posible explicación alternativa para que dos descriptores moleculares estén fuertemente correlacionados sin que uno necesariamente cause al otro.

**d)** ¿Qué tipo de evidencia adicional necesitaríamos para hablar de causalidad con mayor confianza?

---

# Ejercicio 3 — Descriptores y clases de péptidos
**15 puntos — 20 minutos**

La variable `Class` divide los péptidos en:

- `ABP`;
- `NoNABP`.

Selecciona el descriptor:

```text
ESM2_t33_MEAN_753
```

Compara su comportamiento entre ambas clases.

Calcula, para cada clase:

- media;
- mediana;
- desviación estándar;
- mínimo;
- máximo.

Puedes utilizar:

```python
df.groupby("Class")["ESM2_t33_MEAN_753"].agg(
    ["mean", "median", "std", "min", "max"]
)
```

Construye además un boxplot:

```python
sns.boxplot(
    data=df,
    x="Class",
    y="ESM2_t33_MEAN_753"
)

plt.show()
```

### Preguntas

**a)** ¿Qué clase presenta una media mayor?

**b)** ¿Qué clase presenta mayor dispersión?

**c)** ¿Las distribuciones de ambas clases parecen diferentes?

**d)** Si observas una diferencia entre las clases, ¿puedes afirmar que el descriptor **causa** que un péptido pertenezca a `ABP`?

**e)** ¿Qué diferencia existe entre decir "el descriptor está asociado con la clase" y decir "el descriptor determina la clase"?

---

# Ejercicio 4 — Análisis integrador
**10 puntos — 15 minutos**

Utilizando los resultados obtenidos en los ejercicios anteriores, escribe una conclusión estadística de **150–200 palabras**.

Tu conclusión debe responder:

1. ¿Qué descriptor presenta mayor evidencia de asimetría?
2. ¿Qué descriptor presenta mayor dispersión?
3. ¿Qué relación de correlación te pareció más relevante?
4. ¿Qué información aporta la comparación entre `ABP` y `NoNABP`?
5. ¿Por qué estos resultados estadísticos no permiten, por sí solos, establecer relaciones causales?

Incluye al menos **un gráfico** que consideres especialmente útil para sustentar tu conclusión.


# Criterios generales

Se evaluará:

- **Código correcto:** 25 %
- **Cálculos estadísticos:** 25 %
- **Visualizaciones:** 15 %
- **Interpretación estadística:** 25 %
- **Claridad y organización:** 10 %

Una respuesta numéricamente correcta pero sin interpretación podrá recibir una puntuación parcial.
