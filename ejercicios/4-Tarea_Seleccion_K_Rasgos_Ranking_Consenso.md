# Tarea: selección de los mejores K rasgos mediante un ranking de consenso

**Materia:** Ciencia de Datos  
**Duración estimada:** 2 horas  
**Modalidad:** individual  
**Producto:** notebook ejecutable (`.ipynb`) y tabla final (`.csv`)  
**Valor sugerido:** 100 puntos

---

## 1. Situación problemática

Se proporciona un conjunto de datos de clasificación formado por $n$
observaciones, $p$ rasgos numéricos y una variable objetivo binaria $Y$.

El objetivo es seleccionar los **mejores $K$ rasgos** combinando los rankings
obtenidos con distintas métricas. La decisión final no debe depender de una
sola medida, sino del consenso entre varias perspectivas:

- asociación lineal;
- asociación monotónica;
- dependencia general;
- importancia dentro de un bosque aleatorio;
- efecto sobre el desempeño al permutar un rasgo;
- separación local entre clases.

El valor de $K$ será indicado por el profesor. Si no se especifica, utilice:

```python
K = 5
```

---

## 2. Objetivo de aprendizaje

Al finalizar la tarea, el estudiante deberá ser capaz de:

1. calcular diferentes métricas de relevancia de rasgos;
2. convertir métricas con escalas distintas en rankings comparables;
3. construir un ranking de consenso mediante el promedio de posiciones;
4. seleccionar los mejores $K$ rasgos;
5. analizar acuerdos, desacuerdos y limitaciones de la selección;
6. comprobar si el subconjunto seleccionado conserva la capacidad predictiva.

---

## 3. Métricas que deben utilizarse

Calcule las siguientes siete medidas para cada rasgo:

| Métrica | Valor usado para ordenar | Mejor posición |
| --- | --- | --- |
| Pearson | $\left\lvert r(X_j,Y) \right\rvert$ | valor más alto |
| Spearman | $\left\lvert \rho(X_j,Y)\right\rvert$ | valor más alto |
| Información mutua | $I(X_j;Y)$ | valor más alto |
| MDI | `feature_importances_` | valor más alto |
| Importancia por permutación | caída media del desempeño | valor más alto |
| ReliefF | puntuación del rasgo | valor más alto |
| Entropia Normalizada | $H(X_j)/log_2(k)$ | valor más alto |

Se utilizan los valores absolutos de Pearson y Spearman porque una asociación
negativa fuerte también puede ser predictivamente relevante.

> **Nota sobre la entropía:** deberá calcularse respeto a la entropia maxima posible en los datos ($log_2k$).

**Utilice para calcular enetropia**
```python
import numpy as np
from scipy import stats

def numeric_entropy(x: np.ndarray, bins='auto'):
    """
    Calcula la entropía de una variable numérica continua discretizándola.
    """
    if x.size == 0:
        return 0.0
        
    # 1. Calcular el histograma (frecuencias por intervalo)
    # 'counts' almacena cuántos elementos caen en cada 'bin'
    counts, bin_edges = np.histogram(x, bins=bins)
    
    # 2. Calcular la entropía sobre los conteos
    # stats.entropy convierte automáticamente los conteos a probabilidades
    return stats.entropy(counts)

# Ejemplo de uso con datos continuos (incluso con negativos)
x = np.random.normal(loc=0, scale=1, size=1000)
h = numeric_entropy(x)

print(f"Entropía aproximada: {h}")
```

> **Nota sobre $R^2$:** no se utilizará porque el problema es de clasificación.
> En un problema de regresión podría añadirse el $R^2$ univariado calculado en
> validación como una séptima medida.

---

## 4. Regla para construir el ranking de consenso

Para cada métrica $m$, asigne a cada rasgo $X_j$ una posición
$R_{jm}$:

- posición 1: mejor rasgo según esa métrica;
- posición 2: segundo mejor rasgo;
- y así sucesivamente hasta la posición $p$.

Sea $s_{jm}$ el valor del rasgo $X_j$ según la métrica $m$. Primero se
transforma cada valor en una posición descendente:

$$
R_{jm}=\operatorname{rank}_{\mathrm{desc}}(s_{jm}),
$$

de modo que el mayor valor de cada métrica recibe la posición 1. Después, el
ranking promedio del rasgo $X_j$ se calcula como:

$$
\overline{R}_j
=
\frac{1}{M}
\sum_{m=1}^{M}R_{jm},
\qquad j=1,2,\ldots,p,
$$

donde:

- $R_{jm}$ es la posición del rasgo $j$ según la métrica $m$;
- $M=6$ es el número de métricas;
- $p$ es el número total de rasgos;
- un valor pequeño de $\overline{R}_j$ representa un mejor consenso.

Para definir formalmente los mejores $K$ rasgos, sea $\pi$ la permutación de
los índices que ordena los promedios de menor a mayor:

$$
\overline{R}_{\pi(1)}
\leq
\overline{R}_{\pi(2)}
\leq
\cdots
\leq
\overline{R}_{\pi(p)}.
$$

Entonces, el subconjunto seleccionado es:

$$
\mathcal{S}_K
=
\left\{
X_{\pi(1)},X_{\pi(2)},\ldots,X_{\pi(K)}
\right\}.
$$

En caso de empate:

1. seleccione primero el rasgo con mejor ranking de información mutua;
2. si persiste, seleccione el de mejor ranking por permutación;
3. si todavía persiste, ordene alfabéticamente para que el proceso sea
   reproducible.

Use `rank(method="average", ascending=False)` para asignar posiciones. Así,
dos valores iguales reciben el promedio de las posiciones que ocuparían.

---

## 5. Instrucciones

### Parte A. Preparación y control de calidad — 15 puntos

1. Cargue el conjunto de datos.
2. Identifique la variable objetivo y separe $X$ e $Y$.
3. Reporte:
   - dimensiones del conjunto;
   - tipos de datos;
   - cantidad de valores faltantes;
   - distribución de las clases;
   - rasgos constantes o casi constantes.
4. Divida los datos en entrenamiento y prueba con proporción 80/20,
   estratificación y `random_state=42`.

Todas las métricas de selección deben calcularse usando el conjunto de
**entrenamiento**. El conjunto de prueba se reservará para la evaluación final.

### Parte C. Cálculo de métricas — 30 puntos

Para cada rasgo calcule:

1. valor absoluto de Pearson;
2. valor absoluto de Spearman;
3. información mutua;
4. MDI de un `RandomForestClassifier`;
5. importancia por permutación sobre una partición de validación o mediante
   validación cruzada;
6. ReliefF después de escalar los rasgos.
7. Entropia

Utilice al menos estos parámetros para el bosque:

```python
RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1,
)
```

Para la importancia por permutación use al menos 20 repeticiones e indique la
métrica de desempeño seleccionada. Se recomienda `balanced_accuracy` si las
clases están desbalanceadas; en otro caso puede usarse `accuracy`.

### Parte D. Rankings individuales — 15 puntos

Convierta cada columna de valores en posiciones. La tabla deberá contener, como
mínimo:

| Rasgo | Pearson | Rank Pearson | Spearman | Rank Spearman | MI | Rank MI | MDI | Rank MDI | Permutación | Rank Permutación | ReliefF | Rank ReliefF | Rank Entropia|
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | 

Compruebe que:

- un valor alto produce una posición pequeña;
- no se promedian los valores originales de las métricas;
- las posiciones, y no sus escalas, son las que se combinan.

### Parte E. Ranking de consenso y selección Top-K — 15 puntos

1. Calcule el promedio de las siete posiciones.
2. Ordene los rasgos de menor a mayor promedio.
3. Aplique la regla de desempate.
4. Presente los mejores $K$ rasgos.
5. Exporte la tabla completa como `ranking_consenso.csv`.

La tabla final deberá seguir esta estructura:

| Posición final | Rasgo | Rank promedio | Mejor rank | Peor rank | Desviación de ranks | Seleccionado |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 |  |  |  |  |  | Sí |
| 2 |  |  |  |  |  | Sí |

La desviación estándar de las posiciones permitirá distinguir entre:

- **consenso estable:** promedio bajo y poca variación entre métricas;
- **selección discutida:** promedio bajo, pero gran desacuerdo entre métricas.

### Parte F. Visualización — 10 puntos

Construya las siguientes figuras:

1. **Mapa de calor:** filas = rasgos, columnas = rankings de las métricas.
2. **Gráfica de barras:** ranking promedio de los mejores 15 rasgos; destaque
   visualmente los $K$ seleccionados.
3. **Diagrama de dispersión:** ranking MDI frente a ranking por permutación,
   con el nombre de los rasgos más discrepantes.

Cada figura debe tener título, etiquetas, leyenda cuando corresponda y una
interpretación de dos o tres oraciones.

## 6. Plantilla de código

Complete únicamente las secciones marcadas con `TODO`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import mutual_info_classif
from sklearn.inspection import permutation_importance
from sklearn.metrics import balanced_accuracy_score, matthews_corrcoef
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Si es necesario:
# %pip install skrebate
from skrebate import ReliefF

RANDOM_STATE = 42
K = 5

# TODO 1: cargar los datos
datos = pd.read_csv("datos.csv")

# TODO 2: indicar el nombre correcto del objetivo
columna_objetivo = "objetivo"
X = datos.drop(columns=columna_objetivo)
y = datos[columna_objetivo]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=RANDOM_STATE,
)

# TODO 3: calcular los valores de las seis métricas.
# Deben quedar como Series con los nombres de los rasgos como índice.
valores = pd.DataFrame(index=X_train.columns)
valores["pearson"] = ...
valores["spearman"] = ...
valores["mi"] = ...
valores["mdi"] = ...
valores["permutacion"] = ...
valores["relieff"] = ...
valores["entropia"] = ...

# TODO 4: convertir cada métrica en ranking.
columnas_metricas = [
    "pearson", "spearman", "mi", "mdi", "permutacion", "relieff", "entropia"
]

for metrica in columnas_metricas:
    valores[f"rank_{metrica}"] = ...

# TODO 5: calcular consenso y dispersión.
columnas_rank = [f"rank_{m}" for m in columnas_metricas]
valores["rank_promedio"] = ...
valores["rank_minimo"] = ...
valores["rank_maximo"] = ...
valores["rank_std"] = ...

# TODO 6: ordenar aplicando los criterios de desempate.
ranking_final = ...
ranking_final["posicion_final"] = ...
ranking_final["seleccionado"] = ...

mejores_k = ...
print("Mejores rasgos:", mejores_k)

# TODO 7: crear las tres visualizaciones.

# TODO 8: exportar el ranking.
ranking_final.to_csv("ranking_consenso.csv", index=True)
```

---

## 7. Preguntas de análisis

Responda con evidencia de sus tablas y figuras:

1. ¿Qué rasgo ocupó la primera posición y cuál fue su ranking promedio?
2. ¿Qué rasgo mostró mayor acuerdo entre las siete métricas?
3. ¿Cuál presentó mayor desacuerdo? Explique una posible causa.
4. ¿Apareció algún rasgo con Pearson bajo e información mutua alta? ¿Qué tipo
   de relación podría indicar?
5. ¿Existen rasgos con MDI alto y permutación baja? ¿Puede explicarse por
   redundancia?
6. ¿Los $K$ rasgos seleccionados contienen información repetida entre sí?
7. ¿El ranking promedio oculta alguna diferencia relevante entre las métricas?
8. ¿Cambian los mejores $K$ rasgos al modificar la semilla? Realice al menos
   una repetición adicional para comprobarlo.

---

## 8. Entregables

El estudiante deberá entregar:

1. `seleccion_rasgos.ipynb`, completamente ejecutado y comentado;
2. `ranking_consenso.csv`, con valores, rankings y posición final;
3. las tres visualizaciones solicitadas;
4. una conclusión de entre 150 y 250 palabras;
5. una lista explícita con los mejores $K$ rasgos.

No se aceptará únicamente la lista final. El procedimiento debe ser
reproducible y cada decisión debe quedar justificada.

---

## 9. Rúbrica de evaluación

| Criterio | Puntos |
| --- | ---: |
| Preparación, partición y control de calidad | 15 |
| Entropía e interpretación del objetivo | 5 |
| Cálculo correcto de las seis métricas | 30 |
| Construcción de rankings individuales | 15 |
| Ranking de consenso y selección Top-K | 15 |
| Visualizaciones e interpretación | 10 |
| Validación del subconjunto y conclusiones | 10 |
| **Total** | **100** |

### Penalizaciones sugeridas

- calcular la selección usando el conjunto de prueba: hasta **−20 puntos**;
- promediar directamente métricas con escalas distintas: hasta **−15 puntos**;
- ordenar Pearson o Spearman sin valor absoluto: hasta **−5 puntos**;
- no fijar semillas o no documentar parámetros: hasta **−5 puntos**;
- entregar código que no se ejecuta de principio a fin: hasta **−10 puntos**.

---

## 10. Criterio de éxito

La tarea se considera correctamente resuelta cuando el estudiante puede
afirmar, con una tabla reproducible:

> “Estos son los mejores $K$ rasgos porque presentan las menores posiciones
> promedio entre seis métricas complementarias, y su utilidad fue comprobada
> en datos que no participaron en la selección”.
