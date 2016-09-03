# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

direction = random.choice([-1, 1])
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT / 2 - PAD_HEIGHT / 2
paddle2_pos = HEIGHT / 2 - PAD_HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
s1 = 0
s2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = direction*random.randrange(150, 220)/100
    ball_vel[1] = -random.randrange(90, 160)/100     

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, direction # these are numbers
    global s1, s2  # these are ints
    s1 = 0
    s2 = 0
    paddle1_pos = HEIGHT / 2 - PAD_HEIGHT / 2
    paddle2_pos = HEIGHT / 2 - PAD_HEIGHT / 2
    direction = random.choice([-1, 1])
    spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, s1, s2, direction        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle([WIDTH/2, HEIGHT/2], 100, 1, "Grey")    
    # update ball
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS: #left--player1
        if paddle1_pos < ball_pos[1] < paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]*1.1            
        else:  
            s2 += 1
            direction = 1
            spawn_ball()
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:#right--player2
        if paddle2_pos < ball_pos[1] < paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]*1.1            
        else:
            s1 += 1
            direction = -1
            spawn_ball()
            
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS: #horizontal
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    # update paddle's vertical position, keep paddle on the screen    
    paddle1_pos += paddle1_vel   
    paddle2_pos += paddle2_vel

    # draw paddles
    p1_list = [(0, paddle1_pos), (0, paddle1_pos + PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + PAD_HEIGHT), (PAD_WIDTH, paddle1_pos)]
    p2_list = [(WIDTH - PAD_WIDTH, paddle2_pos), (WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT), (WIDTH, paddle2_pos + PAD_HEIGHT), (WIDTH, paddle2_pos)]
    canvas.draw_polygon(p1_list, 1, "Yellow", "Yellow")
    canvas.draw_polygon(p2_list, 1, "Yellow", "Yellow")
    # determine whether paddle and ball collide    
    if paddle1_pos <= 0:    
        paddle1_pos = 0
    if paddle1_pos > HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if paddle2_pos < 0:
        paddle2_pos = 0
    if paddle2_pos > HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
    # draw scores
    canvas.draw_text("P1: "+str(s1), (120, 50), 25, 'Red')
    canvas.draw_text("P2: "+str(s2), (420, 50), 25, 'Red')
def keydown(key):
    global paddle1_vel, paddle2_vel   
    if key == simplegui.KEY_MAP["w"]: #paddle1
        paddle1_vel = -2
    if key == simplegui.KEY_MAP["s"]: 
        paddle1_vel = 2 
    if key == simplegui.KEY_MAP['up']: #paddle2
        paddle2_vel = -2
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 2
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]: #paddle1
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']: #paddle2
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
