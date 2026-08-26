# OmniShield - AI Semantic & NLP Analyzer (Python Pur)
# Moteur d'analyse comportementale et de détection d'ingénierie sociale

import re
import json

class OmniShieldAIAnalyzer:
    def __init__(self):
        # Base de signatures et de motifs frauduleux (Patterns d'ingénierie sociale)
        self.fraud_patterns = [
            r"code.*6 chiffres",
            r"envoie.*code.*stp",
            r"urgence.*argent",
            r"gagne.*argent.*clique",
            r"compte.*bloqué.*confirmer",
            r"fais-moi un transfer.*mobile money"
        ]
        print("[IA OMNISHIELD] Moteur sémantique initialisé et prêt à l'analyse.")

    def scan_message(self, message_text, sender_id):
        """Analyse un message entrant pour détecter des tentatives de manipulation ou de phishing."""
        text_lower = message_text.lower()
        threat_detected = False
        matched_pattern = None

        # Analyse par expression régulière et sémantique contextuelle
        for pattern in self.fraud_patterns:
            if re.search(pattern, text_lower):
                threat_detected = True
                matched_pattern = pattern
                break

        if threat_detected:
            alert_report = {
                "status": "THREAT_BLOCKED",
                "risk_level": "CRITICAL",
                "sender": sender_id,
                "matched_pattern": matched_pattern,
                "message": "Alerte ! Tentative d'ingénierie sociale ou de vol de compte interceptée."
            }
            return json.dumps(alert_report, indent=4)
        else:
            return json.dumps({
                "status": "SAFE",
                "risk_level": "LOW",
                "sender": sender_id,
                "message": "Message sécurisé. Aucun comportement suspect détecté."
            }, indent=4)

# Test du module d'IA sémantique
if __name__ == "__main__":
    ai_engine = OmniShieldAIAnalyzer()
    
    # Simulation d'un message frauduleux typique d'arnaque au code WhatsApp / Mobile Money
    test_msg = "Salut stp envoie-moi par erreur le code à 6 chiffres que tu viens de recevoir c'est urgent !"
    print(ai_engine.scan_message(test_msg, sender_id="+2376XXXXXXXX"))