'''
CS500 1 Fall 2019
Homework 7
Shebna Mathew
PyUnit test module

Tests out the total score function,
which basically takes into account the individual value
of an item in the inventory and checks for a suitable rating.
Including tests for just one item, multiple items
carrying different values
'''

from room import *
import unittest
from Game import *

class TotalScoreGameTest(unittest.TestCase):

    def setUp(self):
        self.room_file = open('aquest_rooms.txt','r')
        self.items_file = open('aquest_items.txt','r')
        self.puzzles_or_monsters_file = open('puzzles_n_monsters.txt','r')

    def tearDown(self):
        self.room_file.close()
        self.items_file.close()
        self.puzzles_or_monsters_file.close()

    def back_to_the_start(self):
        self.room_file.seek(0)
        self.items_file.seek(0)
        self.puzzles_or_monsters_file.seek(0)

    def test_noItem(self):
        self.new_game = Game(self.room_file, self.items_file, self.puzzles_or_monsters_file)
        self.assertEqual(Game.total_score(self.new_game),(0,'NOOB'))
        
    def test_items(self):
        self.back_to_the_start()
        self.new_game2 = Game(self.room_file, self.items_file, self.puzzles_or_monsters_file)
        self.item1 = Item(1,'ROCK','defeats scissors',0,1,10)
        self.item2 = Item(2,'PAPER','defeats rock',0,3,10)
        self.item3 = Item(3,'SCISSORS','defeats paper',0,4,10)
        self.item4 = Item(4,'GOKU','defeats everything',0,2,10)
        self.new_game2.inventory.append(self.item1)
        self.assertEqual(self.new_game2.total_score(),(1,'NEWBIE'))
        self.new_game2.score = 0 # reset the score
        self.new_game2.inventory.append(self.item2)
        self.assertEqual(self.new_game2.total_score(),(4,'PROMISING'))
        self.new_game2.score = 0 # reset the score
        self.new_game2.inventory.append(self.item3)
        self.assertEqual(self.new_game2.total_score(),(8,'NINJA'))
        self.new_game2.score = 0 # reset the score
        self.new_game2.inventory.append(self.item4)
        self.assertEqual(self.new_game2.total_score(),(10,'BATMAN'))
        

    def test_oneItem(self):
        self.back_to_the_start()
        self.new_game3 = Game(self.room_file, self.items_file, self.puzzles_or_monsters_file)
        self.item5 = Item(5,'GRYFFINDOR','lion',0,10,10)
        self.new_game3.inventory.append(self.item5)
        
        self.back_to_the_start()
        self.new_game4 = Game(self.room_file, self.items_file, self.puzzles_or_monsters_file)
        self.item6 = Item(6,'SLYTHERIN','snake',0,0,10)
        self.new_game4.inventory.append(self.item6)

        self.assertEqual(self.new_game3.total_score(),(10,'BATMAN'))
        self.assertEqual(self.new_game4.total_score(),(0,'NEWBIE'))
        

    def test_twoItems(self):
        self.back_to_the_start()
        self.new_game5 = Game(self.room_file, self.items_file, self.puzzles_or_monsters_file)
        self.item7 = Item(7,'RAVENCLAW','eagle',0,5,10)
        self.item8 = Item(8,'HUFFLEPUFF','badger',0,5,10)
        self.new_game5.inventory.append(self.item7)
        self.new_game5.inventory.append(self.item8)
        self.assertEqual(self.new_game5.total_score(),(10,'BATMAN'))
        
    
        


def main():
    
    unittest.main()

main()
        
