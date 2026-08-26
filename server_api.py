# OmniShield - Cloud API Bridge (FastAPI + Supabase dynamique)
# Fait le lien entre les apps clientes (Mobile/PC) et la base Supabase sans valeurs en dur.

from fastapi import FastAPI, HTTPException
import os
from supabase import create_client, Client

app = FastAPI(title="OmniShield Cloud Guard", version="1.0.0")

# Récupération dynamique des identifiants Supabase depuis l'environnement sécurisé (.env)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialisation du client Supabase (si les clés sont absentes, l'API prévient proprement)
supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"status": "ONLINE", "system": "OmniShield Secure Cloud API"}

@app.get("/verify-license/{device_id}")
def verify_license(device_id: str):
    """Interroge la table Supabase des abonnements pour vérifier la licence en temps réel."""
    if not supabase:
        raise HTTPException(status_code=500, detail="Base de données Cloud non configurée (Supabase manquant).")
    
    try:
        response = supabase.table("subscriptions").select("*").eq("device_id", device_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Licence introuvable pour ce terminal.")
        
        return {"status": "SUCCESS", "license_data": response.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/threats/sync")
def sync_threats():
    """Récupère dynamiquement et globalement la liste des menaces depuis Supabase (zéro valeur en dur)."""
    if not supabase:
        raise HTTPException(status_code=500, detail="Base de données Cloud non configurée (Supabase manquant).")
    
    try:
        response = supabase.table("global_threats").select("*").execute()
        return {
            "status": "SUCCESS",
            "total_threats": len(response.data),
            "threats": response.data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))