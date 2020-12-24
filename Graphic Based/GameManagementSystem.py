'''
CS5001 Fall 2019
Homework 7
Shebna Mathew
Game Driver - Main method
'''

from Game import *

def main():

    room_file = open('aquest_rooms.txt','r')
    items_file = open('aquest_items.txt','r')
    puzzles_or_monsters_file = open('puzzles_n_monsters.txt','r')
            
    new_game = Game(room_file, items_file, puzzles_or_monsters_file)
    new_game.canvas.pack()
    new_game.main.mainloop()
            
    room_file.close()
    items_file.close()
    puzzles_or_monsters_file.close()

main()


