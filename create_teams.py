#import clean


def balance_teams(players, teams_names):
    # displays teams as a list of dictionaries. Each dictionary is a team, with 2 keys : name of the team and players in the team
    num_players_by_team = int(len(players)/len(teams_names))
    players_by_team = []
    for i in range(len(teams_names)):
        team = {}
        team['name'] = teams_names[i]
        team['players'] = players[i * num_players_by_team : (i + 1) * num_players_by_team ]
        players_by_team.append(team)
    return players_by_team


def experimented(players, teams_names):
    experimented_players = []
    for player in players:
        if player['experience']:
            experimented_players.append(player)
    return balance_teams(experimented_players, teams_names)


def inexperimented(players, teams_names):
    inexperimented_players = []
    for player in players:
        if not player['experience']:
            inexperimented_players.append(player)
    return balance_teams(inexperimented_players, teams_names)
    

def balance(players, teams_names):
    expert = experimented(players, teams_names)
    inexpert = inexperimented(players, teams_names)
    for i in range(len(teams_names)):
        expert[i]['players'].extend(inexpert[i]['players']) 
    return expert
    


# def main():
#     players, teams = clean.main()
#     # players_by_team = balance_teams(players, teams)
#     return balance(players, teams)
    

# if __name__ == "__main__":
#     main()