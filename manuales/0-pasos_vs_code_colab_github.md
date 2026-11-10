# Guía de Configuración: VS Code + Google Colab + GitHub Copilot

Esta guía describe paso a paso cómo configurar un entorno de desarrollo científico y de ciencia de datos combinando la interfaz de **VS Code**, la asistencia de código con **GitHub Copilot** y el cómputo en la nube de **Google Colab** (evitando la necesidad de instalar Python localmente).

---

## 🎯 Arquitectura del Entorno

* **VS Code:** Editor local ligero e interfaz para trabajar con cuadernos de Jupyter (`.ipynb`).
* **GitHub Copilot:** Asistente de inteligencia artificial para autocompletado, sugerencias y depuración de código.
* **Google Colab (Servidor Remoto):** Provee el entorno de ejecución (Kernel de Python), la memoria RAM y el procesamiento (GPUs/TPUs) en la nube.

---

## 📋 Requisitos Previos

1. Tener instalado **VS Code** en tu computadora ([Descargar VS Code](https://code.visualstudio.com/)).
2. Una cuenta de **Google** (para acceder a Google Colab).
3. Una cuenta de **GitHub** con acceso a **GitHub Copilot** (gratuito para estudiantes y profesores verificados mediante ([GitHub Education](https://github.com/education))).

---

## 🚀 Paso a Paso

### Paso 1: Instalar las Extensiones Necesarias en VS Code

1. Abre **VS Code**.
2. Ve al panel de extensiones en la barra lateral izquierda (`Ctrl + Shift + X` en Windows/Linux o `Cmd + Shift + X` en Mac).
3. Busca e instala las siguientes extensiones:
   * **Python** (de Microsoft).
   * **Jupyter** (de Microsoft).
   * **GitHub Copilot Chat** (de GitHub).
   * **Colab** (de Google / opcional para integración directa).

---

### Paso 2: Activar GitHub Copilot en VS Code

1. Haz clic en el ícono de **Cuentas / Perfil** en la esquina inferior izquierda de VS Code.
2. Selecciona **Sign in with GitHub to use GitHub Copilot**.
3. Sigue las instrucciones en el navegador para autorizar la conexión.
4. Un ícono de **Copilot** aparecerá en la barra de estado inferior indicando que el servicio está activo.

---

### Paso 3: Vincular el Kernel de Colab en VS Code

1. Regresa a **VS Code** y abre tu archivo de cuaderno de Jupyter (`.ipynb`).
2. En la esquina superior derecha del cuaderno, haz clic en el botón de **Select Kernel**. 
3. Selecciona **colab**.
4. Selecciona **New Colab Server CPU, GPU ot TPU**
5. Selecciona **CPU**, **GPU** or **TPU**
6. Continuea hasta que te pida definir nombre del kernel

---

## ✅ Verificación del Funcionamiento

1. **Prueba de Cómputo:** En tu primera celda de código, escribe:
   ```python
   import torch
   print("GPU disponible en Colab:", torch.cuda.is_available())
   ```
   Ejecuta la celda (`Shift + Enter`). Debe mostrar la respuesta procesada desde la nube de Colab.

2. **Prueba de Copilot:** En una celda vacía, escribe un comentario como:
   ```python
   # Función para calcular el diámetro promedio de nanopartículas
   ```
   Presiona `Enter` y verás cómo **GitHub Copilot** te sugiere automáticamente la función en código atenuado. Presiona `Tab` para aceptar la sugerencia.

---

## 📌 Consejos y Buenas Prácticas

* **Cero instalación local:** Este método no requiere que instales Python, Anaconda ni bibliotecas en la computadora física.
* **Persistencia de sesión:** Las sesiones inactivas en la versión gratuita de Colab pueden desconectarse tras un periodo de inactividad. Si la conexión se interrumpe, simplemente vuelve a obtener el token o a reconectar el Kernel desde VS Code.
* **Uso Docente / Laboratorio:** Ideal para salas de cómputo donde no se tienen permisos de administrador para instalar paquetes o donde los equipos tienen recursos limitados.