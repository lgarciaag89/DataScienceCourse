# 4.2 Probabilidad: dependencia, Bayes y distribución normal

**Materia:** Ciencia de Datos  
**Duración:** 2 horas (120 minutos)  
**Modalidad:** explicación breve, discusión, ejercicios guiados y práctica en Python  
**Requisitos:** probabilidad básica, álgebra elemental, media y desviación estándar

## 1. Propósito de la clase

La probabilidad permite cuantificar la incertidumbre y actualizar decisiones
cuando se obtiene nueva información. En esta sesión el estudiante conectará tres
ideas:

1. la probabilidad conjunta y la probabilidad condicional permiten describir
   dependencia e independencia;
2. el teorema de Bayes invierte una probabilidad condicional y actualiza una
   creencia;
3. las distribuciones continuas, en particular la normal, modelan variables
   medidas en una escala continua.

> **Idea central:** una probabilidad no debe interpretarse fuera de su
> condicionamiento. P(`A` dado `B`) no es, en general, igual a P(`B` dado `A`).

## 2. Resultados de aprendizaje

Al terminar la clase, el estudiante podrá:

- calcular probabilidades conjuntas, marginales y condicionales;
- distinguir dependencia de independencia usando una igualdad y un ejemplo;
- aplicar el teorema de Bayes en un problema de diagnóstico o clasificación;
- explicar por qué una probabilidad continua se calcula sobre intervalos y no
  sobre puntos individuales;
- estandarizar una variable normal mediante un puntaje `z`;
- calcular e interpretar probabilidades con `scipy.stats.norm`;
- comunicar una conclusión incluyendo el supuesto utilizado y una limitación.

## 3. Preparación

### Para el docente

- Abrir un notebook de Jupyter, Google Colab o VS Code.
- Verificar que estén instaladas `numpy`, `pandas`, `matplotlib` y `scipy`.
- Preparar una moneda o una encuesta rápida para activar las ideas previas.
- Pedir que cada equipo escriba sus respuestas y no solamente el resultado
  numérico.

### Librerías

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

pd.set_option("display.float_format", "{:.4f}".format)
```

## 4. Secuencia didáctica de 120 minutos

| Tiempo | Actividad | Evidencia de aprendizaje |
|---:|---|---|
| 0–10 min | Activación: moneda, clima y asistencia | Distingue probabilidad conjunta y condicional |
| 10–25 min | Probabilidad condicional | Calcula `P(A\|B)` a partir de una tabla |
| 25–40 min | Dependencia e independencia | Verifica si dos eventos son independientes |
| 40–60 min | Teorema de Bayes y ejemplo de diagnóstico | Actualiza una probabilidad con evidencia |
| 60–68 min | Pausa activa y puesta en común | Explica el error de confundir `P(A\|B)` con `P(B\|A)` |
| 68–83 min | Variables continuas y distribución normal | Interpreta densidad, área, media y desviación |
| 83–100 min | Laboratorio con `scipy.stats.norm` | Calcula probabilidades y puntajes `z` |
| 100–113 min | Reto integrador por equipos | Resuelve y justifica un caso de clasificación |
| 113–120 min | Ticket de salida y retroalimentación | Formula una conclusión y un supuesto |

## 5. Activación (0–10 minutos)

### Pregunta inicial

Supongamos que:

- 60 % de los días son soleados;
- 30 % de los días soleados tienen asistencia alta;
- 10 % de los días nublados tienen asistencia alta.

Preguntar individualmente:

1. ¿Es lo mismo “asistencia alta dado que está soleado” que “día soleado dado
   que la asistencia es alta”?
2. ¿Qué información adicional se necesita para calcular la segunda cantidad?
3. ¿El clima y la asistencia parecen independientes?

Después de escuchar dos respuestas, introducir la notación:

- `A`: asistencia alta;
- `S`: día soleado;
- `P(A|S)`: probabilidad de asistencia alta cuando se sabe que el día es
  soleado.

## 6. 4.2.1 Dependencia e independencia (10–40 minutos)

### 6.1 Conceptos y fórmulas

- **Probabilidad conjunta:** probabilidad de que ocurran ambos eventos:
  `P(A ∩ B)`.
- **Probabilidad marginal:** probabilidad de un evento sin condicionar por otro:
  `P(A)`.
- **Probabilidad condicional:** probabilidad de `A` sabiendo que ocurrió `B`:

  ```text
  P(A|B) = P(A ∩ B) / P(B),    siempre que P(B) > 0.
  ```

- **Regla del producto:**

  ```text
  P(A ∩ B) = P(A|B) P(B).
  ```

Dos eventos son **independientes** si conocer uno no cambia la probabilidad del
otro:

```text
P(A|B) = P(A)
```

Una forma equivalente de comprobarlo es:

```text
P(A ∩ B) = P(A) P(B).
```

Si la igualdad no se cumple, los eventos son dependientes. Independencia no
significa que los eventos sean mutuamente excluyentes: dos eventos excluyentes
con probabilidades positivas no pueden ser independientes.

### 6.2 Ejemplo con una tabla de contingencia

En una muestra de 200 estudiantes se registró si usan una aplicación de estudio
y si aprobaron un examen:

|  | Aprobó | No aprobó | Total |
|---|---:|---:|---:|
| Usa la aplicación | 72 | 48 | 120 |
| No usa la aplicación | 32 | 48 | 80 |
| **Total** | **104** | **96** | **200** |

Sea `U` = usa la aplicación y `P` = aprobó.

```text
P(P) = 104/200 = 0.52
P(P|U) = 72/120 = 0.60
```

Como `0.60` es diferente de `0.52`, el resultado sugiere dependencia. También:

```text
P(U ∩ P) = 72/200 = 0.36
P(U)P(P) = (120/200)(104/200) = 0.312
```

Las dos cantidades son diferentes, por lo que los eventos no son independientes.
Esto muestra asociación, pero no demuestra que la aplicación cause la
aprobación: podrían existir variables de confusión, como horas de estudio.

### 6.3 Actividad guiada (10 minutos)

```python
tabla = pd.DataFrame(
    [[72, 48], [32, 48]],
    index=["Usa aplicación", "No usa aplicación"],
    columns=["Aprobó", "No aprobó"],
)

n = tabla.to_numpy().sum()
p_aprobo = tabla["Aprobó"].sum() / n
p_aprobo_dado_usa = tabla.loc["Usa aplicación", "Aprobó"] / tabla.loc[
    "Usa aplicación"
].sum()
p_conjunta = tabla.loc["Usa aplicación", "Aprobó"] / n
p_producto = (tabla.loc["Usa aplicación"].sum() / n) * p_aprobo

print(f"P(aprobó) = {p_aprobo:.3f}")
print(f"P(aprobó | usa) = {p_aprobo_dado_usa:.3f}")
print(f"P(usa y aprobó) = {p_conjunta:.3f}")
print(f"P(usa)P(aprobó) = {p_producto:.3f}")
```

**Preguntas para discutir:**

1. ¿Qué denominador se usa en `P(aprobó|usa)` y por qué?
2. ¿Qué conclusión cambiaría si la muestra no fuera representativa?
3. ¿Qué variable adicional medirían para discutir causalidad?

## 7. 4.2.2 Teorema de Bayes (40–60 minutos)

### 7.1 Derivación e interpretación

Partiendo de la regla del producto:

```text
P(A ∩ B) = P(A|B)P(B) = P(B|A)P(A)
```

se obtiene:

```text
P(A|B) = P(B|A)P(A) / P(B).
```

En Bayes:

- `P(A)` es la **priori**: lo que se creía antes de observar evidencia;
- `P(B|A)` es la **verosimilitud**: qué tan probable es la evidencia si `A` es
  cierto;
- `P(B)` es la probabilidad total de la evidencia;
- `P(A|B)` es la **posteriori**: la creencia actualizada.

Si `A` y `A^c` son las únicas posibilidades:

```text
P(B) = P(B|A)P(A) + P(B|A^c)P(A^c).
```

### 7.2 Ejemplo de prueba diagnóstica

Una enfermedad afecta al 1 % de una población. Una prueba tiene:

- sensibilidad `P(+|E) = 0.95`;
- tasa de falso positivo `P(+|E^c) = 0.05`.

¿Cuál es la probabilidad de que una persona tenga la enfermedad después de
obtener un resultado positivo?

```text
P(E|+) =
  P(+|E)P(E)
  -------------------------------
  P(+|E)P(E) + P(+|E^c)P(E^c)

P(E|+) = (0.95)(0.01) / ((0.95)(0.01) + (0.05)(0.99))
       ≈ 0.161
```

La probabilidad posterior es aproximadamente **16.1 %**, no 95 %. La diferencia
se debe a que la enfermedad es poco frecuente y hay falsos positivos.

Una forma intuitiva de verlo es con 10,000 personas:

- 100 tienen la enfermedad; aproximadamente 95 dan positivo;
- 9,900 no la tienen; aproximadamente 495 dan falso positivo;
- de los 590 positivos, solo 95 corresponden a personas enfermas;
- `95/590 ≈ 0.161`.

### 7.3 Implementación reproducible

```python
p_enfermedad = 0.01
p_positivo_dado_enfermedad = 0.95
p_positivo_dado_no_enfermedad = 0.05

p_positivo = (
    p_positivo_dado_enfermedad * p_enfermedad
    + p_positivo_dado_no_enfermedad * (1 - p_enfermedad)
)
p_enfermedad_dado_positivo = (
    p_positivo_dado_enfermedad * p_enfermedad / p_positivo
)

print(f"P(+) = {p_positivo:.3f}")
print(f"P(enfermedad | +) = {p_enfermedad_dado_positivo:.3f}")
```

### 7.4 Mini-ejercicio

Una alerta de fraude aparece en 2 % de las transacciones. El sistema detecta
correctamente 90 % de los fraudes y marca por error 3 % de las transacciones
legítimas. Calcular `P(fraude|alerta)`.

**Respuesta esperada:** aproximadamente `0.380`, es decir, 38.0 %. La alerta
incrementa la probabilidad inicial de 2 %, pero no confirma por sí sola el fraude.

## 8. 4.2.3 Distribución continua y normal (68–100 minutos)

### 8.1 Variables discretas y continuas

- Una variable **discreta** cuenta resultados separados, como el número de
  defectos.
- Una variable **continua** puede tomar infinitos valores en un intervalo, como
  tiempo, masa o temperatura.

En una variable continua, la probabilidad de un valor exacto es cero:

```text
P(X = x) = 0
```

Las probabilidades se calculan como áreas bajo una función de densidad:

```text
P(a < X < b) = ∫[a,b] f(x) dx
```

La densidad no es una probabilidad individual; puede ser mayor que 1, pero el
área total bajo la curva siempre es 1.

### 8.2 Distribución normal

Una variable `X` tiene distribución normal con media `μ` y desviación estándar
`σ > 0` si:

```text
X ~ N(μ, σ²)
```

Su densidad es:

```text
f(x) = 1/(σ√(2π)) exp(-1/2 ((x - μ)/σ)²)
```

Características importantes:

- es simétrica alrededor de `μ`;
- media, mediana y moda coinciden;
- `σ` controla la dispersión;
- aproximadamente 68 %, 95 % y 99.7 % de los valores se encuentran a una, dos
  y tres desviaciones estándar de la media, respectivamente;
- la regla 68–95–99.7 es una aproximación, no una definición.

### 8.3 Puntaje z

Para comparar una observación con su distribución se estandariza:

```text
z = (x - μ) / σ
```

Un `z = 2` indica que el valor está dos desviaciones estándar por encima de la
media. La transformación produce una normal estándar `Z ~ N(0, 1)`.

### 8.4 Cálculos con SciPy

Supongamos que el tiempo de procesamiento de una tarea es aproximadamente
normal, con `μ = 50` segundos y `σ = 8` segundos.

```python
mu = 50
sigma = 8

# P(X <= 60)
p_menor_60 = norm.cdf(60, loc=mu, scale=sigma)

# P(42 <= X <= 58)
p_entre = norm.cdf(58, loc=mu, scale=sigma) - norm.cdf(42, loc=mu, scale=sigma)

# Percentil 95
p95 = norm.ppf(0.95, loc=mu, scale=sigma)

# Puntaje z de 60 segundos
z_60 = (60 - mu) / sigma

print(f"P(X <= 60) = {p_menor_60:.4f}")
print(f"P(42 <= X <= 58) = {p_entre:.4f}")
print(f"Percentil 95 = {p95:.2f} segundos")
print(f"z(60) = {z_60:.2f}")
```

`cdf` calcula una probabilidad acumulada y `ppf` encuentra el valor asociado a
un percentil. Para calcular una cola derecha se usa `1 - cdf(x)` o `norm.sf(x)`.

### 8.5 Visualización

```python
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 500)
y = norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(9, 4))
plt.plot(x, y, label="N(50, 8²)")
plt.axvline(60, color="crimson", linestyle="--", label="60 segundos")
plt.fill_between(
    x, y, where=(x <= 60), color="crimson", alpha=0.2, label="P(X <= 60)"
)
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Densidad")
plt.title("Distribución normal del tiempo de procesamiento")
plt.legend()
plt.tight_layout()
plt.show()
```

**Discusión:** el área sombreada representa la probabilidad acumulada; la altura
de la curva en 60 no representa `P(X=60)`.

## 9. Reto integrador por equipos (100–113 minutos)

Cada equipo analiza un clasificador de correo no deseado:

- 8 % de los mensajes son spam;
- el filtro marca como “spam” el 92 % de los mensajes spam;
- marca como “spam” el 4 % de los mensajes legítimos.

Resolver en el notebook:

1. `P(spam|marcado)`;
2. cuántos verdaderos y falsos positivos habría en 10,000 mensajes;
3. explicar por qué la precisión del filtro no es igual a su sensibilidad;
4. indicar una limitación del modelo probabilístico.

**Solución para el docente:**

```python
p_spam = 0.08
p_marcado_dado_spam = 0.92
p_marcado_dado_legitimo = 0.04

p_marcado = (
    p_marcado_dado_spam * p_spam
    + p_marcado_dado_legitimo * (1 - p_spam)
)
p_spam_dado_marcado = p_marcado_dado_spam * p_spam / p_marcado

print(f"P(marcado) = {p_marcado:.3f}")
print(f"P(spam | marcado) = {p_spam_dado_marcado:.3f}")
```

**Resultado esperado:** `P(spam|marcado) ≈ 0.666`; en 10,000 mensajes habrá
aproximadamente 736 verdaderos positivos y 368 falsos positivos. La precisión
es la proporción de mensajes marcados que realmente son spam; la sensibilidad
es la proporción de todo el spam que el filtro detecta.

## 10. Evaluación formativa

### Lista de cotejo

| Criterio | Logrado si el estudiante... |
|---|---|
| Condicional | usa correctamente el evento que aparece después de la barra como condición |
| Independencia | compara `P(A∩B)` con `P(A)P(B)` o `P(A\|B)` con `P(A)` |
| Bayes | identifica priori, verosimilitud y posteriori |
| Continua | interpreta probabilidades como áreas en intervalos |
| Normal | calcula `z` y explica su signo y magnitud |
| Comunicación | reporta resultado, contexto y una limitación |

### Ticket de salida (113–120 minutos)

Responder individualmente:

1. En una frase, explicar por qué un resultado positivo no necesariamente
   significa que una persona esté enferma.
2. Escribir la fórmula de `P(A|B)`.
3. Si `X ~ N(100, 15²)`, calcular el puntaje `z` de `x = 70`.
4. Mencionar un supuesto que debe revisarse antes de usar una distribución
   normal.

**Respuestas esperadas:**  
1. Depende de la prevalencia y de los falsos positivos; se requiere Bayes.  
2. `P(A|B) = P(A∩B)/P(B)`.  
3. `z = -2`.  
4. Por ejemplo, forma aproximadamente simétrica, ausencia de colas extremas o
   que la variable medida sea razonablemente continua.

## 11. Errores frecuentes que debe anticipar el docente

- Confundir `P(A|B)` con `P(B|A)`.
- Usar el total de la tabla como denominador de una probabilidad condicional.
- Creer que una correlación o dependencia demuestra causalidad.
- Interpretar la altura de una densidad como una probabilidad puntual.
- Aplicar la normal sin revisar asimetría, valores atípicos o la naturaleza de
  la variable.
- Redondear demasiado pronto en Bayes; conservar varios decimales hasta el
  resultado final.

## 12. Extensión opcional

Para una siguiente sesión, comparar el modelo normal con una distribución
empírica: simular 10,000 tiempos con `np.random.normal`, construir un
histograma y contrastar la proporción observada con la probabilidad calculada
por `norm.cdf`. Discutir cómo cambia la aproximación con tamaños de muestra
pequeños y grandes.
