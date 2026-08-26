# Visualización de Datos con Matplotlib desde cero

## 1. ¿Qué es la visualización de datos?

La visualización de datos es la técnica de transformar información numérica, tabular o categórica en gráficos para que sea más fácil entender patrones, tendencias, relaciones y anomalías.

Un buen gráfico ayuda a:
- Explorar datos
- Detectar errores o valores atípicos
- Comparar grupos o categorías
- Identificar tendencias a lo largo del tiempo
- Comunicar resultados de forma clara

En ciencia de datos, un gráfico no solo sirve para "verse bien": sirve para contar una historia con los datos.

---

## 2. ¿Qué es Matplotlib?

Matplotlib es la librería más importante y más usada en Python para crear gráficos 2D.

Se utiliza para generar:
- Gráficos de líneas
- Gráficos de barras
- Histogramas
- Diagramas de dispersión
- Boxplots
- Gráficos circulares
- Subgráficos múltiples
- Figuras para reportes y publicaciones

Es una librería muy poderosa, flexible y muy útil cuando quieres controlar cada detalle del gráfico.

No usa Seaborn. Este manual está pensado solamente para Matplotlib.

---

## 3. Importar Matplotlib

La forma más común de importar Matplotlib es:

```python
import matplotlib.pyplot as plt
```

La palabra `plt` es un alias que usaremos para acceder a funciones como:
- `plot()`
- `scatter()`
- `bar()`
- `hist()`
- `pie()`
- `figure()`
- `xlabel()`
- `ylabel()`
- `title()`
- `legend()`
- `grid()`
- `show()`

---

## 4. Flujo básico para crear un gráfico

Para hacer casi cualquier gráfico en Matplotlib, seguimos este flujo:

1. Importar la librería
2. Definir los datos
3. Crear la figura
4. Dibujar el gráfico
5. Agregar títulos, etiquetas y leyenda
6. Mostrarlo o guardarlo

### Ejemplo mínimo

```python
import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

# Crear la figura
plt.figure(figsize=(8, 5))

# Graficar
plt.plot(x, y, color='blue', marker='o', linewidth=2)

# Etiquetas
plt.title('Ejemplo básico de Matplotlib')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True, alpha=0.3)

# Mostrar
plt.show()
```

![alt text](images/example_line.png)

Este ejemplo crea una línea con puntos. Es la base para entender cómo funciona Matplotlib.

---

## 5. Conceptos básicos

### 5.1 Figure

La `figure` es la “ventana” o lienzo en el que se dibuja el gráfico.

```python
fig = plt.figure(figsize=(8, 5))
```

`figsize` controla el tamaño del gráfico en pulgadas.

### 5.2 Axes

Los `axes` son los ejes del gráfico, donde se dibuja la información. Son la parte interna donde se trazan los datos.

### 5.3 Títulos y etiquetas

```python
plt.title('Ventas mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
```

Esto hace que el gráfico sea entendible.

### 5.4 Leyenda

Cuando hay más de una serie, conviene usar una leyenda:

```python
plt.plot(x, ventas, label='Ventas')
plt.plot(x, gastos, label='Gastos')
plt.legend()
```

### 5.5 Grid

La cuadrícula ayuda a leer mejor los valores:

```python
plt.grid(True, alpha=0.3)
```

### 5.6 Guardar gráfico

```python
plt.savefig('mi_grafico.png', dpi=300)
```

`dpi` determina la resolución.

---

## 6. Tipos de gráficos más relevantes

A continuación, los gráficos más útiles en análisis de datos.

---

## 7. Gráfico de líneas

### ¿Cuándo usarlo?

Se usa cuando queremos observar una tendencia o evolución a lo largo del tiempo.

### Ejemplo

```python
import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
ventas = [120, 150, 140, 180, 210, 195]

plt.figure(figsize=(10, 6))
plt.plot(meses, ventas, color='darkgreen', marker='o', linewidth=2)
plt.title('Ventas mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.grid(True, alpha=0.3)
plt.show()
```

![alt text](images/line_ventas.png)

### Interpretación

El gráfico de líneas es ideal para responder preguntas como:
- ¿La variable aumenta o disminuye?
- ¿Hay una tendencia clara?
- ¿Hay cambios bruscos en el tiempo?

### Modificar los valores de los ticks del eje X

Los *ticks* son las marcas y etiquetas que aparecen en los ejes. Podemos
seleccionar qué valores mostrar y cambiar el texto de sus etiquetas:

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [10, 14, 13, 18, 21, 20]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, marker='o')
ax.set_xticks([0, 2, 4])
ax.set_xticklabels(['Inicio', 'Mitad', 'Final'])
ax.set_xlabel('Momento del experimento')
ax.set_ylabel('Medición')
ax.set_title('Personalización de los ticks del eje X')
plt.show()
```

También es posible rotar las etiquetas cuando son largas:

```python
ax.tick_params(axis='x', rotation=45)
```

---

## 8. Gráfico de barras

### ¿Cuándo usarlo?

Se usa para comparar cantidades entre categorías.

### Ejemplo

```python
import matplotlib.pyplot as plt

categorias = ['Ventas', 'IT', 'Recursos Humanos', 'Marketing']
valores = [45000, 52000, 32000, 41000]

plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.title('Salario promedio por departamento')
plt.ylabel('Salario')
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
```

![alt text](images/barras.png)

### Interpretación

Las barras permiten ver diferencias entre grupos de forma directa.

Es muy útil para:
- Comparar ventas por región
- Evaluar rendimiento por equipo
- Mostrar conteos por categoría

---

## 9. Histograma

### ¿Cuándo usarlo?

Se usa para observar la distribución de una variable continua.

### Ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt

# Datos simulados con distribución normal
notas = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10, 6))
plt.hist(notas, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribución de notas')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
```

![alt text](images/histograma.png)

### Interpretación

Un histograma ayuda a responder preguntas como:
- ¿Los datos están concentrados en un rango?
- ¿Hay valores muy altos o muy bajos?
- ¿La distribución es simétrica o sesgada?

---

## 10. Diagrama de dispersión (scatter plot)

### ¿Cuándo usarlo?

Se usa para estudiar la relación entre dos variables numéricas.

### Ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='purple', alpha=0.7)
plt.title('Relación entre dos variables')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True, alpha=0.3)
plt.show()
```
![alt text](images/dispercion.png)

### Interpretación

El scatter plot ayuda a detectar:
- Correlaciones
- Agrupamientos
- Valores atípicos
- Relación lineal o no lineal entre variables

Es un gráfico clave en análisis exploratorio.

---

## 11. Gráfico circular (pie chart)

### ¿Cuándo usarlo?

Se usa para mostrar proporciones de un total.

### Ejemplo

```python
import matplotlib.pyplot as plt

etiquetas = ['A', 'B', 'C', 'D']
valores = [35, 25, 20, 20]

plt.figure(figsize=(7, 7))
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Participación por categoría')
plt.axis('equal')
plt.show()
```

![alt text](images/pie.png)

### Interpretación

Los gráficos circulares muestran partes de un total, pero solo son útiles cuando:
- Hay pocas categorías
- Se quiere comunicar proporción general
- No se requiere comparación detallada entre muchos grupos

> Importante: un pie chart no es la mejor opción para comparar muchas categorías o para mostrar detalles precisos.

---

## 12. Múltiples subgráficos

### ¿Cuándo usarlo?

Cuando quieres comparar varios gráficos en una sola figura.

### Ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title('Seno')

axes[0, 1].plot(x, np.cos(x), color='red')
axes[0, 1].set_title('Coseno')

axes[1, 0].plot(x, x**2, color='green')
axes[1, 0].set_title('Parábola')

axes[1, 1].scatter(x, np.random.randn(100), color='purple', alpha=0.6)
axes[1, 1].set_title('Dispersión aleatoria')

plt.tight_layout()
plt.show()
```

![alt text](images/subgraficos.png)

### Interpretación

Los subgráficos son muy útiles para:
- Comparar varias perspectivas del mismo problema
- Mostrar distintos tipos de análisis en una sola figura
- Presentaciones y reportes

---

## 13. Boxplot

Este será el último gráfico de la sección dedicada a resumir distribuciones.

### ¿Cuándo usarlo?

Se usa para comparar distribuciones y detectar valores atípicos.

### Ejemplo

```python
import numpy as np
import matplotlib.pyplot as plt

grupo1 = np.random.normal(10, 2, 200)
grupo2 = np.random.normal(12, 3, 200)
grupo3 = np.random.normal(9, 4, 200)

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([grupo1, grupo2, grupo3], labels=['Grupo 1', 'Grupo 2', 'Grupo 3'])
ax.set_title('Comparación de distribuciones')
ax.set_ylabel('Valores')
plt.show()
```

![alt text](images/boxplot.png)

### ¿Qué significa cada elemento?

- **Mediana:** línea dentro de la caja; divide los datos en dos mitades.
- **Primer cuartil (Q1):** borde inferior; deja por debajo el 25 % de los datos.
- **Tercer cuartil (Q3):** borde superior; deja por debajo el 75 % de los datos.
- **Caja:** contiene el 50 % central de las observaciones.
- **Rango intercuartílico (IQR):** `Q3 - Q1`, representado por la altura de la caja.
- **Bigotes:** valores extremos que no se consideran atípicos, normalmente dentro de `1.5 * IQR`.
- **Puntos aislados:** valores atípicos según el criterio anterior.

---

## 14. Visualización de clusters

Un gráfico de dispersión permite visualizar las etiquetas asignadas por un
algoritmo de agrupamiento. En este ejemplo se simulan tres clusters.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
centros = [(2, 2), (7, 6), (8, 1)]
datos = []
etiquetas = []

for etiqueta, (centro_x, centro_y) in enumerate(centros):
    cluster = rng.normal(loc=(centro_x, centro_y), scale=0.8, size=(60, 2))
    datos.append(cluster)
    etiquetas.extend([etiqueta] * len(cluster))

datos = np.vstack(datos)
etiquetas = np.array(etiquetas)

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(datos[:, 0], datos[:, 1], c=etiquetas, cmap='viridis', alpha=0.75)
ax.set_title('Visualización de clusters')
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')
ax.legend(*scatter.legend_elements(), title='Cluster')
plt.show()
```

![alt text](images/clusters.png)

Los grupos separados sugieren comportamientos diferentes en las dos
variables. Esta visualización ayuda a evaluar la separación, pero no
sustituye métricas como *silhouette score*.

---

## 15. Cómo elegir el gráfico correcto

La elección del gráfico depende de la pregunta que quieras responder.

### Si quieres ver tendencia:
- Usa gráfico de líneas

### Si quieres comparar categorías:
- Usa gráfico de barras

### Si quieres ver distribución:
- Usa histograma o boxplot

### Si quieres ver relación entre variables:
- Usa scatter plot

### Si quieres ver proporciones:
- Usa pie chart

### Si quieres comparar varias cosas a la vez:
- Usa subgráficos

---

## 16. Buenas prácticas en Matplotlib

1. Usa títulos claros que expliquen el gráfico
2. Etiqueta siempre los ejes
3. Usa leyenda solo cuando sea necesario
4. Evita demasiados colores o demasiados elementos
5. Ajusta el tamaño del gráfico para que se vea bien
6. Usa `plt.tight_layout()` para mejorar el espacio
7. Guarda la imagen con buena resolución (`dpi=300`)
8. No uses gráficos que distorsionen la realidad

---

## 17. Analizar las distribuciones de dos variables

En este ejercicio se carga un `DataFrame` con dos columnas numéricas. Se
visualiza la distribución de cada variable con histogramas y se comparan
ambas mediante un diagrama de dispersión.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos.csv')
variable_x = 'variable_1'
variable_y = 'variable_2'

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(df[variable_x].dropna(), bins=20, color='steelblue', edgecolor='white')
axes[0].set_title(f'Distribución de {variable_x}')
axes[0].set_xlabel(variable_x)
axes[0].set_ylabel('Frecuencia')

axes[1].hist(df[variable_y].dropna(), bins=20, color='darkorange', edgecolor='white')
axes[1].set_title(f'Distribución de {variable_y}')
axes[1].set_xlabel(variable_y)
axes[1].set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df[variable_x], df[variable_y], alpha=0.7)
ax.set_title(f'Relación entre {variable_x} y {variable_y}')
ax.set_xlabel(variable_x)
ax.set_ylabel(variable_y)
plt.show()
```

Para sacar conclusiones, observa la forma, concentración y sesgo de cada
histograma, además de los valores atípicos y datos faltantes. En el scatter
plot, revisa si existe una relación positiva, negativa o inexistente, si es
lineal y si aparecen grupos diferenciados.

---

## 18. Tips útiles de Matplotlib

### `figsize`

Define el tamaño de la figura en pulgadas: el primer valor es el ancho y el
segundo la altura.

```python
plt.figure(figsize=(8, 5))  # horizontal
plt.figure(figsize=(6, 6))  # cuadrada
plt.figure(figsize=(5, 8))  # vertical
```

### `dpi`

Controla la resolución. Para guardar imágenes para un reporte suele ser
suficiente `dpi=150` o `dpi=300`; una resolución mayor produce archivos más
grandes.

```python
plt.savefig('figura.png', dpi=300, bbox_inches='tight')
```

### `marker`

Define la forma de los puntos en líneas o dispersión. Algunos valores útiles
son `'o'` (círculo), `'s'` (cuadrado), `'^'` (triángulo) y `'x'` (equis).

```python
plt.plot(x, y, marker='o')
```

### `linewidth`

Controla el grosor de las líneas. Valores entre `1` y `3` suelen funcionar
bien en gráficos para pantalla.

```python
plt.plot(x, y, linewidth=2)
```

### `alpha`

Controla la transparencia de un elemento gráfico. Su valor va de `0` a `1`:
`0` es completamente transparente y `1` es completamente opaco. Un valor
como `0.3` permite que la cuadrícula se vea sin distraer de los datos.

```python
plt.grid(True, alpha=0.3)
plt.scatter(x, y, alpha=0.6)
```

### Colores y `colormap`

Puedes usar nombres (`'navy'`), códigos hexadecimales (`'#1f77b4'`) o mapas
de color. Usa mapas secuenciales para magnitudes y mapas categóricos para
grupos.

```python
plt.plot(x, y, color='#1f77b4')
plt.scatter(x, y, c=valores, cmap='viridis')
```

Algunos mapas comunes son `'viridis'`, `'plasma'`, `'coolwarm'` y `'tab10'`.
La elección debe mantener suficiente contraste y ser legible.

---

## 19. Resumen

Matplotlib es la base de la visualización en Python.

Con esta librería puedes:
- Hacer gráficos sencillos o complejos
- Explorar datos
- Comunicar resultados
- Crear figuras profesionales
- Trabajar sin depender de Seaborn

Si aprendes bien sus fundamentos, podrás crear la mayoría de visualizaciones que necesitas en ciencia de datos.

---

## 20. Siguiente paso recomendado

Lo más importante es practicar con los tipos de gráficos básicos:
- líneas
- barras
- histogramas
- scatter
- boxplots

Con esos cinco gráficos ya puedes comenzar a analizar la mayoría de conjuntos de datos.

---

## 21. Bibliografía / referencias

- Matplotlib documentation: https://matplotlib.org/stable/contents.html
- Documentación oficial de Python para visualización científica
