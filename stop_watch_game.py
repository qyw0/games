# template for "Stopwatch: The Game"
import simplegui
# define global variables
t=0
s=0
s_w=0
stp=False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A=t//600
    B=t//10%60//10
    C=t//10%60%10
    D=t%10
    return str(A)+':'+str(B)+str(C)+'.'+str(D)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_b():
    timer.start()
    global stp
    stp=False
def stop_b():
    timer.stop()
    global s,s_w,stp
    if stp==False:
        s+=1
    if t%10==0 and not stp:
        s_w+=1
    stp=True
def reset_b():
    global t,s,s_w   
    stop_b()
    t=0
    s=0
    s_w=0
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t+=1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), (40, 110), 40, 'White')
    canvas.draw_text(str(s_w)+"/"+str(s), (130, 40), 25, 'Yellow')
    
# create frame
frame = simplegui.create_frame('stop_watch', 200, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
button1 = frame.add_button('Start', start_b,50)
button2 = frame.add_button('Stop', stop_b, 50)
button3 = frame.add_button('Reset', reset_b,50)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
