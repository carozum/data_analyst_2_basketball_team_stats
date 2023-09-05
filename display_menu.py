import string

def main_menu():   
    print("""
----- MENU -----

Here are your choices:
    A) Display Team Stats
    Q) Quit
""")
    
 
def team_menu(teams):
    alphabet = string.ascii_uppercase
    for i in range(len(teams)):
        print(f"{alphabet[i]})  {teams[i]}")
    