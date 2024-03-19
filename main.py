# Pygame Movement demo
import pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode([600, 500])

clock = pygame.time.Clock()

x = 250
y = 250

dx = 100
dy = 100

# Set up the main loop
running = True
while running:
    dt = clock.tick()

    # End the main loop if the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window white
    screen.fill((225, 225, 225))

    # New code here
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 50)

    if y <= 50 or y >= 450:
        dy *= -1
    if x <= 50 or x >= 550:
        dx *= -1

    x += dx * (dt/1000)
    y += dy * (dt/1000)

    # Update the window
    pygame.display.update()

pygame.quit()