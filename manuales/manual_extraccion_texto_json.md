# Manual: extracción de información de un archivo de texto puro y de un JSON

## 1. ¿Qué es un archivo de texto puro?

Un archivo de texto puro es un archivo que contiene texto simple, sin una estructura formal de datos. Puede ser un `.txt`, `.log`, `.csv` o cualquier archivo plano.

Ejemplo:

```text
Hola mundo
Juan Pérez
25
México
Ingeniería
```

En este tipo de archivo, la información no está organizada en etiquetas ni en pares clave-valor; simplemente está escrita en texto. Para extraer datos, normalmente se leen las líneas y se buscan patrones.

## 2. ¿Qué es JSON?

JSON significa JavaScript Object Notation. Es un formato ligero para almacenar e intercambiar información. Se usa mucho en APIs, aplicaciones web, configuraciones y datos de software.

Una estructura JSON tiene este formato:

```json
{
  "nombre": "Juan",
  "edad": 25,
  "ciudad": "México",
  "hobbies": ["leer", "correr", "programar"]
}
```

### Características de JSON
- Está organizado en pares clave-valor.
- Se escribe entre llaves `{}`.
- Cada clave va acompañada de un valor.
- Los valores pueden ser:
  - texto (`"Juan"`)
  - números (`25`)
  - listas (`["leer", "correr"]`)
  - objetos anidados
  - booleanos (`true`, `false`)
  - nulos (`null`)

### ¿Por qué es importante JSON?
JSON es importante porque:
- es fácil de leer por humanos
- es fácil de procesar por computadoras
- es estándar para enviar datos entre sistemas
- se usa ampliamente en APIs y servicios web

## 3. Diferencia entre texto puro y JSON

### Texto puro
- No tiene estructura definida.
- La información puede estar mezclada o escrita de manera libre.
- Hay que interpretar el contenido manualmente o mediante reglas.

### JSON
- Tiene estructura clara.
- La información está organizada por claves.
- Es más fácil extraer datos específicos.

## 4. Cómo extraer información de un archivo de texto puro

Supongamos que tenemos este archivo llamado `datos.txt`:

```text
Nombre: Ana
Edad: 30
Ciudad: Guadalajara
Correo: ana@email.com
```

### Paso 1: abrir el archivo

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

### Paso 2: mostrar el contenido

```python
print(contenido)
```

### Paso 3: separar por líneas

```python
lineas = contenido.splitlines()

for linea in lineas:
    print(linea)
```

### Paso 4: buscar una línea específica

```python
for linea in lineas:
    if linea.startswith("Ciudad:"):
        ciudad = linea.split(":")[1].strip()
        print("La ciudad es:", ciudad)
```

Salida:

```text
La ciudad es: Guadalajara
```

### Paso 5: extraer varios campos

```python
for linea in lineas:
    if ":" in linea:
        clave, valor = linea.split(":", 1)
        print(clave.strip(), "->", valor.strip())
```

Salida:

```text
Nombre -> Ana
Edad -> 30
Ciudad -> Guadalajara
Correo -> ana@email.com
```

### Resumen
Para archivos de texto puro:
1. se abre el archivo
2. se lee el contenido
3. se separa por líneas o por patrón
4. se localiza la información buscada
5. se limpia el texto y se guarda el resultado

## 5. Cómo extraer información de un JSON

Supongamos que tenemos este archivo llamado `persona.json`:

```json
{
  "nombre": "Ana",
  "edad": 30,
  "ciudad": "Guadalajara",
  "correo": "ana@email.com"
}
```

### Paso 1: abrir el archivo

```python
with open("persona.json", "r", encoding="utf-8") as archivo:
    datos = archivo.read()
```

### Paso 2: convertir el texto JSON a un objeto Python

```python
import json

with open("persona.json", "r", encoding="utf-8") as archivo:
    persona = json.load(archivo)
```

Ahora `persona` es un diccionario de Python y se puede acceder por clave.

### Paso 3: acceder a los datos

```python
print(persona["nombre"])
print(persona["ciudad"])
```

Salida:

```text
Ana
Guadalajara
```

### Paso 4: extraer varios valores

```python
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Correo:", persona["correo"])
```

Salida:

```text
Nombre: Ana
Edad: 30
Correo: ana@email.com
```

## 6. JSON con listas

Un JSON puede tener arreglos o listas. Por ejemplo:

```json
{
  "nombre": "Ana",
  "materias": ["Matemáticas", "Física", "Programación"]
}
```

Para acceder a la primera materia:

```python
import json

with open("persona.json", "r", encoding="utf-8") as archivo:
    persona = json.load(archivo)

print(persona["materias"][0])
```

Salida:

```text
Matemáticas
```

## 7. Ejemplo comparativo

### Archivo de texto puro

```text
Nombre: Ana
Edad: 30
Ciudad: Guadalajara
```

Se extrae así:
- leer el archivo
- separar líneas
- buscar la línea con `Nombre:` o `Ciudad:`
- tomar el valor después de `:`

### JSON

```json
{
  "nombre": "Ana",
  "edad": 30,
  "ciudad": "Guadalajara"
}
```

Se extrae así:
- leer el archivo JSON
- convertirlo a un diccionario con `json.load()`
- acceder por clave: `persona["nombre"]`

## 8. ¿Cuándo usar cada uno?

### Usa texto puro cuando:
- los datos están escritos como un documento legible
- no existe una estructura formal
- el archivo es un registro o log

### Usa JSON cuando:
- los datos deben ser procesados por software
- necesitas consultar información rápida y ordenada
- el archivo es generado por una API o aplicación

## 9. Conclusión

- Un archivo de texto puro contiene información sin estructura formal.
- JSON contiene información organizada en clave-valor.
- Extraer información de un texto puro implica analizar cadenas y patrones.
- Extraer información de JSON implica cargarlo con `json.load()` y acceder a las claves.

JSON es más útil para trabajar con datos estructurados, mientras que el texto puro se usa cuando la información está escrita de manera libre o en un formato simple.

## 10. Código de ejemplo completo

```python
import json

# Leer texto puro
with open("datos.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("Texto puro:")
print(texto)

# Leer JSON
with open("persona.json", "r", encoding="utf-8") as archivo:
    persona = json.load(archivo)

print("\nJSON:")
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
```

## 11. Recomendación práctica

Si vas a trabajar con datos que necesitan ser consultados y manipulados con rapidez, JSON es la mejor opción. Si solo tienes texto escrito, hay que interpretarlo y limpiar la información antes de usarla.

---

Este documento sirve como introducción para entender la diferencia entre ambos tipos de datos y cómo extraer información de cada uno de ellos.
