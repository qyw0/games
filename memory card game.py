# implementation of card game - Memory

import simplegui
import random
state = 0
turns = 0
cards = list(range(8)) + list(range(8))
exposed = [False,False,False,False,False,False,False,False,
           False,False,False,False,False,False,False,False]
n_card1 = 0
n_card2 = 0

# helper function to initialize globals
def new_game():
    global state, turns, exposed, n_card1, n_card2
    state = 0
    turns = 0
    n_card1 = n_card2 = 0
    exposed = [False,False,False,False,False,False,False,False,
               False,False,False,False,False,False,False,False]
    random.shuffle(cards)
    label.set_text("Turns = 0")
     
# define event handlers
def mouseclick(pos):
    n = list(pos)[0]//50
    global state, n_card1, n_card2, turns

    #game state logic
    if exposed[n]:
        pass
    else:
        exposed[n]=True
        if state == 0:
            state = 1
            n_card1 = n
        elif state == 1:
            state = 2
            n_card2 = n
        else:
            if cards[n_card1] == cards[n_card2]:
                exposed[n_card1] = exposed[n_card2] = True
            else:
                exposed[n_card1] = exposed[n_card2] = False
            state = 1
            n_card1 = n
            turns += 1
            label.set_text("Turns = "+str(turns))
                          
# cards are logically 50x100 pixels in size    
def draw(canvas):
    if all(true for true in exposed):
        canvas.draw_text("Congratulations! You used "+str(turns)+" turns",[100,60],30,'Orange')
    else:
        for i in range(16):
            if exposed[i]:
                canvas.draw_text(str(cards[i]),[18+50*i,60],40,'Orange')
            else:
                canvas.draw_polygon([[50*i, 0], [50*i, 100], [50*i+50, 100], [50*i+50, 0]], 
                                    1, 'Green', 'Green')
            canvas.draw_line((50*i, 0), (50*i, 100), 1, 'White')
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
