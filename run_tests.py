# OmniShield - Script de validation et de test d'intégrité avant déploiement
import os
import sys

def test_project_structure():
    print("==================================================")
    print("      🔍 LANCEMENT DES TESTS D'INTÉGRITÉ OMNISHIELD")
    print("==================================================")
    
    required_dirs = [
        "core_engine",
        "ai_modules",
        "localization",
        "enterprise_b2b",
        "frontend_client",
        "billing_gateway"
    ]
    
    missing = []
    for d in required_dirs:
        if os.path.isdir(d):
            print(f"[OK] Dossier trouvé : {d}/")
        else:
            print(f"[ERREUR] Dossier manquant : {d}/")
            missing.append(d)
            
    if missing:
        print(f"\n[ÉCHEC] Il manque {len(missing)} dossier(s) structurel(s).")
        sys.exit(1)
    else:
        print("\n[SUCCÈS] Toute l'arborescence technique est validée et conforme au cahier des charges.")
        print("==================================================")

if __name__ == "__main__":
    test_project_structure()