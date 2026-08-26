# OmniShield - Enterprise Whale Guard (Python Pur)
# Détection des fraudes au président, usurpations d'identité et ordres de virement suspects (B2B)

import time
import json
import re

class WhaleGuard:
    def __init__(self, enterprise_id):
        self.enterprise_id = enterprise_id
        # Mots-clés critiques liés à l'ingénierie sociale ciblée sur les entreprises (Whaling)
        self.whaling_keywords = [
            r"virement.*confidentiel",
            r"cession.*urgente",
            r"contrôle fiscal.*discrétion",
            r"ne parlez à personne.*projet",
            r"changer.*coordonnées bancaires"
        ]
        print(f"[WHALE GUARD] Bouclier anti-fraude B2B initialisé pour l'entreprise : {enterprise_id}")

    def audit_executive_communication(self, sender_name, sender_role, message_content, requested_amount=0):
        """Analyse un message ou un ordre provenant prétendument d'un dirigeant pour déceler une usurpation."""
        content_lower = message_content.lower()
        threat_score = 0
        triggered_rules = []

        # Analyse sémantique des motifs de fraude au président
        for pattern in self.whaling_keywords:
            if re.search(pattern, content_lower):
                threat_score += 40
                triggered_rules.append(pattern)

        # Si le montant demandé est élevé, on augmente le niveau de vigilance
        if requested_amount > 1000000:  # Seuil de 1 million de FCFA par exemple
            threat_score += 30
            triggered_rules.append("HIGH_VALUE_TRANSFER_REQUEST")

        if threat_score >= 40:
            alert_report = {
                "status": "WHALING_ATTACK_DETECTED",
                "risk_level": "CRITICAL_B2B",
                "enterprise": self.enterprise_id,
                "impersonated_sender": f"{sender_name} ({sender_role})",
                "threat_score": threat_score,
                "triggered_rules": triggered_rules,
                "action": "BLOCAGE IMMÉDIAT ET ALERTE DU COMEX / DIRECTION DE LA SÉCURITÉ",
                "timestamp": int(time.time()),
                "message": "Tentative potentielle de fraude au président interceptée. Double validation physique obligatoire."
            }
            return json.dumps(alert_report, indent=4)
        else:
            return json.dumps({
                "status": "COMMUNICATION_AUTHENTICATED",
                "enterprise": self.enterprise_id,
                "sender": sender_name,
                "message": "Aucune anomalie comportementale ou sémantique détectée."
            }, indent=4)

# Test du module B2B Anti-Whaling
if __name__ == "__main__":
    guard = WhaleGuard(enterprise_id="ETS-YEMGA-B2B-01")
    
    # Simulation d'un faux ordre de virement urgent envoyé au comptable
    fake_ceo_message = guard.audit_executive_communication(
        sender_name="PDG Directeur Général",
        sender_role="CEO",
        message_content="Bonjour, effectuez un virement confidentiel et urgent pour cette acquisition, ne parlez à personne de ce projet.",
        requested_amount=5500000
    )
    print(fake_ceo_message)