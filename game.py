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

def start_game():
    pass

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
    
    

title_screen()
