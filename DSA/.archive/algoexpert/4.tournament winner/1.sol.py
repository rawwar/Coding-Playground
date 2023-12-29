def tournamentWinner(competitions, results):
    # Write your code here.
    hm = {}
    win_key = None
    win_val = 0
    for result, (home_team, away_team) in zip(results, competitions):
        if result:
            hm[home_team] = hm.get(home_team,0) + 3
            if win_val < hm[home_team]:
                win_val = hm[home_team]
                win_key = home_team
        else:
            hm[away_team] = hm.get(away_team, 0) + 3
            if win_val < hm[away_team]:
                win_val = hm[away_team]
                win_key = away_team

    return win_key
