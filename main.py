from fetch_odds import fetch_odds
from decision_engine import select_picks
from notify_telegram import send_message

def main():
    players = fetch_odds()
    picks = select_picks(players)

    msg = "MLB Beat the Streak Picks\n\n"

    for p in picks:
        msg += f"{p['player']} ({p['implied_prob']:.3f})\n"

    send_message(msg)

if __name__ == "__main__":
    main()
