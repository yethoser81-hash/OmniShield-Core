# OmniShield - Main Orchestrator & Execution Entry Point
# Fichier maître pour lancer le système de sécurité global

import sys
import os

# Ajout des sous-dossiers au chemin d'exécution Python
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core_engine.security_kernel import OmniShieldKernel
from core_engine.secure_storage import SecureVault
from ai_modules.nlp_semantic import OmniShieldAIAnalyzer
from localization.lang_manager import LanguageManager

def main():
    print("==================================================")
    print("       🛡️  LANCEMENT DU SYSTÈME OMNISHIELD  🛡️      ")
    print("==================================================")

    # 1. Initialisation du Multilinguisme
    i18n = LanguageManager(default_lang="fr")
    print(f"[INIT] Langue système : Français")

    # 2. Démarrage du Noyau de Sécurité
    kernel = OmniShieldKernel(device_id="OS-CAMEROON-MASTER-001")
    kernel.load_license_tier("Pack Intégral")

    # 3. Activation du Coffre-Fort Chiffré
    vault = SecureVault(master_key_secret="SERGES_YEMGA_MASTER_KEY")
    print("[INIT] Coffre-fort numérique prêt et sécurisé.")

    # 4. Activation de l'IA d'analyse
    ai = OmniShieldAIAnalyzer()
    print("[INIT] Moteur d'analyse sémantique et comportementale actif.")

    print("--------------------------------------------------")
    print("🟢 OMNISHIELD EST OPÉRATIONNEL SUR TOUS LES FRONTS.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()