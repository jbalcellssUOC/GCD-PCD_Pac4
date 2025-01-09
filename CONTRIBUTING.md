# Contributing to Orbea Monegros Python Package

¡Gracias por tu interés en contribuir al proyecto Orbea Monegros! Tu ayuda es fundamental para mejorar y hacer crecer este paquete. Sigue esta guía para contribuir de manera efectiva.

## Table of Contents
1. [Cómo empezar](#cómo-empezar)
2. [Estructura del repositorio](#estructura-del-repositorio)
3. [Reglas para contribuir](#reglas-para-contribuir)
4. [Reporte de problemas](#reporte-de-problemas)
5. [Envío de cambios (Pull Requests)](#envío-de-cambios-pull-requests)
6. [Estilo de código](#estilo-de-código)
7. [Contacto](#contacto)

---

## Cómo empezar

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
   cd GCD-PCD_Pac4
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # En macOS/Linux
   .\venv\Scripts\activate    # En Windows
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta los tests para asegurarte de que todo está funcionando:**
   ```bash
   pytest tests/
   ```

---

## Estructura del repositorio

- `orbea_monegros/`: Contiene el código principal del paquete.
- `tests/`: Incluye los tests unitarios.
- `data/`: Archivos de datos necesarios para el análisis.
- `README.md`: Documentación general del proyecto.
- `setup.py`: Archivo para empaquetar y distribuir el proyecto.
- `CONTRIBUTING.md`: Guía para colaborar en el proyecto.
- `requirements.txt`: Dependencias del proyecto.

---

## Reglas para contribuir

1. **Sé respetuoso**: Este es un espacio colaborativo. Sé amable y paciente con los demás colaboradores.
2. **Crea una rama para tu contribución**:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Escribe tests para cualquier funcionalidad nueva**.
4. **Proporciona documentación clara**: Añade o actualiza la documentación si introduces cambios significativos.

---

## Reporte de problemas

Si encuentras un problema o tienes una sugerencia, por favor, crea un [issue en GitHub](https://github.com/jbalcellssUOC/GCD-PCD_Pac4/issues) con:

- Una descripción detallada del problema o sugerencia.
- Pasos para reproducir el problema (si aplica).
- Capturas de pantalla o ejemplos de código (si es relevante).

---

## Envío de cambios (Pull Requests)

1. **Asegúrate de que tu rama está actualizada**:
   ```bash
   git pull origin main
   ```

2. **Confirma tus cambios y escribe mensajes de commit claros**:
   ```bash
   git add .
   git commit -m "Descripción clara del cambio realizado"
   ```

3. **Envía tu Pull Request**:
   - Ve a la página del repositorio en GitHub.
   - Haz clic en "Compare & Pull Request".
   - Proporciona una descripción detallada de los cambios realizados.

4. **Espera revisión**: Un colaborador revisará tu PR y te dará retroalimentación si es necesario.

---

## Estilo de código

- Sigue las normas de estilo de código de [PEP 8](https://peps.python.org/pep-0008/).
- Usa docstrings para documentar funciones y clases.
- Asegúrate de que el código pase las verificaciones de linting:
  ```bash
  flake8 orbea_monegros
  ```

---

## Contacto

Si tienes alguna pregunta, no dudes en ponerte en contacto:

- Autor: Jordi Balcells Saenz
- Email: [jbalcellss@uoc.edu](mailto:jbalcellss@uoc.edu)
- Repositorio: [Orbea Monegros en GitHub](https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git)

¡Gracias por contribuir! ❤️

