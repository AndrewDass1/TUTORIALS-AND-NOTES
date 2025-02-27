import pygame, sys

pygame.init() #Imports all pygame commands

screen = pygame.display.set_mode((insert_number_for_screen_width, insert_number_for_screen_height))
clock = pygame.time.Clock() # Summons pygame's clock to keep track of time

while True: # to make the screen run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #When the user wants to close the pygame, this for loop allows it to be closed

    screen.fill("red") # Game code to add objects or change visuals goes here

    #Code below to display the changes
    pygame.display.flip()

    clock.tick()

pygame.quit()
