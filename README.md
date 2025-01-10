
<div style="display: flex; flex-direction: column; align-items: center;">
  <img src="images/logo-orbea.jpg" alt="Logo Orbea" height="90" />
</div>

<div style="display: flex; flex-direction: column; align-items: center; padding-bottom: 50px">
  <img src="images/orbea-sample.png" alt="Orbea Sample" height="200" />
</div>

<div style="display: flex; justify-content: center; margin-bottom: 20px;">
  <a href="#english-version" style="margin: 0 10px;">
    <img src="images/flag-us.svg" alt="English" title="English" height="25" />
  </a>
  <a href="#spanish-version" style="margin: 0 10px;">
    <img src="images/flag-es.svg" alt="Español" title="Español" height="25" />
  </a>
  <a href="#catalan-version" style="margin: 0 10px;">
    <img src="images/flag-cat.svg" alt="Català" title="Català" height="25" />
  </a>
</div>

# Orbea Monegros Python Package

---

## English Version

Welcome to the **Orbea Monegros** Python package, developed to analyze and manage data from the famous mountain biking event **Orbea Monegros 2024**. This package includes tools to handle anonymized rider data, perform statistical analysis, and generate visualizations of the results.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

The **Orbea Monegros** is one of the most popular mountain biking events held in Sariñena (Huesca). This package allows you to manage and analyze anonymized rider data, providing useful tools for researchers, organizers, and cycling enthusiasts.

---

## Features

- **Statistical Calculations:**
  - Average times.
  - Time distribution by category.
- **Visualizations:**
  - Histograms and comparative charts.
- **Data Manager:**
  - Read and process anonymized datasets.
- **CLI Tools:**
  - Run analysis directly from the command line.

---

## Prerequisites

- **Python 3.8 or later**.
- Dependencies listed in `requirements.txt`.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
   cd GCD-PCD_Pac4
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

---

## Usage

### Import the package

Use the package's features in your code:

```python
from orbea_monegros import analysis

# Example: calculate basic statistics of the dataset
stats = analysis.calculate_statistics("data/dataset.csv")
print(stats)
```

### Run from the command line

If you configured a CLI command in `setup.py`, you can run:

```bash
orbea-analysis --dataset data/dataset.csv
```

---

## Contributing

Contributions are welcome. Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

Basic steps to contribute:

1. Create a branch for your feature:
   ```bash
   git checkout -b feature/new-feature
   ```

2. Ensure tests pass:
   ```bash
   pytest tests/
   ```

3. Submit a Pull Request explaining your changes.

---

## License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using the **Orbea Monegros** package! If you have questions or suggestions, feel free to contact the author:

- **Author:** Jordi Balcells Saenz
- **Email:** [jbalcellss@uoc.edu](mailto:jbalcellss@uoc.edu)
- **Repository:** [https://github.com/jbalcellssUOC/GCD-PCD_Pac4](https://github.com/jbalcellssUOC/GCD-PCD_Pac4)

---

## Spanish Version

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

---

## Catalan Version

Benvingut al paquet de Python **Orbea Monegros**, desenvolupat per analitzar i gestionar les dades de la famosa prova de ciclisme de muntanya **Orbea Monegros 2024**. Aquest paquet inclou eines per gestionar dades anonimitzades dels ciclistes, fer anàlisis estadístiques i generar visualitzacions dels resultats.

## Taula de Continguts

1. [Introducció](#introducció)
2. [Característiques](#característiques)
3. [Requisits previs](#requisits-previs)
4. [Instal·lació](#instal·lació)
5. [Ús](#ús)
6. [Contribuir](#contribuir)
7. [Llicència](#llicència)

---

## Introducció

La **Orbea Monegros** és una de les proves de ciclisme de muntanya més populars, celebrada a Sariñena (Osca). Aquest paquet permet gestionar i analitzar les dades anonimitzades dels ciclistes, proporcionant eines útils per a investigadors, organitzadors i entusiastes del ciclisme.

---

## Característiques

- **Càlcul estadístic:**
  - Temps mitjans.
  - Distribució de temps per categoria.
- **Visualitzacions:**
  - Histogramas i gràfics comparatius.
- **Gestor de dades:**
  - Lectura i processament del dataset anonimitzat.
- **Eines CLI:**
  - Executa anàlisis directament des de la línia de comandaments.

---

## Requisits previs

- **Python 3.8 o superior**.
- Dependències enumerades a `requirements.txt`.

---

## Instal·lació

1. Clona el repositori:
   ```bash
   git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
   cd GCD-PCD_Pac4
   ```

2. Crea un entorn virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

3. Instal·la les dependències:
   ```bash
   pip install -r requirements.txt
   ```

4. Instal·la el paquet en mode editable:
   ```bash
   pip install -e .
   ```

---

## Ús

### Importa el paquet

Usa les funcionalitats del paquet al teu codi:

```python
from orbea_monegros import analysis

# Exemple: calcular estadístiques bàsiques del dataset
stats = analysis.calculate_statistics("data/dataset.csv")
print(stats)
```

### Executar des de la línia de comandaments

Si vas configurar una comanda CLI a `setup.py`, pots executar:

```bash
orbea-analysis --dataset data/dataset.csv
```

---

## Contribuir

Les contribucions són benvingudes. Si us plau, llegeix l'arxiu [CONTRIBUTING.md](CONTRIBUTING.md) per a més informació.

Passos bàsics per contribuir:

1. Crea una branca per a la teva funcionalitat:
   ```bash
   git checkout -b feature/nova-funcionalitat
   ```

2. Assegura't que els tests passen:
   ```bash
   pytest tests/
   ```

3. Envia un Pull Request explicant els teus canvis.

---

## Llicència

Aquest projecte està sota la llicència MIT. Consulta l'arxiu [LICENSE](LICENSE) per a més detalls.

---

Gràcies per usar el paquet **Orbea Monegros**! Si tens preguntes o suggeriments, no dubtis a contactar amb l'autor:

- **Autor:** Jordi Balcells Saenz
- **Email:** [jbalcellss@uoc.edu](mailto:jbalcellss@uoc.edu)
- **Repositori:** [https://github.com/jbalcellssUOC/GCD-PCD_Pac4](https://github.com/jbalcellssUOC/GCD-PCD_Pac4)