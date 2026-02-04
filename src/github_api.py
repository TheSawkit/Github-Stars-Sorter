"""
GitHub API communication module.
"""

import requests
import time
from typing import Dict, List, Any
from .config import API_BASE_URL, REPOS_PER_PAGE, API_RATE_LIMIT_DELAY
from .i18n import translator


def user_exists(username: str, headers: Dict[str, str]) -> bool:
    """Check if user exists on GitHub."""
    url = f"{API_BASE_URL}/users/{username}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def fetch_all_starred_repos(username: str, headers: Dict[str, str]) -> List[Dict[str, Any]]:
    """
    Fetch all starred repositories for the user.
    """
    all_stars = []
    page = 1

    print(translator.get_text("fetching_stars").format(username))

    while True:
        url = f"{API_BASE_URL}/users/{username}/starred"
        params = {"page": page, "per_page": REPOS_PER_PAGE}

        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=10)

            if response.status_code == 404:
                print(translator.get_text("user_not_found_api").format(username))
                break
            elif response.status_code == 403:
                print(translator.get_text("api_rate_limit"))
                break
            elif response.status_code != 200:
                print(translator.get_text("api_error").format(response.status_code))
                break

            data = response.json()
            if not data:
                break

            all_stars.extend(data)
            print(translator.get_text("page_fetched").format(page, len(data)))
            page += 1

            time.sleep(API_RATE_LIMIT_DELAY)

        except requests.exceptions.RequestException as e:
            print(translator.get_text("connection_error").format(e))
            break

    print(translator.get_text("total_stars").format(len(all_stars)))
    return all_stars
