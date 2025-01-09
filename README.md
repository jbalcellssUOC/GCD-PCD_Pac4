# Orbea Monegros Python Package

Bienvenido al paquete de Python **Orbea Monegros**, desarrollado para analizar y gestionar los datos de la famosa prueba de ciclismo de montaña **Orbea Monegros 2024**. Este paquete incluye herramientas para manejar datos anonimizados de los ciclistas, realizar análisis estadísticos y generar visualizaciones de los resultados.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Características](#características)
3. [Requisitos previos](#requisitos-previos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Contribuir](#contribuir)
7. [Licencia](#licencia)

---

## Introducción

La **Orbea Monegros** es una de las pruebas de ciclismo de montaña más populares, celebrada en Sariñena (Huesca). Este paquete permite gestionar y analizar los datos anonimizados de los ciclistas, proporcionando herramientas útiles para investigadores, organizadores y entusiastas del ciclismo.

---

## Características

- **Cálculo estadístico:**
  - Tiempos promedio.
  - Distribución de tiempos por categoría.
- **Visualizaciones:**
  - Histogramas y gráficos comparativos.
- **Gestor de datos:**
  - Lectura y procesamiento del dataset anonimizado.
- **Herramientas CLI:**
  - Ejecuta análisis directamente desde la línea de comandos.

---

## Requisitos previos

- **Python 3.8 o superior**.
- Dependencias enumeradas en `requirements.txt`.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
   cd GCD-PCD_Pac4
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Instala el paquete en modo editable:
   ```bash
   pip install -e .
   ```

---

## Uso

### Importar el paquete

Usa las funcionalidades del paquete en tu código:

```python
from orbea_monegros import analysis

# Ejemplo: calcular estadísticas básicas del dataset
stats = analysis.calculate_statistics("data/dataset.csv")
print(stats)
```

### Ejecutar desde la línea de comandos

Si configuraste un comando CLI en `setup.py`, puedes ejecutar:

```bash
orbea-analysis --dataset data/dataset.csv
```

---

## Contribuir

Contribuciones son bienvenidas. Por favor, lee el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para más información.

Pasos básicos para contribuir:

1. Crea una rama para tu funcionalidad:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

2. Asegúrate de que los tests pasan:
   ```bash
   pytest tests/
   ```

3. Envía un Pull Request explicando tus cambios.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por usar el paquete **Orbea Monegros**! Si tienes preguntas o sugerencias, no dudes en contactar al autor:

- **Autor:** Jordi Balcells Saenz
- **Email:** [jbalcellss@uoc.edu](mailto:jbalcellss@uoc.edu)
- **Repositorio:** [https://github.com/jbalcellssUOC/GCD-PCD_Pac4](https://github.com/jbalcellssUOC/GCD-PCD_Pac4)
