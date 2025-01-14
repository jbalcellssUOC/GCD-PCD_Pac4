# Instal·lació del Paquet Orbea Monegros PAC4

Aquest document descriu els passos necessaris per instal·lar i configurar el paquet **Orbea Monegros PAC4** al teu entorn de desenvolupament o producció.

---

## Requisits previs

Assegura't de complir amb els següents requisits abans de procedir:

1. **Python 3.10 o superior** instal·lat. Pots verificar la teva versió amb:
   ```bash
   python --version
   ```

2. **pip** (el gestor de paquets de Python) instal·lat. Pots verificar-ho amb:
   ```bash
   pip --version
   ```

3. Opcionalment, instal·la **virtualenv** per crear un entorn virtual:
   ```bash
   pip install virtualenv
   ```

4. Accés al repositori del projecte a GitHub:
   [https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git](https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git)

---

## Instal·lació

### 1. Clonar el repositori

Primer, clona el repositori del projecte des de GitHub:

```bash
git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
cd GCD-PCD_Pac4
```

### 2. Crear un entorn virtual (recomanat)

Per evitar conflictes entre dependències, es recomana utilitzar un entorn virtual:

```bash
python -m venv venv
```

Activa l'entorn virtual:
- A macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- A Windows:
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Instal·lar les dependències

Un cop dins de l'entorn virtual, instal·la les dependències necessàries:

```bash
pip install -r requirements.txt
```

### 4. Instal·lar el paquet en mode editable

Per treballar amb el paquet en desenvolupament, instal·la'l en mode editable:

```bash
pip install -e .
```

---

## Execució de proves

Per assegurar-te que tot funciona correctament, executa els tests inclosos:

```bash
pytest tests/
```

---

## Ús del paquet

Després de la instal·lació, pots utilitzar el paquet des de qualsevol script o directament des de la línia de comandes:

### Importar en un script:

```python
from orbea_monegros import main
main()
```

### Comanda al terminal:

Si vas definir un script executable a `setup.py`, executa:

```bash
orbea-analysis
```

---

## Desinstal·lació

Per desinstal·lar el paquet, simplement executa:

```bash
pip uninstall orbea-monegros
```

Si vols eliminar també l'entorn virtual, simplement elimina la carpeta `venv/`:

```bash
rm -rf venv  # A macOS/Linux
del venv     # A Windows
```

---

Ja està! Ara pots utilitzar i desenvolupar amb el paquet **Orbea Monegros PAC4**.
