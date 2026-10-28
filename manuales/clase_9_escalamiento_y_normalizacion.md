# Clase 9 — Escalamiento y normalización de datos

**Duración:** 2 horas  
**Asignatura:** Ciencia de Datos  
**Semana:** 9 (12–18 de octubre de 2026)  
**Contexto:** propiedades de materiales y análisis basado en distancias

## Temas

- Representación de observaciones y variables como puntos en un espacio.
- Distancia euclidiana y efecto de las unidades.
- Estandarización con `StandardScaler`.
- Escalamiento al intervalo [0, 1] con `MinMaxScaler`.
- Escalamiento robusto y normalización por fila.
- Uso correcto de `fit`, `transform` y `fit_transform`.
- Efectos del escalamiento en algoritmos basados en distancias, como K-Means.

## Objetivos de aprendizaje

Al finalizar la clase, el estudiante será capaz de:

1. Representar las observaciones de una tabla como puntos definidos por sus variables.
2. Explicar por qué las unidades de medida pueden alterar una distancia euclidiana.
3. Diferenciar estandarización, escalamiento Min-Max, escalamiento robusto y normalización por fila.
4. Aplicar `StandardScaler` y `MinMaxScaler` a variables numéricas con Python.
5. Interpretar qué información conserva y qué limitaciones tiene cada transformación.
6. Ajustar un escalador con los datos de entrenamiento y aplicarlo a otros datos sin fuga de información.
7. Argumentar por qué escalar es una decisión analítica y no un método para limpiar datos.

## Distribución de la clase

| Tiempo | Tema | Actividad |
|---:|---|---|
| 0–10 min | Activación | Comparar diferencias de tamaño y densidad |
| 10–30 min | Observaciones, variables y distancias | Interpretación geométrica y ejemplo |
| 30–60 min | Métodos de escalamiento | Estandarización, Min-Max, robusto y normalización |
| 60–85 min | Demostración con Python | Transformar datos y comparar distancias |
| 85–110 min | Ejercicio en parejas | Cálculo manual y prueba de sensibilidad a extremos |
| 110–120 min | Cierre | Discusión, comprobación de aprendizaje y conexión con K-Means |

---

# 1. Activación: ¿qué diferencia domina? (10 min)

Consideremos dos materiales medidos en las mismas unidades:

| Material | Tamaño (nm) | Densidad (g/cm³) |
|---|---:|---:|
| A | 10 | 2.0 |
| B | 20 | 2.5 |

La diferencia de tamaño es **10 nm** y la de densidad es **0.5 g/cm³**. Si usamos esos números directamente como coordenadas, la distancia euclidiana es:

$$
d(A,B)=\sqrt{(20-10)^2+(2.5-2.0)^2}
=\sqrt{100+0.25}\approx10.012
$$

La distancia suma las diferencias **al cuadrado**: el tamaño aporta 100 y la densidad aporta 0.25. Así, con esta representación, el tamaño domina el resultado.

Pero el resultado depende de las unidades: si el tamaño se expresa en micrómetros, la diferencia es 0.01 en vez de 10, y su aporte al cuadrado pasa a ser 0.0001. La densidad dominaría entonces la distancia. Los materiales no cambiaron; solo cambió la unidad usada para escribir el tamaño.

**Idea clave:** al calcular distancias directamente, las variables con valores numéricos de mayor escala pueden dominar. Eso no significa que sean científicamente más importantes.

---

# 2. Observaciones, variables y distancias (20 min)

En una tabla de propiedades:

- Cada **fila** representa una observación; por ejemplo, un material.
- Cada **columna** representa una variable o propiedad; por ejemplo, tamaño, densidad o módulo elástico.
- Un identificador, como el nombre o código del material, sirve para rastrear la observación, pero no se incluye en el cálculo de una distancia.

Con tres propiedades, cada material puede representarse como un punto:

$$
x_i=(x_{i1},x_{i2},x_{i3})
$$

La distancia euclidiana entre dos observaciones es:

$$
d(x_i,x_j)=\sqrt{\sum_{p=1}^{m}(x_{ip}-x_{jp})^2}
$$

## 2.1 Ejemplo del efecto de las unidades

Los materiales A y B del ejemplo inicial corresponden a los puntos $(10,2.0)$ y $(20,2.5)$:

$$
d=\sqrt{(20-10)^2+(2.5-2.0)^2}
 =\sqrt{100+0.25}\approx10.012
$$

La contribución del tamaño al cuadrado es 100; la de la densidad es 0.25. Por eso, el tamaño domina esta distancia sin escalar. Si se expresa en micrómetros en vez de nanómetros, los valores de tamaño pasan de 10 y 20 a 0.01 y 0.02:

$$
d=\sqrt{(0.02-0.01)^2+(2.5-2)^2}
 =\sqrt{0.0001+0.25}\approx0.5001
$$

La relación entre los materiales no cambió; cambió la representación numérica y, con ella, la distancia calculada. En consecuencia, también puede cambiar qué observaciones se consideran cercanas.

---

# 3. Métodos de escalamiento (30 min)

Escalar transforma los valores de las variables para hacerlos más comparables bajo algún criterio. No existe una transformación universalmente correcta: la elección debe considerar los datos, el método de análisis y el significado de las propiedades.

## 3.1 Estandarización: `StandardScaler`

Para cada variable, resta su media y divide por su desviación estándar:

$$
z_{ip}=\frac{x_{ip}-\mu_p}{\sigma_p}
$$

Después de ajustar la transformación, cada variable tiene media cercana a 0 y desviación estándar 1, salvo las variables constantes.

- Conserva el orden relativo de los valores de cada variable.
- Centra los valores alrededor de la media.
- Puede verse afectado por valores extremos, porque estos influyen en la media y la desviación estándar.
- **No** convierte los datos en una distribución normal.

En `scikit-learn`, `StandardScaler` usa la desviación estándar poblacional para ajustar la transformación.

## 3.2 Escalamiento Min-Max: `MinMaxScaler`

La transformación predeterminada lleva los valores usados para ajustar el escalador al intervalo [0, 1]:

$$
u_{ip}=\frac{x_{ip}-\min(x_p)}{\max(x_p)-\min(x_p)}
$$

- Los valores mínimo y máximo de ajuste se transforman a 0 y 1.
- Los valores intermedios conservan su posición relativa dentro del rango.
- Los extremos determinan el rango y pueden comprimir la mayoría de las observaciones.
- Un dato nuevo puede quedar fuera de [0, 1] si supera el máximo o queda por debajo del mínimo de ajuste.

## 3.3 Escalamiento robusto: `RobustScaler`

`RobustScaler` centra cada variable con su mediana y divide por su rango intercuartílico (IQR):

$$
x'_{ip}=\frac{x_{ip}-\operatorname{mediana}(x_p)}{\operatorname{IQR}(x_p)}
$$

Puede ser una opción cuando hay valores extremos que distorsionan la media y la desviación estándar. No elimina esos valores ni garantiza que la variable transformada quede en un intervalo fijo.

## 3.4 Normalización por fila

La normalización de cada fila a norma 1 es distinta del escalamiento de columnas. En `scikit-learn`, `Normalizer` actúa sobre cada observación para que su vector tenga norma unitaria.

- Puede ser útil cuando importa la dirección o el perfil relativo de una observación.
- Reduce el efecto de la magnitud total de cada fila.
- No sustituye a `StandardScaler`, `MinMaxScaler` ni `RobustScaler`.

> **Diferencia esencial:** los escaladores de este tema ajustan las columnas; la normalización por norma 1 transforma cada fila.

## 3.5 Comparación para decidir

| Método | Qué utiliza | Puede ser conveniente cuando… | Precaución |
|---|---|---|---|
| Sin escalar | Valores y unidades originales | Las unidades ya son comparables y tienen interpretación adecuada | Una variable de gran escala puede dominar |
| `StandardScaler` | Media y desviación estándar | Se busca centrar y comparar variaciones relativas | Los extremos influyen en ambos parámetros |
| `MinMaxScaler` | Mínimo y máximo | Se necesita un rango conocido para los datos de ajuste | Un extremo puede comprimir el resto |
| `RobustScaler` | Mediana e IQR | Hay valores extremos y se quiere reducir su influencia | No limita los datos a un rango fijo |
| `Normalizer` | Norma de cada fila | Interesa comparar perfiles o direcciones | Se pierde parte de la información de magnitud |

El escalamiento asigna pesos implícitos a las variables. Antes de aplicarlo, conviene preguntar: **¿qué significa que dos materiales difieran en una desviación estándar en cada propiedad?** Esa decisión no sustituye el criterio del dominio.

---

# 4. Demostración con Python (25 min)

La siguiente demostración crea una tabla pequeña en el propio código, por lo que puede ejecutarse sin descargar un archivo de datos. Las propiedades y valores son sintéticos y sirven para observar cómo actúan las transformaciones.

```python
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import (
    MinMaxScaler,
    RobustScaler,
    StandardScaler,
)

df = pd.DataFrame(
    {
        "material": ["M1", "M2", "M3", "M4", "M5"],
        "tamano_nm": [10, 12, 15, 20, 100],
        "densidad_g_cm3": [2.0, 2.1, 2.4, 2.5, 2.6],
        "modulo_GPa": [50, 55, 60, 70, 75],
    }
)

columnas = ["tamano_nm", "densidad_g_cm3", "modulo_GPa"]
X = df[columnas].copy()

assert not X.isna().any().any()

estandarizador = StandardScaler()
Z = estandarizador.fit_transform(X)

escalador_minmax = MinMaxScaler()
U = escalador_minmax.fit_transform(X)

escalador_robusto = RobustScaler()
R = escalador_robusto.fit_transform(X)

print("Desviación estándar poblacional original:")
print(X.std(ddof=0).round(3))

print("\nDesviación estándar después de StandardScaler:")
print(pd.DataFrame(Z, columns=columnas).std(ddof=0).round(3))

print("\nMínimos y máximos después de MinMaxScaler:")
print(pd.DataFrame(U, columns=columnas).agg(["min", "max"]).round(3))

print("\nDatos después de RobustScaler:")
print(pd.DataFrame(R, columns=columnas).round(3))

print("\nDistancias desde el primer material:")
print("Sin escalar:", pairwise_distances(X)[0].round(3))
print("Estandarizados:", pairwise_distances(Z)[0].round(3))
print("Escalados a [0, 1]:", pairwise_distances(U)[0].round(3))
```

## 4.1 Preguntas para guiar la demostración

1. ¿Qué columna tiene la desviación estándar más grande antes de escalar?
2. ¿Por qué la distancia sin escalar puede reflejar principalmente diferencias de tamaño?
3. ¿Qué indica que la desviación estándar de cada columna estandarizada sea 1?
4. ¿Todas las observaciones conservan la misma distancia entre sí después de escalar?
5. ¿Qué efecto puede tener el valor de 100 nm sobre `MinMaxScaler`?
6. ¿El escalamiento eliminó o corrigió ese valor extremo?

**Punto de interpretación:** las distancias cambian porque cambia la contribución relativa de las variables. La transformación no decide cuál propiedad es relevante para la pregunta científica.

## 4.2 `fit`, `transform` y fuga de información

- `fit` estima los parámetros de la transformación, como medias, desviaciones, mínimos o máximos.
- `transform` aplica los parámetros ya estimados a los datos.
- `fit_transform` realiza ambas operaciones sobre los mismos datos.

En un análisis predictivo, primero se separan entrenamiento y prueba. El escalador se ajusta **solo** con entrenamiento; después se aplica a ambos conjuntos:

```python
from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(
    X,
    test_size=0.2,
    random_state=42,
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Si se usa `fit_transform` antes de separar los datos, la información de prueba influye en los parámetros del escalador. Esto causa **fuga de información** y puede producir una evaluación demasiado optimista.

En la primera demostración de esta clase se ajusta cada transformación a todo el conjunto únicamente para describir sus efectos; no se entrena ni evalúa un modelo predictivo.

---

# 5. Ejercicio en parejas (25 min)

## Parte A — Cálculo manual

Consideren la variable:

$$
x=[2,4,6]
$$

Usen la desviación estándar poblacional y calculen:

1. La media y la desviación estándar poblacional.
2. Los tres valores transformados con `StandardScaler`.
3. Los tres valores transformados con `MinMaxScaler`.
4. Qué valores quedan centrados en 0 y cuáles quedan en el intervalo [0, 1].

## Parte B — Efecto de un valor extremo

Agreguen el valor 100:

$$
x=[2,4,6,100]
$$

Antes de ejecutar Python, predigan qué ocurrirá con los valores transformados de 2, 4 y 6. Después, verifiquen con:

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

x = np.array([[2], [4], [6]], dtype=float)
x_con_extremo = np.array([[2], [4], [6], [100]], dtype=float)

for nombre, escalador in [
    ("StandardScaler", StandardScaler()),
    ("MinMaxScaler", MinMaxScaler()),
]:
    anteriores = escalador.fit_transform(x).ravel()
    nuevos = escalador.fit_transform(x_con_extremo).ravel()[:3]
    print(nombre)
    print("Sin extremo:", anteriores.round(3))
    print("Con extremo:", nuevos.round(3))
```

## Parte C — Interpretación

En parejas, respondan:

1. ¿Los valores transformados de 2, 4 y 6 cambian al incluir 100? ¿Por qué?
2. ¿Qué método resulta más sensible a ese extremo en este ejemplo?
3. ¿Qué información se pierde o se modifica al escalar?
4. ¿Qué criterio del dominio usarían para decidir cómo tratar las propiedades de un material?

### Respuestas orientativas para la discusión

- Para [2, 4, 6], la media es 4 y la desviación estándar poblacional es aproximadamente 1.633. Los valores estandarizados son aproximadamente [-1.225, 0, 1.225].
- Los valores Min-Max son [0, 0.5, 1].
- Al añadir 100, cambian los parámetros de ambos escaladores y, por tanto, también cambian las transformaciones de los valores originales.
- Min-Max coloca los valores de 2, 4 y 6 muy cerca de 0 porque 100 amplía el rango. `StandardScaler` también cambia al recalcular la media y la desviación estándar.
- El escalamiento no elimina el valor extremo ni determina si es un error de medición: eso requiere revisar el contexto y la calidad de los datos.

---

# 6. Cierre (10 min)

## Comprobación de aprendizaje

Antes de terminar, cada estudiante responde en una o dos frases:

1. ¿Por qué las unidades pueden cambiar una distancia euclidiana?
2. ¿Cuál es la diferencia entre estandarizar columnas y normalizar filas?
3. ¿Qué error se comete al ajustar el escalador antes de separar entrenamiento y prueba?
4. ¿Escalar equivale a limpiar los datos o eliminar anomalías? ¿Por qué?

## Ideas clave

- Las distancias dependen de las escalas y unidades de las variables.
- `StandardScaler`, `MinMaxScaler` y `RobustScaler` transforman columnas con criterios distintos.
- `Normalizer` opera por fila y no es equivalente a escalar columnas.
- El método elegido cambia la geometría de los datos y debe justificarse con la pregunta científica.
- Escalar no elimina anomalías ni reemplaza la revisión de calidad de datos.
- En un flujo predictivo, el escalador se ajusta con entrenamiento y se reutiliza para transformar validación y prueba.

**Conexión con la siguiente clase:** K-Means utiliza distancias; por ello, sus agrupamientos pueden cambiar según las decisiones de escalamiento tomadas aquí.

## Referencia

Documentación oficial de scikit-learn: [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html).
