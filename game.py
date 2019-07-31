# PYTHON TEXT RPG:
# ===============

import cmd
import textwrap
import sys  
import os   
import time
import random

screen_width = 100

##### Player Setup #####
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'

myPlayer = Player()


##### Title Screen #####
def title_screen_selections():
    print("Please enter a valid command:")
    option = input(">>> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command:")
        option = input(">>> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def title_screen():
    clear_screen()
    print('########################')
    print('# Welcome to Text RPG! #')
    print('########################')
    print('        - Play -        ')
    print('        - Help -        ')
    print('        - Quit -        ')
    print('                        ')
    title_screen_selections()

def help_menu():
    print('########################')
    print('# Welcome to RPG! Help #')
    print('########################')
    print('- Use up, down, left, right to move')
    print('- Type in a command to do something')
    print('- Use "look" to inspect something')
    print('')
    print('Good luck and have fun!')
    title_screen_selections()
    



##### MAP #####
"""    
Player starts at b2

     a  b  c  d
    -------------
    |  |  |  |  |  1
    ------------- 
    |  |  |  |  |  2
    -------------
    |  |  |  |  |  3
    -------------
    |  |  |  |  |  4
    -------------
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 }

zonemap = {
    'a1': {ZONENAME: "Town Shaky", 
           DESCRIPTION : 'This is the shaky part of town.', 
           EXAMINATION : 'You see some dark figures lurking around.', 
           SOLVED : False, 
           UP : '', DOWN : 'a2', LEFT : '', RIGHT : 'b1',
    },
    'a2': {ZONENAME: "Town Entrance", 
           DESCRIPTION : 'This is the entrance to the town.', 
           EXAMINATION : 'You see a gate with guards. Above them is a sign that reads: WELCOME!', 
           SOLVED : False, 
           UP : 'a1', DOWN : 'a3', LEFT : '', RIGHT : 'b2',
    }, 
    'a3': {ZONENAME: "Town Market", 
           DESCRIPTION : 'The town has its own market where you can buy anything.', 
           EXAMINATION : 'The smells coming from the food section is amazing...', 
           SOLVED : False, 
           UP : 'a2', DOWN : 'a4', LEFT : '', RIGHT : 'b3',
    }, 
    'a4': {ZONENAME: "Town", 
           DESCRIPTION : 'This is where people live.', 
           EXAMINATION : 'You see many houses.', 
           SOLVED : False, 
           UP : 'a3', DOWN : '', LEFT : '', RIGHT : 'b4',
    },
    'b1': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : '', DOWN : 'b2', LEFT : 'a1', RIGHT : 'c1',
    }, 
    'b2': {ZONENAME: "Home", 
           DESCRIPTION : 'You see a beautiful house. Oh, wait! It is YOUR house.', 
           EXAMINATION : 'Your home looks the same - nothing has changed.', 
           SOLVED : False, 
           UP : 'b1', DOWN : 'b3', LEFT : 'a2', RIGHT : 'c2',
    }, 
    'b3': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'b2', DOWN : 'b4', LEFT : 'a3', RIGHT : 'c3',
    }, 
    'b4': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'b3', DOWN : '', LEFT : 'a4', RIGHT : 'c4',
    },
    'c1': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : '', DOWN : 'c2', LEFT : 'b1', RIGHT : 'd1',
    }, 
    'c2': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'c1', DOWN : 'c3', LEFT : 'b2', RIGHT : 'd2',
    }, 
    'c3': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'c2', DOWN : 'c4', LEFT : 'b3', RIGHT : 'd3',
    }, 
    'c4': {ZONENAME: "Explosion", 
           DESCRIPTION : 'There is a HUGE explosion.', 
           EXAMINATION : 'You have encountered C4. You might not survive this...', 
           SOLVED : False, 
           UP : 'c3', DOWN : '', LEFT : 'b4', RIGHT : 'd4',
    },
    'd1': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : '', DOWN : 'd2', LEFT : 'c1', RIGHT : '',
    }, 
    'd2': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'd1', DOWN : 'd3', LEFT : 'c2', RIGHT : '',
    }, 
    'd3': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'd2', DOWN : 'd4', LEFT : 'c3', RIGHT : '',
    }, 
    'd4': {ZONENAME: "", 
           DESCRIPTION : '', 
           EXAMINATION : '', 
           SOLVED : False, 
           UP : 'd3', DOWN : '', LEFT : 'c4', RIGHT : '',
    },
}


##### GAME INTERACTIVITY #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('\n' + myPlayer.location)
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    


##### GAME FUNCTIONALITY #####
def start_game():
    pass

print_location()

#title_screen()
