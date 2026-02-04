"""
Module de communication avec l'API GitHub.
"""

import requests
import time
from typing import Dict, List, Any
from .config import API_BASE_URL, REPOS_PER_PAGE, API_RATE_LIMIT_DELAY


def user_exists(username: str, headers: Dict[str, str]) -> bool:
    """Vérifie si l'utilisateur existe sur GitHub."""
    url = f"{API_BASE_URL}/users/{username}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def fetch_all_starred_repos(username: str, headers: Dict[str, str]) -> List[Dict[str, Any]]:
    """
    Récupère tous les dépôts étoilés de l'utilisateur.
    """
    all_stars = []
    page = 1

    print(f"🚀 Récupération des stars pour {username}...")

    while True:
        url = f"{API_BASE_URL}/users/{username}/starred"
        params = {"page": page, "per_page": REPOS_PER_PAGE}

        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=10)

            if response.status_code == 404:
                print(f"❌ Utilisateur '{username}' introuvable.")
                break
            elif response.status_code == 403:
                print("❌ Limite API atteinte. Utilise un token pour continuer.")
                break
            elif response.status_code != 200:
                print(f"❌ Erreur API: {response.status_code}")
                break

            data = response.json()
            if not data:
                break

            all_stars.extend(data)
            print(f"✅ Page {page} récupérée ({len(data)} repos)...")
            page += 1

            time.sleep(API_RATE_LIMIT_DELAY)

        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de connexion: {e}")
            break

    print(f"📦 Total : {len(all_stars)} étoiles.")
    return all_stars
