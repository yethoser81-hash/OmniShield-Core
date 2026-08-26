# OmniShield - Intercept Hook & Notification Monitor (Python Pur)
# Surveillance et interception en temps réel des flux de notifications et d'appels

import time
import json
import re

class InterceptHook:
    def __init__(self, device_id):
        self.device_id = device_id
        self.is_monitoring = True
        # Motifs de phishing et d'attaques par notification courantes
        self.phishing_url_patterns = [
            r"bit\.ly\/",
            r"tinyurl\.com\/",
            r"whatsapp-verify\..*",
            r"momo-claim\..*",
            r"orange-bonus\..*"
        ]
        print(f"[INTERCEPT HOOK] Module d'interception active initialisé pour : {device_id}")

    def hook_incoming_notification(self, app_source, notification_title, notification_body):
        """Intercepte toute notification entrante (WhatsApp, SMS, Messenger, Email) et l'analyse."""
        if not self.is_monitoring:
            return json.dumps({"status": "MONITORING_OFF", "action": "Bypass"})

        full_content = f"{notification_title} {notification_body}".lower()
        threat_detected = False
        matched_threat = None

        # Analyse instantanée des liens malveillants ou des mots-clés d'arnaque
        for pattern in self.phishing_url_patterns:
            if re.search(pattern, full_content):
                threat_detected = True
                matched_threat = pattern
                break

        if threat_detected:
            intercept_report = {
                "status": "NOTIFICATION_INTERCEPTED",
                "risk_level": "CRITICAL",
                "source_app": app_source,
                "threat_pattern": matched_threat,
                "action": "NOTIFICATION BLOQUÉE & MISE EN QUARANTAINE",
                "timestamp": int(time.time()),
                "warning": "Tentative d'attaque par lien piégé ou fausse alerte interceptée."
            }
            print(f"[ALERTE INTERCEPTION] Menace détectée depuis {app_source} ! Action immédiate.")
            return json.dumps(intercept_report, indent=4)
        else:
            return json.dumps({
                "status": "NOTIFICATION_SAFE",
                "source_app": app_source,
                "action": "ALLOW_PASS"
            }, indent=4)

    def toggle_hook_status(self, activate=True):
        """Active ou désactive la surveillance des flux d'interception."""
        self.is_monitoring = activate
        status_str = "ACTIF" if activate else "INACTIF"
        return json.dumps({"status": f"HOOK_STATUS_{status_str}"}, indent=4)

# Test du module d'interception
if __name__ == "__main__":
    hook = InterceptHook(device_id="OS-CAMEROON-HOOK-01")
    
    # Simulation d'une notification frauduleuse reçue sur WhatsApp avec un lien de phishing
    fake_notification = hook.hook_incoming_notification(
        app_source="WhatsApp",
        notification_title="Gagnez un cadeau !",
        notification_body="Cliquez vite sur https://bit.ly/4x9Fake pour réclamer votre lot."
    )
    print(fake_notification)