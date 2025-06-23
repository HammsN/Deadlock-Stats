import requests
from datetime import datetime, timezone

# Small program to get total match history data

def get_steamID():
    try:
        account_id = int(input("Enter SteamID64: "))
        return account_id      
    except ValueError:
        print("Invalid ID, try again")
        return get_steamID()
   
   
def get_response(id):
    url = f"https://api.deadlock-api.com/v1/players/{id}/match-history"
    response = requests.get(url)
    
    if response.status_code == 200: 
        return response.json()
    else:
        raise Exception("Something wrong, server down or unidentified ID (Code:",str(response.status_code), ")")
     
def fetch_stats(data):
    total_games, wins, losses, abandons, denies, net_worth = 0,0,0,0,0,0
    
    print("Match History")
    print("-------------------------")

    for match in data:
        total_games += 1
        
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

    winrate = round((wins/total_games) * 100,2) if total_games else 0
    
    print(f"Games played: {total_games} games")
    print(f"Total Denies: {denies} denies")
    print(f"Total pmoney: {net_worth} souls")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Abandons: {abandons}")
    print(f"Winrate: {winrate}%")
    
    
def main():
    account_id = str(get_steamID())
    history = get_response(account_id)
    fetch_stats(history)
    input()

main()
    

