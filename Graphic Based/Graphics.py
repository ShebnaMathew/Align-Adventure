#import turtle
from tkinter import *
from tkinter import ttk
#import tkinter as tk
##ececec

class Graphics:

    def __init__(self):

        self.main = Tk()
        self.setup()

    def setup(self):
        self.canvas = Canvas(self.main, bg = "white", height = 500, width = 1000)
        self.filename = PhotoImage(file = "courtyard.png")
        self.image = self.canvas.create_image(50, 50, anchor = NW, image = self.filename)

        self.location = Label(self.main, text = "Courtyard", fg = "blue")
        self.location.configure(font=("Courier", 44))
        self.location.place(x = 500, y = 50)

        self.description = Label(self.main, text = "A beautiful courtyard with flowers\n on both sides of the stone walkway.\nThe walkway leads north.", fg = "blue")
        self.description.place(x = 500, y = 100)
        
        
        self.look_button = Button(self.main, text = "Look", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 50)
        self.drop_button = Button(self.main, text = "Drop", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 75)
        self.take_button = Button(self.main, text = "Take", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 100)
        self.inventory_button = Button(self.main, text = "Inventory", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 125)
        self.use_button = Button(self.main, text = "Use", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 150)

        self.north_button = Button(self.main, text = "North", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 175)
        self.east_button = Button(self.main, text = "East", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 200)
        self.south_button = Button(self.main, text = "South", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 225)
        self.west_button = Button(self.main, text = "West", width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 250)
        
        self.quit_button = Button(self.main, text = "Quit", command = self.quit_game, width = 10, activebackground = "#33b5e5", relief = FLAT).place(x = 900, y = 300)
        #self.quit_button.configure(width = 10, activebackground = "#33b5e5", relief = FLAT)
        #self.quit_button.place(x = 900, y = 300)
        
    

    def quit_game(self):
        self.main.destroy()
    
