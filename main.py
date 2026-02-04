from typing import Dict
from src import github_api, sorter, exporters, config


def setup_config() -> tuple[str, Dict[str, str]]:
    """Configure l'utilisateur et les headers (Token)."""
    print("👋 Bienvenue dans GitHub Stars Sorter !")
    print("-" * 40)

    username = ""
    headers = {"Accept": "application/vnd.github.v3+json"}

    use_token = input("🔑 Utiliser un GitHub Token ? [y/N] : ").lower()
    if use_token == 'y':
        token = input("👉 Entre ton token : ").strip()
        headers["Authorization"] = f"token {token}"
        print("✅ Token configuré.")

    while True:
        username = input("\n👤 Entre ton nom d'utilisateur GitHub : ").strip()
        if not username:
            continue

        print(f"🔍 Vérification de '{username}'...")
        if github_api.user_exists(username, headers):
            print(f"✅ Utilisateur '{username}' validé.")
            break
        else:
            print(
                f"❌ L'utilisateur '{username}' n'existe pas ou l'API est inaccessible. Réessaie.")

    print("-" * 40 + "\n")
    return username, headers


def main():
    """Lancement du processus de tri."""
    try:
        username, headers = setup_config()

        stars = github_api.fetch_all_starred_repos(username, headers)
        if not stars:
            return

        sorted_data = sorter.organize_by_category(stars)

        exporters.save_to_json(sorted_data, config.JSON_FILENAME)
        exporters.save_to_md(sorted_data, config.MD_FILENAME, username)

        print(f"\n✅ Terminé avec succès pour {username} !")

    except KeyboardInterrupt:
        print("\n👋 À plus !")
    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    main()
