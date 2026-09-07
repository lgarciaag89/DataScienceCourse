# Evaluación práctica de Estadística con Python
## Descriptores moleculares de péptidos

**Duración:** 2 horas  
**Valor:** 100 puntos  
**Temas:** 4.1.1 Tendencias y dispersión; 4.1.2 Correlación y causalidad

---

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

# Ejercicio 1 — Exploración del conjunto de datos
**10 puntos — 10 minutos**

Realiza una exploración inicial del dataset.

### 1.1

Determina:

- número de filas;
- número de columnas;
- número de variables numéricas;
- número de variables categóricas.

### 1.2

Determina cuántos péptidos pertenecen a cada clase.

### 1.3

Verifica si existen valores faltantes.

### Preguntas

**a)** ¿Cuántos péptidos contiene el conjunto de datos?

**b)** ¿Cuántos descriptores numéricos contiene?

**c)** ¿Las dos clases tienen el mismo número de observaciones? Si no, indica cuál es mayoritaria.

**d)** ¿Existen valores faltantes?

---

# Ejercicio 2 — Tendencias centrales
**15 puntos — 15 minutos**

Trabaja con los siguientes tres descriptores:

```text
ESM2_t33_MEAN_1202
ESM2_t33_MEAN_529
CHOQUET[D;0.5;AO2;0.9]_C_pbs
```

Para cada descriptor calcula:

- media;
- mediana;
- moda;
- mínimo;
- máximo.

Construye una tabla resumen.

### Preguntas

**a)** ¿En cuál descriptor la media y la mediana son más similares?

**b)** ¿En cuál existe una diferencia más evidente entre media y mediana?

**c)** ¿Qué puede indicar una diferencia grande entre media y mediana?

**d)** Para cada descriptor, indica cuál medida de tendencia central consideras más representativa y explica por qué.

---

# Ejercicio 3 — Dispersión
**15 puntos — 15 minutos**

Para los tres descriptores anteriores calcula:

- rango;
- varianza;
- desviación estándar;
- Q1;
- Q3;
- IQR.

Utiliza:

```python
serie.quantile(0.25)
serie.quantile(0.75)
```

y recuerda:

```text
IQR = Q3 - Q1
```

Construye una tabla con los resultados.

### Preguntas

**a)** ¿Cuál descriptor presenta el mayor rango?

**b)** ¿Cuál presenta el mayor IQR?

**c)** ¿Cuál presenta mayor desviación estándar?

**d)** ¿Puedes concluir que el descriptor con mayor desviación estándar es necesariamente el más variable? Explica considerando que los descriptores pueden estar en escalas diferentes.

---

# Ejercicio 4 — Simetría, asimetría y valores atípicos
**15 puntos — 20 minutos**

Analiza los siguientes dos descriptores:

```text
ESM2_t33_MEAN_1202
CHOQUET[D;0.5;AO2;0.9]_C_pbs
```

Para cada uno:

1. construye un histograma;
2. construye un boxplot;
3. calcula media y mediana;
4. calcula el IQR;
5. identifica posibles valores atípicos utilizando el criterio:

```text
Límite inferior = Q1 - 1.5 × IQR

Límite superior = Q3 + 1.5 × IQR
```

### Preguntas

**a)** ¿Cuál de los dos descriptores presenta una distribución más aproximadamente simétrica?

**b)** ¿Cuál presenta una mayor asimetría?

**c)** ¿La comparación entre media y mediana respalda tu observación?

**d)** ¿Existen posibles valores atípicos?

**e)** Explica cómo los valores extremos pueden afectar la media.

**f)** ¿Qué medida —media o mediana— sería más robusta frente a valores extremos? Explica.

---

# Ejercicio 5 — Correlación entre descriptores
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

# Ejercicio 6 — Correlación y causalidad
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

# Ejercicio 7 — Descriptores y clases de péptidos
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

# Ejercicio 8 — Análisis integrador
**10 puntos — 15 minutos**

Utilizando los resultados obtenidos en los ejercicios anteriores, escribe una conclusión estadística de **150–200 palabras**.

Tu conclusión debe responder:

1. ¿Qué descriptor presenta mayor evidencia de asimetría?
2. ¿Qué descriptor presenta mayor dispersión?
3. ¿Qué relación de correlación te pareció más relevante?
4. ¿Qué información aporta la comparación entre `ABP` y `NoNABP`?
5. ¿Por qué estos resultados estadísticos no permiten, por sí solos, establecer relaciones causales?

Incluye al menos **un gráfico** que consideres especialmente útil para sustentar tu conclusión.

---

# Distribución de puntos

| Ejercicio | Tema | Puntos |
|---|---|---:|
| 1 | Exploración | 10 |
| 2 | Tendencia central | 15 |
| 3 | Dispersión | 15 |
| 4 | Simetría, asimetría y outliers | 15 |
| 5 | Correlación | 15 |
| 6 | Correlación y causalidad | 15 |
| 7 | Comparación por clase | 15 |
| 8 | Integración | 10 |
| **Total** | | **100** |

---

# Criterios generales

Se evaluará:

- **Código correcto:** 25 %
- **Cálculos estadísticos:** 25 %
- **Visualizaciones:** 15 %
- **Interpretación estadística:** 25 %
- **Claridad y organización:** 10 %

Una respuesta numéricamente correcta pero sin interpretación podrá recibir una puntuación parcial.
