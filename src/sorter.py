"""
Repository sorting and classification logic.
"""

from typing import Dict, List, Any
from .config import CATEGORIES, SCORE
from .i18n import translator


def get_smart_category(repo: Dict[str, Any]) -> str:
    """
    Analyze repository to assign the best category.
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

    if all(score == 0 for score in scores.values()):
        return translator.get_text("uncategorized")

    max_category = max(scores.items(), key=lambda x: x[1])[0]
    return max_category


def organize_by_category(repos: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Classifies a repos list into a category dictionary.
    """
    print("🧠 " + translator.get_text("classification_in_progress"))

    organized_data = {cat: [] for cat in CATEGORIES}
    organized_data[translator.get_text("uncategorized")] = []

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
