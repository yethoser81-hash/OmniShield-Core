# OmniShield - Localization & Multilingual Manager (Python Pur)
# Gestion des langues pour l'expansion internationale (Afrique & Occident)

import json

class LanguageManager:
    def __init__(self, default_lang="fr"):
        self.current_lang = default_lang
        # Dictionnaires intégrés pour la démonstration souveraine
        self.translations = {
            "fr": {
                "status_active": "Essai 30 Jours Actif",
                "shield_title": "État des Boucliers de Sécurité",
                "scan_btn": "Lancer un audit de sécurité",
                "trap_btn": "Armer le piège d'urgence"
            },
            "en": {
                "status_active": "30-Day Trial Active",
                "shield_title": "Security Shield Status",
                "scan_btn": "Run Security Audit",
                "trap_btn": "Arm Emergency Trap"
            },
            "es": {
                "status_active": "Prueba de 30 días activa",
                "shield_title": "Estado de los Escudos de Seguridad",
                "scan_btn": "Ejecutar auditoría de seguridad",
                "trap_btn": "Armar trampa de emergencia"
            }
        }
        print(f"[I18N] Module multilingue initialisé. Langue par défaut : {default_lang}")

    def set_language(self, lang_code):
        """Modifie la langue active de l'application."""
        if lang_code in self.translations:
            self.current_lang = lang_code
            return json.dumps({"status": "SUCCESS", "lang": lang_code}, indent=4)
        return json.dumps({"status": "ERROR", "message": "Langue non supportée."}, indent=4)

    def get_text(self, key):
        """Récupère le texte traduit selon la langue active."""
        lang_dict = self.translations.get(self.current_lang, self.translations["fr"])
        return lang_dict.get(key, key)

# Test du module multilingue
if __name__ == "__main__":
    i18n = LanguageManager(default_lang="fr")
    print("FR :", i18n.get_text("shield_title"))
    
    i18n.set_language("en")
    print("EN :", i18n.get_text("shield_title"))