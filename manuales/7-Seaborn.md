# Manual de visualización de datos con Seaborn

## 1. ¿Qué es Seaborn?

Seaborn es una biblioteca de Python para explorar y comunicar patrones en
datos. Está construida sobre Matplotlib y trabaja especialmente bien con datos
tabulares de pandas. Ofrece funciones de alto nivel para crear gráficos
estadísticos con menos código, agrupar observaciones por categorías y mostrar
distribuciones, relaciones y comparaciones.

Seaborn complementa a Matplotlib: se puede usar Seaborn para construir el
gráfico y Matplotlib para ajustar detalles o guardar la figura.

### Objetivos

Al terminar este manual podrás:

- preparar datos tabulares para graficarlos;
- elegir gráficos apropiados para distribuciones, relaciones y categorías;
- usar color y paneles para comparar grupos;
- personalizar, guardar e interpretar visualizaciones;
- reconocer limitaciones estadísticas comunes de los gráficos.

---

## 2. Instalación e importación

Si Seaborn no está instalado en el entorno de Python:

```bash
python -m pip install seaborn
```

En un notebook, también se puede ejecutar:

```python
%pip install seaborn
```

Importamos Seaborn, pandas y Matplotlib. El alias convencional de Seaborn es
`sns`.

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print("Versión de Seaborn:", sns.__version__)
```

Se recomienda Seaborn 0.12 o posterior para usar opciones como
`errorbar=`. El resto de los ejemplos sigue la interfaz moderna de Seaborn.

---

## 3. Preparar los datos

Seaborn suele recibir los datos en formato **largo**: cada fila representa una
observación y cada columna una variable. El argumento `data` recibe el
DataFrame, mientras que `x`, `y`, `hue` y otros argumentos indican los nombres
de sus columnas.

Usaremos datos simulados para que todos los ejemplos se puedan ejecutar sin
descargar archivos:

```python
rng = np.random.default_rng(42)
n = 180

grupo = np.repeat(["Control", "Tratamiento A", "Tratamiento B"], n // 3)
horas = rng.uniform(0, 10, n)
efecto_grupo = pd.Series(grupo).map({
    "Control": 0,
    "Tratamiento A": 4,
    "Tratamiento B": 8,
}).to_numpy()
respuesta = 12 + 2.5 * horas + efecto_grupo + rng.normal(0, 5, n)

df = pd.DataFrame({
    "grupo": grupo,
    "horas": horas,
    "respuesta": respuesta,
    "medicion": rng.normal(50, 12, n),
})

df.head()
```

Antes de graficar, revisa los tipos de datos, los valores faltantes y las
categorías:

```python
df.info()
print(df.isna().sum())
print(df["grupo"].value_counts())
```

Los nombres de columnas en los ejemplos son cadenas de texto porque se
seleccionan mediante el argumento `data=df`. Si se pasan series directamente,
también se pueden proporcionar los datos sin el argumento `data`.

---

## 4. Estilo general

`set_theme()` configura el estilo y la apariencia predeterminada de los
gráficos Seaborn y Matplotlib:

```python
sns.set_theme(
    context="notebook",
    style="whitegrid",
    palette="deep",
)
```

- `context`: escala general de texto y elementos (`paper`, `notebook`,
  `talk` o `poster`).
- `style`: fondo y cuadrícula (`white`, `dark`, `whitegrid`, `darkgrid` o
  `ticks`).
- `palette`: paleta de colores predeterminada.

El tema es global para la sesión. Para un gráfico aislado se pueden ajustar
los parámetros de estilo en la propia función o usar `sns.axes_style()` y
`sns.plotting_context()` como administradores de contexto.

---

## 5. Tipos de funciones: ejes y figuras

Muchas funciones de Seaborn se dividen en dos familias:

### Funciones de ejes

Funciones como `scatterplot()`, `histplot()`, `boxplot()` y `heatmap()` dibujan
en un único conjunto de ejes (*Axes*). Pueden recibir `ax=` para integrarse en
una figura de Matplotlib:

```python
fig, ax = plt.subplots(figsize=(7, 4))
sns.scatterplot(data=df, x="horas", y="respuesta", ax=ax)
plt.show()
```

### Funciones de figura

Funciones como `relplot()`, `displot()` y `catplot()` crean una figura y pueden
dividir los datos en paneles mediante `row=` o `col=`. Devuelven un objeto de
Seaborn con métodos para modificar la figura:

```python
g = sns.relplot(
    data=df,
    x="horas",
    y="respuesta",
    col="grupo",
    kind="scatter",
)
g.set_axis_labels("Horas de estudio", "Respuesta")
plt.show()
```

Como regla práctica: usa funciones de ejes cuando quieras controlar un gráfico
individual o componer subgráficos de Matplotlib; usa funciones de figura para
comparar automáticamente varios subconjuntos.

---

## 6. Gráficos de distribuciones

### 6.1 Histograma y densidad

`histplot()` muestra cuántas observaciones caen en cada intervalo. Se puede
añadir una estimación de densidad con `kde=True`.

```python
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(
    data=df,
    x="medicion",
    bins=20,
    kde=True,
    color="steelblue",
    ax=ax,
)
ax.set(title="Distribución de las mediciones", xlabel="Medición", ylabel="Frecuencia")
plt.show()
```

El número y ancho de los intervalos influyen en la apariencia del histograma.
Conviene probar más de una resolución y evitar concluir que hay grupos o
patrones solo por la elección de `bins`.

Para comparar distribuciones por grupo, `hue` asigna un color a cada categoría.
Con `multiple="layer"` las distribuciones se superponen; `multiple="dodge"`
las coloca lado a lado y `multiple="stack"` las apila.

```python
sns.histplot(
    data=df,
    x="medicion",
    hue="grupo",
    bins=18,
    element="step",
    stat="density",
    common_norm=False,
)
plt.title("Distribución de mediciones por grupo")
plt.show()
```

`common_norm=False` normaliza cada grupo de forma independiente. Esto facilita
comparar la forma de las distribuciones, pero no el tamaño relativo de cada
grupo.

### 6.2 Función de distribución acumulada

`ecdfplot()` muestra la proporción de observaciones menor o igual a cada valor.
No depende de intervalos:

```python
sns.ecdfplot(data=df, x="medicion", hue="grupo")
plt.title("Distribución acumulada por grupo")
plt.ylabel("Proporción acumulada")
plt.show()
```

### 6.3 Diagramas de caja y violín

Un diagrama de caja resume la mediana, los cuartiles y posibles observaciones
alejadas del centro:

```python
sns.boxplot(data=df, x="grupo", y="respuesta")
plt.title("Respuesta por grupo")
plt.xlabel("Grupo")
plt.ylabel("Respuesta")
plt.show()
```

Un diagrama de violín añade una representación suavizada de la distribución:

```python
sns.violinplot(
    data=df,
    x="grupo",
    y="respuesta",
    inner="quart",
    cut=0,
)
plt.title("Distribución de la respuesta por grupo")
plt.show()
```

La forma del violín es una estimación de densidad y depende de sus parámetros
de suavizado; no debe interpretarse como una observación directa de los datos.
Para muestras pequeñas, muestra también los puntos o prefiere un gráfico más
transparente:

```python
sns.stripplot(
    data=df,
    x="grupo",
    y="respuesta",
    jitter=True,
    alpha=0.55,
    color="black",
)
plt.show()
```

---

## 7. Gráficos de relaciones

### 7.1 Diagrama de dispersión

`scatterplot()` sirve para estudiar la relación entre dos variables
cuantitativas. `hue` diferencia grupos y `style` puede usar símbolos distintos:

```python
sns.scatterplot(
    data=df,
    x="horas",
    y="respuesta",
    hue="grupo",
    style="grupo",
    s=65,
    alpha=0.8,
)
plt.title("Horas y respuesta")
plt.xlabel("Horas")
plt.ylabel("Respuesta")
plt.show()
```

La transparencia (`alpha`) ayuda cuando muchos puntos se superponen. Si hay
una cantidad muy grande de observaciones, considera usar un mapa de densidad o
una muestra representativa en vez de dibujar cada punto.

### 7.2 Gráfico de línea

`lineplot()` resume observaciones que comparten el mismo valor de `x`. De forma
predeterminada calcula una estimación central y muestra un intervalo de
incertidumbre, que suele ser un intervalo de confianza del 95 %:

```python
df_tiempo = df.assign(
    hora_redondeada=(df["horas"] // 2) * 2
)

sns.lineplot(
    data=df_tiempo,
    x="hora_redondeada",
    y="respuesta",
    hue="grupo",
    marker="o",
    errorbar=("ci", 95),
)
plt.title("Respuesta promedio según horas")
plt.show()
```

Si las observaciones son medidas repetidas de individuos, no basta con resumir
por `x`: también se debe conservar y representar la identidad de cada
individuo (por ejemplo, con `units=` y `estimator=None`, según el diseño).
Para datos de series temporales, verifica que el eje temporal esté ordenado y
que las observaciones tengan el significado esperado.

### 7.3 Tendencia y regresión

`regplot()` dibuja los datos y ajusta una tendencia lineal:

```python
sns.regplot(
    data=df,
    x="horas",
    y="respuesta",
    scatter_kws={"alpha": 0.45},
    line_kws={"color": "black"},
)
plt.title("Tendencia lineal: horas y respuesta")
plt.show()
```

Una línea ajustada no demuestra causalidad ni garantiza que una relación sea
lineal. Examina el patrón de los puntos y los residuos, y considera
transformaciones o modelos adecuados si la forma de la relación lo requiere.

---

## 8. Gráficos para comparar categorías

`countplot()` cuenta observaciones por categoría:

```python
sns.countplot(data=df, x="grupo")
plt.title("Número de observaciones por grupo")
plt.ylabel("Conteo")
plt.show()
```

`barplot()` resume una variable numérica por categoría. Por defecto muestra la
media y un intervalo de incertidumbre:

```python
sns.barplot(
    data=df,
    x="grupo",
    y="respuesta",
    errorbar=("ci", 95),
)
plt.title("Media de respuesta e intervalo de confianza")
plt.show()
```

Una barra oculta la forma de la distribución y su altura no muestra cuántas
observaciones hay en cada grupo. Para describir datos, acompaña el resumen con
un `boxplot`, `violinplot` o puntos individuales, y reporta el tamaño de
muestra cuando sea relevante.

---

## 9. Relaciones entre varias variables

### 9.1 Matriz de dispersión

`pairplot()` genera gráficos para todas las parejas de variables numéricas y
distribuciones en la diagonal:

```python
sns.pairplot(
    data=df,
    vars=["horas", "respuesta", "medicion"],
    hue="grupo",
    corner=True,
    plot_kws={"alpha": 0.6},
)
plt.show()
```

Una matriz de dispersión puede volverse difícil de leer con muchas variables
o filas. Selecciona variables de interés o una muestra antes de generarla.

### 9.2 Mapa de calor de correlaciones

La correlación de Pearson resume asociaciones lineales entre variables
numéricas. Un mapa de calor facilita comparar los coeficientes:

```python
correlaciones = df[["horas", "respuesta", "medicion"]].corr()

fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(
    correlaciones,
    annot=True,
    fmt=".2f",
    cmap="vlag",
    center=0,
    vmin=-1,
    vmax=1,
    ax=ax,
)
ax.set_title("Correlaciones de Pearson")
plt.show()
```

La correlación mide asociación lineal, no causalidad. Una correlación cercana a
cero no descarta relaciones no lineales. Los valores faltantes también pueden
hacer que cada coeficiente se calcule con un subconjunto diferente de filas;
revisa cómo se trataron antes de interpretar la matriz.

---

## 10. Facetas: comparar subconjuntos en paneles

Las facetas crean paneles con escalas y ejes comparables. `relplot()` puede
separar el gráfico por una o más variables categóricas:

```python
g = sns.relplot(
    data=df,
    x="horas",
    y="respuesta",
    hue="grupo",
    col="grupo",
    kind="scatter",
    height=3.5,
    aspect=1,
)
g.set_axis_labels("Horas", "Respuesta")
g.set_titles("{col_name}")
plt.show()
```

Otras funciones de figura útiles son:

- `displot()`: histogramas, densidades y distribuciones acumuladas en paneles;
- `catplot()`: gráficos categóricos como cajas, violines, puntos y barras;
- `lmplot()`: relaciones con ajuste de regresión y facetas.

Si necesitas escalas independientes, `FacetGrid` ofrece opciones como
`sharex=False` y `sharey=False`; úsalas con cuidado, porque dificultan
comparar visualmente magnitudes entre paneles.

---

## 11. Colores y leyendas

Usa `hue` para codificar una variable que quieras comparar. Una paleta
categórica (`deep`, `muted`, `colorblind`) es adecuada para grupos sin orden.
Para valores numéricos continuos, considera una paleta secuencial como
`"viridis"`:

```python
sns.scatterplot(
    data=df,
    x="horas",
    y="respuesta",
    hue="medicion",
    palette="viridis",
)
plt.show()
```

Buenas prácticas:

- limita el número de categorías de color para mantener una leyenda legible;
- elige paletas perceptualmente claras y considera a personas con deficiencias
  en la visión del color;
- no uses el mismo atributo visual para comunicar variables distintas;
- si los grupos tienen un orden real, usa ese orden en los datos y en la
  leyenda;
- proporciona una leyenda clara, especialmente si el color representa valores
  continuos.

---

## 12. Personalizar y guardar gráficos

La mayoría de las funciones de ejes devuelven el objeto `Axes` de Matplotlib.
Puedes guardarlo en una variable y personalizar etiquetas, límites y título:

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax = sns.scatterplot(
    data=df,
    x="horas",
    y="respuesta",
    hue="grupo",
    ax=ax,
)
ax.set(
    title="Respuesta en función de las horas",
    xlabel="Horas de estudio",
    ylabel="Respuesta observada",
)
ax.legend(title="Grupo")
fig.tight_layout()
fig.savefig("respuesta_por_horas.png", dpi=300, bbox_inches="tight")
plt.show()
```

`dpi=300` suele ser suficiente para imágenes rasterizadas en informes. Para
documentos que lo permitan, Matplotlib también puede guardar formatos
vectoriales, como PDF o SVG:

```python
fig.savefig("respuesta_por_horas.pdf", bbox_inches="tight")
```

En notebooks se puede usar `plt.show()` para mostrar la figura. En scripts,
conviene incluirlo explícitamente al final del bloque de visualización.

---

## 13. Errores frecuentes y recomendaciones

1. **Elegir el gráfico por apariencia y no por pregunta.** Decide primero si
   buscas comparar cantidades, ver una distribución, estudiar una relación o
   mostrar una tendencia.
2. **Confundir conteos con proporciones.** Un grupo más grande puede parecer
   tener una distribución distinta solo porque tiene más observaciones.
   Considera normalizar cuando compares formas.
3. **Ocultar los datos con resúmenes.** Una media no describe asimetría,
   multimodalidad ni valores atípicos. Añade puntos o distribuciones cuando
   sea importante.
4. **Usar demasiadas categorías en `hue`.** La leyenda y los colores se vuelven
   difíciles de interpretar.
5. **Interpretar el intervalo como rango de datos.** El intervalo de
   incertidumbre de `barplot()` o `lineplot()` no es el rango donde se
   encuentra la mayoría de las observaciones.
6. **Interpretar una asociación como causa.** Un gráfico describe patrones;
   establecer causas requiere un diseño y análisis apropiados.
7. **No revisar datos faltantes o tipos.** Las columnas numéricas guardadas
   como texto y los valores faltantes pueden producir gráficos inesperados.
8. **Crear gráficos ilegibles.** Etiqueta ejes con unidades, usa títulos
   informativos y aumenta el tamaño de la figura si hay muchas categorías.

---

## 14. Guía rápida para elegir un gráfico

| Pregunta | Gráfico recomendado | Función Seaborn |
|---|---|---|
| ¿Cómo se distribuye una variable numérica? | Histograma o densidad | `histplot()` |
| ¿Cómo se compara una distribución acumulada? | ECDF | `ecdfplot()` |
| ¿Cómo se distribuye una variable por grupo? | Caja, violín o puntos | `boxplot()`, `violinplot()`, `stripplot()` |
| ¿Cómo se relacionan dos variables numéricas? | Dispersión | `scatterplot()` |
| ¿Cómo cambia un resumen con una variable ordenada? | Línea | `lineplot()` |
| ¿Cuántas observaciones hay por categoría? | Conteo | `countplot()` |
| ¿Cómo se comparan resúmenes numéricos entre grupos? | Barras o puntos | `barplot()`, `pointplot()` |
| ¿Qué pares de variables muestran patrones? | Matriz de dispersión | `pairplot()` |
| ¿Cómo se relacionan varias variables numéricas? | Mapa de calor | `heatmap()` |

---

## 4.3 Estadística con Seaborn

En esta sección se reúnen tres familias de herramientas estadísticas de
Seaborn: gráficos de distribución, categóricos y matriciales; grids para
comparar subconjuntos; y gráficos de regresión lineal. La elección de una
función depende de la pregunta, del tipo de variable y de si se necesita un
solo eje o una figura con varios paneles.

### 4.3.1 Gráficos de distribución, categóricos y matriciales

#### Distribuciones: una variable o varios grupos

Para observar una variable numérica se puede elegir entre varias
representaciones:

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.histplot(data=df, x="respuesta", bins=18, ax=axes[0])
axes[0].set_title("Histograma")

sns.kdeplot(data=df, x="respuesta", fill=True, ax=axes[1])
axes[1].set_title("Densidad estimada")

sns.ecdfplot(data=df, x="respuesta", ax=axes[2])
axes[2].set_title("Distribución acumulada")

fig.tight_layout()
plt.show()
```

- `histplot()` muestra frecuencias o densidades por intervalos.
- `kdeplot()` estima una curva suavizada; el suavizado puede ocultar o
  exagerar estructuras, en especial con muestras pequeñas.
- `ecdfplot()` muestra la fracción de observaciones menor o igual que cada
  valor y no requiere definir intervalos.

Para comparar grupos puede usarse `hue`. Por ejemplo, las curvas de densidad
se pueden superponer:

```python
sns.kdeplot(
    data=df,
    x="respuesta",
    hue="grupo",
    fill=True,
    common_norm=False,
    alpha=0.25,
)
plt.title("Densidad de respuesta por grupo")
plt.show()
```

`common_norm=False` normaliza cada grupo por separado. Si interesa comparar
frecuencias absolutas, es preferible mostrar conteos con un histograma y
revisar el tamaño de cada grupo.

#### Gráficos categóricos

Los gráficos categóricos permiten comparar mediciones numéricas entre grupos
o contar observaciones. Las funciones de bajo nivel aceptan `x`, `y` y `hue`;
`catplot()` permite cambiar el tipo de gráfico mediante `kind` y dividirlo en
paneles.

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.stripplot(
    data=df, x="grupo", y="respuesta", jitter=True, alpha=0.55, ax=axes[0]
)
axes[0].set_title("Observaciones")

sns.boxplot(data=df, x="grupo", y="respuesta", ax=axes[1])
axes[1].set_title("Mediana y cuartiles")

sns.violinplot(
    data=df, x="grupo", y="respuesta", inner="quart", cut=0, ax=axes[2]
)
axes[2].set_title("Distribución suavizada")

fig.tight_layout()
plt.show()
```

Otras formas de representar las mismas categorías:

```python
# Conteo de observaciones en cada categoría
sns.countplot(data=df, x="grupo")
plt.title("Tamaño de cada grupo")
plt.show()

# Resumen de respuesta por categoría (media e intervalo de confianza)
sns.barplot(data=df, x="grupo", y="respuesta", errorbar=("ci", 95))
plt.title("Media de respuesta por grupo")
plt.show()
```

`countplot()` es apropiado para conteos; `barplot()` resume una variable
numérica y, por defecto, presenta la media y un intervalo de confianza. Una
barra no muestra la distribución completa. Para cambiar el tipo de gráfico
categórico usando una interfaz de figura:

```python
g = sns.catplot(
    data=df,
    x="grupo",
    y="respuesta",
    kind="box",
    col="grupo",
    height=3.5,
)
g.set_axis_labels("Grupo", "Respuesta")
plt.show()
```

Entre los valores útiles de `kind` para `catplot()` están `"strip"`,
`"swarm"`, `"box"`, `"violin"`, `"boxen"`, `"point"`, `"bar"` y `"count"`.
`swarm` evita superponer puntos, pero puede tardar o saturarse con muchos
datos; en ese caso, `strip` con transparencia o una representación resumida
puede ser más adecuada.

#### Gráficos matriciales

Los mapas de calor representan una matriz mediante color. Para correlaciones,
primero se seleccionan las variables numéricas y después se calcula la matriz:

```python
variables = ["horas", "respuesta", "medicion"]
matriz_corr = df[variables].corr()

fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(
    matriz_corr,
    annot=True,
    fmt=".2f",
    cmap="vlag",
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    ax=ax,
)
ax.set_title("Correlación entre variables")
plt.show()
```

También puede construirse una matriz con resúmenes calculados a partir de
datos categóricos:

```python
tabla = df.pivot_table(
    index="grupo",
    values=["horas", "respuesta", "medicion"],
    aggfunc="mean",
)

sns.heatmap(tabla, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Promedio de variables por grupo")
plt.show()
```

`clustermap()` añade agrupamiento jerárquico de filas y columnas. Es una
opción para explorar qué filas o variables tienen perfiles parecidos:

```python
sns.clustermap(
    matriz_corr,
    annot=True,
    fmt=".2f",
    cmap="vlag",
    center=0,
    figsize=(6, 6),
)
plt.show()
```

El orden reacomodado por `clustermap()` depende de una distancia y un método
de enlace; no representa una relación causal ni necesariamente grupos
reales. La correlación tampoco mide cualquier tipo de dependencia.

### 4.3.2 Grids

Un *grid* organiza varios gráficos en una figura para comparar subconjuntos o
variables. Seaborn ofrece dos estrategias:

1. **Funciones de figura de alto nivel**, como `relplot()`, `displot()` y
   `catplot()`, que generan grids de forma directa.
2. **Clases Grid**, como `FacetGrid`, `PairGrid` y `JointGrid`, que permiten
   mayor control sobre qué dibujar en cada panel.

#### Facetas con `relplot()`, `displot()` y `catplot()`

`col` crea columnas de paneles y `row` crea filas. `hue` añade otra
codificación por color:

```python
g = sns.relplot(
    data=df,
    x="horas",
    y="respuesta",
    hue="grupo",
    col="grupo",
    kind="scatter",
    height=3.5,
)
g.set_axis_labels("Horas", "Respuesta")
g.set_titles("Grupo: {col_name}")
plt.show()
```

La misma idea se aplica a distribuciones y datos categóricos:

```python
# Histogramas en un panel por grupo
g = sns.displot(
    data=df,
    x="medicion",
    col="grupo",
    kind="hist",
    bins=15,
    height=3.5,
)
g.set_axis_labels("Medición", "Frecuencia")
plt.show()

# Comparación categórica en paneles
g = sns.catplot(
    data=df,
    x="grupo",
    y="respuesta",
    col="grupo",
    kind="violin",
    height=3.5,
)
plt.show()
```

En algunos casos es mejor comparar todos los grupos en un mismo eje con
`hue`, en vez de separarlos en paneles. Los paneles ayudan a reducir
superposición; un eje compartido ayuda a comparar directamente las
magnitudes.

#### Control explícito con `FacetGrid`

`FacetGrid` permite definir la estructura de paneles y mapear una función de
gráfico en cada uno:

```python
g = sns.FacetGrid(df, col="grupo", height=3.5, sharex=True, sharey=True)
g.map_dataframe(
    sns.scatterplot,
    x="horas",
    y="respuesta",
    alpha=0.7,
)
g.set_axis_labels("Horas", "Respuesta")
g.set_titles("Grupo: {col_name}")
plt.show()
```

Para incorporar una leyenda o una variable adicional, es posible usar
`hue=` al crear el grid:

```python
g = sns.FacetGrid(df, col="grupo", hue="grupo", height=3.5)
g.map_dataframe(sns.scatterplot, x="horas", y="respuesta")
g.add_legend(title="Grupo")
plt.show()
```

#### Comparar muchas variables con `PairGrid` y `pairplot()`

`pairplot()` es la forma rápida de mostrar relaciones entre varias variables
numéricas:

```python
sns.pairplot(
    data=df,
    vars=["horas", "respuesta", "medicion"],
    hue="grupo",
    corner=True,
    diag_kind="hist",
    plot_kws={"alpha": 0.6},
)
plt.show()
```

Para escoger gráficos distintos en la diagonal y fuera de ella, usa
`PairGrid`:

```python
g = sns.PairGrid(
    df,
    vars=["horas", "respuesta", "medicion"],
    hue="grupo",
    corner=True,
)
g.map_diag(sns.histplot, alpha=0.5)
g.map_offdiag(sns.scatterplot, alpha=0.6)
g.add_legend()
plt.show()
```

#### Relación conjunta con `JointGrid` y `jointplot()`

`jointplot()` muestra la relación entre dos variables y sus distribuciones
marginales:

```python
sns.jointplot(
    data=df,
    x="horas",
    y="respuesta",
    kind="scatter",
    height=6,
)
plt.show()
```

Algunos valores de `kind` son `"scatter"`, `"kde"`, `"hist"` y `"reg"`.
`JointGrid` permite personalizar cada componente por separado:

```python
g = sns.JointGrid(data=df, x="horas", y="respuesta", height=6)
g.plot_joint(sns.scatterplot, alpha=0.6)
g.plot_marginals(sns.histplot, kde=True)
plt.show()
```

`pairplot()` y los grids generan muchos elementos gráficos. Limita las
variables y usa una muestra cuando el conjunto de datos sea grande.

### 4.3.3 Gráficos de regresión lineal

Los gráficos de regresión combinan observaciones con una estimación de la
relación entre variables. Son herramientas exploratorias; no prueban que una
variable cause cambios en otra.

#### `regplot()`: un eje y control detallado

`regplot()` dibuja una nube de puntos y ajusta una recta de regresión con un
intervalo de confianza:

```python
fig, ax = plt.subplots(figsize=(7, 5))
sns.regplot(
    data=df,
    x="horas",
    y="respuesta",
    ci=95,
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "black"},
    ax=ax,
)
ax.set(title="Regresión lineal", xlabel="Horas", ylabel="Respuesta")
plt.show()
```

También se puede dar a la función dos vectores directamente, sin `data` ni
nombres de columnas:

```python
sns.regplot(x=df["horas"], y=df["respuesta"], ci=None)
plt.xlabel("Horas")
plt.ylabel("Respuesta")
plt.show()
```

Opciones útiles:

- `ci=95`: intervalo de confianza; usa `ci=None` para ocultarlo.
- `order=2`: ajusta un polinomio de segundo grado en lugar de una recta.
- `robust=True`: usa una estimación robusta frente a valores extremos.
- `lowess=True`: añade una tendencia local suavizada; no es una recta lineal.
- `x_estimator=np.mean`: resume las respuestas en valores repetidos de `x`.

Ejemplo de tendencia polinómica:

```python
sns.regplot(
    data=df,
    x="horas",
    y="respuesta",
    order=2,
    scatter_kws={"alpha": 0.4},
)
plt.title("Tendencia polinómica de segundo grado")
plt.show()
```

El ajuste polinómico puede seguir mejor una curvatura, pero aumenta el riesgo
de sobreajuste y no debe elegirse solo porque la línea parezca más cercana a
los puntos.

#### `lmplot()`: regresión con grupos y facetas

`lmplot()` es una función de figura: además de estimar regresiones, permite
crear una línea por grupo (`hue`) o separar grupos en paneles (`col`/`row`):

```python
sns.lmplot(
    data=df,
    x="horas",
    y="respuesta",
    hue="grupo",
    height=5,
    scatter_kws={"alpha": 0.5},
    ci=95,
)
plt.show()
```

Para poner cada ajuste en su propio panel:

```python
sns.lmplot(
    data=df,
    x="horas",
    y="respuesta",
    col="grupo",
    col_wrap=3,
    height=3.5,
    scatter_kws={"alpha": 0.5},
)
plt.show()
```

`regplot()` es conveniente cuando se necesita controlar un `Axes` específico
o combinarlo con otros gráficos. `lmplot()` es práctico para regresiones por
grupos y facetas, pero devuelve un objeto de figura (`FacetGrid`), no un
`Axes`.

#### Supuestos e interpretación

Una recta resume una asociación lineal. Antes de interpretarla:

- inspecciona si el patrón entre variables parece aproximadamente lineal;
- revisa valores atípicos que puedan influir mucho en el ajuste;
- recuerda que las observaciones dependientes o medidas repetidas requieren
  un análisis que considere esa estructura;
- distingue el intervalo de confianza de la recta del rango donde se
  encuentran los datos individuales;
- no extrapoles fuera del intervalo observado sin justificación;
- no infieras causalidad de una asociación gráfica.

Seaborn facilita la visualización del ajuste, pero el modelado, las pruebas
de supuestos y las conclusiones estadísticas pueden requerir herramientas
adicionales.

## 4.4 Ejercicios

Usando el DataFrame `df` de este manual:

1. Crea un histograma de `respuesta` separado por `grupo`. Normaliza cada
   grupo por separado e indica qué diferencias observas en la forma de las
   distribuciones.
2. Compara `respuesta` entre grupos con un diagrama de caja y uno de violín.
   ¿Qué información aporta cada uno?
3. Crea un diagrama de dispersión de `horas` y `respuesta`, con color por
   `grupo`. Describe el patrón y explica por qué no permite concluir causalidad.
4. Calcula y representa la matriz de correlación de las variables numéricas.
   ¿Por qué no se debe interpretar la correlación como causalidad?
5. Guarda uno de tus gráficos en PNG con una resolución de 300 dpi y en PDF.
6. Modifica el tamaño, el estilo y la paleta. Comprueba que las etiquetas y
   la leyenda sigan siendo legibles.

### Reto

Añade una columna categórica `condicion` (por ejemplo, `"mañana"` y `"tarde"`)
y crea paneles que comparen la relación entre `horas` y `respuesta` para cada
condición. Mantén las escalas iguales para que la comparación sea justa.

---

## 4.5 Resumen

Seaborn permite explorar datos tabulares con funciones estadísticas de alto
nivel. El flujo habitual consiste en preparar un DataFrame, elegir una función
según la pregunta, mapear variables con argumentos como `x`, `y` y `hue`, y
terminar con etiquetas y una interpretación cuidadosa. Seaborn facilita la
creación del gráfico, pero no sustituye la revisión de los datos ni el
razonamiento estadístico.

Para personalizaciones avanzadas, consulta también el manual del curso
[Visualización de Datos con Matplotlib](./Visualizacion_Datos_Matplotlib_Desde_Cero.md)
y la [documentación oficial de Seaborn](https://seaborn.pydata.org/).
