import requests, time
from datetime import datetime, timezone

account_id = 76561198247074470
url = f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"

response = requests.get(url)
print(f"Response={response}") #print response code

if response.status_code == 200:
    
    data = response.json()
    
    total_games, wins, losses, abandons = 0,0,0,0
    
    print("Match History")
    print("-------------------------")

    for match in data:
        total_games += 1
        
        match_id = match.get("match_id")
        
        unixTime = match.get("start_time")
        time_started = datetime.fromtimestamp(unixTime, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        
        duration = match.get("match_duration_s")
        #match_result = match.get("match_result") #Amber Hand = 0, Sapphire Flames = 1
        player_team = match.get("player_team") #0 = Loss, 1 = Victory
        
        isAbandon = match.get("team_abandoned")
        
        print(isAbandon)
        
        if isAbandon is True:
            abandons += 1
        else:
            if player_team == 1:
                wins += 1
            elif player_team == 0:
                losses += 1
            

        """
        print(f"Match ID: {match_id}")
        print(f"Start Time: {time_started}")
        print(f"Duration: {duration / 60}m:{duration % 60}s")
        
        #print(f"Match Result: {match_result}")
        print(f"Player Team: {player_team}")
        
        print("---------------------------------------------------")
        """
        
    print(f"Games played: {total_games}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Abandons: {abandons}")
    print("Winrate:", float((wins/total_games) * 100), "%")
    
    input()
  
else:
    print("Sometin wrong, " + str(response.status_code))
    input()
    

