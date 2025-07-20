import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.display.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    display = pygame.display
    screen = display.get_surface()
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        # Control FPS
        dt = clock.tick(60)/1000

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update entities
        player.update(dt)

        # Draw Screen
        screen.fill(pygame.Color(0,0,0))
        player.draw(screen)
        display.flip()


if __name__ == "__main__":
    main()


