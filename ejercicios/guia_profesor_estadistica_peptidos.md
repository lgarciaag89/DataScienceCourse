# Guía del profesor — Evaluación de Estadística con Python
## Dataset: peptides.csv

**Datos:** 9,816 observaciones × 128 columnas  
**Clases:** `ABP` = 4,017; `NoNABP` = 5,799  
**Descriptores numéricos:** 127  
**Valores faltantes:** ninguno

---

# Ejercicio 1 — Exploración

Resultados esperados:

- 9,816 péptidos.
- 128 columnas en total.
- 127 descriptores numéricos.
- 1 variable categórica: `Class`.
- `ABP`: 4,017.
- `NoNABP`: 5,799.
- No existen valores faltantes.

El objetivo es que el estudiante sepa distinguir la variable de clase de los descriptores.

---

# Ejercicio 2 — Tendencias centrales

Descriptores seleccionados:

```text
ESM2_t33_MEAN_1202
ESM2_t33_MEAN_529
CHOQUET[D;0.5;AO2;0.9]_C_pbs
```

Valores globales relevantes:

| Descriptor | Media | Mediana | Desv. estándar | Sesgo |
|---|---:|---:|---:|---:|
| ESM2_t33_MEAN_1202 | 0.06566 | 0.05995 | 0.07939 | 0.029 |
| ESM2_t33_MEAN_529 | 0.03215 | 0.03358 | 0.05675 | 0.033 |
| CHOQUET[D;0.5;AO2;0.9]_C_pbs | 0.01032 | 0.000819 | 0.05681 | 14.380 |

El tercer descriptor es deliberadamente seleccionado porque presenta una diferencia muy marcada entre media y mediana y una asimetría positiva extrema.

### Interpretación esperada

Para `CHOQUET[D;0.5;AO2;0.9]_C_pbs`, la media está muy por encima de la mediana. Esto es consistente con una distribución fuertemente sesgada hacia la derecha.

No es necesario que el alumno conozca el significado químico del descriptor.

---

# Ejercicio 3 — Dispersión

Punto didáctico importante:

El descriptor `ESM2_t33_MEAN_1202` tiene una desviación estándar mayor que `ESM2_t33_MEAN_529`, pero las escalas y unidades de los descriptores pueden ser diferentes.

La conclusión correcta es que **no debe utilizarse únicamente la desviación estándar absoluta para comparar variabilidad entre variables en escalas distintas**.

Se puede aceptar como respuesta adicional el coeficiente de variación, siempre que el alumno explique sus limitaciones cuando la media está próxima a cero.

---

# Ejercicio 4 — Simetría y outliers

Dos descriptores fueron seleccionados deliberadamente para producir un contraste claro.

### `ESM2_t33_MEAN_1202`

Sesgo:

```text
≈ 0.029
```

Esto indica una distribución aproximadamente simétrica en términos de asimetría lineal.

Media:

```text
≈ 0.06566
```

Mediana:

```text
≈ 0.05995
```

La diferencia no es exactamente cero, pero es pequeña comparada con el comportamiento del tercer descriptor.

### `CHOQUET[D;0.5;AO2;0.9]_C_pbs`

Sesgo:

```text
≈ 14.38
```

Esto representa una asimetría positiva extrema.

Media:

```text
≈ 0.01032
```

Mediana:

```text
≈ 0.000819
```

La media es mucho mayor que la mediana debido a una cola derecha muy pronunciada.

### Criterio de corrección

El estudiante debe reconocer:

- `ESM2_t33_MEAN_1202`: aproximadamente simétrica.
- `CHOQUET[D;0.5;AO2;0.9]_C_pbs`: fuertemente asimétrica positiva.
- Los valores extremos afectan considerablemente la media.
- La mediana es más robusta frente a valores extremos.

No exigir que el estudiante conozca el concepto de "skewness" formalmente si todavía no se ha enseñado.

---

# Ejercicio 5 — Correlación

Entre los 127 descriptores aparecen asociaciones fuertes.

Una de las mayores correlaciones positivas observadas es aproximadamente:

```text
r = 0.954
```

entre:

```text
MIC_GOWAWA[0.0;1;NONE;0.0;0.0;1;S-OWA;1.0;0.0]_P_scv
```

y

```text
MIC_GOWAWA[0.1;0;AO1-OWA;1.0;0.0;2;S-OWA;0.8;0.1]_P_khh
```

También aparecen correlaciones negativas fuertes. Una de las mayores magnitudes negativas observadas es aproximadamente:

```text
r = -0.739
```

entre:

```text
ESM2_t33_MEAN_837
```

y

```text
ESM2_t33_MEAN_78
```

### Nota

Los resultados pueden cambiar ligeramente dependiendo de cómo el estudiante procese la matriz, pero deben permanecer próximos a estos valores.

### Interpretación esperada

- `r` cercano a +1: asociación lineal positiva fuerte.
- `r` cercano a -1: asociación lineal negativa fuerte.
- La correlación mide asociación lineal, no causalidad.

---

# Ejercicio 6 — Correlación y causalidad

La respuesta central es:

> No. Incluso una correlación de 0.95 no demuestra causalidad.

Los dos descriptores pueden estar midiendo aspectos relacionados de las mismas características moleculares.

En este contexto es especialmente importante evitar que el estudiante interprete:

```text
correlación alta → causalidad
```

como una regla válida.

### Respuestas aceptables

Como explicaciones alternativas se pueden aceptar:

- ambos descriptores dependen de propiedades moleculares relacionadas;
- una tercera característica del péptido influye en ambos;
- los descriptores pueden contener información redundante;
- la asociación puede surgir de la estructura matemática de los descriptores.

---

# Ejercicio 7 — Comparación por clase

Descriptor:

```text
ESM2_t33_MEAN_753
```

Este descriptor presenta una diferencia relativamente marcada entre las clases.

El tamaño del efecto estandarizado entre `ABP` y `NoNABP` es aproximadamente:

```text
1.85
```

Esto hace que sea adecuado para la discusión estadística.

### Lo que debe evaluarse

El alumno debe ser capaz de distinguir:

> "Las distribuciones de las dos clases son diferentes."

de:

> "El descriptor causa que el péptido sea ABP."

La segunda afirmación **no está justificada** por una comparación descriptiva.

---

# Ejercicio 8 — Integración

No existe una única conclusión correcta.

Se debe evaluar que el estudiante:

1. utilice correctamente los resultados;
2. diferencie tendencia central y dispersión;
3. interprete los gráficos;
4. interprete la correlación;
5. no confunda asociación con causalidad.

---

# Rúbrica sugerida

## Código — 25 puntos

| Criterio | Puntos |
|---|---:|
| Carga y manipulación correcta del CSV | 5 |
| Uso correcto de Pandas/NumPy | 8 |
| Cálculos estadísticos | 8 |
| Código organizado | 4 |

## Estadística — 25 puntos

| Criterio | Puntos |
|---|---:|
| Tendencia central | 8 |
| Dispersión | 8 |
| Simetría/outliers | 9 |

## Visualización — 15 puntos

| Criterio | Puntos |
|---|---:|
| Histograma | 4 |
| Boxplot | 4 |
| Scatter plot | 4 |
| Etiquetas/legibilidad | 3 |

## Interpretación — 25 puntos

| Criterio | Puntos |
|---|---:|
| Interpretación de media/mediana | 5 |
| Interpretación de dispersión | 5 |
| Interpretación de correlación | 5 |
| Correlación ≠ causalidad | 10 |

## Claridad — 10 puntos

- respuestas claras;
- conclusiones justificadas;
- uso apropiado de terminología estadística.

---

# Observación para futuras versiones

Este dataset permite construir una evaluación bastante buena porque contiene:

- descriptores aproximadamente simétricos;
- descriptores extremadamente asimétricos;
- posibles valores atípicos;
- correlaciones positivas fuertes;
- correlaciones negativas fuertes;
- una variable `Class` con dos grupos;
- diferencias descriptivas entre las clases.

Por ello no es necesario introducir datos artificiales: la evaluación puede basarse completamente en el dataset real.
