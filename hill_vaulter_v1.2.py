import pygame
import pgzrun

#creates a truck actor and positions it
truck = Actor('truck')
truck.pos = 200,250

#creates the track and positions it
track = Actor('green_track')
track.pos = 0,0
track.bottomleft = 0,500

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

#green track colour = (42, 149, 14, 255) (R, G, B, A)

#displays and draws everything onto the screen
def draw():
#    screen.fill((0, 50, 200))    #fills the background of the screen with an rgb colour
    screen.blit('red_sky_background', (0,0))    #'blits' the background onto the screen
    track.draw()    #draws the track on the screen
    truck.draw()    #draws the truck on the screen
#    print(screen.surface.get_at((79,143)))
#    print(truck.midbottom)

#updates the screen a 60 times a second, scrolls track
def update():
#    truck.left += 2
#    if truck.left > WIDTH:
#        truck.right = 0
#    on_left_button()
#    on_right_button()
    on_up_button()
    on_down_button()
    #on_space_button()
    track_scrolling()

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

#changes the costume (image) of the truck actor
def set_truck_hurt():
    truck.image = 'truck2'
    sounds.eep.play()
    clock.schedule_unique(set_truck_normal, 1.0)

#switches the truck costume back to normal
def set_truck_normal():
    truck.image = 'truck'
   
#print(truck.size)