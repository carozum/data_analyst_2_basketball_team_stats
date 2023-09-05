from operator import itemgetter

def sort_players(list_to_be_sorted, key_name):
    # thanks to stackoverflow : https://stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
    return sorted(list_to_be_sorted, key=itemgetter(key_name))


def list_as_string(my_list, key):
    #display from a list of dictionaries, a string depending on selected key and on the type the selected element.
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
    players = sort_players(team['players'], 'height')
    
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
    
  