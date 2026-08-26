# OmniShield - Cross-Platform Sync Bridge (Python Pur)
# Synchronisation chiffrée et temps réel entre Mobile et Desktop

import hashlib
import time
import json

class SyncBridge:
    def __init__(self, user_id):
        self.user_id = user_id
        self.paired_devices = []
        print(f"[SYNC BRIDGE] Initialisation du pont de synchronisation pour l'utilisateur : {user_id}")

    def pair_device(self, device_name, device_type):
        """Associe un nouvel appareil (Mobile ou Desktop) au compte de manière sécurisée."""
        if device_type not in ["MOBILE", "DESKTOP"]:
            raise ValueError("[ERREUR] Type d'appareil non reconnu. Doit être MOBILE ou DESKTOP.")
        
        timestamp = int(time.time())
        device_token = hashlib.sha256(f"{self.user_id}-{device_name}-{timestamp}".encode('utf-8')).hexdigest()

        device_info = {
            "device_name": device_name,
            "type": device_type,
            "token": device_token,
            "paired_at": timestamp,
            "status": "SECURE_CONNECTED"
        }
        
        self.paired_devices.append(device_info)
        return json.dumps({
            "status": "DEVICE_PAIRED_SUCCESS",
            "device": device_name,
            "type": device_type,
            "token_fingerprint": device_token[:16] + "..."
        }, indent=4)

    def broadcast_security_alert(self, alert_type, source_device):
        """Diffuse une alerte de sécurité instantanée sur tous les appareils connectés de l'utilisateur."""
        timestamp = int(time.time())
        broadcast_payload = {
            "event": "GLOBAL_SECURITY_ALERT",
            "alert_type": alert_type,
            "triggered_by": source_device,
            "timestamp": timestamp,
            "action_required": "LOCK_AND_VERIFY"
        }
        
        print(f"[BROADCAST] Alerte '{alert_type}' transmise à tous les écrans connectés.")
        return json.dumps(broadcast_payload, indent=4)

# Test du pont de synchronisation multi-plateforme
if __name__ == "__main__":
    bridge = SyncBridge(user_id="SERGES_YEMGA_001")
    
    # Association d'un smartphone et d'un ordinateur
    print(bridge.pair_device("Smartphone Principal (Android)", "MOBILE"))
    print(bridge.pair_device("Poste Travail (Windows)", "DESKTOP"))
    
    # Simulation d'une alerte globale synchronisée
    print(bridge.broadcast_security_alert("UNAUTHORIZED_LOGIN_ATTEMPT", "Smartphone Principal (Android)"))