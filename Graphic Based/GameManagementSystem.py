'''
CS5001 Fall 2019
Homework 7
Shebna Mathew
Game Driver - Main method
'''

from Game import *
from Graphics import *

MENU_CHOICE = [['N', 'Start a New Game'],
                        ['R','Resume an Existing Game'],
                        ['Q', 'Quit']]

GAME_CHOICE = [['N,S,E,W', '(Go North, South, East or West)'],
                        ['I','Print current inventory of Items the player has collected'],
                        ['T', 'Take an item from the current room'],
                        ['D','Drop an item they are carrying in their inventory'],
                        ['U','Use an item to solve a puzzle or defeat a monster'],
                        ['L','Look at (or examine) an item in the current room'],
                        ['Q','Quit']]
def main():

    #graphic = Graphics()
    #graphic.canvas.pack()
    #graphic.main.mainloop()

    room_file = open('aquest_rooms.txt','r')
    items_file = open('aquest_items.txt','r')
    puzzles_or_monsters_file = open('puzzles_n_monsters.txt','r')
            
    new_game = Game(room_file, items_file, puzzles_or_monsters_file)
    new_game.canvas.pack()
    new_game.main.mainloop()
    #new_game.start_game(GAME_CHOICE)
            
    room_file.close()
    items_file.close()
    puzzles_or_monsters_file.close()
    
##    while True:
##
##        user_choice = menu(MENU_CHOICE)
##
##        # start a new game
##        if user_choice == 'N':
##            room_file = open('aquest_rooms.txt','r')
##            items_file = open('aquest_items.txt','r')
##            puzzles_or_monsters_file = open('puzzles_n_monsters.txt','r')
##            
##            new_game = Game(room_file, items_file, puzzles_or_monsters_file)
##            new_game.canvas.pack()
##            new_game.main.mainloop()
##            #new_game.start_game(GAME_CHOICE)
##            
##            room_file.close()
##            items_file.close()
##            puzzles_or_monsters_file.close()
##            
##        # resume the last game    
##        elif user_choice == 'R':
##            load_game_file = open('outfile.pkl','rb')
##            load_game = pickle.load(load_game_file)
##            load_game.canvas.pack()
##            load_game.main.mainloop()
##            #load_game.start_game(GAME_CHOICE)
##            load_game_file.close()
##            
##        else: break
##    
##
##
##    print('Ok bye. Thanks for playing.')
    

main()


