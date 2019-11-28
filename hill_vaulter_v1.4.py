import pygame
import pgzrun

#creates a truck actor and positions it
truck = Actor('truck')
truck.pos = 200,250

#creates a front wheel and positions it
wheel_front = Actor('car_wheel_rough')
wheel_front.midbottom = 375,20

#creates a back wheel and positions it
wheel_back = Actor('green_dot_car_wheel_rough')
wheel_back.midbottom = 75,20

#creates the track and positions it
track = Actor('green_track')
track.pos = 0,0
track.bottomleft = 0,500

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

#green track colour = (42, 149, 14, 255) (R, G, B, A)

#displays and draws everything onto the screen in the order that it's in
def draw():
    #screen.fill((0, 50, 200))
    screen.blit('red_sky_background', (0,0))    #'blits' the background onto the screen
    track.draw()    #draws the track to the screen
    wheel_front.draw()    #draws the front wheel to the screen
    wheel_back.draw()    #draws the back wheel to the screen
    #truck.draw()
    #print(screen.surface.get_at((79,143)))
    #print(screen.surface.get_at((int(wheel_front.midbottom[0]),int(wheel_front.midbottom[1]))))
    #print(truck.midbottom)

#updates the screen a 60 times a second, scrolls track
def update():
    draw()
    #truck.left += 2
    #if truck.left > WIDTH:
        #truck.right = 0
    #on_left_button()
    #on_right_button()
    #on_up_button()
    #on_down_button()
    #on_space_button()
    #if truck.colliderect(track):
    #    truck.y += 10     #moves truck down if collides with track
    if keyboard[keys.RIGHT]:
        wheel_front.angle -= 20
        wheel_back.angle -= 20
    track_scrolling()
    #clock.schedule(track_scrolling(), 1.0)
    #clock.schedule(animate(keep_wheels_on_track()), 10.0)
    animate(move_front_wheel_up())
    animate(move_back_wheel_up())
    animate(move_front_wheel_down())
    animate(move_back_wheel_down())
    
#4 functions to below are to keep the wheels on the track, and stop them going below it
def move_front_wheel_up():
    colour_wheel_front_midbottom = screen.surface.get_at((int(wheel_front.midbottom[0]),int(wheel_front.midbottom[1])))
    while colour_wheel_front_midbottom == (42, 149, 14, 255):  
        wheel_front.y -= 2
        colour_wheel_front_midbottom = screen.surface.get_at((int(wheel_front.midbottom[0]),int(wheel_front.midbottom[1])))
    
def move_back_wheel_up():    
    colour_wheel_back_midbottom = screen.surface.get_at((int(wheel_back.midbottom[0]),int(wheel_back.midbottom[1])))
    while colour_wheel_back_midbottom == (42, 149, 14, 255):
        colour_wheel_back_midbottom = screen.surface.get_at((int(wheel_back.midbottom[0]),int(wheel_back.midbottom[1])))
        wheel_back.y -= 2

def move_front_wheel_down():
    colour_wheel_front_midbottom = screen.surface.get_at((int(wheel_front.midbottom[0]),int(wheel_front.midbottom[1])))
    while colour_wheel_front_midbottom != (42, 149, 14, 255):
        wheel_front.y += 2
        colour_wheel_front_midbottom = screen.surface.get_at((int(wheel_front.midbottom[0]),int(wheel_front.midbottom[1])))
    
def move_back_wheel_down():
    colour_wheel_back_midbottom = screen.surface.get_at((int(wheel_back.midbottom[0]),int(wheel_back.midbottom[1])))
    while colour_wheel_back_midbottom != (42, 149, 14, 255):
        wheel_back.y += 2
        colour_wheel_back_midbottom = screen.surface.get_at((int(wheel_back.midbottom[0]),int(wheel_back.midbottom[1])))
   
#function that makes the track actor 'scroll' across the screen when right key pressed
def track_scrolling():
    if track.right > 1000:
        if keyboard[keys.RIGHT]:
            track.right -= 5

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
def set_truck_hurt():
    truck.image = 'truck2'
    sounds.eep.play()
    clock.schedule_unique(set_truck_normal, 1.0)

#resets the truck image
def set_truck_normal():
    truck.image = 'truck'

#print(truck.size)