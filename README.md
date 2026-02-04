# 🌟 GitHub Stars Sorter

Organisez automatiquement vos repositories « starred » sur GitHub par catégories intelligentes.

Ce script analyse le nom, la description et les tags de vos étoiles pour les classer dans un catalogue élégant et un fichier JSON exploitable.

## 🚀 Fonctionnalités

- 🧠 **Classification Intelligente** : Système de scoring basé sur des mots-clés thématiques.
- 📁 **Export Multi-format** : Génère un `README.md` (votre catalogue) et un `mes_stars_github_triees.json`.
- 📊 **Résumé Console** : Affiche un aperçu statistique de votre collection.
- 🛠 **Interactif** : Plus besoin de modifier le code, le script vous demande tout au démarrage.

## 📦 Installation

1. Clonez ce dépôt ou téléchargez le script.
2. Installez la bibliothèque nécessaire :

   ```bash
   pip install requests
   ```

## 🛠 Usage

1. Lancez simplement le script :

   ```bash
   python main.py
   ```

2. Suivez les instructions à l'écran :
   - Entrez votre **nom d'utilisateur** GitHub.
   - Choisissez si vous voulez utiliser un **Token** (recommandé pour ne pas être bridé par GitHub).

## 📂 Résultats

Les fichiers générés se trouvent dans le dossier `exports/` :

- `README.md` : Votre catalogue étoilé, prêt à être partagé.
- `mes_stars_github_triees.json` : Vos données structurées.

## ✨ Exemple de Catalogue

Le catalogue généré ressemble à ceci :

- Table des matières automatique.
- Tableaux classés par étoiles (décroissant).
- Liens directs et descriptions nettoyées.

---

_Fait avec ❤️ par [SAWKIT](https://github.com/TheSawkit)_
