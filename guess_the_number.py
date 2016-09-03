# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number=random.randrange(0, 100)
    global n
    n=0
    global m
    m=7
    global id
    id=100
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "New Game!\nrange is [0,100)\n"
    return new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game()
    global secret_number
    secret_number=random.randrange(0, 1000)
    global n
    n=0
    global m
    m=10
    global id
    id=1000
    print "New Game!\nrange is [0,1000)\n"
    
def input_guess(guess):
    # main game logic goes here	
    guess=int(guess)
    global n
    print "Guess was "+str(guess)
    
    if n==m-1 and not guess==secret_number:
        print "You Lose, the number is "+str(secret_number)+"\n\n"
        restart()
    elif guess>secret_number:
        n+=1
        print "Lower\n"+"==Remain "+str(m-n)+" guesses=="
    elif guess<secret_number:
        n+=1
        print "Higher\n"+"==Remain "+str(m-n)+" guesses=="      
    else: 
        print "Correct\n\n"
        restart()
    
def restart():
    if id==100:
        range100()
    else:
        range1000()
    
# create frame
f=simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)",range100,200)
f.add_button("Range is [0,1000)",range1000,200)
f.add_input("Enter a guess",input_guess,200)

# call new_game 
new_game()

