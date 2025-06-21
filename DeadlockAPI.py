import requests, time
from datetime import datetime, timezone

# Small program to get total match history data

account_id = input("Enter SteamID64: ")

def validate(id):
    if isinstance(id, int):
        return id
    else:
        print("Invalid ID")
        new_id = input("Enter SteamID64: ")
        validate(new_id)
    
url = f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"

response = requests.get(url)


if response.status_code == 200:
    
    data = response.json()
    
    total_games, wins, losses, abandons, denies, net_worth = 0,0,0,0,0,0
    
    print("Match History")
    print("-------------------------")

    for match in data:
        total_games += 1
        
        match_id = match.get("match_id")
        
        unixTime = match.get("start_time")
        time_started = datetime.fromtimestamp(unixTime, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        
        duration = match.get("match_duration_s")
        match_result = match.get("match_result") #Amber Hand = 0, Sapphire Flames = 1
        player_team = match.get("player_team") #0 = Loss, 1 = Victory
        denies += match.get("denies")
        net_worth += match.get("net_worth")
        isAbandon = match.get("team_abandoned")
        
        if isAbandon is True:
            abandons += 1
        else:
            if player_team == 1:
                wins += 1
            elif player_team == 0:
                losses += 1
    
    winrate = float((wins/total_games) * 100) % "%.2f" if total_games else 0
    
    print(f"Games played: {total_games}")
    print(f"Total Denies: {denies}")
    print(f"Total pmoney: {net_worth}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Abandons: {abandons}")
    print(f"Winrate: {winrate}%")
    
    input()
  
else:
    print("Something wrong, server down maybe " + str(response.status_code))
    input()
    

