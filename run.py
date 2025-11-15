from playerstyles import get_player_data, get_team_defense_data
from matchup_agent import analyze_matchup

player = input("Player name: ")
team = input("Opponent: ")

off = get_player_data(player)
defn = get_team_defense_data(team)

report = analyze_matchup(player, off, defn, team)

print("\n=== MATCHUP REPORT ===\n")
print(report)
