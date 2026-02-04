from typing import Dict
from src import github_api, sorter, exporters, config
from src.i18n import translator


def setup_config() -> tuple[str, Dict[str, str]]:
    """Configure user and headers (Token)."""
    print(translator.get_text("welcome"))
    print(translator.get_text("separator"))

    username = ""
    headers = {"Accept": "application/vnd.github.v3+json"}

    use_token = input(translator.get_text("use_token_prompt")).lower()
    if use_token == 'y':
        token = input(translator.get_text("enter_token")).strip()
        headers["Authorization"] = f"token {token}"
        print(translator.get_text("token_configured"))

    while True:
        username = input(translator.get_text("enter_username")).strip()
        if not username:
            continue

        print(translator.get_text("checking_user").format(username))
        if github_api.user_exists(username, headers):
            print(translator.get_text("user_validated").format(username))
            break
        else:
            print(translator.get_text("user_not_found").format(username))

    print(translator.get_text("separator") + "\n")
    return username, headers


def main():
    """Starting the sorting process."""
    try:
        username, headers = setup_config()

        stars = github_api.fetch_all_starred_repos(username, headers)
        if not stars:
            return

        sorted_data = sorter.organize_by_category(stars)

        exporters.save_to_json(sorted_data)
        exporters.save_to_md(sorted_data, config.MD_FILENAME, username)

        print(translator.get_text("process_complete").format(username))

    except KeyboardInterrupt:
        print("\n👋 À plus !")
    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    main()
