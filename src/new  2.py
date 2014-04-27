# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 5
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
DEFAULT_PADDLE_VEL = 120/60.

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,0]
ball_radius = 5

score1, score2 = 0, 0
paddle1_vel, paddle2_vel = 0, 0
paddle1_key_pressed, paddle2_key_pressed = 0, 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = (1 if direction else -1) * random.randrange(120, 240)/60.
    #The project said upward, so I understand ball_vel[1] < 0
    #ball_vel[1] = (1 if random.randrange(0,2) == 1 else -1)*random.randrange(60, 120)/60.
    ball_vel[1] = -random.randrange(60, 120)/60.

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1, score2 = 0, 0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] *= -1
    elif ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] *= -1
        
    if ball_pos[0] - BALL_RADIUS > WIDTH:
        spawn_ball(LEFT)
        score1 += 1
    elif ball_pos[0] + BALL_RADIUS < 0:
        spawn_ball(RIGHT)
        score2 += 1
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos + HALF_PAD_HEIGHT > HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos - HALF_PAD_HEIGHT < 0:
        paddle1_pos = HALF_PAD_HEIGHT
    if paddle2_pos + HALF_PAD_HEIGHT > HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos - HALF_PAD_HEIGHT < 0:
        paddle2_pos = HALF_PAD_HEIGHT
        
    if ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH and ball_pos[1] + BALL_RADIUS >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] - BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT and ball_vel[0] > 0:
        ball_vel[0] += .1 * ball_vel[0]
        ball_vel[0] *= -1
        ball_vel[1] += .1 * ball_vel[0]
    elif ball_pos[0] - BALL_RADIUS < PAD_WIDTH and ball_pos[1] + BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] - BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT and ball_vel[0] < 0:
        ball_vel[0] += .1 * ball_vel[0]
        ball_vel[0] *= -1
        ball_vel[1] += .1 * ball_vel[0]
        
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT),], 1, 'White', 'White')
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT),], 1, 'White', 'White')
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2 - 20, 20), 15, 'White')
    canvas.draw_text(str(score2), (WIDTH/2 + 12, 20), 15, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_key_pressed, paddle2_key_pressed
    if key == simplegui.KEY_MAP["up"]:
        paddle2_key_pressed += 1
        paddle2_vel = -DEFAULT_PADDLE_VEL
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_key_pressed += 1
        paddle2_vel = DEFAULT_PADDLE_VEL
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_key_pressed += 1
        paddle1_vel = -DEFAULT_PADDLE_VEL
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_key_pressed += 1
        paddle1_vel = DEFAULT_PADDLE_VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_key_pressed, paddle2_key_pressed
    if key == simplegui.KEY_MAP["up"]:
        paddle2_key_pressed -= 1
        if paddle2_key_pressed > 0:
            paddle2_vel = DEFAULT_PADDLE_VEL
        else:
            paddle2_vel, paddle2_key_pressed = 0, 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_key_pressed -= 1
        if paddle2_key_pressed > 0:
            paddle2_vel = -DEFAULT_PADDLE_VEL
        else:
            paddle2_vel, paddle2_key_pressed = 0, 0
            
    if key == simplegui.KEY_MAP["w"]:
        paddle1_key_pressed -= 1
        if paddle1_key_pressed > 0:
            paddle1_vel = DEFAULT_PADDLE_VEL
        else:
            paddle1_vel, paddle1_key_pressed = 0, 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_key_pressed -= 1
        if paddle1_key_pressed > 0:
            paddle1_vel = -DEFAULT_PADDLE_VEL
        else:
            paddle1_vel, paddle1_key_pressed = 0, 0
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game)

# start frame
new_game()
frame.start()
