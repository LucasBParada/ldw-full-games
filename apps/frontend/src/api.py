import httpx

BASE_URL = "http://127.0.0.1:5000"


class ApiClient:

    @staticmethod
    def get_health():
        r = httpx.get(f"{BASE_URL}/health")
        r.raise_for_status()
        return r.json()

    # ---------------- HOSTS ----------------
    @staticmethod
    def get_hosts():
        r = httpx.get(f"{BASE_URL}/hosts/")
        r.raise_for_status()
        return r.json()

    @staticmethod
    def create_host(payload: dict):
        r = httpx.post(f"{BASE_URL}/hosts/", json=payload)
        r.raise_for_status()
        return r.json()

    # ---------------- GAMES ----------------
    @staticmethod
    def get_games():
        r = httpx.get(f"{BASE_URL}/games/")
        r.raise_for_status()
        return r.json()

    @staticmethod
    def create_game(payload: dict):
        r = httpx.post(f"{BASE_URL}/games/", json=payload)
        r.raise_for_status()
        return r.json()

    # ---------------- PLAYERS ----------------
    @staticmethod
    def get_players():
        r = httpx.get(f"{BASE_URL}/players/")
        r.raise_for_status()
        return r.json()

    @staticmethod
    def create_player(payload: dict):
        r = httpx.post(f"{BASE_URL}/players/", json=payload)
        r.raise_for_status()
        return r.json()