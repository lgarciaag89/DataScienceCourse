# Conferencia: reducción de dimensionalidad

- **Curso:** Ciencia de Datos
- **Audiencia:** Licenciatura en Nanotecnología (séptimo semestre)
- **Duración:** 60 minutos
- **Material práctico:** [clase_practica_reduccion_dimensionalidad.ipynb](../clase_practica_reduccion_dimensionalidad.ipynb)
- **Clase siguiente:** [clase_practica_kmeans_jerarquico.ipynb](../clase_practica_kmeans_jerarquico.ipynb)

## Propósito

Medimos muchas variables por muestra, pero no podemos visualizarlas todas y varias aportan información repetida. Esta clase presenta la idea de reducir dimensiones, dos técnicas (PCA y t-SNE) y cómo decidir cuánto reducir. El énfasis está en **cuándo y cómo usarlas e interpretarlas**, no en su desarrollo matemático.

Al terminar, el estudiante podrá:

1. Explicar por qué conviene reducir dimensiones.
2. Aplicar PCA con datos estandarizados y elegir cuántos componentes conservar.
3. Interpretar *loadings* y biplots a nivel básico.
4. Usar t-SNE solo para visualizar, conociendo sus límites.

## Distribución del tiempo

| Bloque | Minutos |
| --- | ---: |
| Motivación | 8 |
| Preparación: correlación y escalamiento | 7 |
| PCA e interpretación | 20 |
| t-SNE | 8 |
| Demostración, actividad y cierre | 17 |
| **Total** | **60** |

---

## 1. Motivación

Razones para reducir dimensiones:

- **Visualizar:** solo percibimos 2 o 3 dimensiones.
- **Quitar redundancia:** variables correlacionadas repiten información.
- **Reducir ruido y costo:** menos variables, modelos más rápidos y estables.
- **Evitar la maldición de la dimensionalidad:** con muchas dimensiones las distancias pierden contraste y los métodos basados en distancia (como el clustering) empeoran.

| Estrategia | Qué hace | Ejemplo |
| --- | --- | --- |
| Selección de rasgos | Conserva un subconjunto de las variables | Ranking de consenso (tarea 4) |
| Extracción de rasgos | Crea variables nuevas a partir de las originales | PCA, t-SNE |

**Pregunta para el grupo:** si dos variables tienen correlación de 0.98, ¿cuánta información nueva aporta la segunda?

---

## 2. Preparación de los datos

**Ejemplo ilustrativo.** Imaginemos una tabla de 200 nanopartículas, cada una con 10 propiedades numéricas: tamaño, potencial zeta, área superficial, banda de absorción, entre otras. Algunas están claramente relacionadas (p. ej. tamaño y área superficial).

- **Correlación:** un mapa de calor de la matriz de correlación muestra qué variables son redundantes. Muchos bloques de alta correlación indican que pocas dimensiones pueden resumir los datos.
- **Escalamiento:** PCA se guía por la varianza, así que una variable con escala grande (p. ej. área en m²/g frente a un índice entre 0 y 1) dominaría solo por sus unidades. Por eso se estandariza antes (media 0, desviación 1).

> Regla: si las variables tienen unidades distintas, estandariza antes de PCA.

---

## 3. PCA (Análisis de Componentes Principales)

### Idea

PCA crea nuevos ejes, los **componentes principales**, que son combinaciones de las variables originales. Son independientes entre sí y están ordenados: PC1 recoge la mayor variación de los datos, PC2 la siguiente, y así sucesivamente. Nos quedamos con los primeros.

### ¿Cuántos componentes conservar?

| Criterio | Regla |
| --- | --- |
| Varianza acumulada | Conservar los que sumen 80 % o 90 % |
| Scree plot | Donde la curva deja de bajar de forma marcada (codo) |
| Kaiser | Componentes con autovalor mayor que 1 (datos estandarizados) |

Los criterios pueden dar resultados distintos. La decisión depende del objetivo: visualizar (2–3 componentes) o conservar información para otro análisis (más).

#### Ejemplo (datos hipotéticos)

Tabla de 8 variables estandarizadas (varianza total = 8):

| Componente | Autovalor | Varianza explicada | Varianza acumulada |
| --- | ---: | ---: | ---: |
| PC1 | 3.20 | 40 % | 40 % |
| PC2 | 1.76 | 22 % | 62 % |
| PC3 | 1.20 | 15 % | 77 % |
| PC4 | 0.80 | 10 % | 87 % |
| PC5 | 0.48 | 6 % | 93 % |
| PC6 | 0.32 | 4 % | 97 % |
| PC7 | 0.16 | 2 % | 99 % |
| PC8 | 0.08 | 1 % | 100 % |

- **Varianza acumulada:** con umbral de 80 % se conservan 4 componentes (87 %); con 90 %, 5 componentes (93 %).
- **Scree plot:** la curva cae mucho entre PC1, PC2 y PC3 (40 → 22 → 15) y luego se aplana (10, 6, 4, 2, 1). El codo está alrededor de PC3 o PC4: 3 o 4 componentes. Es una decisión visual.
- **Kaiser:** un autovalor menor que 1 explica menos que una variable estandarizada original. Se conservan PC1, PC2 y PC3 (3.20, 1.76, 1.20); PC4 (0.80) queda fuera: 3 componentes.

Los criterios dan 5, 4, 3 y 4 componentes. Una decisión razonable sería conservar 4: llega al 87 %, coincide con el codo y solo difiere de Kaiser por uno. Si el objetivo fuera visualizar, bastarían 2 o 3.

### Interpretación

- **Loadings:** pesos de cada variable en cada componente (p. ej. `PC1 = 0.42·variable_A + 0.39·variable_B + …`). Un peso alto en valor absoluto indica que la variable define fuertemente el eje; el signo indica la dirección: mismo signo, las variables suben juntas; signos opuestos, se mueven al contrario.
- **Biplot:** gráfico que muestra a la vez las muestras (puntos proyectados en PC1 y PC2) y las variables originales (flechas dibujadas con sus loadings). Se lee así: flecha larga, la variable pesa mucho en esos componentes; flechas en la misma dirección, variables correlacionadas; flechas opuestas, correlación negativa; flechas casi perpendiculares, poca relación; una muestra hacia donde apunta una flecha tiene valores altos en esa variable. Solo representa lo que capturan PC1 y PC2: si explican poca varianza, sus conclusiones son menos fiables.

En el ejemplo de las nanopartículas, si PC1 tiene pesos altos en tamaño y área superficial, podría leerse como un eje de "tamaño/superficie". Esa lectura es una **interpretación nuestra**, no algo que el método entregue.

### Precauciones

- El signo de un componente es arbitrario.
- PCA no usa etiquetas: separa lo que más varía, no necesariamente lo que distingue a las clases.
- Solo captura relaciones lineales.

---

## 4. t-SNE

Técnica no lineal que conserva las vecindades: muestras parecidas quedan juntas en un mapa 2D. Suele separar grupos mejor que PCA, pero:

- las **distancias entre grupos** y su **tamaño** no significan nada;
- depende de la **perplexity** y de la semilla: probar varios valores;
- no sirve para datos nuevos;
- es solo para **visualizar**, no para modelar ni para descubrir grupos reales.

| | PCA | t-SNE |
| --- | --- | --- |
| Tipo | Lineal | No lineal |
| Interpretable | Sí (loadings) | No |
| Datos nuevos | Sí | No |
| Uso | Reducir, visualizar, preprocesar | Solo visualizar |

**Perplexity (perplejidad):** parámetro de t-SNE que controla cuántos vecinos cercanos considera cada punto; se interpreta como el número efectivo de vecinos.

- Valores bajos (p. ej. 5): resaltan estructura local fina, pero pueden fragmentar un grupo real en subgrupos o crear "islas" de ruido.
- Valores altos (p. ej. 50–100): muestran mejor la estructura global, pero pueden mezclar grupos pequeños.
- Rango típico: 5 a 50 (por defecto suele usarse 30). Debe ser menor que el número de muestras.
- No hay un valor "correcto": se prueban varios (p. ej. 5, 30 y 60) y solo se confía en lo que se mantiene igual en todos.

---

## 5. Demostración en el notebook

El notebook aplica todo lo anterior a un conjunto de datos de ejemplo de química de bebidas incluido en scikit-learn (178 muestras y 13 variables químicas; la etiqueta real se usa solo para colorear). Se recorre en este orden:

1. Matriz de correlación.
2. Efecto de escalar o no antes de PCA.
3. Scree plot y varianza acumulada.
4. Proyección en 2D, *loadings* y biplot.
5. Comparación de PCA con t-SNE.
6. Clustering con K-means usando todas las variables o solo los primeros componentes.

Mensaje principal de la demostración: **escalar es indispensable**, y **reducir a pocos componentes puede conservar casi toda la estructura útil**.

---

## 6. Actividad

1. Aplica PCA a `ejercicios/data/peptides.csv` (quita `Class`, trata faltantes y estandariza). ¿Cuántos componentes explican el 90 %?
2. Compara el clustering con todas las variables frente a los primeros componentes.
3. Repite el PCA sin estandarizar y explica qué cambia.
4. Interpreta PC1 y PC2 en un párrafo.

### Preguntas de discusión

- ¿Qué criterio usarías para elegir el número de componentes y por qué?
- ¿Qué conclusiones **no** debes sacar de un gráfico t-SNE?
- ¿Cuándo preferirías selección de rasgos en lugar de extracción?

### Respuestas orientativas

- Los tres criterios son orientativos; se justifica según el objetivo y se verifica que el análisis posterior no empeore.
- No interpretar distancias ni tamaños entre grupos, ni usar t-SNE para afirmar que existen clusters.
- Selección si se quiere conservar variables con significado propio o ahorrar mediciones; extracción si hay mucha redundancia y no importa perder la interpretación directa.

---

## 7. Cierre

- Reducir dimensiones sirve para visualizar, quitar redundancia y reducir ruido.
- Estandariza antes de PCA.
- Elige el número de componentes con varianza acumulada, scree plot y el objetivo del análisis.
- t-SNE es solo para visualizar.
- Siguiente clase: clustering con K-means y jerárquico.
