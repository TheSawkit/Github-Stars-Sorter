"""
Logique de tri et de classification des repositories.
"""

from typing import Dict, List, Any
from .config import CATEGORIES, SCORE


def get_smart_category(repo: Dict[str, Any]) -> str:
    """
    Analyse le repo pour lui attribuer la meilleure catégorie.
    """
    name = str(repo.get("name") or "").lower()
    desc = str(repo.get("description") or "").lower()
    topics = repo.get("topics", [])
    lang = str(repo.get("language") or "").lower()

    text_content = f"{name} {desc} {' '.join(topics)} {lang}"

    scores = {cat: 0 for cat in CATEGORIES}

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in text_content:
                if keyword in name:
                    scores[category] += SCORE["NAME_MATCH"]
                elif keyword in topics:
                    scores[category] += SCORE["TOPIC_MATCH"]
                else:
                    scores[category] += SCORE["GENERAL_MATCH"]

    best_cat = max(scores, key=scores.get)
    return best_cat if scores[best_cat] > 0 else "Uncategorized"


def organize_by_category(repos: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Classe une liste de repos dans un dictionnaire de catégories.
    """
    print("🧠 Classification en cours...")

    organized_data = {cat: [] for cat in CATEGORIES}
    organized_data["Uncategorized"] = []

    for repo in repos:
        category = get_smart_category(repo)
        organized_data[category].append({
            "name": repo.get("name", "Unknown"),
            "url": repo.get("html_url", ""),
            "description": repo.get("description"),
            "stars": repo.get("stargazers_count", 0),
            "language": repo.get("language"),
            "topics": repo.get("topics", [])
        })

    clean_data = {}
    for category, repos in organized_data.items():
        if repos:
            clean_data[category] = repos

    return clean_data
