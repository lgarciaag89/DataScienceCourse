# Clase 4.2 — Probabilidad

**Duración:** 2 horas  
**Asignatura:** Ciencia de Datos  

## Temas

- **4.2 Probabilidad**
- **4.2.1 Dependencia e independencia**
- **4.2.2 Teorema de Bayes**
- **4.2.3 Distribución continua y normal**

---

## Objetivos de aprendizaje

Al finalizar la clase, el estudiante será capaz de:

1. Interpretar la probabilidad en el contexto de un conjunto de datos.
2. Calcular probabilidades simples, conjuntas y condicionales.
3. Determinar si dos eventos son dependientes o independientes.
4. Aplicar el Teorema de Bayes a problemas sencillos de clasificación y diagnóstico.
5. Diferenciar variables aleatorias discretas y continuas.
6. Interpretar una distribución normal a partir de su media y desviación estándar.
7. Calcular e interpretar un **Z-score**.
8. Calcular probabilidades asociadas a una distribución normal utilizando Python.

---

## Distribución de la clase

| Tiempo | Tema | Actividad |
|---:|---|---|
| 0–10 min | Introducción | Probabilidad y Ciencia de Datos |
| 10–30 min | Probabilidad básica y condicional | Conceptos y ejemplos |
| 30–50 min | Dependencia e independencia | Ejemplo y ejercicio |
| 50–75 min | Teorema de Bayes | Explicación y problema aplicado |
| 75–80 min | Transición | Preguntas y recapitulación |
| 80–95 min | Variables continuas | Densidad y probabilidad |
| 95–115 min | Distribución normal | Normal, Z-score y Python |
| 115–120 min | Cierre | Ejercicio integrador |

---

# 1. Introducción a la probabilidad

La **probabilidad** permite cuantificar la incertidumbre asociada a un evento.

Supongamos que tenemos un dataset con **1000 péptidos**, de los cuales **300 son antimicrobianos (AMP)**.

Si seleccionamos un péptido al azar:

$$
P(AMP)=\frac{300}{1000}=0.30
$$

Por tanto, existe una probabilidad del **30 %** de seleccionar un péptido antimicrobiano.

## 1.1 Eventos

Podemos definir el evento:

$$
A=\{\text{el péptido es antimicrobiano}\}
$$

La probabilidad del evento es:

$$
P(A)=0.30
$$

### Complemento

El complemento de $A$ representa que el evento no ocurra:

$$
P(\bar{A})=1-P(A)
$$

Por tanto:

$$
P(\text{no AMP})=1-0.30=0.70
$$

## 1.2 Intersección de eventos

La expresión

$$
P(A\cap B)
$$

representa la probabilidad de que **A y B ocurran simultáneamente**.

Por ejemplo:

- $A$: el péptido es AMP.
- $B$: el péptido tiene carga positiva.

Entonces:

$$
P(A\cap B)
$$

representa la probabilidad de seleccionar un péptido que **sea AMP y tenga carga positiva**.

---

# 2. Probabilidad condicional

La probabilidad condicional permite calcular la probabilidad de un evento cuando sabemos que otro evento ya ocurrió.

Se representa mediante:

$$
P(A|B)
$$

que se lee:

> Probabilidad de A dado B.

Su definición es:

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

## Ejemplo

Consideremos el siguiente conjunto de péptidos:

| | AMP | No AMP | Total |
|---|---:|---:|---:|
| Carga positiva | 240 | 140 | 380 |
| No positiva | 60 | 560 | 620 |
| **Total** | **300** | **700** | **1000** |

Queremos responder:

> Si sabemos que un péptido tiene carga positiva, ¿cuál es la probabilidad de que sea AMP?

El universo relevante ya no son los 1000 péptidos, sino los **380 péptidos con carga positiva**.

Por tanto:

$$
P(AMP|Carga+)=\frac{240}{380}\approx0.632
$$

La probabilidad es aproximadamente **63.2 %**.

Sin embargo:

$$
P(Carga+|AMP)=\frac{240}{300}=0.80
$$

Por tanto:

$$
P(AMP|Carga+)\neq P(Carga+|AMP)
$$

> **Importante:** invertir la condición cambia el significado de la probabilidad.

---

# 3. Dependencia e independencia

## 3.1 Eventos independientes

Dos eventos $A$ y $B$ son **independientes** cuando conocer que ocurrió uno no modifica la probabilidad del otro.

Una condición de independencia es:

$$
P(A|B)=P(A)
$$

Otra forma equivalente es:

$$
P(A\cap B)=P(A)P(B)
$$

## 3.2 Eventos dependientes

Dos eventos son **dependientes** cuando conocer la ocurrencia de uno modifica la probabilidad del otro.

En el ejemplo anterior:

$$
P(AMP)=0.30
$$

pero:

$$
P(AMP|Carga+)\approx0.632
$$

Como:

$$
P(AMP|Carga+)\neq P(AMP)
$$

los eventos **ser AMP** y **tener carga positiva** no son independientes.

La información sobre la carga modifica nuestra estimación de la probabilidad de que el péptido sea antimicrobiano.

## Ejercicio 1

Considera la siguiente tabla:

| | Activo | No activo | Total |
|---|---:|---:|---:|
| Grupo A | 40 | 60 | 100 |
| Grupo B | 20 | 80 | 100 |
| **Total** | **60** | **140** | **200** |

Calcula:

1. $P(Activo)$.
2. $P(Grupo\ A)$.
3. $P(Activo|Grupo\ A)$.
4. $P(Activo|Grupo\ B)$.
5. ¿Son independientes los eventos **pertenecer al Grupo A** y **ser activo**?
6. Justifica tu respuesta utilizando probabilidades.

---

# 4. Teorema de Bayes

El **Teorema de Bayes** permite actualizar una probabilidad cuando obtenemos nueva evidencia.

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

## 4.1 Interpretación

Los términos pueden interpretarse como:

- $P(A)$: **probabilidad previa (prior)**.
- $P(B|A)$: **verosimilitud (likelihood)**.
- $P(B)$: probabilidad de observar la evidencia.
- $P(A|B)$: **probabilidad posterior (posterior)**.

En términos sencillos:

> Tenemos una creencia inicial, observamos nueva evidencia y actualizamos nuestra probabilidad.

---

## 4.2 Ejemplo: prueba diagnóstica

Supongamos una enfermedad cuya prevalencia es:

$$
P(E)=0.01
$$

Una prueba diagnóstica tiene una sensibilidad de:

$$
P(+|E)=0.95
$$

La tasa de falsos positivos es:

$$
P(+|\bar{E})=0.05
$$

Una persona obtiene un resultado positivo.

**Pregunta:** ¿Cuál es la probabilidad de que realmente tenga la enfermedad?

Primero calculamos la probabilidad total de obtener un resultado positivo:

$$
P(+)=P(+|E)P(E)+P(+|\bar{E})P(\bar{E})
$$

Como:

$$
P(\bar{E})=0.99
$$

entonces:

$$
P(+)=0.95(0.01)+0.05(0.99)
$$

$$
P(+)=0.059
$$

Aplicamos Bayes:

$$
P(E|+)=\frac{P(+|E)P(E)}{P(+)}
$$

$$
P(E|+)=\frac{0.95(0.01)}{0.059}
$$

$$
P(E|+)\approx0.161
$$

Por tanto, la probabilidad de que la persona realmente tenga la enfermedad dado un resultado positivo es aproximadamente:

$$
\boxed{16.1\%}
$$

### Pregunta para discutir

¿Cómo puede una prueba con una sensibilidad del 95 % producir una probabilidad posterior de solamente 16.1 %?

La respuesta está relacionada con la **baja prevalencia inicial de la enfermedad**.

---

## 4.3 Conexión con Machine Learning

Muchos problemas de clasificación pueden expresarse como:

$$
P(Clase|Datos)
$$

Por ejemplo:

$$
P(AMP|Descriptores)
$$

El objetivo es estimar la probabilidad de que una instancia pertenezca a una determinada clase dadas sus características.

Esta idea constituye la base de algoritmos como **Naive Bayes**.

---

# 5. Variables aleatorias

Una **variable aleatoria** asigna valores numéricos a los resultados de un experimento aleatorio.

Existen dos tipos principales:

- Variables aleatorias **discretas**.
- Variables aleatorias **continuas**.

## 5.1 Variable discreta

Toma un conjunto finito o contable de valores.

Ejemplos:

- Número de moléculas activas.
- Número de errores de un modelo.
- Número de estudiantes que aprueban un examen.

## 5.2 Variable continua

Puede tomar cualquier valor dentro de un intervalo.

Ejemplos en datos científicos:

- Masa molecular.
- Temperatura.
- Concentración.
- Energía.
- Hidrofobicidad.
- Valores de descriptores moleculares.

---

# 6. Distribuciones continuas

En una variable continua no calculamos normalmente la probabilidad de obtener exactamente un valor.

Para una variable continua $X$:

$$
P(X=x)=0
$$

En cambio, calculamos la probabilidad de que $X$ se encuentre dentro de un intervalo:

$$
P(a<X<b)
$$

Esta probabilidad corresponde al **área bajo la curva de densidad** entre $a$ y $b$.

El área total bajo una función de densidad es:

$$
\int_{-\infty}^{+\infty}f(x)\,dx=1
$$

Por tanto, toda el área bajo la curva representa el **100 % de probabilidad**.

---

# 7. Distribución normal

Una de las distribuciones continuas más importantes en estadística es la **distribución normal**.

Se representa como:

$$
X\sim N(\mu,\sigma^2)
$$

donde:

- $\mu$: media de la distribución.
- $\sigma$: desviación estándar.
- $\sigma^2$: varianza.

## 7.1 Interpretación de los parámetros

La media $\mu$ determina el **centro de la distribución**.

La desviación estándar $\sigma$ determina qué tan dispersos se encuentran los datos alrededor de la media.

Una desviación estándar pequeña produce una distribución más concentrada.

Una desviación estándar grande produce una distribución más dispersa.

---

# 8. Regla 68–95–99.7

Para una variable aproximadamente normal:

- Aproximadamente **68 %** de las observaciones se encuentran entre:

$$
\mu-\sigma<X<\mu+\sigma
$$

- Aproximadamente **95 %** se encuentran entre:

$$
\mu-2\sigma<X<\mu+2\sigma
$$

- Aproximadamente **99.7 %** se encuentran entre:

$$
\mu-3\sigma<X<\mu+3\sigma
$$

Esta propiedad permite interpretar rápidamente qué tan inusual es una observación.

---

# 9. Z-score

El **Z-score** indica a cuántas desviaciones estándar se encuentra una observación respecto a la media.

$$
Z=\frac{x-\mu}{\sigma}
$$

## Ejemplo

Supongamos:

$$
\mu=50
$$

$$
\sigma=10
$$

Para una observación:

$$
x=70
$$

obtenemos:

$$
Z=\frac{70-50}{10}=2
$$

Esto significa que el valor 70 se encuentra **2 desviaciones estándar por encima de la media**.

Para:

$$
x=35
$$

obtenemos:

$$
Z=\frac{35-50}{10}=-1.5
$$

El valor se encuentra **1.5 desviaciones estándar por debajo de la media**.

### Interpretación general

- $Z=0$: el valor coincide con la media.
- $Z>0$: el valor está por encima de la media.
- $Z<0$: el valor está por debajo de la media.
- $|Z|$ grande: el valor se encuentra relativamente lejos de la media.

---

# 10. Distribución normal con Python

Utilizaremos `scipy.stats.norm`.

```python
from scipy.stats import norm

mu = 50
sigma = 10
```

## 10.1 Probabilidad de $X<60$

```python
p = norm.cdf(60, loc=mu, scale=sigma)
print(p)
```

Resultado aproximado:

```text
0.8413
```

Por tanto:

$$
P(X<60)\approx0.8413
$$

Es decir, aproximadamente **84.13 %**.

---

## 10.2 Probabilidad de $X>60$

```python
p = 1 - norm.cdf(60, loc=mu, scale=sigma)
print(p)
```

Resultado aproximado:

$$
P(X>60)\approx0.1587
$$

Es decir, aproximadamente **15.87 %**.

---

## 10.3 Probabilidad entre dos valores

Queremos calcular:

$$
P(40<X<60)
$$

En Python:

```python
p = (
    norm.cdf(60, loc=mu, scale=sigma)
    - norm.cdf(40, loc=mu, scale=sigma)
)

print(p)
```

Resultado aproximado:

$$
P(40<X<60)\approx0.6827
$$

Esto corresponde aproximadamente al **68 %** esperado dentro de una desviación estándar de la media.

---

# 11. Visualización de una distribución normal

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 50
sigma = 10

x = np.linspace(10, 90, 500)
y = norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(9, 5))
plt.plot(x, y)
plt.axvline(mu, linestyle="--", label="Media")
plt.xlabel("X")
plt.ylabel("Densidad")
plt.title("Distribución normal")
plt.legend()
plt.show()
```

### Preguntas

1. ¿Dónde se encuentra el centro de la distribución?
2. ¿Qué ocurriría si aumentamos `sigma` de 10 a 20?
3. ¿Qué ocurriría si cambiamos `mu` de 50 a 70?
4. ¿El área total bajo la curva cambia al modificar $\mu$ o $\sigma$?

---

# 12. Ejercicio práctico con Python

Supongamos que tenemos los valores de un descriptor molecular para un conjunto de péptidos:

```python
import numpy as np

np.random.seed(42)

descriptor = np.random.normal(
    loc=50,
    scale=10,
    size=1000
)
```

Calcula la media y la desviación estándar:

```python
media = np.mean(descriptor)
desviacion = np.std(descriptor)

print("Media:", media)
print("Desviación estándar:", desviacion)
```

Visualiza la distribución:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))
plt.hist(descriptor, bins=30, density=True, alpha=0.7)
plt.xlabel("Valor del descriptor")
plt.ylabel("Densidad")
plt.title("Distribución del descriptor molecular")
plt.show()
```

### Actividades

1. Calcula la media.
2. Calcula la desviación estándar.
3. Calcula el Z-score de una observación con valor 65.
4. Determina qué porcentaje de observaciones tiene valores inferiores a 60.
5. Determina qué porcentaje tiene valores entre 40 y 60.
6. Compara los resultados empíricos con los esperados para una distribución normal.

---

# 13. Ejercicio integrador

En un dataset, el **30 % de los péptidos son antimicrobianos**.

El **70 % de los AMP** presenta una determinada característica molecular:

$$
P(C|AMP)=0.70
$$

Mientras que solamente el **20 % de los no-AMP** presenta esa característica:

$$
P(C|No\ AMP)=0.20
$$

Además, un descriptor $D$ de los péptidos AMP sigue aproximadamente una distribución:

$$
D\sim N(50,10^2)
$$

## Preguntas

1. ¿Son independientes los eventos **ser AMP** y **presentar la característica C**? Justifica.
2. Calcula $P(C)$.
3. Si un péptido presenta la característica C, calcula:

$$
P(AMP|C)
$$

4. ¿Qué significa afirmar que $D\sim N(50,10^2)$?
5. Calcula el Z-score de un péptido con:

$$
D=65
$$

6. ¿Qué porcentaje aproximado de péptidos tendrá:

$$
40<D<60
$$

7. Utiliza Python para calcular exactamente:

$$
P(D<65)
$$

8. ¿Considerarías que un péptido con $D=80$ tiene un valor inusual? Justifica utilizando su Z-score.

---

# 14. Resumen de la clase

La secuencia conceptual estudiada fue:

```text
Datos
  ↓
Eventos
  ↓
Probabilidad
  ↓
Probabilidad condicional
  ↓
Dependencia / Independencia
  ↓
Teorema de Bayes
  ↓
Variables aleatorias
  ↓
Distribuciones continuas
  ↓
Distribución normal
  ↓
Z-score
```

## Ideas fundamentales

### Probabilidad condicional

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

### Independencia

$$
P(A|B)=P(A)
$$

o equivalentemente:

$$
P(A\cap B)=P(A)P(B)
$$

### Teorema de Bayes

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

### Distribución normal

$$
X\sim N(\mu,\sigma^2)
$$

### Z-score

$$
Z=\frac{x-\mu}{\sigma}
$$

---

# 15. Conexión con Ciencia de Datos

Estos conceptos aparecen continuamente en Ciencia de Datos y Machine Learning:

- estimación de incertidumbre;
- análisis de variables;
- detección de valores atípicos;
- clasificación probabilística;
- inferencia estadística;
- evaluación de modelos;
- Naive Bayes;
- modelado de distribuciones;
- análisis de datos científicos.

La probabilidad proporciona así una base para los siguientes temas del curso:

```text
Probabilidad
     ↓
Inferencia estadística
     ↓
Machine Learning
```
