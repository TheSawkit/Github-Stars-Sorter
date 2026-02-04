"""
Manages folder creation and JSON/Markdown exports.
"""

import json
import time
from pathlib import Path
from typing import Dict, List, Any
from .config import OUTPUT_DIR, FRENCH_JSON_FILENAME, ENGLISH_JSON_FILENAME
from .i18n import translator


def ensure_output_dir():
    """Create export directory if it doesn't exist."""
    Path(OUTPUT_DIR).mkdir(exist_ok=True)


def get_json_filename():
    """Returns the appropriate JSON filename based on the current language."""
    if translator.is_french():
        return FRENCH_JSON_FILENAME
    else:
        return ENGLISH_JSON_FILENAME


def save_to_json(data: Dict[str, List[Dict[str, Any]]], filename: str | None = None):
    """Save data in JSON format."""
    if filename is None:
        filename = get_json_filename()

    if not isinstance(filename, str):
        raise TypeError("Filename must be a string.")

    ensure_output_dir()
    path = Path(OUTPUT_DIR) / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(translator.get_text("json_saved").format(path))


def save_to_md(data: Dict[str, List[Dict[str, Any]]], filename: str, username: str):
    """Generate the README.md catalog."""
    ensure_output_dir()
    path = Path(OUTPUT_DIR) / filename

    profile_url = f"https://github.com/{username}"

    if translator.is_french():
        catalog_subtitle = "> Une collection organisée de mes découvertes, outils et ressources favoris sur GitHub."
        summary_title = "## 📊 Sommaire"
        no_description = "_Pas de description_"
        back_to_top = "[↑ Retour](#-sommaire)"
        generated_text = f"*Généré pour [{username}]({profile_url}) le {time.strftime('%Y-%m-%d')}, avec [GitHub Stars Sorter](https://github.com/TheSawkit/Github-Stars-Sorter) codé avec ❤️ par [SAWKIT](https://github.com/TheSawkit).*"
    else:
        catalog_subtitle = "> An organized collection of my favorite discoveries, tools and resources on GitHub."
        summary_title = "## 📊 Summary"
        no_description = "_No description_"
        back_to_top = "[↑ Back to Top](#-summary)"
        generated_text = f"*Generated for [{username}]({profile_url}) on {time.strftime('%Y-%m-%d')}, with [GitHub Stars Sorter](https://github.com/TheSawkit/Github-Stars-Sorter) coded with ❤️ by [SAWKIT](https://github.com/TheSawkit).*"

    lines = [
        f"# ✨ GitHub Stars - [{username}]({profile_url})",
        translator.get_text("last_sync_badge").format("TheSawkit", "Github-Stars-Sorter"),
        "",
        catalog_subtitle,
        "",
        summary_title,
    ]

    # Summary
    for cat in sorted(data.keys()):
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("--", "-")
        translated_cat = translator.get_category_name(cat) or cat
        lines.append(f"- [{translated_cat}](#{anchor}) ({len(data[cat])})")

    # Details
    for cat in sorted(data.keys()):
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("--", "-")
        translated_cat = translator.get_category_name(cat) or cat
        lines.append(f"\n## {translated_cat}")
        if translator.is_french():
            lines.append("| Projet | Description | ⭐ | Langage |")
            lines.append("| :--- | :--- | :---: | :---: |")
        else:
            lines.append("| Project | Description | ⭐ | Language |")
            lines.append("| :--- | :--- | :---: | :---: |")

        repos = sorted(data[cat], key=lambda x: x["stars"], reverse=True)
        for r in repos:
            name_link = f"[{r['name']}]({r['url']})"
            desc = (r['description'] or no_description).replace(
                "|", "\\|").replace("\n", " ")
            lines.append(
                f"| {name_link} | {desc} | {r['stars']} | `{r['language'] or '-'}` |")

        lines.append(f"\n{back_to_top}")

    lines.append(f"\n---\n{generated_text}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(translator.get_text("readme_generated").format(path))
