# Contribuir al paquet Python d'Orbea Monegros PAC4

Gràcies pel teu interès a contribuir al projecte Orbea Monegros PAC4! La teva ajuda és fonamental per millorar i fer créixer aquest paquet. Segueix aquesta guia per contribuir de manera efectiva.

## Taula de continguts

- [Contribuir al paquet Python d'Orbea Monegros PAC4](#contribuir-al-paquet-python-dorbea-monegros-pac4)
  - [Taula de continguts](#taula-de-continguts)
  - [Com començar](#com-començar)
  - [Estructura del repositori](#estructura-del-repositori)
  - [Regles per contribuir](#regles-per-contribuir)
  - [Informar de problemes](#informar-de-problemes)
  - [Enviament de canvis (Pull Requests)](#enviament-de-canvis-pull-requests)
  - [Estil de codi](#estil-de-codi)
  - [Contacte](#contacte)

---

## Com començar

1. **Clona el repositori:**

   ```bash
   git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
   cd GCD-PCD_Pac4
   ```

2. **Crea un entorn virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # A macOS/Linux
   .\venv\Scripts\activate    # A Windows
   ```

3. **Instal·la les dependències:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Executa els tests per assegurar-te que tot funciona:**

   ```bash
   pytest tests/
   ```

---

## Estructura del repositori

- `orbea_monegros/`: Conté el codi principal del paquet.
- `tests/`: Inclou els tests unitaris.
- `data/`: Arxius de dades necessaris per a l'anàlisi.
- `README.md`: Documentació general del projecte.
- `setup.py`: Arxiu per empaquetar i distribuir el projecte.
- `CONTRIBUTING.md`: Guia per col·laborar en el projecte.
- `requirements.txt`: Dependències del projecte.

---

## Regles per contribuir

1. **Sigues respectuós**: Aquest és un espai col·laboratiu. Sigues amable i pacient amb els altres col·laboradors.
2. **Crea una branca per a la teva contribució**:

   ```bash
   git checkout -b feature/nova-funcionalitat
   ```

3. **Escriu tests per a qualsevol funcionalitat nova**.
4. **Proporciona documentació clara**: Afegeix o actualitza la documentació si introdueixes canvis significatius.

---

## Informar de problemes

Si trobes un problema o tens una suggerència, si us plau, crea un [issue a GitHub](https://github.com/jbalcellssUOC/GCD-PCD_Pac4/issues) amb:

- Una descripció detallada del problema o suggerència.
- Passos per reproduir el problema (si s'escau).
- Captures de pantalla o exemples de codi (si és rellevant).

---

## Enviament de canvis (Pull Requests)

1. **Assegura't que la teva branca està actualitzada**:

   ```bash
   git pull origin main
   ```

2. **Confirma els teus canvis i escriu missatges de commit clars**:

   ```bash
   git add .
   git commit -m "Descripció clara del canvi realitzat"
   ```

3. **Envia el teu Pull Request**:
   - Ves a la pàgina del repositori a GitHub.
   - Fes clic a "Compare & Pull Request".
   - Proporciona una descripció detallada dels canvis realitzats.

4. **Espera revisió**: Un col·laborador revisarà el teu PR i et donarà retroalimentació si és necessari.

---

## Estil de codi

- Segueix les normes d'estil de codi de [PEP 8](https://peps.python.org/pep-0008/).
- Fes servir docstrings per documentar funcions i classes.
- Assegura't que el codi passi les verificacions de linting:

  ```bash
  flake8 orbea_monegros
  ```

---

## Contacte

Si tens alguna pregunta, no dubtis a posar-te en contacte:

- Autor: Jordi Balcells Saenz
- Email: [jbalcellss@uoc.edu](mailto:jbalcellss@uoc.edu)
- Repositori: [Orbea Monegros PAC4 a GitHub](https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git)

Gràcies per contribuir! ❤️
