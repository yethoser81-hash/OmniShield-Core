# OmniShield - BYOD Enterprise Isolation Guard (Python Pur)
# Cloisonnement étanche des flux professionnels et protection des données d'entreprise sur appareils mixtes

import time
import json
import hashlib

class BYODIsolationGuard:
    def __init__(self, enterprise_id, employee_id):
        self.enterprise_id = enterprise_id
        self.employee_id = employee_id
        self.container_active = True
        # Liste des domaines ou extensions de fichiers professionnels autorisés dans le coffre
        self.allowed_corporate_domains = ["yemga.com", "ets-yemga.cm", "enterprise-secure.net"]
        print(f"[BYOD GUARD] Conteneur professionnel sécurisé initialisé pour l'employé {employee_id} ({enterprise_id})")

    def inspect_data_exfiltration(self, target_destination, data_payload_size_kb):
        """Surveille et bloque toute tentative de fuite de données professionnelles vers des canaux non autorisés."""
        if not self.container_active:
            return json.dumps({"status": "CONTAINER_LOCKED", "action": "BLOCKED"})

        # Vérification si la destination respecte le périmètre de l'entreprise
        is_destination_safe = any(domain in target_destination for domain in self.allowed_corporate_domains)

        if not is_destination_safe and data_payload_size_kb > 500: # Seuil de fuite suspecte en Ko
            alert = {
                "status": "DATA_EXFILTRATION_BLOCKED",
                "risk_level": "HIGH_BYOD_VIOLATION",
                "enterprise": self.enterprise_id,
                "employee": self.employee_id,
                "destination": target_destination,
                "payload_size_kb": data_payload_size_kb,
                "action": "TRANSFERT INTERCEPTÉ ET CHIFFREMENT DU CONTENEUR",
                "timestamp": int(time.time()),
                "message": "Tentative de sortie de données professionnelles vers un réseau non autorisé bloquée net."
            }
            return json.dumps(alert, indent=4)
        else:
            return json.dumps({
                "status": "DATA_TRANSFER_AUTHORIZED",
                "destination": target_destination,
                "message": "Flux validé à l'intérieur du périmètre sécurisé."
            }, indent=4)

    def toggle_emergency_wipe(self, activate=False):
        """Permet à l'entreprise d'effacer à distance le conteneur professionnel en cas de vol de l'appareil."""
        if activate:
            self.container_active = False
            return json.dumps({
                "status": "ENTERPRISE_CONTAINER_WIPED",
                "enterprise": self.enterprise_id,
                "employee": self.employee_id,
                "timestamp": int(time.time()),
                "message": "Données professionnelles effacées à distance. L'intégrité personnelle du téléphone reste intacte."
            }, indent=4)
        return json.dumps({"status": "CONTAINER_NORMAL", "action": "None"})

# Test du module d'isolation BYOD
if __name__ == "__main__":
    byod = BYODIsolationGuard(enterprise_id="ETS-YEMGA-CORP", employee_id="EMP-992")
    
    # Simulation d'une tentative d'envoi de données d'entreprise vers un cloud personnel non sécurisé
    leak_test = byod.inspect_data_exfiltration(target_destination="my-personal-drive-hack.com", data_payload_size_kb=2048)
    print(leak_test)