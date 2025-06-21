import requests, time
from datetime import datetime, timezone

account_id = 76561198247074470
url = f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"

params = {
    "limit": 10
}

response = requests.get(url, params=params)
print(f"Response={response}") #print response code

if response.status_code == 200:
    
    data = response.json()
    totalGamesPlayed = 0
    
    print("Match History")
    print("-------------------------")

    for match in data:
        totalGamesPlayed += 1
        
        match_id = match.get("match_id")
        
        unixTime = match.get("start_time")
        timeStarted = datetime.fromtimestamp(unixTime, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        
        duration = match.get("match_duration_s")

        print(f"Match ID: {match_id}")
        print(f"Start Time: {timeStarted}")
        print(f"Duration: {duration / 60} minutes")
        
        print("---------------------------------------------------")
        
    print("Games played:", str(totalGamesPlayed))
    input()
  
else:
    print("Somin wrong, " + str(response.status_code))
    input()
    

