from operator import itemgetter



def sort_players(team_players, key_name):
    # @params {team_players} list of dictionaries
    # @params {key_name} the key in those dictionaries
    # @returns the same list of dictionaries sorted according to the specified key
    # thanks to stackoverflow : https://stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
    return sorted(team_players, key=itemgetter(key_name))




def list_as_string(team_players, key):
    # @params {team_players} list of each player as a dictionary
    # @params {key}
    # print a string with comma separated values of the values for the key 
    list_str = ''
    for i in range(len(team_players)):
        player = team_players[i]
        
        #check if player[key] is a list (case of guardians) and join it to a string.
        if type(player[key]) == list:
            element = ", ".join(player[key])
        else : 
            element = player[key]
        
        # check if this is the last element: change comma to dot
        if i < len(team_players) -1 :
            list_str = list_str + element + ', '
        else: 
            list_str = list_str + element + '.'
    return list_str



def calculate_experienced_average(team_players):
    #team_player is a list of dictionaries (one for each player)
    num_inexperienced = 0
    num_experienced = 0
    total_height = 0
    for player in team_players:
        if player['experience']:
            num_experienced +=1
        else :
            num_inexperienced +=1
        total_height += player['height']
    average_height = round(total_height / len(team_players), 1)  
    return num_experienced, num_inexperienced, average_height



def print_stats(team):
    #team is a dictionary with 2 keys : "name" which is a string and "team_players" which is a list of players (dictionaries). 
    name = team['name'].upper()
    team_players = sort_players(team['players'], 'height')
    
    # name of the team
    print(f"\nTeam: {name} Stats\n")
    print("-" * 100)
    
    # number of players in the team
    print(f"Total players : {len(team_players)}")
    
    #number of inexperienced / experienced players + average height
    num_experienced, num_inexperienced, average_height = calculate_experienced_average(team_players)
    
    print(f"Total experienced: {num_experienced}")
    print(f"Total inexperienced: {num_inexperienced}")
    print(f"Average height: {average_height} inches")
    
    # name of the player
    str_players = 'Players on Team :\n\t ' + list_as_string(team_players, 'name')
    print(str_players)  
    
    #guargians of all the players
    print(f"Guardians: \n\t{list_as_string(team_players, 'guardians')}")
    
    print()
    print("-" * 100)
    
    return num_experienced, num_inexperienced, average_height