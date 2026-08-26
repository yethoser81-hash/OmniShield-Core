# OmniShield - Global Threat Blacklist (Python Pur)
# Gestion décentralisée et chiffrée des listes noires de menaces

import json
import hashlib
import time

class GlobalBlacklist:
    def __init__(self):
        # Base de données locale en mémoire (simulant un stockage chiffré)
        self.blacklist_db = {
            "phishing_domains": ["bit.ly/fake-momo", "whatsapp-verify-secure.cm"],
            "fraudulent_numbers": ["+237699999999", "+237677777777"],
            "malware_signatures": ["e3b0c44298fc1c149afbf4c8996fb924"]
        }
        print("[GLOBAL BLACKLIST] Base de données souveraine des menaces initialisée.")

    def check_threat(self, indicator, indicator_type):
        """Vérifie si un numéro, un domaine ou une signature est présent sur liste noire."""
        is_blacklisted = False
        
        if indicator_type == "domain" and indicator in self.blacklist_db["phishing_domains"]:
            is_blacklisted = True
        elif indicator_type == "phone" and indicator in self.blacklist_db["fraudulent_numbers"]:
            is_blacklisted = True
        elif indicator_type == "signature" and indicator in self.blacklist_db["malware_signatures"]:
            is_blacklisted = True

        if is_blacklisted:
            return json.dumps({
                "status": "THREAT_MATCHED",
                "indicator": indicator,
                "type": indicator_type,
                "action": "BLOCK_INSTANTLY",
                "timestamp": int(time.time())
            }, indent=4)
        else:
            return json.dumps({
                "status": "CLEAN",
                "indicator": indicator,
                "action": "ALLOW"
            }, indent=4)

    def add_to_blacklist(self, indicator, indicator_type):
        """Ajoute dynamiquement une nouvelle menace détectée à la liste noire."""
        if indicator_type == "domain":
            self.blacklist_db["phishing_domains"].append(indicator)
        elif indicator_type == "phone":
            self.blacklist_db["fraudulent_numbers"].append(indicator)
        
        return json.dumps({"status": "SUCCESS", "message": f"Menace ajoutée à la base globale : {indicator}"}, indent=4)

if __name__ == "__main__":
    bl = GlobalBlacklist()
    print(bl.check_threat("+237699999999", "phone"))