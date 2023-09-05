A program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. 

1. This data will be translated into a new collection and the fields changed to something that makes more sense for Python to do its comparisons: booleans for experience and integers for height.

2. Dunder Main statement inside this file.

3. The teams will be created first only nesting the same number of players inside each team, then adding a new functionality to be able to balance teams between experimented and in-experiemented players. 

4. Display the stats on each team in a readable way. 

5. Add a menu so that the user can quit the stats tool.

6. Organize players by size.

7. Save the team analysis inside of the team's data structure.

##Structure of the data: 

teams = [
    'Panthers',
    'Bandits',
    'Warriors',
]

players = [
    {
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {...},
    {...},
    ...
]

players_by_team = [
    {
        'name': 'Panthers',
        'team_players': [
            {},
            {},
            {},
            ...
        ]
    },
    {
        'name': 'Panthers',
        'players': [
            {},
            {},
            {},
            ...
        ]
    },
    {
        'name': 'Warriors',
        'players': [
            {},
            {},
            {},
            ...
        ]
    },

]
