import requests
import matplotlib.pyplot as plt

def fetch_team_stats(team_id, season):
    url = f"https://www.balldontlie.io/api/v1/teams/{team_id}/stats"
    params = {'season': season}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def plot_bar_graph(team_stats, season):
    player_stats = team_stats['data'][0]['team']['players']
    player_names = [player['first_name'] + ' ' + player['last_name'] for player in player_stats]
    points_per_game = [player['pts'] for player in player_stats]

    plt.figure(figsize=(10, 6))
    plt.bar(player_names, points_per_game, color='skyblue')
    plt.xlabel('Player')
    plt.ylabel('Points per Game')
    plt.title(f'Points per Game for {season} Season')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Change for each team and season
team_id = 1 
season = '2021'  
team_stats = fetch_team_stats(team_id, season)

if team_stats:
    plot_bar_graph(team_stats, season)
else:
    print("Failed to fetch team stats from the NBA API.")
