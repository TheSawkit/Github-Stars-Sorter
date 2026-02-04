"""
Internationalization module.
Handles translations between French and English based on system locale.
"""

import locale


class Translator:
    """Handles translation between French and English."""

    def __init__(self):
        """Initialize translator with translations dictionary."""
        self.translations = {
            "en": {
                # Main.py translations
                "welcome": "👋 Welcome to GitHub Stars Sorter!",
                "separator": "-" * 40,
                "use_token_prompt": "🔑 Use GitHub Token? [y/N]: ",
                "enter_token": "👉 Enter your token: ",
                "token_configured": "✅ Token configured.",
                "enter_username": "\n👤 Enter your GitHub username: ",
                "checking_user": "🔍 Checking '{}'...",
                "user_validated": "✅ User '{}' validated.",
                "user_not_found": "❌ User '{}' does not exist or API is unreachable. Try again.",
                "process_complete": "\n✅ Successfully completed for {}!",
                "classification_in_progress": "Classification in progress...",
                "user_not_found_api": "❌ User '{}' not found.",
                "api_rate_limit": "❌ API rate limit reached. Use a token to continue.",
                "api_error": "❌ API Error: {}",
                "page_fetched": "✅ Page {} fetched ({} repos)...",
                "connection_error": "❌ Connection error: {}",
                "total_stars": "📦 Total: {} stars.",
                "readme_generated": "📝 README generated: {}",

                # GitHub API translations
                "fetching_stars": "🚀 Fetching stars for {}...",

                # Exporters translations
                "json_saved": "✨ JSON saved: {}",
                "catalog_title": "# ✨ GitHub Stars - [{}]({})",
                "catalog_subtitle": "> An organized collection of my favorite discoveries, tools and resources on GitHub.",
                "summary_title": "## 📊 Summary",
                "last_sync_badge": "![GitHub last commit](https://img.shields.io/github/last-commit/{}/{}?label=Last%20Sync&style=flat-square)",

                # Categories translations
                "categories": {
                    "Languages & Frameworks": "Languages & Frameworks",
                    "I.A & Data Science": "AI & Data Science",
                    "DevOps & Cloud": "DevOps & Cloud",
                    "Security & Privacy": "Security & Privacy",
                    "Web Tools & Design": "Web Tools & Design",
                    "Systems & OS": "Systems & OS",
                    "Hardware & IoT": "Hardware & IoT",
                    "Networking": "Networking",
                    "Gaming & Media": "Gaming & Media",
                    "Education & Guides": "Education & Guides",
                    "Tools & Utilities": "Tools & Utilities"
                },

                # Sorter translations
                "uncategorized": "Uncategorized"
            },
            "fr": {
                # Main.py translations
                "welcome": "👋 Bienvenue dans GitHub Stars Sorter !",
                "separator": "-" * 40,
                "use_token_prompt": "🔑 Utiliser un GitHub Token ? [y/N] : ",
                "enter_token": "👉 Entre ton token : ",
                "token_configured": "✅ Token configuré.",
                "enter_username": "\n👤 Entre ton nom d'utilisateur GitHub : ",
                "checking_user": "🔍 Vérification de '{}'...",
                "user_validated": "✅ Utilisateur '{}' validé.",
                "user_not_found": "❌ L'utilisateur '{}' n'existe pas ou l'API est inaccessible. Réessaie.",
                "process_complete": "\n✅ Terminé avec succès pour {} !",
                "classification_in_progress": "Classification en cours...",
                "user_not_found_api": "❌ Utilisateur '{}' introuvable.",
                "api_rate_limit": "❌ Limite API atteinte. Utilise un token pour continuer.",
                "api_error": "❌ Erreur API: {}",
                "page_fetched": "✅ Page {} récupérée ({} repos)...",
                "connection_error": "❌ Erreur de connexion: {}",
                "total_stars": "📦 Total : {} étoiles.",
                "readme_generated": "📝 README généré: {}",

                # GitHub API translations
                "fetching_stars": "🚀 Récupération des stars pour {}...",

                # Exporters translations
                "json_saved": "✨ JSON sauvegardé: {}",
                "catalog_title": "# ✨ GitHub Stars - [{}]({})",
                "catalog_subtitle": "> Une collection organisée de mes découvertes, outils et ressources favoris sur GitHub.",
                "summary_title": "## 📊 Sommaire",
                "last_sync_badge": "![GitHub last commit](https://img.shields.io/github/last-commit/{}/{}?label=Last%20Sync&style=flat-square)",

                # Categories translations
                "categories": {
                    "Languages & Frameworks": "Languages & Frameworks",
                    "I.A & Data Science": "I.A & Data Science",
                    "DevOps & Cloud": "DevOps & Cloud",
                    "Security & Privacy": "Security & Privacy",
                    "Web Tools & Design": "Web Tools & Design",
                    "Systems & OS": "Systems & OS",
                    "Hardware & IoT": "Hardware & IoT",
                    "Networking": "Networking",
                    "Gaming & Media": "Gaming & Media",
                    "Education & Guides": "Education & Guides",
                    "Tools & Utilities": "Tools & Utilities"
                },
                # Sorter translations
                "uncategorized": "Non classé"
            }
        }

        self.current_lang = self._detect_language()

    def _detect_language(self) -> str:
        """
        Detect system language.
        Returns 'fr' for French, 'en' for others.
        """
        try:
            loc = locale.getdefaultlocale()
            if loc and len(loc) > 0 and loc[0]:
                if 'fr' in loc[0].lower():
                    return 'fr'
                else:
                    return 'en'
            else:
                return 'en'
        except:
            return 'en'

    def get_text(self, key: str) -> str:
        """
        Get translated text for the current language.

        Args:
            key: Translation key

        Returns:
            Translated text
        """
        return self.translations[self.current_lang].get(key, key)

    def get_category_name(self, category_key: str) -> str:
        """
        Get translated category name.

        Args:
            category_key: Category key

        Returns:
            Translated category name
        """
        categories = self.translations[self.current_lang].get("categories", {})
        return categories.get(category_key, category_key)

    def is_french(self) -> bool:
        return self.current_lang == 'fr'


translator = Translator()