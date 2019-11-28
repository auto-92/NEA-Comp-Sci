import pygame
import pgzrun
import random
from math import sqrt, atan

#creates a truck actor and positions it
truck = Actor('truck')
truck.pos = 200,250

#creates a front wheel and positions it
wheel_front = Actor('cartoon_van_wheel')
wheel_front.center = 200,10

#creates a back wheel and positions it
wheel_back = Actor('cartoon_van_wheel')
wheel_back.center = 100,10

#creates a vehicle body to put on the wheels
vehicle_body = Actor('cartoon_van_body', anchor=((wheel_back.center[0], wheel_back.center[1])))

#creates the track and positions it
track = Actor('track_1_green')
track.pos = 0,0
track.bottomleft = 0,500

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

backgrounds = ['sky_background', 'red_sky_background', 'milkyway_background', 'beige_background']
current_background = random.choice(backgrounds)

#green track colour = (42, 149, 14, 255) (R, G, B, A)

#displays and draws everything onto the screen in the order that it's in
def draw():
#    screen.fill((0, 50, 200))
    screen.blit(current_background, (0,0))    #'blits' the background onto the screen
    track.draw()    #draws the track to the screen
    wheel_front.draw()    #draws the front wheel to the screen
    wheel_back.draw()    #draws the back wheel to the screen
    vehicle_body.draw()
#    truck.draw()
#    print(screen.surface.get_at((79,143)))
#    print(screen.surface.get_at((int(wheel_front.midbottom[0]),int(wheel_front.midbottom[1]))))
#    print(truck.midbottom)

#updates the screen a 60 times a second, scrolls track
def update():
    draw()
#    truck.left += 2
#    if truck.left > WIDTH:
#        truck.right = 0
#    on_left_button()
#    on_right_button()
#    on_up_button()
#    on_down_button()
#    on_space_button()
#    if truck.colliderect(track):
#        truck.y += 10     #moves truck down if collides with track
    wheels_x_position()
    wheel_front.x = wheel_front_x_position
    vehicle_body.angle = 0
#    print_distance_between_wheels()
#    print_distance_between_wheels_1()
#    print_distance_between_wheels_2()
    rotate_wheels()
    global velocity
    if (1.5 * ((wheel_front.center[1] - wheel_back.center[1])/10)) > 0:
        velocity = 1.1 * ((wheel_front.center[1] - wheel_back.center[1])/20) + 1
    else:
        velocity = 2
    track_scrolling()
#    clock.schedule(animate(keep_wheels_on_track()), 10.0)
    animate(move_front_wheel_up())
    animate(move_back_wheel_up())
    animate(move_front_wheel_down())
    animate(move_back_wheel_down())
#    print(wheel_front.center[1] - wheel_back.center[1])
#    get_bottom_of_front_tyre()
#    get_bottom_of_back_tyre()
#    print(vehicle_body.distance_to(wheel_back))


#def get_bottom_of_front_tyre():
#    global bottom_of_front_tyre
#    bottom_of_front_tyre = (wheel_front.center[0], wheel_front.center[1]+50)
#    print(bottom_of_front_tyre)
#    
#def get_bottom_of_back_tyre():
#    global bottom_of_back_tyre
#    bottom_of_back_tyre = (wheel_back.center[0], wheel_back.center[1]+50)
#    print(bottom_of_back_tyre)
#    print(track.left)

#a function to keep the distance between the front and back wheels the same, so that the body doesnt stretch up/down hill
def wheels_x_position():
    global wheel_front_x_position
    if wheel_front.y == wheel_back.y:
        wheel_front_x_position = wheel_back.x + 100.0
    elif (wheel_front.center[1] - wheel_back.center[1]) > 0.0:
        wheel_front_x_position = wheel_back.x + sqrt(((100.0)**2.0) - ((wheel_front.center[1] - wheel_back.center[1])**2.0))
    elif (wheel_back.center[1] - wheel_front.center[1]) > 0.0:
        wheel_front_x_position = wheel_back.x + sqrt(((100.0)**2.0) - ((wheel_back.center[1] - wheel_front.center[1])**2.0))
        
#a function to print the distance between the centres of the two wheels
def print_distance_between_wheels():
    if (wheel_front.center[1] - wheel_back.center[1]) == 0:
        print((wheel_front.center[0] - wheel_back.center[0]))

#rotates the wheels when the left/right keys are pressed
def rotate_wheels():
    if keyboard[keys.RIGHT]:
        wheel_front.angle -= 50
        wheel_back.angle -= 50
    if keyboard[keys.LEFT]:
        wheel_front.angle += 50
        wheel_back.angle += 50

#4 functions below are to keep the wheels on the track, and stop them going below it
def move_front_wheel_up():
    colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+25))
    while colour_wheel_front_tyre_bottom == (42, 149, 14, 255):  
        wheel_front.y -= 2
        colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+25))
def move_back_wheel_up():    
    colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+25))
    while colour_wheel_back_tyre_bottom == (42, 149, 14, 255):
        colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+25))
        wheel_back.y -= 2
def move_front_wheel_down():
    colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+25))
    while colour_wheel_front_tyre_bottom != (42, 149, 14, 255):
        wheel_front.y += 2
        colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1])+25))
def move_back_wheel_down():
    colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+25))
    while colour_wheel_back_tyre_bottom != (42, 149, 14, 255):
        wheel_back.y += 2
        colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1])+25))

#function that makes the track actor 'scroll' across the screen when right key pressed
def track_scrolling():
    if track.right > 1000:
        if keyboard[keys.RIGHT] and velocity > 0:
            track.right -= velocity
    if track.left < 0:
        if keyboard[keys.LEFT]:
            track.left += velocity
            
#moves truck left
def on_left_button():
    if keyboard.left:
        truck.left -= 7

#moves truck right
def on_right_button():
    if keyboard.right:
        truck.right += 5

#moves truck up
def on_up_button():
    if keyboard.up:
        truck.y -= 5

#moves truck down
def on_down_button():
    if keyboard.down:
        truck.y += 5
        
#moves the truck to a certain position using an in-built function
def on_space_button():
    if keyboard.space:
        animate(truck, pos=(400, 100))

#print(truck.size)