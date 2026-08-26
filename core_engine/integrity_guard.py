# OmniShield - Binary Integrity Guard (Python Pur)
# Autocontrôle permanent et protection contre le piratage du code (Anti-Tampering)

import hashlib
import os
import json
import time

class IntegrityGuard:
    def __init__(self, target_directory="core_engine"):
        self.target_directory = target_directory
        self.baseline_registry = {}
        print(f"[INTEGRITY GUARD] Initialisation du bouclier d'intégrité sur : {target_directory}")

    def generate_file_hash(self, filepath):
        """Génère une empreinte cryptographique SHA-256 d'un fichier source."""
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            return None

    def create_baseline(self, file_list):
        """Enregistre l'état de référence sain de l'application."""
        for file_path in file_list:
            file_hash = self.generate_file_hash(file_path)
            if file_hash:
                self.baseline_registry[file_path] = file_hash
        print(f"[BASELINE] Empreintes de référence enregistrées pour {len(self.baseline_registry)} fichiers.")

    def audit_system_integrity(self, file_list):
        """Vérifie en temps réel si un fichier a été modifié ou corrompu par un tiers."""
        compromised_files = []
        
        for file_path in file_list:
            current_hash = self.generate_file_hash(file_path)
            original_hash = self.baseline_registry.get(file_path)
            
            if current_hash != original_hash:
                compromised_files.append(file_path)

        if compromised_files:
            alert = {
                "status": "CRITICAL_INTEGRITY_BREACH",
                "risk": "Le code source ou un binaire a été altéré ou piraté !",
                "compromised_files": compromised_files,
                "action": "Verrouillage immédiat du système et purge des caches.",
                "timestamp": int(time.time())
            }
            return json.dumps(alert, indent=4)
        else:
            return json.dumps({
                "status": "INTEGRITY_VERIFIED",
                "message": "Aucune modification détectée. Le système est intègre et sécurisé."
            }, indent=4)

# Test du module d'intégrité
if __name__ == "__main__":
    guard = IntegrityGuard()
    
    # Simulation d'une liste de fichiers à surveiller dans le noyau
    monitored_files = ["core_engine/security_kernel.py", "core_engine/sync_bridge.py"]
    
    # Création fictive d'une référence (pour le test, on simule l'existence)
    guard.baseline_registry = {
        "core_engine/security_kernel.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "core_engine/sync_bridge.py": "a8f5f167f44f4964e6c998dee827110c"
    }
    
    print(guard.audit_system_integrity(monitored_files))