# Piscine Python for Data Science - Day 0

## 📌 Contexte
Ce dépôt contient mon travail pour la **Piscine Python for Data Science** de l’école 42.  
Le **Day 0** est une journée d’introduction dédiée aux bases du langage Python et aux bonnes pratiques imposées par la piscine.

- Langage : Python 3.10
- Objectif : maîtriser les fondamentaux de Python avant d’aborder la Data Science
- Méthodologie : rigueur, lisibilité, respect strict des consignes

---

## 📂 Structure du dépôt (Day 0)

├── ex00/
│ └── Hello.py
├── ex01/
│ └── format_ft_time.py
├── ex02/
│ └── find_ft_type.py
├── ex03/
│ └── NULL_not_found.py
├── ex04/
│ └── whatis.py
├── ex05/
│ └── building.py
├── ex06/
│ ├── ft_filter.py
│ └── filterstring.py
├── ex07/
│ └── sos.py
├── ex08/
│ └── Loading.py
├── ex09/
│ ├── ft_package/
│ ├── README.md
│ ├── LICENSE
│ └── pyproject.toml
└── README.md


---

## 🧠 Contenu des exercices

### ex00 - First python script
Manipulation des structures de base  
list, tuple, set, dict  
Objectif : comprendre la mutabilité et l’affichage des objets

### ex01 - First use of package
Manipulation du temps et du formatage de dates  
Introduction aux bibliothèques standard Python

### ex02 - First function python
Création d’une fonction typée  
Identification et affichage du type des objets

### ex03 - NULL not found
Détection et gestion des différentes formes de valeurs nulles en Python  
None, NaN, False, 0, chaîne vide

### ex04 - The Even and the Odd
Gestion des arguments en ligne de commande  
Contrôle des erreurs et assertions

### ex05 - First standalone program python
Programme autonome avec `main()`  
Analyse de chaînes de caractères  
Utilisation des fonctionnalités natives du langage

### ex06 - ft_filter
Recréation de la fonction `filter`  
Utilisation obligatoire de list comprehensions et lambda  
Programme de filtrage de chaînes

### ex07 - Dictionaries SoS
Encodage d’un message en Morse  
Utilisation d’un dictionnaire comme structure centrale

### ex08 - Loading
Recréation simplifiée de `tqdm`  
Utilisation du mot-clé `yield`  
Gestion de l’affichage dynamique dans le terminal

### ex09 - My first package creation
Création et publication d’un package Python installable via pip  
Découverte de la structuration d’un projet Python professionnel

---

## ⚠️ Règles importantes respectées

- Aucun code exécuté dans le scope global
- Présence obligatoire d’un `main()` dans chaque programme
- Toutes les fonctions possèdent une documentation (`__doc__`)
- Aucune variable globale
- Imports explicites uniquement
- Gestion stricte des erreurs (aucune exception non catchée)
- Respect de la norme via `flake8`

---

## 🛠️ Outils

```bash
Python 3.10
pip install flake8
alias norminette=flake8
```
