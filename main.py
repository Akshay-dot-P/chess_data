from fastapi import FastAPI

from lichess_data_fetch import fetch_top_classical_players  # Import updated path

app = FastAPI()

@app.get("/top-classical-players")
def get_top_classical_players():
    top_players = fetch_top_classical_players()
    if top_players:
        return {"top_players": top_players}
    else:
        return {"message": "Failed to fetch top classical players"}
