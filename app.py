from constants import PLAYERS, TEAMS
from clean import clean_data
from create_teams import balance
from display_statistics import print_stats, calculate_experienced_average
from display_menu import main_menu, team_menu
import copy

def main():
    # import and clean data
    players = copy.deepcopy(PLAYERS)
    teams = copy.deepcopy(TEAMS)
    players = clean_data(players)
    players_by_team = balance(players, teams)
    for team in players_by_team:
        team['num_experienced'], team['num_inexperienced'], team['average_height']  = calculate_experienced_average(team['players'])

    
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
                team_A = players_by_team[0]
                print_stats(team_A)
            elif team_selected == "B":
                team_B = players_by_team[1]
                print_stats(team_B)
            elif team_selected == "C":
                team_C = players_by_team[2]
                print_stats(team_C)
            else: 
                continue
            print(players_by_team)
        else: 
            break

if __name__ == '__main__':
    main()

    