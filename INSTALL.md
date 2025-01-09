# Instalación del Paquete Orbea Monegros

Este documento describe los pasos necesarios para instalar y configurar el paquete **Orbea Monegros** en tu entorno de desarrollo o producción.

---

## Requisitos previos

Asegúrate de cumplir con los siguientes requisitos antes de proceder:

1. **Python 3.8 o superior** instalado. Puedes verificar tu versión con:
   ```bash
   python --version
   ```

2. **pip** (el gestor de paquetes de Python) instalado. Puedes verificarlo con:
   ```bash
   pip --version
   ```

3. Opcionalmente, instala **virtualenv** para crear un entorno virtual:
   ```bash
   pip install virtualenv
   ```

4. Acceso al repositorio del proyecto en GitHub:
   [https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git](https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git)

---

## Instalación

### 1. Clonar el repositorio

Primero, clona el repositorio del proyecto desde GitHub:

```bash
git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
cd GCD-PCD_Pac4
```

### 2. Crear un entorno virtual (recomendado)

Para evitar conflictos entre dependencias, se recomienda utilizar un entorno virtual:

```bash
python -m venv venv
```

Activa el entorno virtual:
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- En Windows:
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Instalar las dependencias

Una vez dentro del entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 4. Instalar el paquete en modo editable

Para trabajar con el paquete en desarrollo, instálalo en modo editable:

```bash
pip install -e .
```

---

## Ejecución de pruebas

Para asegurarte de que todo está funcionando correctamente, ejecuta los tests incluidos:

```bash
pytest tests/
```

---

## Uso del paquete

Tras la instalación, puedes utilizar el paquete desde cualquier script o directamente desde la línea de comandos:

### Importar en un script:

```python
from orbea_monegros import main
main()
```

### Comando en la terminal:

Si definiste un script ejecutable en `setup.py`, ejecuta:

```bash
orbea-analysis
```

---

## Desinstalación

Para desinstalar el paquete, simplemente ejecuta:

```bash
pip uninstall orbea-monegros
```

Si deseas eliminar también el entorno virtual, simplemente elimina la carpeta `venv/`:

```bash
rm -rf venv  # En macOS/Linux
del venv     # En Windows
```

---

¡Listo! Ahora puedes usar y desarrollar el paquete **Orbea Monegros**.

