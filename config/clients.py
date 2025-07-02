import json

with open("config/clients.json", "r", encoding="utf-8") as f:
    CLIENTS = json.load(f)

def get_client_by_token(platform: str, token: str):
    for client in CLIENTS:
        if client.get("platform") == platform and client.get("token") == token:
            return client
    return None
