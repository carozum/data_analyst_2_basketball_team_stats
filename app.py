from constants import PLAYERS, TEAMS
from clean import clean_data
from create_teams import balance
from display_statistics import display_stats
from display_menu import main_menu, team_menu
import copy

def main():
    # import and clean data
    players = copy.deepcopy(PLAYERS)
    teams = copy.deepcopy(TEAMS)
    players = clean_data(players)
    players_by_team = balance(players, teams)
    
    print("-" * 100)
    print("\n\nBASKETBALL TEAM STATS TOOL\n\n")
    print("-" * 100)
    
    while True:
        main_menu()
        answer = input("Enter an option A or Q:    ").upper()
        
        if answer == 'A':
            team_menu(teams)
            team_selected = input("Choose a team:   ").upper()
            #display stats
            if team_selected == "A":
                display_stats(players_by_team[0])
            elif team_selected == "B":
                display_stats(players_by_team[1])
            elif team_selected == "C":
                display_stats(players_by_team[2])
            else: 
                continue
        else: 
            break

if __name__ == '__main__':
    main()

    