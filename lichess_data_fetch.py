import requests

def fetch_top_classical_players():
    lichess_api_url = "https://lichess.org/player/top/500/classical"
    response = requests.get(lichess_api_url)

    if response.status_code == 200:
        player_data = response.json()
        top_players = player_data['users']
        return top_players
    else:
        return None
