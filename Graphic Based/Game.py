'''
CS5001 Fall 2019
Homework 7
Shebna Mathew

Game class
Menu function
'''
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from room import *


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
        
        self.setup_graphics()

    def setup_graphics(self):
        '''
        Function: setup_graphics
        Input: None
        Does: Sets up the graphics for the game
        '''

        self.main = Tk()
        self.canvas = Canvas(self.main, bg = "white", height = 1000, width = 1200)

        # initial room picture
        self.filename = PhotoImage(file = "courtyard.png")
        self.image = self.canvas.create_image(50, 50, anchor = NW, image = self.filename)
        
        self.setup_labels()
        self.setup_buttons()
        

    def setup_buttons(self):
        '''
        Function: setup_buttons
        Input: None
        Does: Sets up all the buttons on the canvas
        '''

        self.look_button = Button(self.main, text = "Look",
                                  command = self.look,
                                  width = 10, activebackground = "#33b5e5",
                                  relief = FLAT).place(x = 1100, y = 50)
        
        self.drop_button = Button(self.main, text = "Drop",
                                  command = self.drop,
                                  width = 10, activebackground = "#33b5e5",
                                  relief = FLAT).place(x = 1100, y = 75)
        
        self.take_button = Button(self.main, text = "Take",
                                  command = self.take,
                                  width = 10, activebackground = "#33b5e5",
                                  relief = FLAT).place(x = 1100, y = 100)
        
        self.inventory_button = Button(self.main, text = "Inventory",
                                       command = self.display_inventory,
                                       width = 10, activebackground = "#33b5e5",
                                       relief = FLAT).place(x = 1100, y = 125)
        
        self.use_button = Button(self.main, text = "Use",
                                 command = self.use,
                                 width = 10, activebackground = "#33b5e5",
                                 relief = FLAT).place(x = 1100, y = 150)

        self.north_button = Button(self.main, text = "North",
                                   command = self.go_north,
                                   width = 10, activebackground = "#33b5e5",
                                   relief = FLAT).place(x = 1100, y = 175)
        
        self.east_button = Button(self.main, text = "East",
                                  command = self.go_east,
                                  width = 10, activebackground = "#33b5e5",
                                  relief = FLAT).place(x = 1100, y = 200)
        
        self.south_button = Button(self.main, text = "South",
                                   command = self.go_south,
                                   width = 10, activebackground = "#33b5e5",
                                   relief = FLAT).place(x = 1100, y = 225)
        
        self.west_button = Button(self.main, text = "West",
                                  command = self.go_west,
                                  width = 10, activebackground = "#33b5e5",
                                  relief = FLAT).place(x = 1100, y = 250)
        
        self.quit_button = Button(self.main, text = "Quit",
                                  command = self.quit_game,
                                  width = 10, activebackground = "#33b5e5",
                                  relief = FLAT).place(x = 1100, y = 300)

    def setup_labels(self):
        '''
        Function: setup_labels
        Input: None
        Does: Sets up all the graphic labels on the canvas
        '''

        # current room
        self.location_text = StringVar()
        self.location_text.set("Courtyard")
        self.location = Label(self.main, textvariable = self.location_text,
                              fg = "blue", font=("Courier", 30)).place(x = 700, y = 50)

        # current room description and items
        room_items = self.rooms[self.current_room].contextual_description() + "\n\n"
        for each in self.rooms[self.current_room].items:
            room_items += 'In the room, we have ' + each.name

        self.description_text = StringVar()
        self.description_text.set(room_items)
        self.description = Label(self.main, textvariable = self.description_text,
                                 fg = "blue", wraplength = 300).place(x = 700, y = 100)

        # room status - go, no-go, puzzle
        self.puzzle_box = self.canvas.create_rectangle(700, 250, 1050, 400,
                                                          outline="red", width=2)
        
        self.puzzle_title = Label(self.main, text = "Room Status", fg = "red",
                                    wraplength = 300, font=("Courier", 24)).place(x = 800, y = 260)
        self.puzzle_text = StringVar()
        self.puzzle_text.set("")
        self.puzzle = Label(self.main, textvariable = self.puzzle_text,
                            wraplength = 300, font=("Courier", 18)).place(x = 710, y = 290)

        # last item status
        self.item_box = self.canvas.create_rectangle(700, 425, 1050, 575,
                                                          outline="orange", width=2)
        
        self.item_title = Label(self.main, text = "Last Item Status", fg = "orange",
                                    wraplength = 300, font=("Courier", 24)).place(x = 750, y = 435)
        self.item_text = StringVar()
        self.item_text.set("")
        self.item_action = Label(self.main, textvariable = self.item_text,
                                 wraplength = 300, font=("Courier", 18)).place(x = 710, y = 465)

        # inventory status
        self.inventory_box = self.canvas.create_rectangle(700, 600, 1050, 750,
                                                          outline="pink", width=2)
        self.inventory_list = Label(self.main, text = "Inventory", fg = "pink",
                                    wraplength = 300, font=("Courier", 24)).place(x = 800, y = 610)
        
        self.inventory_text = StringVar()
        self.inventory_text.set("")
        self.inventory_list = Label(self.main, textvariable = self.inventory_text,
                                    wraplength = 300, font=("Courier", 18)).place(x = 710, y = 640)
        
        
        
    def quit_game(self):
        '''
        Function: quit_game
        Input: None
        Does: Shows the information dialog box with the score
            and quits the game. 
        '''
        self.score, self.rating = self.total_score()
        messagebox.showinfo(title="Score", message='\nTOTAL SCORE: ' + str(self.score)
              + '\nYOUR RATING: ' + self.rating)
        self.main.destroy()
    
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
        

    def go_north(self):
        self.go_to_room(0)

    def go_east(self):
        self.go_to_room(2)

    def go_south(self):
        self.go_to_room(1)

    def go_west(self):
        self.go_to_room(3)

    def take(self):
        while True:
            new_item = simpledialog.askstring(title="Take",
                                  prompt="What do you want to take?")
            if new_item.upper() in self.item_names: break
        self.take_item(new_item.upper())
            
    def drop(self):
        while True:
            #drop_item = input('Drop what? ')
            drop_item = simpledialog.askstring(title="Drop",
                                  prompt="What do you want to drop?")
            if drop_item.upper() in self.item_names: break
        self.drop_item(drop_item.upper())

    def use(self):
        while True:
            #use_item = input('Use what? ')
            use_item = simpledialog.askstring(title="Use",
                                  prompt="What do you want to use?")
            if use_item.upper() in self.item_names: break
        self.use_item(use_item.upper())

    def look(self):
        while True:
            look_item = simpledialog.askstring(title="Look",
                                  prompt="What do you want to look at?")
            if look_item.upper() in self.item_names: break
        index_item = self.item_names.index(look_item.upper())
        self.item_text.set(self.items[index_item].description)

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
        self.location_text.set("")
        self.description_text.set("")
        
        if self.room > 0:
            self.current_room = self.room-1
            
        elif self.room < 0:
            self.puzzle_text.set("Puzzle!" + self.rooms[self.current_room].contextual_description())
            
        else:
            self.puzzle_text.set("Nope can\'t go there.")

        self.filename = PhotoImage(file = self.rooms[self.current_room].picture)
        self.canvas.itemconfig(self.image, image=self.filename)
            
        display = self.rooms[self.current_room].name.upper()
        
        description = '\n' + self.rooms[self.current_room].contextual_description()
        
        for each in self.rooms[self.current_room].items:
            description += '\n' + 'In the room, we have ' + each.name
        
        self.location_text.set(display)
        self.description_text.set(description)


    def display_inventory(self):
        '''
        Function: display_inventory
        Input: Nothing
        Does: Displays each item a player has in his/her inventory
        '''
        display = ""
        if len(self.inventory) > 0:
            for each in self.inventory:
                display += each.name + ", "
        else:
            display += 'Empty!'
        self.inventory_text.set(display)


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
                display = item + ' ADDED to your inventory'
            else:
                display = 'Toooo heavy. You need to calm down. Maybe drop something ?'
        else:
            display = 'Can\'t take what\'s not there. *eyeroll*'
        self.item_text.set(display)
        self.display_inventory()



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
            display = item + ' DROPPED from your inventory'
            
        else:
            display = 'Can\'t drop what you don\'t have.'
            
        self.item_text.set(display)
        self.display_inventory()


            
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
                name, can_use = self.items[index_item].use()
                if success and can_use:
                    display = 'SUCCESS! You used ' + item + ' on ' + self.rooms[self.current_room].puzzles[0].name
                    self.rooms[self.current_room].puzzles[0].target.reverse_effects()
                    self.rooms[self.current_room].puzzles[0].deactivate()
                else:
                    display = 'Nothing happened. You tried.'
            else:
                display = 'Nothing to use it on.'
        else:
            display = 'You don\'t even have that. Stop swinging.'
            
        self.item_text.set(display)
        self.display_inventory()

            

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
            if self.score < 2500:
                self.rating = 'NEWBIE'
            elif self.score >= 2500 and self.score <= 5000:
                self.rating = 'PROMISING'
            elif self.score > 5000 and self.score < 7500:
                self.rating = 'NINJA'
            else:
                self.rating = 'BATMAN'
            
        return self.score, self.rating
                

    def __str__(self):
        return str(self.rooms) + str(self.items) + str(self.puzzles) + str(self.monsters)
