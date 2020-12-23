'''
CS5001 Fall 2019
Homework 7
Shebna Mathew

Game class
Menu function
'''

from room import *
import pickle


def menu(options):
    '''
    Reusing lab menu function
    Input: list containing the list of options
    Returns: user choice
    Does: loops through the option list and
    displays it to the user and then prompts for their choice
    '''
    valid_options = []
    
    while True:
        print('\n' + '-'*27 + '\nWhat do you want to do?\n')
        
        for each in options:
            print(each[0], ': ', each[1])
            if ',' in each[0]:
                valid_options.extend(list(each[0].replace(',','')))
            valid_options.append(each[0])
        user_choice = (input('\nYour choice:')).upper()
        if user_choice in valid_options: return user_choice


'''
Class : Game
Functions: load data from files: Room, Items, Puzzles, Monsters;
    start a game, go to a room, display inventory,
    take an item, drop an item, use an item, calculate total score.
'''

class Game:
    
    def __init__(self, room_file, items_file, puzzles_or_monsters_file):
        self.rooms = []
        self.items = []
        self.puzzles = []
        self.monsters = []
        self.item_names = []
        self.puzzles_names = []
        self.monsters_names = []
        self.item_in_room = {}
        self.load_rooms(room_file)
        self.load_items(items_file)
        self.load_puzzles_and_monsters(puzzles_or_monsters_file)
        self.inventory = []
        self.current_room = 0
        self.score = 0
        self.weight = 0
        self.rating = 'NOOB'
        

    
    def load_rooms(self, room_file):
        '''
        Function: load_rooms
        Input: File containing the Room data
        Does: Iterates over each line extracting data,
            creating a Room object for each room,
            populating each field in the object with the correct data,
            gets the item(s) present in each room and stores them in item_in_room,
            a dictionary where key: item name, value: room name,
            to correctly link the item object to its room when Item object are created.
        '''
        next(room_file)
        self.infile = room_file.readlines()
        for each in self.infile:
            each = each.strip().split('|')
            each[3] = [int(i) for i in each[3].split()]
            room = Room(each[0],each[1],each[2],each[3],each[7])
            self.rooms.append(room)
            for every in each[6].upper().split(','):
                self.item_in_room[every] = int(each[0])

        

    def load_items(self, items_file):
        '''
        Function: load_items
        Input: File containing the Items data
        Does: Iterates over each line extracting data,
            creating an Item object for each item,
            populating each field in the object with the correct data.
            Iterate over the item_in_room dictionary and
            link an item to its corresponding room.
        '''
        next(items_file)
        self.infile = items_file.readlines()
        for each in self.infile:
            each = each.strip().split('|')
            self.items.append(Item(each[0],each[1].upper(),each[2],int(each[3]),int(each[4]),int(each[5])))
            self.item_names.append(each[1].upper())
            if each[1].upper() in self.item_in_room:
                self.rooms[self.item_in_room[each[1].upper()]-1].add_item(self.items[-1])
            
            

    def load_puzzles_and_monsters(self, puzzles_or_monsters_file):
        '''
        Function: load_puzzles_and_monsters
        Input: File containing the Puzzles and Monsters data
        Does: Iterates over each line extracting data,
            creating a Puzzle object for each Puzzle and Monster and
            a Monster object for each Monster
            populating each field in the object with the correct data.
            Link a Puzzle/Monster to its corresponding room(if it has a room as a target)
        '''
        next(puzzles_or_monsters_file)
        self.infile = puzzles_or_monsters_file.readlines()
        
        for each in self.infile:
            each = each.strip().split('|')
            each = [True if i == 'T' else i for i in each]
            self.puzzles.append(Puzzle(each[0],each[1],each[5],bool(each[2]),bool(each[3]),each[4],each[6]))
            self.puzzles_names.append(each[0].upper())
            if each[-1] != '*':
                self.monsters.append(Monster(each[0],each[1],each[5],bool(each[2]),bool(each[3]),each[4],each[6],bool(each[7]),each[8]))
                self.monsters_names.append(each[0].upper())

            if 'Room' in each[5]:
                index = int(each[5].replace('Room ',''))
                self.puzzles[-1].target = self.rooms[index - 1]
                self.rooms[index - 1].add_puzzle(self.puzzles[-1])
        

    
    def start_game(self, choices):
        '''
        Function: start_game
        Input: all the choices a user has to play a game
        Does: Keep prompting the player for a move. A player can choose to
            go in a certain direction, take an item, use an item, drop an item,
            look at an item, see what's in the inventory.
            Each move calls a sub function to complete the action.
        '''
        print('*'*49)
        print('*'+ ' '*9 + ' Welcome to this \'adventure\'.' + ' '*9 +'*')
        print('*'*49)
        
        while True:

            # keep displaying the current room a player is in, and the items
            print('-'*50)
            print('You are in the', self.rooms[self.current_room].name.upper())
            print(self.rooms[self.current_room].contextual_description())
            for each in self.rooms[self.current_room].items:
                        print('In the room, we have ', each.name)
                        
            user_choice = menu(choices)

            if user_choice == 'N':
                self.go_to_room(0)
                
            elif user_choice == 'S':
                self.go_to_room(1)

            elif user_choice == 'E':
                self.go_to_room(2)
                
            elif user_choice == 'W':
                self.go_to_room(3)
                
            elif user_choice == 'I':
                self.display_inventory()
                    
            elif user_choice == 'T':
                while True:
                    new_item = input('Take what? ')
                    if new_item.upper() in self.item_names: break
                self.take_item(new_item.upper())

            elif user_choice == 'D':
                while True:
                    drop_item = input('Drop what? ')
                    if drop_item.upper() in self.item_names: break
                self.drop_item(drop_item.upper())
                
            elif user_choice == 'U':
                while True:
                    use_item = input('Use what? ')
                    if use_item.upper() in self.item_names: break
                self.use_item(use_item.upper())
                
            elif user_choice == 'L':
                while True:
                    look_item = input('At what? ')
                    if look_item.upper() in self.item_names: break
                index_item = self.item_names.index((look_item.upper()))
                print(self.items[index_item].description)

            else:
                outfile = open('outfile.pkl','wb')
                pickle.dump(self, outfile, pickle.HIGHEST_PROTOCOL)
                break

        # display the total score & rating once a player quits
        self.score, self.rating = self.total_score()
        print('\nTOTAL SCORE: ' + str(self.score)
              + '\nYOUR RATING: ' + self.rating)


    def go_to_room(self, room_direction):
        '''
        Function: go_to_room
        Inputs: the relative direction from the current room
        Does: checks if a player can go in that direction.
            A positive number indicates an open way.
            A negative number indicates that that direction is blocked by a puzzle.
            The player has to solve the puzzle first to get through to that direction.
            A zero indicates a closed path.
        '''
        
        self.room = self.rooms[self.current_room].adjacent_rooms[room_direction]
        if self.room > 0:
            self.current_room = self.room-1
            
        elif self.room < 0:
            print('PUZZLE !')
            self.rooms[self.current_room].contextual_description()
            
        else:
            print('Nope can\'t go there.')


    def display_inventory(self):
        '''
        Function: display_inventory
        Input: Nothing
        Does: Displays each item a player has in his/her inventory
        '''

        if len(self.inventory) > 0:
            for each in self.inventory: print(each.name)
        else:
            print('Empty!')


    def take_item(self, item):
        '''
        Function: take_item
        Input: an item name
        Does: checks if an item is available in the current room,
            if it is, checks if the total weight in the inventory exceeds 10,
            if it is does not, the item is added to the inventory
        '''

        index_item = self.item_names.index(item)

        if self.items[index_item] in self.rooms[self.current_room].items:
            if (self.items[index_item].weight + self.weight) <= 10:
                self.weight += self.items[index_item].weight
                self.inventory.append(self.items[index_item])
                self.rooms[self.current_room].items.remove(self.items[index_item])
                print(item + ' ADDED to your inventory')
            else:
                print('Toooo heavy. You need to calm down.')
        else: print('Can\'t take what\'s not there. *eyeroll*')



    def drop_item(self, item):
        '''
        Function: drop_item
        Input: an item name
        Does: checks if the item is present in the inventory
            and then drops it in the current room
        '''

        index_item = self.item_names.index(item)
        if self.items[index_item] in self.inventory:
            self.inventory.remove(self.items[index_item])
            self.rooms[self.current_room].add_item(self.items[index_item])
            self.weight -= self.items[index_item].weight
            print(item + ' DROPPED from your inventory')
        else:
            print('Can\'t drop what you don\'t have.')


            
    def use_item(self, item):
        '''
        Function: use_item
        Input: an item name
        Does: checks if the item is presen in the inventory,
            checks to see if there's a puzzle to use it against,
            tries to solve the puzzle and if it works, the item is used
        '''

        index_item = self.item_names.index((item.upper()))
        if self.items[index_item] in self.inventory:
            if self.rooms[self.current_room].has_puzzle():
                success = self.rooms[self.current_room].puzzles[0].try_to_solve(item)
                can_use = self.items[index_item].use()
                if success and can_use:
                    print('SUCCESS! You used ' + item + ' on ' + self.rooms[self.current_room].puzzles[0].name)
                    self.rooms[self.current_room].puzzles[0].target.reverse_effects()
                    self.rooms[self.current_room].puzzles[0].deactivate()
                else: print('Nothing happened. You tried.')
            else: print('Nothing to use it on.')
        else: print('You don\'t even have that. Stop swinging.')

            

    def total_score(self):
        '''
        Function: total_score
        Input: Nothing
        Does: calculates the total score by adding up the values
            of all the items in the player's inventory
            and displaying a suitable rating
        '''

        if len(self.inventory) > 0:
            for each in self.inventory:
                self.score += each.value
            if self.score < 3:
                self.rating = 'NEWBIE'
            elif self.score >= 3 and self.score <= 7:
                self.rating = 'PROMISING'
            elif self.score > 7 and self.score < 10:
                self.rating = 'NINJA'
            else:
                self.rating = 'BATMAN'
            
        return self.score, self.rating
                

    def __str__(self):
        return str(self.rooms) + str(self.items) + str(self.puzzles) + str(self.monsters)
