# Pygame Movement demo
import pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode([500, 500])

# Set up the main loop
running = True
while running:

    # End the main loop if the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window white
    screen.fill((225, 225, 225))

    # New code here

    # Update the window
    pygame.display.update()

pygame.quit()