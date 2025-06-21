import requests, time

account_id = 76561198247074470
url = f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"


response = requests.get(url)
print(f"Response={response}") #print response code



"""
if response.status_code == 200:
    data = response.json()
    
    print("Response Data")
    print("-------------------------")

    for match in data:
        match_id = match.get("match_id")
        start_time = match.get("start_time")
        duration = match.get("duration_s")
        game_mode = match.get("game_mode")
        match_mode = match.get("match_mode")
        winning_team = match.get("winning_team")

        print(f"Match ID: {match_id}")
        print(f"Start Time: {start_time}")
        print(f"Duration: {duration / 60} minutes")
        print(f"Game Mode: {game_mode}")
        print(f"Match Mode: {match_mode}")
        print(f"Winning Team: {winning_team}")
        print("---------------------------------------------------")
        
    input()
  
else:
    print("Somin wrong, " + str(response.status_code))
    input()
    

"""
