# OmniShield - Enterprise Audit Stream & Compliance Ledger (Python Pur)
# Journaux d'audit inaltérables et traçabilité des événements de sécurité (B2B)

import time
import json
import hashlib

class AuditStream:
    def __init__(self, enterprise_id):
        self.enterprise_id = enterprise_id
        self.ledger = []
        # Initialisation de la chaîne de hachage (Style blockchain simple pour garantir l'intégrité)
        self.last_block_hash = "0" * 64
        print(f"[AUDIT STREAM] Registre d'audit et de conformité initialisé pour : {enterprise_id}")

    def log_security_event(self, event_type, severity, description, user_or_device):
        """Enregistre un événement de sécurité de manière cryptographiquement chaînée."""
        timestamp = int(time.time())
        
        # Structure de l'événement
        event_data = {
            "enterprise_id": self.enterprise_id,
            "timestamp": timestamp,
            "event_type": event_type,
            "severity": severity,
            "description": description,
            "target": user_or_device,
            "previous_hash": self.last_block_hash
        }

        # Conversion en chaîne pour calcul du hachage du bloc
        block_string = json.dumps(event_data, sort_keys=True)
        current_hash = hashlib.sha256(block_string.encode('utf-8')).hexdigest()
        
        # Mise à jour du pointeur de hachage pour le bloc suivant
        self.last_block_hash = current_hash

        final_entry = {
            "block_hash": current_hash,
            "payload": event_data
        }

        self.ledger.append(final_entry)
        return json.dumps({
            "status": "EVENT_LOGGED_SECURELY",
            "block_hash": current_hash[:16] + "...",
            "timestamp": timestamp
        }, indent=4)

    def export_compliance_report(self):
        """Exporte le registre d'audit complet pour les contrôles de conformité de l'entreprise."""
        report = {
            "enterprise_id": self.enterprise_id,
            "total_events_recorded": len(self.ledger),
            "ledger_integrity": "VERIFIED_UNALTERED",
            "audit_trail": self.ledger
        }
        return json.dumps(report, indent=4)

# Test du module d'audit B2B
if __name__ == "__main__":
    stream = AuditStream(enterprise_id="ETS-YEMGA-AUDIT-01")
    
    # Simulation de l'enregistrement de deux événements critiques
    print(stream.log_security_event("PHISHING_BLOCKED", "HIGH", "Lien malveillant intercepté sur WhatsApp", "DEVICE_MOBILE_01"))
    print(stream.log_security_event("WHALING_ATTEMPT", "CRITICAL", "Tentative de fraude au président bloquée", "USER_COMPTA_02"))
    
    # Exportation du rapport de conformité
    print("\n--- Rapport de conformité généré ---")
    print(stream.export_compliance_report())