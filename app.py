from constants import PLAYERS, TEAMS
import copy


def clean_data(players):
    # players is a list of dictionaries. Each dictionary representing a player.
    cleaned = []
    for player in players:
        cleaned_player = {}
        # clean name
        cleaned_player['name'] = player['name']
        # clean height
        cleaned_player['height'] = int(player['height'].split()[0])
        # clean experience
        if player['experience'] == "YES":
            cleaned_player['experience'] = True
        else:
            cleaned_player['experience'] = False
        # clean guardians
        cleaned_player['guardians'] = player['guardians'].split(" and ")
        # add cleaned player
        cleaned.append(cleaned_player)
    return cleaned




def balance_teams(players, teams_names):
    # displays teams as a list of dictionaries. Each dictionary is a team, with 2 keys : name of the team and players in the team
    num_players_by_team = int(len(players)/len(teams))
    players_by_team = []
    for i in range(len(teams_names)):
        team = {}
        team['name'] = teams_names[i]
        team['players'] = players[i * num_players_by_team : (i + 1) * num_players_by_team ]
        players_by_team.append(team)
    return players_by_team




def list_as_string(my_list, key):
    #display a list of dictionaries as a string depending on selected key and on the type of the element.
    list_str = ''
    for i in range(len(my_list)):
        item = my_list[i]
        
        #check if item[key] is a list (case of guardians) and join it to a string.
        if type(item[key]) == list:
            element = ", ".join(item[key])
        else : 
            element = item[key]
        
        # check if this is the last element: change comma to dot
        if i < len(my_list) -1 :
            list_str = list_str + element + ', '
        else: 
            list_str = list_str + element + '.'
    return list_str


def display_stats(team):
    #team is a dictionary with 2 keys : "name" which is a string and "players" which is a list of players (dictionaries)
    name = team['name'].upper()
    players = team['players']
    
    # name of the team
    print(f"\nTeam: {name} Stats\n")
    print("-" * 100)
    
    # number of players in the team
    print(f"Total players : {int(len(players))}")
    
    #number of inexperienced / experienced players + average height
    num_inexperienced = 0
    num_experienced = 0
    total_height = 0
    for player in players:
        if player['experience']:
            num_experienced +=1
        else :
            num_inexperienced +=1
        total_height += player['height']
    print(f"Total experienced: {num_experienced}")
    print(f"Total inexperienced: {num_inexperienced}")
    print(f"Average height: {round(total_height / len(players), 1)} inches")
    
    # name of the player
    str_players = 'Players on Team :\n\t ' + list_as_string(players, 'name')
    print(str_players)  
    
    #guargians of all the players
    print(f"Guardians: \n\t{list_as_string(players, 'guardians')}")
    
    print()
    print("-" * 100)
    
    

# The main calls to your program should be protected inside Dunder Main to prevent automatic execution if your script is imported. This does not mean everything you write has to be contained within Dunder Main. You can still import and define functions outside of dunder main, you can still extract pieces of logic into those functions. 
if __name__ == '__main__':
    # import and clean data
    players = copy.deepcopy(PLAYERS)
    teams = copy.deepcopy(TEAMS)
    players = clean_data(players)
    players_by_team = balance_teams(players, teams)
    
    #display stats
    print("-" * 100)
    print("\n\nBASKETBALL TEAM STATS TOOL\n\n")
    print("-" * 100)
    
    for team in players_by_team:
        display_stats(team)

    