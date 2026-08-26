# OmniShield - Secure Database Manager (SQLite Chiffré / Local)
# Gestion des tables de données : Licences, Utilisateurs, Menaces et Journaux

import sqlite3
import os
import json
import time

class SecureDatabaseManager:
    def __init__(self, db_path="core_engine/omnishield_vault.db"):
        self.db_path = db_path
        self._initialize_database()
        print(f"[DATABASE] Base de données sécurisée connectée sur : {self.db_path}")

    def _get_connection(self):
        """Établit la connexion à la base de données locale."""
        return sqlite3.connect(self.db_path)

    def _initialize_database(self):
        """Crée les tables indispensables si elles n'existent pas (Licences, Logs, Menaces)."""
        conn = self._get_connection()
        cursor = conn.cursor()

        # Table des licences et abonnements (Gère les packs et la période d'essai de 30 jours)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS licenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT UNIQUE,
                edition_type TEXT,
                status TEXT,
                start_date INTEGER,
                expiry_date INTEGER
            )
        """)

        # Table des journaux de sécurité et d'audit
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS security_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp INTEGER,
                event_type TEXT,
                severity TEXT,
                description TEXT,
                target TEXT
            )
        """)

        # Table de la liste noire locale des menaces (Phishing / Mobile Money)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS local_threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                indicator TEXT UNIQUE,
                threat_type TEXT,
                detected_at INTEGER
            )
        """)

        conn.commit()
        conn.close()

    def register_license(self, device_id, edition_type, trial_days=30):
        """Enregistre ou met à jour la licence d'un utilisateur avec sa période d'essai."""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        start_time = int(time.time())
        expiry_time = start_time + (trial_days * 86400) # 30 jours en secondes

        cursor.execute("""
            INSERT OR REPLACE INTO licenses (device_id, edition_type, status, start_date, expiry_date)
            VALUES (?, ?, 'ACTIVE', ?, ?)
        """, (device_id, edition_type, start_time, expiry_time))

        conn.commit()
        conn.close()
        return json.dumps({"status": "SUCCESS", "message": f"Licence {edition_type} enregistrée pour {device_id}."})

    def log_event(self, event_type, severity, description, target):
        """Consigne un événement de sécurité de manière permanente dans la base."""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO security_logs (timestamp, event_type, severity, description, target)
            VALUES (?, ?, ?, ?, ?)
        """, (int(time.time()), event_type, severity, description, target))

        conn.commit()
        conn.close()

# Test de la base de données
if __name__ == "__main__":
    db = SecureDatabaseManager()
    print(db.register_license("DEVICE_SERGES_01", "Licence Intégrale Bundle"))
    db.log_event("INITIALIZATION", "INFO", "Base de données initialisée avec succès", "SYSTEM")