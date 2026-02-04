# 🌟 GitHub Stars Sorter

[![Python](https://img.shields.io/badge/Python-3.14%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/license-MIT-darkgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub stars](https://img.shields.io/github/stars/TheSawkit/Github-Stars-Sorter?style=social)](https://github.com/TheSawkit/Github-Stars-Sorter)

[🇺🇸 English](#english) | [🇫🇷 Français](#français)

---

`<a name="english"></a>`

## 🇬🇧 English

Automatically organize your starred GitHub repositories into smart categories.

This script analyzes the name, description, and tags of your stars to classify them into an elegant catalog and an exploitable JSON file.

### 🚀 Key Features

- 🧠 **Smart Classification**: Scoring system based on thematic keywords.
- 📁 **Multi-format Export**: Generates a `README.md` (your catalog) and `github_stars_sorted.json`.
- 📊 **Console Summary**: Displays a statistical overview of your collection.
- 🛠 **Interactive**: No need to modify the code, the script asks you everything at startup.

### 📦 Getting Started

1. Clone this repository or download the script.
2. Install the required library:

   ```bash
   pip install requests
   ```

### 🛠 How to Use

1. Simply run the script:

   ```bash
   python main.py
   ```
2. Follow the on-screen instructions:

   - Enter your GitHub **username**.
   - Choose whether you want to use a **Token** (recommended to avoid being rate-limited by GitHub).

### 📂 Output Files

Generated files are located in the `exports/` folder:

- `README.md`: Your starred catalog, ready to be shared.
- `github_stars_sorted.json`: Your structured data.

### ✨ Sample Catalog

The generated catalog looks like this:

- Automatic table of contents.
- Tables sorted by stars (descending).
- Direct links and cleaned descriptions.

---

`<a name="français"></a>`

## 🇫🇷 Français

Organisez automatiquement vos repositories « starred » sur GitHub par catégories intelligentes.

Ce script analyse le nom, la description et les tags de vos étoiles pour les classer dans un catalogue élégant et un fichier JSON exploitable.

### 🚀 Fonctionnalités Clés

- 🧠 **Classification Intelligente** : Système de scoring basé sur des mots-clés thématiques.
- 📁 **Export Multi-format** : Génère un `README.md` (votre catalogue) et un `mes_stars_github_triees.json`.
- 📊 **Résumé Console** : Affiche un aperçu statistique de votre collection.
- 🛠 **Interactif** : Plus besoin de modifier le code, le script vous demande tout au démarrage.

### 📦 Premiers Pas

1. Clonez ce dépôt ou téléchargez le script.
2. Installez la bibliothèque nécessaire :

   ```bash
   pip install requests
   ```

### 🛠 Comment Utiliser

1. Lancez simplement le script :

   ```bash
   python main.py
   ```
2. Suivez les instructions à l'écran :

   - Entrez votre **nom d'utilisateur** GitHub.
   - Choisissez si vous voulez utiliser un **Token** (recommandé pour ne pas être bridé par GitHub).

### 📂 Fichiers Générés

Les fichiers générés se trouvent dans le dossier `exports/` :

- `README.md` : Votre catalogue étoilé, prêt à être partagé.
- `mes_stars_github_triees.json` : Vos données structurées.

### ✨ Exemple de Catalogue (Français)

Le catalogue généré ressemble à ceci :

- Table des matières automatique.
- Tableaux classés par étoiles (décroissant).
- Liens directs et descriptions nettoyées.

---

_Fait avec ❤️ par [SAWKIT](https://github.com/TheSawkit)_
