import pygame
import pgzrun

#creates a truck actor and positions it
truck = Actor('truck')
truck.pos = 200,250

#determines the width and height of the game window
WIDTH = 1000
HEIGHT = 500

#displays and draws everything onto the screen
def draw():
    #screen.fill((0, 50, 200))    #fills the background of the screen with an rgb colour
    screen.blit('red_sky_background', (0,0))    #'blits' the background onto the screen
    truck.draw()    #draws the truck on the screen

#updates the screen a 60 times a second
def update():
    if truck.left > WIDTH:
        truck.right = 20
    on_left_button()
    on_right_button()
    on_up_button()
    on_down_button()
    on_space_button()
    truck.angle = 0
        
#changes truck picture if clicked on
def on_mouse_down(pos):
    if truck.collidepoint(pos):
        set_truck_hurt()

#moves truck left
def on_left_button():
    if keyboard.left:
        truck.left -= 5

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
        animate(truck, pos=(500, 250))

#changes the costume (image) of the truck actor
def set_truck_hurt():
    truck.image = 'truck2'
    sounds.eep.play()
    clock.schedule_unique(set_truck_normal, 1.0)

#switches the truck costume back to normal
def set_truck_normal():
    truck.image = 'truck'
   
#print(truck.size)