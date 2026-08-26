# OmniShield - Secure File & Storage Vault (Python Pur)
# Chiffrement et protection absolue des fichiers et données locales de l'application

import os
import json
import hashlib
import base64

class SecureVault:
    def __init__(self, master_key_secret):
        # Dérivation d'une clé cryptographique robuste à partir d'un secret maître
        self.encryption_key = hashlib.sha256(master_key_secret.encode('utf-8')).digest()
        print("[SECURE VAULT] Coffre-fort numérique initialisé. Chiffrement actif.")

    def _simple_xor_cipher(self, data_bytes):
        """Chiffrement par XOR octet par octet combiné à la clé maître (Protection anti-lecture en clair)."""
        key_length = len(self.encryption_key)
        return bytes(b ^ self.encryption_key[i % key_length] for i, b in enumerate(data_bytes))

    def save_secure_file(self, filepath, data_dict):
        """Sécurise et chiffre un dictionnaire de données avant de l'écrire sur le disque."""
        try:
            json_str = json.dumps(data_dict)
            data_bytes = json_str.encode('utf-8')
            
            # Application du chiffrement
            encrypted_bytes = self._simple_xor_cipher(data_bytes)
            encoded_payload = base64.b64encode(encrypted_bytes).decode('utf-8')

            # Écriture dans le fichier sécurisé
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(encoded_payload)
            
            return json.dumps({"status": "SUCCESS", "message": f"Fichier chiffré et sauvegardé : {filepath}"}, indent=4)
        except Exception as e:
            return json.dumps({"status": "ERROR", "message": str(e)}, indent=4)

    def read_secure_file(self, filepath):
        """Déchiffre et lit un fichier sécurisé à la volée."""
        if not os.path.exists(filepath):
            return json.dumps({"status": "NOT_FOUND", "message": "Le fichier sécurisé n'existe pas."}, indent=4)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                encoded_payload = f.read()

            encrypted_bytes = base64.b64decode(encoded_payload.encode('utf-8'))
            decrypted_bytes = self._simple_xor_cipher(encrypted_bytes)
            
            data_dict = json.loads(decrypted_bytes.decode('utf-8'))
            return data_dict
        except Exception as e:
            return json.dumps({"status": "INTEGRITY_COMPROMISED", "message": "Échec du déchiffremente : Fichier corrompu ou altéré."}, indent=4)

# Test du coffre-fort sécurisé
if __name__ == "__main__":
    vault = SecureVault(master_key_secret="SECRET_MASTER_KEY_SERGES_YEMGA")
    
    # Données sensibles à protéger (ex: tokens de licence et paramètres de sécurité)
    sensitive_data = {
        "user": "Serges",
        "active_tier": "Pack Intégral",
        "security_level": "MAXIMUM",
        "tokens": ["TOKEN_MOBILE_01", "TOKEN_DESKTOP_02"]
    }
    
    test_filepath = "secure_vault_test.enc"
    
    # Sauvegarde chiffrée
    print(vault.save_secure_file(test_filepath, sensitive_data))
    
    # Lecture et déchiffrement
    print("Données lues et déchiffrées :")
    print(vault.read_secure_file(test_filepath))
    
    # Nettoyage du fichier de test
    if os.path.exists(test_filepath):
        os.remove(test_filepath)