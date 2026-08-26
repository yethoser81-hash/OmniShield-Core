# OmniShield - Mobile Money & USSD Fraud Detector (Python Pur)
# Surveillance et verrouillage des flux financiers (OM / MoMo)

import re
import json
import hashlib
import time

class MobileMoneyGuard:
    def __init__(self):
        # Motifs suspects liés au piratage de comptes Mobile Money ou transferts non autorisés
        self.suspicious_ussd_patterns = [
            r"\*150#.*transfert",
            r"\*126#.*code",
            r"changement.*code.*pin",
            r"retrait.*force"
        ]
        print("[MOBILE MONEY GUARD] Module de protection financière initialisé.")

    def audit_transaction(self, user_id, transaction_amount, destination_number, is_active_hours=True):
        """Audite une tentative de transaction financière et applique un verrouillage si anomalie."""
        # Règle de sécurité stricte : vérification des seuils et des comportements anormaux
        MAX_AUTHORIZED_INSTANT = 500000 # Plafond de sécurité en FCFA par défaut
        
        risk_score = 0
        warnings = []

        if transaction_amount > MAX_AUTHORIZED_INSTANT:
            risk_score += 50
            warnings.append("Montant inhabituel dépassant le seuil de sécurité instantanée.")

        if not is_active_hours:
            risk_score += 30
            warnings.append("Transaction initiée à une heure anormale (Activité nocturne suspecte).")

        # Si le score de risque est élevé, on bloque et on exige une authentification forte
        if risk_score >= 40:
            security_lock = {
                "status": "TRANSACTION_BLOCKED",
                "risk_score": risk_score,
                "user": user_id,
                "action": "Exigence d'une double authentification vocale ou biométrique.",
                "warnings": warnings,
                "timestamp": int(time.time())
            }
            return json.dumps(security_lock, indent=4)
        else:
            return json.dumps({
                "status": "TRANSACTION_AUTHORIZED",
                "risk_score": risk_score,
                "user": user_id,
                "message": "Flux financier validé par le bouclier de sécurité."
            }, indent=4)

    def verify_ussd_intercept(self, ussd_string):
        """Intercepte et analyse une requête USSD exécutée sur l'appareil."""
        for pattern in self.suspicious_ussd_patterns:
            if re.search(pattern, ussd_string.lower()):
                return json.dumps({
                    "status": "USSD_INTERCEPT_ALERT",
                    "threat": "Tentative potentielle de manipulation de code USSD à distance.",
                    "action": "Exécution bloquée instantanément."
                }, indent=4)
        return json.dumps({"status": "USSD_SAFE", "action": "Allow"}, indent=4)

# Test du module de protection financière
if __name__ == "__main__":
    mm_guard = MobileMoneyGuard()
    
    # Simulation d'une tentative de gros virement suspect en pleine nuit
    print(mm_guard.audit_transaction("USER_9921", 750000, "+2376XXXXXXXX", is_active_hours=False))