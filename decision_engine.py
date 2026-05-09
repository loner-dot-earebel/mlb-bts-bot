def select_picks(players):
    if not players:
        return []

    sorted_players = sorted(players, key=lambda x: x["implied_prob"], reverse=True)

    return sorted_players[:2]
