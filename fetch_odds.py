import requests
from bs4 import BeautifulSoup

URL = "PASTE_DRAFTKINGS_URL_HERE"

def parse_odds(odds):
    odds = int(odds)
    if odds < 0:
        return abs(odds) / (abs(odds) + 100)
    return 100 / (odds + 100)

def fetch_odds():
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    players = []

    text = soup.get_text(" ")

    # simple fallback extraction (we can improve later)
    import re
    matches = re.findall(r"([A-Za-z .'-]+)\s+(-\d{3,4})", text)

    for name, odds in matches:
        try:
            players.append({
                "player": name.strip(),
                "odds": int(odds),
                "implied_prob": parse_odds(odds)
            })
        except:
            pass

    return players
