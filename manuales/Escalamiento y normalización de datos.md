---
marp: true
theme: default
paginate: true
math: mathjax
---

# Escalamiento y distancias
Ciencia de Datos · Semana 9 · 12–18 octubre de 2026

**Sesión teórica: 120 minutos**

**Meta:** explicar cómo las unidades y la escala alteran las distancias.

---

## Ruta de la sesión · 120 min

Activación: 10 min. Distancias: 20 min. Métodos de escalamiento: 30 min. Demostración: 25 min. Ejercicio: 25 min. Cierre: 10 min.

---

## Una pregunta para comenzar

Dos materiales difieren en 10 nm de tamaño y 0.5 g/cm³ de densidad. ¿Cuál diferencia domina una distancia euclidiana calculada directamente?

Los números dependen de las unidades. Dominar la distancia no implica mayor relevancia científica.

---

## Observaciones y variables

Filas: materiales. Columnas: propiedades.

Cada material es un punto $x_i=(x_{i1},x_{i2},x_{i3})$. Los identificadores permiten rastrear observaciones; no se incluyen en la distancia.

---

## Distancia euclidiana

$$d(x_i,x_j)=\sqrt{\sum_{p=1}^{m}(x_{ip}-x_{jp})^2}$$

Para (10, 2) y (20, 2.5): $d=\sqrt{100+0.25}\approx10.012$. Si el tamaño se expresa en micrómetros, cambia su contribución. La unidad elegida altera el agrupamiento.

---

## StandardScaler

$$z_{ip}=\frac{x_{ip}-\mu_p}{\sigma_p}$$

Centra cada variable y ajusta su desviación estándar a 1, salvo variables constantes. En scikit-learn se usa la desviación poblacional.

No hace que los datos sigan una distribución normal. Los valores extremos afectan la media y la desviación.

---

## MinMaxScaler

$$u_{ip}=\frac{x_{ip}-\min(x_p)}{\max(x_p)-\min(x_p)}$$

Por defecto, transforma los datos de ajuste al intervalo [0,1]. Nuevos datos pueden quedar fuera. Los extremos determinan el rango; observaciones centrales pueden quedar comprimidas.

---

## RobustScaler y normalización

RobustScaler centra por la mediana y divide por el rango intercuartílico. Puede ser útil cuando existen extremos.

Normalizar cada fila a norma 1 es otra operación: enfatiza dirección y reduce el papel de la magnitud. No es equivalente a escalar columnas.

---

## Cómo decidir

Compara sin escalar, estandarización y rango [0,1].

Pregunta qué significa una diferencia de una desviación estándar en cada propiedad. Escalar asigna pesos implícitos; no reemplaza el criterio del dominio.

---

## Demostración

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("materiales_sinteticos.csv")
columnas = ["tamano_nm", "densidad_g_cm3", "modulo_GPa"]
X = df[columnas].copy()
assert not X.isna().any().any()
scaler = StandardScaler()
Z = scaler.fit_transform(X)
from sklearn.preprocessing import MinMaxScaler
U = MinMaxScaler().fit_transform(X)
print(X.std(ddof=0))
print(Z.std(axis=0))
print(U.min(axis=0), U.max(axis=0))
```

---

## Fit y transform

`fit` estima los parámetros; `transform` aplica la transformación. `fit_transform` combina ambas operaciones.

En evaluación predictiva, se ajusta con entrenamiento y se transforma validación/test. En esta exploración descriptiva trabajamos con todo el conjunto; no estimamos rendimiento predictivo.

---

## Ejercicio en parejas · 25 min

Calcula a mano StandardScaler para [2,4,6], con desviación poblacional. Compara con MinMaxScaler.

Predice qué pasa si añadimos 100 y después verifica. ¿Cambian los valores transformados de 2,4,6?

---

## Salida · 10 min

Explica por qué escalar no equivale a limpiar ni a eliminar anomalías.

Anticipación: K-Means utiliza distancias, por lo que heredará estas decisiones.

Referencia: documentación oficial de scikit-learn, Preprocessing data: https://scikit-learn.org/stable/modules/preprocessing.html
