package main

const HOME_TEAM_WON = 1

func TournamentWinner(competitions [][]string, results []int) string {
	// Write your code here.
	win_key := ""
	scores := map[string]int{win_key: 0}

	for idx, competition := range competitions {
		result := results[idx]
		homeTeam, awayTeam := competition[0], competition[1]

		winningTeam := awayTeam
		if result == HOME_TEAM_WON {
			winningTeam = homeTeam
		}

		scores[winningTeam] += 3

		if scores[winningTeam] > scores[win_key] {
			win_key = winningTeam
		}
	}
	return win_key
}
