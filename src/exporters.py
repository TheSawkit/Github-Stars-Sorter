"""
Gestion de la création des dossiers et des exports JSON/Markdown.
"""

import json
import time
from pathlib import Path
from typing import Dict, List, Any
from .config import OUTPUT_DIR


def ensure_output_dir():
    """Crée le dossier d'export s'il n'existe pas."""
    Path(OUTPUT_DIR).mkdir(exist_ok=True)


def save_to_json(data: Dict[str, List[Dict[str, Any]]], filename: str):
    """Sauvegarde les données au format JSON."""
    ensure_output_dir()
    path = Path(OUTPUT_DIR) / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✨ JSON sauvegardé: {path}")


def save_to_md(data: Dict[str, List[Dict[str, Any]]], filename: str, username: str):
    """Génère le catalogue README.md."""
    ensure_output_dir()
    path = Path(OUTPUT_DIR) / filename

    profile_url = f"https://github.com/{username}"

    lines = [
        f"# ✨ GitHub Stars - [{username}]({profile_url})",
        "![GitHub last commit](https://img.shields.io/github/last-commit/TheSawkit/Github-Stars-Sorter?label=Last%20Sync&style=flat-square)",
        "",
        "> Une collection organisée de mes découvertes, outils et ressources favoris sur GitHub.",
        "",
        "## 📊 Sommaire",
    ]

    # Sommaire
    for cat in sorted(data.keys()):
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("--", "-")
        lines.append(f"- [{cat}](#{anchor}) ({len(data[cat])})")

    # Détails
    for cat in sorted(data.keys()):
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("--", "-")
        lines.append(f"\n## {cat}")
        lines.append("| Projet | Description | ⭐ | Langage |")
        lines.append("| :--- | :--- | :---: | :---: |")

        repos = sorted(data[cat], key=lambda x: x["stars"], reverse=True)
        for r in repos:
            name_link = f"[{r['name']}]({r['url']})"
            desc = (r['description'] or "_Pas de description_").replace(
                "|", "\\|").replace("\n", " ")
            lines.append(
                f"| {name_link} | {desc} | {r['stars']} | `{r['language'] or '-'}` |")

        lines.append("\n[↑ Retour](#-sommaire)")

    lines.append(
        f"\n---\n*Généré pour [{username}]({profile_url}) le {time.strftime('%Y-%m-%d')}, avec [GitHub Stars Sorter](https://github.com/TheSawkit/Github-Stars-Sorter) codé avec ❤️ par [SAWKIT](https://github.com/TheSawkit).*")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"📝 README généré: {path}")
