# Align-Adventure
A Simple Adventure game built with Python Graphics implemented using the Python tkinter library - a one week project.

Adventure Games (like Scott Adams Adventures), King’s Quest, and others were all the rage when I was a kid. These games were definitely no Fortnite or Halo (most were text-only or lightweight graphics) but they were similar interactive to novels where YOU were at the center of the story, controlling the story flow and narrative. Besides being entertaining, they helped an entire generation of us to hone our critical thinking skills and inspired us to build similar open-world systems. From a computer science perspective, these simplistic “virtual worlds” allow us to practice our programming skills, and in particular some concepts of Object Oriented Programming (OOP).

What are you given?

The “starter pack” of code has everything you need to manage Rooms, Puzzles and Monsters. The code works as is, but it won’t do much until you finish the Item class, initialize the objects from the files, and “plug” everything together by writing the game management system. You are also given 3 data files which contain our “business rules” (actually the interactive story) for AlignQuest. More on that below. You are free to use all of the code given (the framework classes know how to work together), a subset of the code I’ve given you, or start entirely from scratch. It’s entirely your choice how you proceed as long as you meet the requirements.

Where’s the data?

All of the data for the basic game resides in 3 files – one for Rooms (aquest_rooms.txt), one for Items (aquest_items.txt), and one for Monsters & Puzzles (puzzles_n_monsters.txt). Rather than “hardcoding” specific business rules in the code, the code framework implements general relationships between objects and the “rules” for how those objects can interact. The actual “story” (or game) resides in the data files. In fact, you can make different “game stories” by supplying different data in the three files given. In your copious free time after you’re done with the assignment, go ahead and create a new storyline with your own items, rooms and puzzles/monsters. I’d love to see what you come up with.

How do I use the data?

Each file has the metadata (data about the data) as the first row in the file. When you read the file for input, be sure you “throw away” the first line read since that data is only there to give you a sense of what each field contains.
Everything you need to properly initialize the game objects are in the respective files. The only “tricky” element is how I’ve encoded the room movement data. Things work this way: There are 4 numbers representing North, South, East, and West from the “current room” the player is standing in (in virtual space). (a) A positive number in any of those directions means the room with that number is adjacent to the current room in that direction. (b) A zero (0) in any one of those directions means that they are blocked from going in that direction (e.g. a wall is there, or some impassable hazard). (c) A negative number means that a puzzle has affected the room. Once the puzzle or monster is de-activated, the negative number is shifted to the positive value (abs(x)) which leads us to option (a) allowing the player to freely travel to the adjacent room in that direction. All of this is handled by the Room and Puzzle classes, but hopefully this discussion gives you insight into how the data “drives” the story narrative as we automate the process flow.

e.g. (rooms data) "...The walkway leads north.|2 0 0 0|None|None|Hair Clippers|courtyard.png"

In the above example the directional values are 2 0 0 0 meaning travel North is allowed (leading to the adjacent Room 2) whilst all other directions (South, East, West) are blocked because of zeros (0) for those values
