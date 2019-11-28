import random
from random import randint
import math

#creates a front wheel and positions it
wheel_front = Actor('cartoon_van_wheel')
wheel_front.center = 245,10

#creates a back wheel and positions it
wheel_back = Actor('cartoon_van_wheel')
wheel_back.center = 100,10

#global midpoint_between_wheels
#midpoint_between_wheels = (((wheel_front.x + wheel_back.x)/2), ((wheel_front.y + wheel_back.y)/2))

#creates a vehicle body to put on the wheels
vehicle_body = Actor('cartoon_van_body_2')
vehicle_body.midbottom = 172, 250

#creates the track and positions it
track = Actor('track_1_green')
track.pos = 0,0
track.bottomleft = 0,500

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

backgrounds = ['sky_background', 'red_sky_background', 'milkyway_background', 'beige_background']
current_background = random.choice(backgrounds)

font_list = ['amatic-bold', 'amatic-sc-regular', 'arbutus-regular',
'membra', 'ostrich-regular', 'peralta-regular', 'walterturncoat']
current_font = random.choice(font_list)

music.play('automation')
#colours = [0,0,0,0]

#green track colour = (42, 149, 14, 255) (R, G, B, A)

#displays and draws everything onto the screen in the order that it's in
def draw():
    screen.blit(current_background, (0,0))    #'blits' the background onto the screen
#    screen.fill((colours[0], colours[1], colours[2]))
    track.draw()    #draws the track to the screen
    wheel_front.draw()    #draws the front wheel to the screen
    wheel_back.draw()    #draws the back wheel to the screen
    vehicle_body.draw()    #draws the vehicle_body to the screen
#    print(screen.surface.get_at((79,143)))
    '''Used to to tell me the RGB of the screen at a point, as well as the transparency'''
#    screen.draw.text("Text color", (50, 30), color=(0,0,200,0))
    screen.draw.text("Hill Vaulter", center = (500, 30), fontname='faster-one-regular', fontsize=50)
#    screen.draw.text("Top Right", topright=(990, 10), fontname=current_font)
#    screen.draw.text("Allow me to demonstrate wrapped text.", center=(120, 410), fontname=current_font, width=100, lineheight=0.75)
#    screen.draw.text("Outlined text", center = (500, 65), owidth=1.1, ocolor=(255,0,0), color=(255,255,255))
#    screen.draw.text("Drop shadow", (640, 110), shadow=(2,2), scolor="#202020")
#    screen.draw.text("Color gradient", (540, 170), color="red", gcolor="purple")
#    screen.draw.text("Transparency", (700, 240), alpha=0.5)
#    screen.draw.text("Vertical text", midleft=(400, 440), angle=45)
#    screen.draw.text("All together now:\nCombining the above options",
#        midbottom=(427,350), width=400, fontname=current_font, fontsize=35,
#        color="#AAFF00", gcolor="#66AA00", owidth=1.5, lineheight=0.75, ocolor="black", alpha=0.8)
    if track.right < 1050 and track.right > 980:
        screen.draw.text("LeVel CoMpLeTeD!", midtop=(500,425), fontname='membra', fontsize=45, color=(randint(0,255),randint(0,255),randint(0,255)))
            
#updates the screen a 60 times a second, scrolls track
def update():
    draw()
    wheels_x_position()
    wheel_front.x = wheel_front_x_position
    rotate_wheels()
    global velocity
    if (1.5 * ((wheel_front.center[1] - wheel_back.center[1])/10)) > 0:
        velocity = 1.1 * ((wheel_front.center[1] - wheel_back.center[1])/20) + 1
    else:
        velocity = 2
    track_scrolling()
    move_front_wheel_up()
    move_back_wheel_up()
    move_front_wheel_down()
    move_back_wheel_down()
    global angle_wheels_to_horiz
    angle_wheels_to_horiz = ((180*math.atan(((wheel_back.y - wheel_front.y)/(wheel_front.x - wheel_back.x))))/math.pi)
    vehicle_body.angle = angle_wheels_to_horiz
    vehicle_body.center = (((wheel_front.x + wheel_back.x)/2), ((wheel_front.y + wheel_back.y)/2))
    play_level_complete_once()
    rewind_track()
#    print((wheel_front.center[1] - wheel_back.center[1]))
#    print((34*math.sin(180*angle_wheels_to_horiz/math.pi)))
#    print(track.right)

#function and variable below used to play a 2-second chime which sounds when you complete a level
'''more complicated than thought, only need it to play at the end, but if put in update() it plays 60 times a second'''
global played
played = False
def play_level_complete_once():
    global played
    if track.right < 1010 and track.right > 980 and played == False:
        sounds.level_complete.play()
        played = True
    if track.right >= 1010 or track.right <= 980:
        played = False

#function to rewind the track back to start quickly while 'R' is held down
def rewind_track():
    if keyboard.r and track.right < 9900:
        track.right += 50

#a function to keep the distance between the front and back wheels the same, so that the wheels stay with the vehicle body
'''distance between currently set to be 145.0 pixels'''
def wheels_x_position():
    global wheel_front_x_position
    if wheel_front.y == wheel_back.y:
        wheel_front_x_position = wheel_back.x + 145.0
    elif (wheel_front.center[1] - wheel_back.center[1]) > 0.0:
        wheel_front_x_position = wheel_back.x + math.sqrt(((145.0)**2.0) - ((wheel_front.center[1] - wheel_back.center[1])**2.0))
    elif (wheel_back.center[1] - wheel_front.center[1]) > 0.0:
        wheel_front_x_position = wheel_back.x + math.sqrt(((145.0)**2.0) - ((wheel_back.center[1] - wheel_front.center[1])**2.0))

#rotates the wheels when the left/right keys are pressed
'''usually works best when set to 5'''
def rotate_wheels():
    if keyboard[keys.RIGHT]:
        wheel_front.angle -= 5
        wheel_back.angle -= 5
    if keyboard[keys.LEFT]:
        wheel_front.angle += 5
        wheel_back.angle += 5

#4 functions below are to keep the wheels on the track, and stop them going below it
'''each wheel has two functions, one to bring it up, one to bring it down'''
def move_front_wheel_up():
    colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+28))
    while colour_wheel_front_tyre_bottom == (42, 149, 14, 255):  
        wheel_front.y -= 2
        colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+28))

def move_back_wheel_up():    
    colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+28))
    while colour_wheel_back_tyre_bottom == (42, 149, 14, 255):
        colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+28))
        wheel_back.y -= 2

def move_front_wheel_down():
    colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+28))
    while colour_wheel_front_tyre_bottom != (42, 149, 14, 255):
        wheel_front.y += 2
        colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+28))

def move_back_wheel_down():
    colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+28))
    while colour_wheel_back_tyre_bottom != (42, 149, 14, 255):
        wheel_back.y += 2
        colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+28))

#function that makes the track actor 'scroll' across the screen when right key pressed
'''moves the track either left or right to make it look like truck is moving'''
def track_scrolling():
    if track.right > 1000:
        if keyboard[keys.RIGHT] and velocity > 0:
            track.right -= velocity
    if track.left < 0:
        if keyboard[keys.LEFT]:
            track.left += velocity