#from constants import PLAYERS, TEAMS
#import copy

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


# def main():
#     players = copy.deepcopy(PLAYERS)
#     teams = copy.deepcopy(TEAMS)
#     players = clean_data(players)
#     return players, teams

# if __name__ == "__main__":
#     main()
