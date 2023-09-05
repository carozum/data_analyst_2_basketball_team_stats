from constants import PLAYERS, TEAMS
from clean import clean_data
from create_teams import balance
from display import display_stats
import copy

def main():
    # import and clean data
    players = copy.deepcopy(PLAYERS)
    teams = copy.deepcopy(TEAMS)
    players = clean_data(players)
    players_by_team = balance(players, teams)
    
    #display stats
    print("-" * 100)
    print("\n\nBASKETBALL TEAM STATS TOOL\n\n")
    print("-" * 100)
    
    for team in players_by_team:
        display_stats(team)


if __name__ == '__main__':
    main()

    