# Manejo de Datos mediante Lenguaje Python

## 2. Manejo de datos mediante lenguaje Python

Este documento proporciona una guía completa sobre el análisis, procesamiento y visualización de datos utilizando Python, cubriendo NumPy, Pandas, visualización con Matplotlib y álgebra de datos.

---

## 2.1 Análisis de datos con NumPy

### 2.1.1 Arreglos, Indexación y Operaciones

#### Descripción

NumPy (Numerical Python) es una librería fundamental para computación numérica en Python. Proporciona soporte para:
- Arreglos multidimensionales (arrays)
- Funciones matemáticas de alto nivel
- Operaciones vectorizadas eficientes
- Generación de números aleatorios
- Álgebra lineal

#### Explicación

**¿Por qué usar NumPy?**
- **Eficiencia**: Las operaciones en NumPy son mucho más rápidas que las listas de Python puro
- **Facilidad**: Sintaxis clara y concisa para operaciones matriciales
- **Funcionalidad**: Incluye herramientas para álgebra lineal, estadística y más

**Conceptos principales:**
1. **ndarray**: Estructura principal de NumPy, arreglo multidimensional
2. **dtype**: Tipo de datos de los elementos del arreglo
3. **shape**: Dimensiones del arreglo
4. **Indexación**: Acceso a elementos individuales o grupos
5. **Broadcasting**: Operaciones con arreglos de diferentes tamaños

#### Ejemplos

**Creación de arreglos:**

```python
import numpy as np

# Crear arreglo a partir de una lista
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# Crear arreglo de ceros
arr2 = np.zeros((3, 4))
print(arr2)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Crear arreglo de unos
arr3 = np.ones((2, 3))

# Crear arreglo con secuencia
arr4 = np.arange(0, 10, 2)  # [0 2 4 6 8]

# Crear arreglo con espaciado lineal
arr5 = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]

# Arreglo de números aleatorios
arr6 = np.random.rand(3, 3)  # Matriz 3x3 con valores aleatorios entre 0 y 1
```

**Indexación y slicing:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Indexación simple
print(arr[0])     # 10
print(arr[-1])    # 50

# Slicing
print(arr[1:4])   # [20 30 40]
print(arr[::2])   # [10 30 50] - cada segundo elemento

# Arreglos multidimensionales
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 1])    # 2 - fila 0, columna 1
print(arr2d[1:, :2])  # filas 1-2, columnas 0-1
```

**Operaciones:**

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Operaciones aritméticas (elemento a elemento)
print(a + b)      # [ 6  8 10 12]
print(a - b)      # [-4 -4 -4 -4]
print(a * b)      # [ 5 12 21 32]
print(a / b)      # [0.2  0.33... 0.42... 0.5]
print(a ** 2)     # [ 1  4  9 16]

# Funciones estadísticas
print(np.sum(a))      # 10
print(np.mean(a))     # 2.5
print(np.std(a))      # 1.118... - desviación estándar
print(np.max(a))      # 4
print(np.min(a))      # 1

# Operaciones matriciales
matriz = np.array([[1, 2], [3, 4]])
print(np.sum(matriz, axis=0))  # [4 6] - suma por columnas
print(np.sum(matriz, axis=1))  # [3 7] - suma por filas
```

---

## 2.2 Análisis de datos con Pandas

### 2.2.1 Series, DataFrames y Agrupación

#### Descripción

Pandas es la librería más popular para análisis y manipulación de datos tabulares en Python. Proporciona:
- **Series**: Arreglos unidimensionales con índice
- **DataFrame**: Tablas bidimensionales (similares a hojas de cálculo)
- **Operaciones de agrupación, filtrado y transformación**
- **Manejo de datos faltantes**
- **Lectura/escritura de archivos (CSV, Excel, SQL)**

#### Explicación

**Series vs DataFrame:**
- **Series**: Es como una columna de datos con etiquetas (índice)
- **DataFrame**: Es como una tabla con múltiples Series (columnas)

**Características principales:**
1. Indexación flexible
2. Manejo inteligente de valores faltantes (NaN)
3. Alineación automática de datos por índice
4. Operaciones de agrupación poderosas

#### Ejemplos

**Crear Series:**

```python
import pandas as pd

# Crear una Serie simple
s1 = pd.Series([10, 20, 30, 40])
print(s1)
# 0    10
# 1    20
# 2    30
# 3    40

# Serie con índice personalizado
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s2['a'])  # 10

# Serie a partir de un diccionario
datos = {'manzanas': 100, 'naranjas': 150, 'plátanos': 200}
s3 = pd.Series(datos)
```

**Crear DataFrames:**

```python
# A partir de un diccionario
df = pd.DataFrame({
    'Nombre': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Edad': [25, 30, 35, 28],
    'Salario': [40000, 50000, 60000, 45000]
})

#     Nombre  Edad  Salario
# 0     Ana   25    40000
# 1   Bruno   30    50000
# 2  Carlos   35    60000
# 3   Diana   28    45000

# Acceder a datos
print(df['Nombre'])        # Columna completa
print(df.loc[0])          # Fila 0
print(df.iloc[0, 1])      # Elemento [0, 1]

# Información del DataFrame
print(df.shape)           # (4, 3) - 4 filas, 3 columnas
print(df.info())          # Tipos de datos y valores no nulos
print(df.describe())      # Estadísticas descriptivas
```

**Agrupación (GroupBy):**

```python
# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Departamento': ['Ventas', 'IT', 'Ventas', 'IT', 'HR'],
    'Nombre': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eva'],
    'Salario': [40000, 50000, 45000, 55000, 35000]
})

# Agrupar por departamento y calcular el promedio de salarios
promedio_salarios = df.groupby('Departamento')['Salario'].mean()
# Departamento
# HR        35000
# IT        52500
# Ventas    42500

# Múltiples agregaciones
resumen = df.groupby('Departamento').agg({
    'Salario': ['mean', 'sum', 'count'],
    'Nombre': 'count'
})

# Contar registros por grupo
conteo = df.groupby('Departamento').size()
```

### 2.2.2 Merge, Join y Concatenación

#### Descripción

Estas operaciones permiten combinar múltiples DataFrames de diferentes formas, esencial para integrar datos de múltiples fuentes.

#### Explicación

**Tipos de combinación:**
1. **Merge**: Combina en base a columnas comunes (como un JOIN en SQL)
2. **Join**: Combina en base a índices
3. **Concatenate**: Une DataFrames verticalmente (apila filas)

#### Ejemplos

**Merge (INNER JOIN):**

```python
# DataFrames a combinar
empleados = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Departamento_ID': [101, 102, 101, 103]
})

departamentos = pd.DataFrame({
    'Departamento_ID': [101, 102, 103],
    'Departamento': ['Ventas', 'IT', 'HR']
})

# Merge - combine por columna común
resultado = pd.merge(empleados, departamentos, on='Departamento_ID')
#    ID  Nombre Departamento_ID Departamento
# 0   1     Ana             101      Ventas
# 1   2   Bruno             102         IT
# 2   3  Carlos             101      Ventas
# 3   4   Diana             103         HR

# Left merge - mantiene todos los registros de la izquierda
resultado_left = pd.merge(empleados, departamentos, on='Departamento_ID', how='left')

# Right merge - mantiene todos los registros de la derecha
resultado_right = pd.merge(empleados, departamentos, on='Departamento_ID', how='right')

# Outer merge - mantiene todos los registros de ambos
resultado_outer = pd.merge(empleados, departamentos, on='Departamento_ID', how='outer')
```

**Join:**

```python
# Join usa el índice
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

df2 = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
}, index=['x', 'y', 'z'])

resultado = df1.join(df2)
#    A  B  C   D
# x  1  4  7  10
# y  2  5  8  11
# z  3  6  9  12
```

**Concatenación:**

```python
# Concatenar vertically (apilando filas)
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

resultado = pd.concat([df1, df2], ignore_index=True)
#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8

# Concatenar horizontalmente (lado a lado)
resultado_h = pd.concat([df1, df2], axis=1)
#    A  B  A  B
# 0  1  3  5  7
# 1  2  4  6  8
```

### 2.2.3 Operaciones

#### Descripción

Operaciones comunes sobre DataFrames para limpieza, transformación y análisis de datos.

#### Ejemplos

**Selección y filtrado:**

```python
df = pd.DataFrame({
    'Nombre': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Edad': [25, 30, 35, 28],
    'Salario': [40000, 50000, 60000, 45000]
})

# Seleccionar columnas
print(df[['Nombre', 'Edad']])

# Filtrado simple
print(df[df['Edad'] > 28])

# Filtrado múltiple
print(df[(df['Edad'] > 25) & (df['Salario'] > 45000)])

# Usar isin()
print(df[df['Nombre'].isin(['Ana', 'Bruno'])])
```

**Añadir y eliminar columnas:**

```python
# Añadir nueva columna
df['Bono'] = df['Salario'] * 0.1

# Eliminar columna
df_nuevo = df.drop('Bono', axis=1)

# Renombrar columnas
df_renombrado = df.rename(columns={'Salario': 'Sueldo'})
```

**Valores faltantes:**

```python
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8]
})

# Detectar valores faltantes
print(df.isna())

# Contar valores faltantes
print(df.isna().sum())

# Eliminar filas con valores faltantes
df_limpio = df.dropna()

# Llenar valores faltantes
df_rellenado = df.fillna(0)  # Llenar con 0
df_rellenado = df.fillna(df.mean())  # Llenar con promedio
```

**Ordenamiento y duplicados:**

```python
df = pd.DataFrame({
    'Nombre': ['Ana', 'Bruno', 'Ana', 'Diana'],
    'Edad': [25, 30, 25, 28]
})

# Ordenar
df_ordenado = df.sort_values('Edad', ascending=False)

# Eliminar duplicados
df_unico = df.drop_duplicates()

# Eliminar duplicados considerando solo algunas columnas
df_unico = df.drop_duplicates(subset=['Nombre'])
```

**Transformaciones:**

```python
df = pd.DataFrame({
    'Nombre': ['Ana', 'Bruno', 'Carlos'],
    'Salario': [40000, 50000, 60000]
})

# Aplicar función a cada valor
df['Salario_Miles'] = df['Salario'].apply(lambda x: x / 1000)

# Aplicar función con map
df['Nivel'] = df['Salario'].apply(
    lambda x: 'Bajo' if x < 45000 else 'Medio' if x < 55000 else 'Alto'
)

# Operaciones vectorizadas
df['Incremento'] = df['Salario'] * 1.1
```

---

## 2.3 Visualización de Datos

#### Descripción

La visualización de datos es crucial para:
- Explorar y entender patrones
- Comunicar resultados
- Detectar anomalías
- Tomar decisiones basadas en datos

#### Conceptos principales

1. **Exploración**: Entender la distribución y relaciones en los datos
2. **Comunicación**: Crear gráficos claros para presentar hallazgos
3. **Elección de gráficos**: Seleccionar el tipo adecuado según los datos

---

## 2.4 Librería Matplotlib

#### Descripción

Matplotlib es la librería más popular para crear gráficos estáticos, animados e interactivos en Python.

#### Explicación

**¿Por qué Matplotlib?**
- Amplia gama de tipos de gráficos
- Alta personalización
- Integración con Jupyter Notebooks
- Publicable (calidad de artículos científicos)

#### Ejemplos

**Gráfico de líneas:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Función Seno')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Gráfico de barras:**

```python
# Datos
categorias = ['Ventas', 'IT', 'HR', 'Marketing']
valores = [45000, 52500, 35000, 40000]

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color=['red', 'blue', 'green', 'orange'])
plt.ylabel('Salario Promedio')
plt.title('Salario Promedio por Departamento')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Histograma:**

```python
# Datos
datos = np.random.normal(100, 15, 1000)  # Media 100, desv est 15, 1000 valores

plt.figure(figsize=(10, 6))
plt.hist(datos, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución Normal')
plt.show()
```

**Scatter plot (Diagrama de dispersión):**

```python
# Datos
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, s=50, color='purple')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot: Relación entre X e Y')
plt.grid(True, alpha=0.3)
plt.show()
```

**Box plot:**

```python
# Datos
datos = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure(figsize=(10, 6))
plt.boxplot(datos, labels=['Grupo 1', 'Grupo 2', 'Grupo 3'])
plt.ylabel('Valores')
plt.title('Comparación de Distribuciones')
plt.show()
```

**Múltiples subgráficos:**

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Subgráfico 1: Línea
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Seno')

# Subgráfico 2: Coseno
axes[0, 1].plot(x, np.cos(x), color='red')
axes[0, 1].set_title('Coseno')

# Subgráfico 3: Parábola
axes[1, 0].plot(x, x**2, color='green')
axes[1, 0].set_title('Parábola')

# Subgráfico 4: Scatter
axes[1, 1].scatter(x, np.random.randn(100), alpha=0.6)
axes[1, 1].set_title('Puntos Aleatorios')

plt.tight_layout()
plt.show()
```

---

## 3. Álgebra de Datos

### 3.1 Vectores

#### Descripción

Un vector es una matriz unidimensional de números. En álgebra lineal, los vectores se usan para representar magnitudes y direcciones en un espacio.

#### Explicación

**Operaciones con vectores:**
1. **Adición**: Suma componente a componente
2. **Sustracción**: Resta componente a componente
3. **Multiplicación escalar**: Multiplicar cada componente por un número
4. **Producto punto (dot product)**: Suma de productos de componentes correspondientes
5. **Magnitud**: Longitud del vector
6. **Normalización**: Convertir a vector unitario

#### Ejemplos

**Operaciones básicas:**

```python
import numpy as np

# Crear vectores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Adición
suma = v1 + v2  # [5, 7, 9]

# Sustracción
resta = v1 - v2  # [-3, -3, -3]

# Multiplicación escalar
escalar = 2
v_escalado = v1 * escalar  # [2, 4, 6]

# Producto punto
producto_punto = np.dot(v1, v2)  # 1*4 + 2*5 + 3*6 = 32

# Magnitud del vector
magnitud = np.linalg.norm(v1)  # sqrt(1² + 2² + 3²) ≈ 3.74

# Normalización (vector unitario)
v_normalizado = v1 / np.linalg.norm(v1)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Escalado: {v_escalado}")
print(f"Producto punto: {producto_punto}")
print(f"Magnitud: {magnitud}")
print(f"Normalizado: {v_normalizado}")
```

**Aplicación práctica: Similitud entre vectores:**

```python
# Calcular similitud de coseno entre dos vectores
def similitud_coseno(v1, v2):
    """Calcula el coseno de similitud entre dos vectores"""
    producto = np.dot(v1, v2)
    norma_v1 = np.linalg.norm(v1)
    norma_v2 = np.linalg.norm(v2)
    
    if norma_v1 == 0 or norma_v2 == 0:
        return 0
    
    return producto / (norma_v1 * norma_v2)

# Ejemplo
v_usuario1 = np.array([1, 0, 1, 1, 0])  # Preferencias de usuario 1
v_usuario2 = np.array([1, 1, 0, 1, 1])  # Preferencias de usuario 2

similitud = similitud_coseno(v_usuario1, v_usuario2)
print(f"Similitud: {similitud:.3f}")  # Valores entre 0 y 1
```

### 3.2 Matrices

#### Descripción

Una matriz es un arreglo bidimensional de números. Son fundamentales en álgebra lineal y en el análisis de datos.

#### Explicación

**Operaciones con matrices:**
1. **Adición/Sustracción**: Operación elemento a elemento
2. **Multiplicación de matrices**: Producto matricial (distinto del elemento a elemento)
3. **Transpuesta**: Intercambia filas y columnas
4. **Determinante**: Valor escalar que describe propiedades de la matriz
5. **Inversa**: Matriz que al multiplicar da la identidad
6. **Valores propios (eigenvalues)**: Escalares que describen transformaciones

#### Ejemplos

**Operaciones básicas:**

```python
import numpy as np

# Crear matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matriz A:")
print(A)
print("\\nMatriz B:")
print(B)

# Adición
suma = A + B
print("\\nA + B =")
print(suma)

# Sustracción
resta = A - B
print("\\nA - B =")
print(resta)

# Multiplicación elemento a elemento (Hadamard)
producto_elemento = A * B
print("\\nA * B (elemento a elemento) =")
print(producto_elemento)

# Multiplicación matricial (dot product)
producto_matriz = np.dot(A, B)
print("\\nA · B (matricial) =")
print(producto_matriz)

# Transpuesta
A_transpuesta = A.T
print("\\nTranspuesta de A =")
print(A_transpuesta)

# Determinante
det_A = np.linalg.det(A)
print(f"\\nDeterminante de A = {det_A}")

# Inversa (si existe)
A_inversa = np.linalg.inv(A)
print("\\nInversa de A =")
print(A_inversa)

# Verificación: A * A^(-1) = I
identidad = np.dot(A, A_inversa)
print("\\nA · A^(-1) (debe ser identidad) =")
print(np.round(identidad, 10))
```

**Valores y vectores propios (Eigenvalues y Eigenvectors):**

```python
# Calcular valores propios y vectores propios
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Valores propios: {eigenvalues}")
print("\\nVectores propios:")
print(eigenvectors)

# Verificación: A * v = λ * v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    λ = eigenvalues[i]
    
    lado_izq = np.dot(A, v)
    lado_der = λ * v
    
    print(f"\\nAutovector {i+1}: {v}")
    print(f"Autovalor {i+1}: {λ}")
    print(f"A·v = {lado_izq}, λ·v = {lado_der}")
```

**Sistemas de ecuaciones lineales:**

```python
# Resolver: A·x = b
# 1x + 2y = 5
# 3x + 4y = 11

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 11])

# Resolver
x = np.linalg.solve(A, b)
print(f"Solución: x = {x[0]}, y = {x[1]}")

# Verificación
print(f"Verificación: A·x = {np.dot(A, x)}, debería ser {b}")
```

**Aplicación: Descomposición de valores singulares (SVD):**

```python
# SVD es útil para compresión, análisis de componentes principales, etc.
A = np.array([[1, 2], [3, 4], [5, 6]])

U, s, Vt = np.linalg.svd(A)

print("U:")
print(U)
print("\\nValores singulares:")
print(s)
print("\\nV^T:")
print(Vt)

# Reconstruir A a partir de SVD
A_reconstructed = np.dot(U, np.dot(np.diag(s), Vt))
print("\\nA reconstruida:")
print(A_reconstructed)
```

---

## Resumen

Esta guía ha cubierto los conceptos fundamentales para trabajar con datos en Python:

- **NumPy**: Operaciones numéricas eficientes con arreglos
- **Pandas**: Análisis y manipulación de datos tabulares
- **Matplotlib**: Visualización de datos
- **Álgebra lineal**: Conceptos matemáticos fundamentales

Estos conocimientos forman la base para técnicas más avanzadas como machine learning, análisis estadístico y ciencia de datos.

---

## Recursos Adicionales

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [NumPy Tutorial de Álgebra Lineal](https://numpy.org/doc/stable/reference/routines.linalg.html)
