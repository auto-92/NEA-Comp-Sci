import pygame
import pgzrun
import random
import math

#creates a truck actor and positions it
truck = Actor('truck')
truck.pos = 200,250

#creates a front wheel and positions it
wheel_front = Actor('car_wheel_rough')
wheel_front.center = 375,20

#creates a back wheel and positions it
wheel_back = Actor('car_wheel_rough')
wheel_back.center = 75,20

#creates a vehicle body to put on the wheels
vehicle_body = Actor('fast_car_body', anchor=((wheel_back.center)))

#creates the track and positions it
track = Actor('track_1_rock')
track.pos = 0,0
track.bottomleft = 0,500

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

#velocity = math.exp(float((wheel_front.center[1] - wheel_back.center[1])/10))

#green track colour = (42, 149, 14, 255) (R, G, B, A)
#brown colour of track = (106, 79, 13, 255)
#beige background colour = (231, 199, 84, 255)

#displays and draws everything onto the screen in the order that it's in
def draw():
#    screen.fill((0, 50, 200))
    screen.blit('beige_background', (0,0))    #'blits' the background onto the screen
    track.draw()    #draws the track to the screen
    wheel_front.draw()    #draws the front wheel to the screen
    wheel_back.draw()    #draws the back wheel to the screen
#    vehicle_body.draw()
#    truck.draw()
#    print(screen.surface.get_at((1,1)))
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
    colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1]+55)))
    while colour_wheel_front_tyre_bottom != (231, 199, 84, 255):  
        wheel_front.y -= 2
        colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1]+55)))
def move_back_wheel_up():    
    colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1]+55)))
    while colour_wheel_back_tyre_bottom != (231, 199, 84, 255):
        colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1]+55)))
        wheel_back.y -= 2
def move_front_wheel_down():
    colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1]+55)))
    while colour_wheel_front_tyre_bottom == (231, 199, 84, 255):
        wheel_front.y += 2
        colour_wheel_front_tyre_bottom = screen.surface.get_at((int(wheel_front.center[0]),int(wheel_front.center[1]+55)))
def move_back_wheel_down():
    colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1]+55)))
    while colour_wheel_back_tyre_bottom == (231, 199, 84, 255):
        wheel_back.y += 2
        colour_wheel_back_tyre_bottom = screen.surface.get_at((int(wheel_back.center[0]),int(wheel_back.center[1]+55)))
        
#function that makes the track actor 'scroll' across the screen when right key pressed
def track_scrolling():
    global velocity
    if track.right > 1000:
        if keyboard[keys.RIGHT]:
            track.right -= velocity
    if track.left < 0:
        if keyboard[keys.LEFT]:
            track.left += velocity

#changes truck picture if clicked on
def on_mouse_down(pos):
    if truck.collidepoint(pos):
        set_truck_hurt()

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

#changes truck image to another and plays a sound
#def set_truck_hurt():
#    truck.image = 'truck2'
#    sounds.eep.play()
#    clock.schedule_unique(set_truck_normal, 1.0)
#
#resets the truck image
#def set_truck_normal():
#    truck.image = 'truck'

#print(truck.size)


