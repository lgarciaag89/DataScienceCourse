# Estadística y probabilidad computacional

**Materia:** Ciencia de Datos  
**Duración:** 2 horas (120 minutos)  
**Tema:** 4.1 Estadística  
**Subtemas:** 4.1.1 Tendencias y dispersión; 4.1.2 Correlación y causalidad

Este material está diseñado para desarrollarse en un notebook de Jupyter, Google
Colab o VS Code. La clase combina interpretación estadística con cálculos
reproducibles en Python.

---

## 1. Propósito de la clase

La estadística descriptiva permite resumir y explorar un conjunto de datos antes
de construir modelos o tomar decisiones. En esta sesión el estudiante:

- calculará medidas de tendencia central y dispersión;
- interpretará histogramas, boxplots y diagramas de dispersión;
- calculará e interpretará la correlación;
- distinguirá una asociación estadística de una relación causal;
- comunicará conclusiones considerando el contexto y las limitaciones de los
  datos.

> **Idea central:** un número o una gráfica no es una conclusión por sí misma.
> Siempre hay que preguntar qué se midió, cómo se midió y qué otras variables
> podrían explicar el resultado.

## 2. Preparación

### Librerías

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.float_format", "{:.2f}".format)
```

### Recomendación para el docente

Antes de la clase, abrir un notebook con una celda para cada sección. Pedir que
los estudiantes modifiquen los datos y escriban una interpretación en Markdown
después de cada ejercicio. La interpretación es tan importante como el código.

---

## 3. Secuencia didáctica de 120 minutos

| Tiempo | Actividad | Evidencia de aprendizaje |
| ---: | --- | --- |
| 0–10 min | Activación: ¿cómo resumirían las edades de un grupo? | Diferencian dato individual y resumen |
| 10–30 min | Tendencia central: media, mediana y moda | Calculan e interpretan medidas |
| 30–50 min | Dispersión y valores atípicos | Comparan variabilidad con rango, varianza, desviación y cuantiles |
| 50–65 min | Ejercicio guiado de exploración | Construyen un resumen y dos gráficas |
| 65–75 min | Pausa y discusión de resultados | Explican qué medida es más representativa |
| 75–95 min | Correlación y diagrama de dispersión | Calculan `r` y describen dirección e intensidad |
| 95–110 min | Correlación no implica causalidad | Identifican una tercera variable y proponen un diseño |
| 110–118 min | Reto individual | Analizan un conjunto nuevo |
| 118–120 min | Cierre / ticket de salida | Redactan una conclusión con una limitación |

---

## 4. 4.1.1 Tendencias y dispersión

### Tendencia central

Las medidas de tendencia central describen **alrededor de qué valor se
concentran los datos**. Permiten resumir un conjunto de observaciones mediante
un valor representativo y responder a la pregunta: *¿cuál es el valor típico
de los datos?*

- **Media:** suma de los valores dividida entre el número de observaciones.
  Es útil cuando los datos son relativamente homogéneos, pero es sensible a
  valores extremos.
- **Mediana:** valor central al ordenar los datos. Es más robusta frente a
  valores extremos y resulta especialmente útil cuando la distribución es
  asimétrica.
- **Moda:** valor o valores más frecuentes. Es especialmente útil para datos
  categóricos o discretos.

La medida más adecuada depende de la forma de la distribución y del contexto.
Por ejemplo, para describir ingresos con algunos valores muy altos suele ser
preferible la mediana, mientras que la media puede ser útil para calcular un
promedio general.

### Dispersión

Las medidas de dispersión indican **qué tan separados están los datos entre sí
y respecto a su valor central**. Ayudan a evaluar la variabilidad, estabilidad
y heterogeneidad de un conjunto, y responden a la pregunta: *¿qué tan
consistentes son los datos?*

- **Rango:** máximo menos mínimo. Ofrece una idea rápida de la amplitud de los
  datos, aunque es muy sensible a valores extremos.
- **Varianza:** promedio de las desviaciones cuadráticas respecto a la media.
  Una varianza grande indica mayor dispersión, pero sus unidades quedan
  elevadas al cuadrado.
- **Desviación estándar:** raíz cuadrada de la varianza; está en las mismas
  unidades que los datos y permite interpretar qué tan alejadas están
  normalmente las observaciones de la media.
- **Cuartiles y rango intercuartílico (IQR):** el IQR es `Q3 - Q1` y describe
  la dispersión del 50 % central. Es poco sensible a valores atípicos.
- **Coeficiente de variación:** razón entre la desviación estándar y la media,
  normalmente expresada como porcentaje. Permite comparar la variabilidad
  relativa entre variables con escalas o unidades diferentes.

La tendencia central y la dispersión deben analizarse juntas. Dos grupos pueden
tener la misma media, pero uno presentar datos muy concentrados y otro datos
muy separados. En presencia de valores extremos, una combinación robusta es la
**mediana con el IQR**, mientras que la **media con la desviación estándar**
resulta adecuada cuando los datos son aproximadamente simétricos y no contienen
valores atípicos importantes.

En una muestra, NumPy y Pandas usan normalmente `ddof=1` para estimar la
desviación estándar y la varianza muestrales:

```python
edades = pd.Series([22, 27, 31, 25, 29, 24, 26])

resumen = pd.Series({
    "media": edades.mean(),
    "mediana": edades.median(),
    "moda": edades.mode().iloc[0],
    "mínimo": edades.min(),
    "máximo": edades.max(),
    "rango": edades.max() - edades.min(),
    "varianza_muestral": edades.var(),
    "desviación_muestral": edades.std(),
    "Q1": edades.quantile(0.25),
    "Q3": edades.quantile(0.75),
    "IQR": edades.quantile(0.75) - edades.quantile(0.25),
})

print(resumen)
```

### Interpretación con y sin un valor extremo

```python
datos = pd.Series([10, 11, 11, 12, 12, 13, 14, 15])
datos_con_extremo = pd.concat([datos, pd.Series([60])], ignore_index=True)

comparacion = pd.DataFrame({
    "sin_extremo": [
        datos.mean(), datos.median(), datos.std(), datos.quantile(0.75) - datos.quantile(0.25)
    ],
    "con_extremo": [
        datos_con_extremo.mean(), datos_con_extremo.median(),
        datos_con_extremo.std(),
        datos_con_extremo.quantile(0.75) - datos_con_extremo.quantile(0.25)
    ],
}, index=["media", "mediana", "desviación estándar", "IQR"])

print(comparacion)
```

**Preguntas para discutir:**

1. ¿Qué medida cambia más al agregar 60?
2. ¿Qué medida usarían para describir el valor típico?
3. ¿El valor 60 debe eliminarse automáticamente? No: primero hay que verificar
   si es un error, una medición válida o un caso de otra población.

### Visualización de la distribución

```python
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].hist(datos_con_extremo, bins=8, edgecolor="black")
axes[0].set_title("Histograma")
axes[0].set_xlabel("Valor")
axes[0].set_ylabel("Frecuencia")

axes[1].boxplot(datos_con_extremo, vert=False)
axes[1].set_title("Diagrama de caja")
axes[1].set_xlabel("Valor")

plt.tight_layout()
plt.show()
```

El histograma ayuda a observar forma, concentración y asimetría. El boxplot
resume mediana, cuartiles y posibles valores atípicos. Ninguno sustituye la
revisión del contexto.

---

## 5. Ejercicio 1: resumen de un DataFrame (20 minutos)

### Situación

Se registró el tiempo de estudio semanal y la calificación de ocho estudiantes.

```python
estudiantes = pd.DataFrame({
    "estudiante": ["Ana", "Luis", "María", "José", "Sofía", "Diego", "Elena", "Pablo"],
    "horas_estudio": [2, 4, 5, 3, 8, 6, 4, 10],
    "calificacion": [62, 70, 75, 68, 88, 80, 73, 91],
})

print(estudiantes)
print(estudiantes[["horas_estudio", "calificacion"]].describe())
```

### Actividades

1. Calcular media, mediana, desviación estándar e IQR de ambas variables.
2. Crear un histograma de `horas_estudio`.
3. Crear un boxplot de `calificacion`.
4. Escribir tres conclusiones, incluyendo una que mencione la variabilidad.

### Posible solución

```python
variables = ["horas_estudio", "calificacion"]

resumen = estudiantes[variables].agg(["mean", "median", "std", "min", "max"])
resumen.loc["IQR"] = (
    estudiantes[variables].quantile(0.75)
    - estudiantes[variables].quantile(0.25)
)
print(resumen)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].hist(estudiantes["horas_estudio"], bins=6, edgecolor="black")
axes[0].set(title="Horas de estudio", xlabel="Horas", ylabel="Estudiantes")
axes[1].boxplot(estudiantes["calificacion"], vert=False)
axes[1].set(title="Calificaciones", xlabel="Puntos")
plt.tight_layout()
plt.show()
```

**Criterio de revisión:** una buena respuesta no solo dice “la media es 5.25”;
explica qué representa, en qué unidades está y si la media parece representativa
al observar la distribución.

---

## 6. 4.1.2 Correlación y causalidad

### Correlación

La correlación de Pearson, denotada por `r`, mide la asociación lineal entre dos
variables cuantitativas:

- `r` cercano a `1`: asociación lineal positiva;
- `r` cercano a `-1`: asociación lineal negativa;
- `r` cercano a `0`: poca asociación lineal.

La correlación no describe necesariamente relaciones no lineales y no demuestra
que una variable cause a la otra. Un valor de `r` también puede verse afectado
por valores atípicos, selección de la muestra y rango restringido.

```python
r = estudiantes["horas_estudio"].corr(estudiantes["calificacion"])
print(f"Correlación de Pearson: {r:.3f}")

plt.figure(figsize=(6, 4))
plt.scatter(estudiantes["horas_estudio"], estudiantes["calificacion"])
plt.xlabel("Horas de estudio por semana")
plt.ylabel("Calificación")
plt.title(f"Relación entre estudio y calificación (r = {r:.2f})")
plt.grid(alpha=0.3)
plt.show()
```

### Correlación no implica causalidad

Una asociación entre `X` y `Y` puede aparecer por:

1. **Causalidad directa:** `X` influye en `Y`.
2. **Causalidad inversa:** `Y` influye en `X`.
3. **Variable confusora:** una tercera variable `Z` influye en ambas.
4. **Coincidencia o sesgo de selección.**

Por ejemplo, helados vendidos y casos de insolación pueden aumentar al mismo
tiempo. Esto no significa que comer helado cause insolación: la temperatura
puede ser la variable confusora.

### Simulación de una variable confusora

```python
rng = np.random.default_rng(42)
n = 100
temperatura = rng.normal(28, 4, n)
helados = 20 + 3 * temperatura + rng.normal(0, 5, n)
insolaciones = -20 + 2 * temperatura + rng.normal(0, 5, n)

simulados = pd.DataFrame({
    "temperatura": temperatura,
    "helados": helados,
    "insolaciones": insolaciones,
})

print(simulados.corr(numeric_only=True).round(2))

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].scatter(simulados["helados"], simulados["insolaciones"])
axes[0].set(xlabel="Helados vendidos", ylabel="Insolaciones",
            title="Asociación observada")
axes[1].scatter(simulados["temperatura"], simulados["insolaciones"])
axes[1].set(xlabel="Temperatura", ylabel="Insolaciones",
            title="Variable confusora")
plt.tight_layout()
plt.show()
```

**Conclusión esperada:** la correlación entre helados e insolaciones es una
señal para investigar, no una prueba de causalidad. Para evaluar causalidad se
requiere conocimiento del proceso y, cuando sea posible, un experimento o un
diseño observacional que controle variables relevantes.

---

## 7. Ejercicio 2: asociación vs. explicación (20 minutos)

Usar el DataFrame `simulados` y responder:

1. ¿Cuál es la correlación entre `helados` e `insolaciones`?
2. ¿Qué variable podría explicar el aumento simultáneo?
3. ¿Qué afirmación sería incorrecta: “están asociadas” o “los helados causan
   insolaciones”? Explicar.
4. Proponer una variable adicional que convendría medir.
5. ¿Qué tipo de estudio ayudaría a evaluar la explicación causal?

### Extensión opcional

Calcular la correlación entre temperatura e insolaciones, y entre temperatura y
helados. Comparar las tres correlaciones y explicar por qué el patrón cambia al
considerar la variable confusora.

---

## 8. Reto individual de cierre (8 minutos)

```python
rng = np.random.default_rng(7)
ventas = pd.DataFrame({
    "publicidad": rng.integers(10, 80, 12),
    "ventas": [42, 48, 51, 55, 58, 61, 63, 66, 70, 72, 75, 78],
})
```

El estudiante debe:

1. calcular media, mediana y desviación estándar de `ventas`;
2. hacer un diagrama de dispersión;
3. calcular `r`;
4. redactar una conclusión que use la palabra **asociación** y una advertencia
   sobre causalidad.

> Para una práctica más realista, sustituir la columna `publicidad` por datos
> proporcionados por el docente y discutir cómo el tamaño de muestra afecta la
> interpretación.

## 9. Ticket de salida (2 minutos)

Responder en dos o tres líneas:

1. ¿Cuándo preferirías la mediana sobre la media?
2. ¿Qué significa una correlación de `r = -0.8`?
3. ¿Por qué una correlación alta no basta para afirmar causalidad?

## 10. Evaluación rápida

| Criterio | Logrado cuando el estudiante... |
| --- | --- |
| Tendencia | Calcula media y mediana e interpreta sus unidades |
| Dispersión | Explica qué indica la desviación estándar o el IQR |
| Visualización | Relaciona la forma de una gráfica con el resumen numérico |
| Correlación | Interpreta dirección e intensidad sin confundirla con causalidad |
| Comunicación | Presenta una conclusión, una limitación y una pregunta para continuar |

## 11. Errores frecuentes para discutir

- Confundir media con mediana.
- Reportar muchas cifras decimales sin significado.
- Comparar desviaciones estándar de variables con unidades diferentes sin
  considerar la escala.
- Interpretar `r` como porcentaje de causalidad.
- Eliminar valores atípicos únicamente porque cambian la media.
- Concluir a partir de una gráfica sin revisar el tamaño y la selección de la
  muestra.
