import pygame

pygame.init()  # initialize all Pygame variables, functions, etc.
window_width = 800
window_height = 600
gameDisplay = pygame.display.set_mode((window_width, window_height))  # make a window
clock = pygame.time.Clock()
playing = True

while playing:  # main while loop that runs until the user exits the window

    for event in pygame.event.get():  # event is a mouse click, keyboard hit, etc.
        if event.type == pygame.QUIT:
            playing = False

        print(event)

    pygame.display.update()  # refresh the display
    clock.tick(60)

pygame.quit()
quit()
