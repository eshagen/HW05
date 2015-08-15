#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0):
    print "%s walks through the door to see a dimly lit hallway." % user_name
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' % user_name
        if (count > 0):
            print "but %s's not happy about it" %user_name
        infinite_stairway_room(count + 1)
    
    if next == "jump out window":
        dead("You fell to your death.")


def gold_room():
    print "This room is full of gold.  How much will %s take?" % user_name

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, %s isn't greedy, %s wins!" % (user_name, user_name)
        exit(0)
    else:
        dead("You greedy bastard %s!") % user_name


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" % user_name
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at %s then slaps your face off.") % user_name
        elif next == "taunt bear" or next == "taunt" and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." % user_name
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off.") % user_name
        elif next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here %s see the great evil Cthulhu." % user_name
    print "He, it, whatever stares at %s and %s goes insane." % (user_name, user_name)
    print "Do %s flee for your life or eat their head?" % user_name

    next = raw_input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    global user_name
    try:
        user_name = raw_input("What's your name\n>")
    except:
        print "Enter a real name"
    print "%s is in a dark room." % user_name
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
