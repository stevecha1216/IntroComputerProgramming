#Steve Cha, Due 2/20/2019, 002
"""
adventure.py (9 points)

Create the shortest text adventure game ever. The player is in a room with a
chest in it. The player can choose to open the chest or leave it alone. If
they open it, an outcome will be randomly generated.

1.  Ask the player for their name.
2.  Using the player's name, ask the player if they are a Warrior, Wizard or a
    Programmer (in our game, these occupations are mutually exclusive, though
    I'm sure you're all programming wizards!)
3.  Create a variable that contains the player's full name, which will consist
    of their occupation, a space, and their name. For example:
    Programmer Joe
4.  Using the len function (returns the number of characters in a string, for
    example, len('hello') -> 5), determine how long the player's full name is.
5.  Print out a greeting based on the player's full name.
    * if it's 15 characters or less, print out: .xX WELCOME <full_name> Xx.
    * othwerise, just print out: Welcome <occupation>
6.  If the player typed in Programmer (exactly, including casing) as their
    occupation, then print out: "There is no treasure here for you. The real
    treasure is the time spent programming."
7.  If the player did not type in one of the occupations specified (Wizard,
    Warrior, or Programmer), then print out: "Come back when you have a real
    job!"
8.  If the player is a Wizard or a Warrior... set the scene for the player.
    Print out a sentence or two:
    * describing the room that the player is in
    * stating that the player is standing in front of a treasure chest
9.  Then... ask the player if they would like to:
    * 'open' the chest (also accept 'OPEN' and 'Open'), or....
    * 'leave' it alone (also accept 'LEAVE' and 'Leave')
10. If they open the chest ...
    * generate a random number from 1 up-to and including 20 (use the random
    * module to do this)
    * if the number is 1 up-to and including 5, something bad happens
    * if the number is 6 up-to and including 10, nothing interesting happens
    * if the number is 11 up-to and including 15, something good happens
    * if the number is greater than 15, something great happens
11. If they choose to leave, display a message saying that nothing happens
12. If they don't enter either some permutation of 'leave' or 'open', scold
    them and end the game.

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name, the date, and your class section at the top of your
  file (above these instructions)

Example Output below (you can create your own outcomes). Anything that starts
with > is user input:

Example Run 1 (note the contents of the welcome message, and the result of
entering Programmer as an occupation):
-----
Hello adventurer, what is your name?
> I_HAVE_A_LONG_NAME
I_HAVE_A_LONG_NAME -  are you a Warrior, Wizard or Programmer?
> Programmer
There is not treasure here for you. The real treasure is the time spent programming.

Example Run 2 (note the contents of the welcome message):
-----
Hello adventurer, what is your name?
> Joe
Joe -  are you a Warrior, Wizard or Programmer?
> Wizard
.xX WELCOME Wizard Joe Xx.
You're in a dimly lit room, standing in front of an enormous steel chest.
Do you want to open the chest or leave the room?
> open
You open the chest to find a stack of pizzas with ice cream on top? That's not gross, is it?

Example Run 3 (assume that the player answered Wizard or Warrior):
-----
You're in a dimly lit room, standing in front of an enormous steel chest.
Do you want to open the chest or leave the room?
> leave
Nothing happens. Most. Boring. Game. Created.

Example Run 4 (assume that the player answered Wizard or Warrior):
-----
You're in a dimly lit room, standing in front of an enormous steel chest.
Do you want to open the chest or leave the room?
> open
As you open the chest, a bright light flashes, and you are transported to
to your Intro to Programming class (wait, is that good or bad?)

Example Run 5 (assume that the player answered Wizard or Warrior):
-----
You're in a dimly lit room, standing in front of an enormous steel chest.
Do you want to open the chest or leave the room?
> open
You open the chest to find several stacks of floppy disks. Um. Yay?

Example Run 6 (assume that the player answered Wizard or Warrior):
-----
You're in a dimly lit room, standing in front of an enormous steel chest.
Do you want to open the chest or leave the room?
> break the chest open!!!
You didn't open or leave the chest, and consequently a magic spell turns
you into a tiny lemur. Things could we worse, I guess. Game over.
"""


#asks for name
name = input("What is your name?\n>")
#asks for player class and creates a full title and name for the user
playerclass = input("Are you a warrior, wizard, or programmer?\n>")
if playerclass == "warrior" or playerclass == "Warrior":
    playername = "Warrior " + name
elif playerclass == "wizard" or playerclass == "Wizard":
    playername = "Wizard " + name
elif playerclass == "programmer" or  playerclass == "Programmer":
    playername = "Programmer " + name
else:
    playername = "Loser " + name
#finds the length of the full title and name and prints it in a certain way according to the length
namelength = len(playername)
if namelength <= 15:
    print(".xX WELCOME, " + playername + " Xx.")
elif namelength >= 16 and playername == "Loser " + name:
    print("Welcome, Loser")
else:
    print("Welcome " + playerclass)
#Programmers go back to programming while wizards and warriors are placed in a dark room with a chest
if playerclass == "programmer" or playerclass == "Programmer":
    print("There is no treasure here for you. The real treasure is the time spent programming.")
elif playerclass == "wizard" or playerclass == "warrior" or playerclass == "Wizard" or playerclass == "Warrior":
    print("You are in a dark room")
    print("You see a treasure chest in front of you.")
    print("You see a sign next to it. It says the chest is cursed.")
    print("You really want to know what's in the chest and have it.")
    print("You go back in forth in your mind.")
    print("What if the curse is lame, like you lose your leg hair permanently? Then the treasure inside the chest would totally be worth it.")
    print("What if there isn't even a curse?")
    print("You are so conflicted.")
    chest = input("Open the chest or leave it alone?\n>")
    #Open chest -RNG happens, different outcomes based on the randomly generated number
    if chest == "open" or chest == "OPEN" or chest == "Open":
        import random
        rng = random.randint(1, 20)
        if rng >= 1 and rng <= 5:
            print("Aww narticle farticles the curse is that you are now boneless.")
            print("Good news is that you can see the treasure in the chest! It's a shiny rock.")
            print("Bad news is that you can't get to it and pick it up. Or move. Oops")
        elif rng >= 6 and rng <= 10:
            print("You open the chest.")
            print("You see nothing in it.")
            print("You feel no curse.")
            print("You are disappointed.")
        elif rng >= 11 and rng <= 15:
            print("Wow you got a shiny rock! AND the curse was lame! Welp, I didn't need nosehairs anyways")
        elif rng >= 16 and rng <= 20:
            print("OMG! TWO SHINY ROCKS! AND NO CURSE AT ALL! NIIIIIICE!")
    #If You choose to leave, nothing happens
    elif chest == "LEAVE" or chest == "Leave" or chest == "leave":
        print("Nothing happens...")
    #If you don't pick between the two, I scold you and end the game
    else:
        print("WHAT THE HECK YOU BUM!?!?! YOU HAD ONE JOB!: PICK BETWEEN OPEN OR LEAVE!!! JEEZ!!!!")
#If you're not a wizard, warrior, or programmer, this happens
else:
    print("Come back when you have a real job!")


