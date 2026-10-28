# Clase práctica — Métricas y normalización: ¿quién es el material más parecido?

**Asignatura:** Ciencia de Datos  
**Duración:** 2 horas  
**Modalidad:** práctica guiada en parejas, con Python y scikit-learn  
**Contexto:** comparar materiales a partir de sus propiedades

Esta sesión conecta la clase de [métricas de similitud y distancia](./Metricas%20de%20similitud%20y%20distancia.md) con la de [escalamiento y normalización](./clase_9_escalamiento_y_normalizacion.md). La pregunta que guía toda la práctica es:

> **¿Cambiar la métrica o escalar los datos puede cambiar qué observación consideramos más cercana?**

## Resultados de aprendizaje

Al finalizar, cada estudiante podrá:

1. Calcular distancias euclidiana y Manhattan entre observaciones numéricas.
2. Comparar distancias y vecinos más cercanos antes y después de aplicar `StandardScaler` y `MinMaxScaler`.
3. Explicar por qué una transformación puede cambiar el orden de cercanía.
4. Elegir y justificar una combinación de representación, escalador y métrica para una pregunta concreta.
5. Distinguir una diferencia matemática de una conclusión científicamente válida.

## Preparación

- Un equipo por pareja con Python, Jupyter o Google Colab.
- Paquetes: `pandas`, `scikit-learn` y `matplotlib`.
- No se requiere un archivo de datos externo: el conjunto sintético se crea durante la sesión.
- Antes de comenzar, recordar: las filas son materiales; las columnas son propiedades; el identificador no entra en el cálculo.

## Secuencia de la sesión

| Tiempo | Actividad | Evidencia de aprendizaje |
| ---: | --- | --- |
| 0–10 min | Activación y predicción individual | Predicción del material más cercano a A y explicación |
| 10–25 min | Repaso conectado: métrica, escala y unidades | Elección razonada de qué calcular y transformar |
| 25–45 min | Práctica guiada: distancias sin escalar | Matriz y ranking de vecinos |
| 45–70 min | Práctica guiada: `StandardScaler` y `MinMaxScaler` | Comparación del ranking entre representaciones |
| 70–90 min | Reto en parejas: cambiar la métrica | Tabla comparativa y argumento |
| 90–110 min | Análisis crítico y extensiones | Respuestas a preguntas de interpretación |
| 110–117 min | Puesta en común | Defensa breve de una decisión |
| 117–120 min | Ticket de salida | Respuesta individual de síntesis |

---

## 1. Activación — predice antes de calcular (10 min)

Se quiere encontrar el material más parecido a **A**, que tiene tamaño de 10 nm y densidad de 2.00 g/cm³.

1. Sin usar Python, ¿cuál material creen que será el vecino más cercano a A?
2. ¿Qué propiedad creen que influirá más en la distancia?
3. ¿Esperan que la respuesta dependa de la métrica o de escalar las columnas?

Cada estudiante anota una predicción y la conserva para compararla con los resultados.

## 2. Repaso conectado (15 min)

Recordatorio de las dos decisiones que se combinarán:

- **Métrica:** define cómo se acumulan las diferencias. Euclidiana eleva las diferencias al cuadrado antes de sumarlas; Manhattan suma diferencias absolutas.
- **Escalamiento:** cambia la representación numérica de las columnas y, por tanto, su contribución a las distancias.

La estandarización no es una métrica y no decide qué propiedad es científicamente más importante. Es una transformación que cambia la geometría de los datos. El resultado depende de ambas decisiones.

## 3. Práctica guiada: conjunto de materiales (20 min)

Ejecutar esta celda y describir la tabla. Los valores son sintéticos y sirven para estudiar el efecto de las decisiones analíticas; no representan mediciones experimentales.

```python
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.DataFrame(
    {
        "material": ["A", "B", "C", "D", "E", "F"],
        "tamano_nm": [10, 10.5, 30, 9, 12, 15],
        "densidad_g_cm3": [2.00, 2.20, 2.01, 1.90, 2.10, 2.05],
    }
)

columnas = ["tamano_nm", "densidad_g_cm3"]
X = df[columnas]
display(df)
```

**Comprueben antes de continuar:**

- `material` identifica la fila y se excluye de `X`.
- Las dos columnas numéricas tienen unidades y rangos diferentes.
- No hay valores faltantes en este ejemplo.

## 4. Distancias sin escalar (25 min)

Calcular las distancias entre todos los pares y ordenar los vecinos de A. La primera columna de cada matriz corresponde a A.

```python
D_euclidiana = pairwise_distances(X, metric="euclidean")
D_manhattan = pairwise_distances(X, metric="manhattan")

print("Euclidiana, sin escalar:")
display(pd.DataFrame(D_euclidiana, index=df["material"], columns=df["material"]).round(3))

print("Manhattan, sin escalar:")
display(pd.DataFrame(D_manhattan, index=df["material"], columns=df["material"]).round(3))

def ranking_desde_a(distancias, nombres):
    orden = distancias[0].argsort()
    return [(nombres[i], round(distancias[0, i], 3)) for i in orden if i != 0]

print("Vecinos de A (euclidiana):", ranking_desde_a(D_euclidiana, df["material"]))
print("Vecinos de A (Manhattan):", ranking_desde_a(D_manhattan, df["material"]))
```

**Anoten:** vecino más cercano, distancia a B y distancia a C para cada métrica. ¿La métrica cambió el primer vecino en los datos originales?

## 5. Escalar columnas y recalcular (25 min)

Se ajusta cada escalador con este conjunto porque la actividad es descriptiva: estamos explorando cómo cambia la geometría de estas seis observaciones, no evaluando un modelo predictivo.

```python
escaladores = {
    "StandardScaler": StandardScaler(),
    "MinMaxScaler": MinMaxScaler(),
}

resultados = {}
for nombre, escalador in escaladores.items():
    X_transformado = escalador.fit_transform(X)
    resultados[nombre] = {
        "euclidiana": pairwise_distances(X_transformado, metric="euclidean"),
        "manhattan": pairwise_distances(X_transformado, metric="manhattan"),
    }

for nombre, distancias in resultados.items():
    print(f"\n{nombre}")
    print("Euclidiana:", ranking_desde_a(distancias["euclidiana"], df["material"]))
    print("Manhattan:", ranking_desde_a(distancias["manhattan"], df["material"]))
```

Completar esta tabla con el vecino más cercano a A:

| Representación | Euclidiana | Manhattan |
| --- | --- | --- |
| Sin escalar |  |  |
| `StandardScaler` |  |  |
| `MinMaxScaler` |  |  |

**Preguntas de análisis:**

1. ¿Se mantuvo el mismo vecino de A después de escalar?
2. ¿Cambió el ranking al cambiar de euclidiana a Manhattan?
3. ¿Qué propiedad contribuye más a la distancia sin escalar? ¿Y después de estandarizar?
4. ¿Por qué `StandardScaler` y `MinMaxScaler` no tienen que producir las mismas distancias?
5. ¿El vecino que resulta más cercano es automáticamente el material científicamente más similar?

## 6. Reto en parejas — una decisión justificada (20 min)

Cada pareja selecciona una de estas preguntas y la resuelve con una tabla de resultados y una recomendación breve:

### Reto A: otra unidad

La tabla registra el tamaño en nanómetros. Como 1 000 nm = 1 µm, conviertan esa columna a micrómetros y vuelvan a calcular la distancia euclidiana **sin escalar**. Después, busquen explícitamente cuál material (B, C, D, E o F) tiene la menor distancia a **A**; A es el material de referencia y no se cuenta a sí mismo:

```python
X_um = X.copy()
X_um["tamano_nm"] = X_um["tamano_nm"] / 1_000

D_um = pairwise_distances(X_um, metric="euclidean")
print("Vecinos de A con tamaño en micrómetros:",
      ranking_desde_a(D_um, df["material"]))
```

Comparen ese vecino más cercano a A con el obtenido en la sección 4. El resultado esperado es **B** con el tamaño en nanómetros y **C** al expresarlo en micrómetros.

**¿Por qué cambia?** La conversión representa los mismos tamaños físicos, pero cambia los números de esa columna por un factor de 1 000. Al mezclar tamaño y densidad en una distancia euclidiana sin escalar, ese cambio altera cuánto pesa numéricamente cada propiedad. La conversión no cambió los materiales: muestra que calcular distancias sin escalar puede hacer que la conclusión dependa de las unidades elegidas. Expliquen qué decisión tomarían para comparar los materiales y por qué.

### Reto B: comparar otro punto de referencia

Repetir la comparación tomando C como material de referencia. ¿La combinación que seleccionaron en la sección anterior también les resulta adecuada para C?

## 7. Puesta en común y criterios de decisión (20 min)

Cada pareja dispone de un minuto para presentar:

- la pregunta analítica que eligió;
- la métrica y transformación usadas;
- qué resultado cambió respecto a los datos sin escalar;
- una limitación o supuesto de su conclusión.

Usar estos criterios para discutir las recomendaciones:

| Pregunta | Consideración |
| --- | --- |
| ¿Las variables tienen escalas o unidades diferentes? | Comparar resultados con y sin escalamiento; justificar los pesos implícitos. |
| ¿Importa la diferencia absoluta o la mayor discrepancia por variable? | Elegir la métrica de acuerdo con la interpretación del problema. |
| ¿Importa más el perfil relativo que el nivel de las propiedades? | Evaluar si normalizar filas tiene sentido en el dominio. |
| ¿Se está construyendo un modelo predictivo? | Ajustar el escalador solo con entrenamiento y aplicar `transform` a validación y prueba. |
| ¿La decisión cambia al variar métrica o escalador? | Reportar esa sensibilidad; no ocultarla eligiendo el resultado más conveniente. |

> **Conclusión de la práctica:** una distancia no es una verdad independiente de la representación. Métrica y escalamiento codifican supuestos; deben elegirse según la pregunta y el conocimiento del dominio.

## 8. Ticket de salida (3 min)

Responder individualmente, en dos o tres frases:

> En el ejemplo, el vecino más cercano a A cambia al escalar. ¿Qué cambió realmente: los materiales o la manera de medir sus diferencias? ¿Qué información necesitas antes de recomendar una transformación?

## Guía breve para quien imparte

### Resultados esperados del ejemplo

Los rankings de A son:

| Representación | Euclidiana: orden de cercanía | Manhattan: orden de cercanía |
| --- | --- | --- |
| Sin escalar | B, D, E, F, C | B, D, E, F, C |
| `StandardScaler` | F, D, E, B, C | D, F, E, B, C |
| `MinMaxScaler` | F, D, E, B, C | D, F, E, B, C |

Las cifras pueden variar por redondeo, pero el orden debe coincidir con el código. Sin escalar, las diferencias numéricas de tamaño dominan buena parte de la comparación. Al escalar columnas, las diferencias se expresan con relación a la variabilidad o al rango de cada propiedad; por eso cambia el vecino de A. Manhattan y euclidiana también pueden ordenar de forma distinta después del escalamiento.

### Respuestas que conviene reforzar

- Cambia la distancia calculada, no las propiedades físicas de los materiales.
- Estandarizar no vuelve las variables igualmente importantes desde el punto de vista científico: asigna un peso asociado a su dispersión observada.
- Min-Max depende de extremos y no garantiza que futuros valores queden entre 0 y 1.
- Normalizar filas modifica la magnitud de cada observación; no es intercambiable con estandarizar columnas.
- En una tarea predictiva, ajustar el escalador antes de separar los datos puede filtrar información del conjunto de prueba. Debe ajustarse con entrenamiento y reutilizarse con `transform`.
- Un resultado de cercanía es una herramienta para responder una pregunta concreta, no una etiqueta objetiva de similitud.

## Evaluación formativa

| Criterio | Logrado cuando… |
| --- | --- |
| Cálculo | Ejecuta ambas métricas y excluye correctamente la diagonal al ordenar vecinos. |
| Comparación | Completa la tabla de rankings para las tres representaciones. |
| Interpretación | Relaciona el cambio de ranking con las diferencias de escala y con la métrica. |
| Justificación | Recomienda una decisión y explicita un supuesto o limitación del dominio. |

## Referencias

- [Métricas de similitud y distancia](./Metricas%20de%20similitud%20y%20distancia.md), material de la clase previa.
- [Escalamiento y normalización](./clase_9_escalamiento_y_normalizacion.md), material de la clase previa.
- [Preprocesamiento de datos en scikit-learn](https://scikit-learn.org/stable/modules/preprocessing.html).
- [Métricas de distancias en scikit-learn](https://scikit-learn.org/stable/modules/metrics.html#pairwise-metrics-affinities-and-kernels).
