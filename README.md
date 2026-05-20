# Classic AI Problems in Python

Repository-ul acesta contine mai multe mini-proiecte de inteligenta artificiala implementate in Python.

Proiectele acestea sunt realizate pentru a exersa concepte precum reprezentarea starilor, generarea succesorilor, cautarea in spatiul starilor, cautarea euristica precum si luarea deciziilor in jocuri.

## Proiecte incluse

### 1.Problema misionarilor si canibalilor

Proiectul acesta rezolva problema clasica a misionarilor si canibalilor folosind algoritmi de cautare.

Scopul este transportarea tuturor misionarilor si canibalilor de pe un mal pe celalalt, respectand conditia ca misionarii sa nu fie niciodata depasiti numeric de canibali pe niciun mal.

Algoritmii folositi:
- BFS
- A*

Concepte utilizate:

- reprezentarea unei stari
- verificarea starilor valide
- generarea succesorilor
- cautare neinformata
- cautare informata
- reconstructia drumului solutiei

### 2. Jocul X si 0 cu AI

Acest proiect implementeaza jocul X si 0 in terminal,unde utilizatorul joaca impotriva unui AI.

AI-ul alege mutarile folosind algoritmul Minimax, impreuna cu Alpha-Beta pruning si memoizare.

Algoritmii si conceptele folosite in proiect:

- Minimax
- Alpha-Beta pruning
- memoizare
- generarea mutarilor posibile
- evaluarea starilor finale
- alegerea mutarii optime

### 3.8-Puzzle

Proiectul rezolva problema 8-Puzzle,o problema clasica de cautare.

Scopul este transformarea unei configuratii initiale intr-o configuratie finala, prin mutari valide ale pieselor.

Concepte utilizate:

- reprezentarea starilor
- generarea mutarilor valide
- cautare in spatiul starilor
- functie euristica
- reconstructia drumului solutiei

## Tehnologiile folosite
- Python
- Algoritmul BFS
- Algoritmul A*
- Minimax
- Alpha-Beta pruning
- reprezentarea starilor
- algoritmi de cautare

## Cum se ruleaza

Fiecare proiect se afla intr-un folder separat.

Pentrua rula un proiect, intra in folderul corespunzator si ruleaza fisierul `main.py`.

Exemplu:
```bash
python main.py
