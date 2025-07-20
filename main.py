import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialization
    pygame.init()
    pygame.display.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display = pygame.display
    screen = display.get_surface()
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)

    AsteroidField.containers = (updatables)

    # Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #AsteroidField
    asteroid_field = AsteroidField()

    while True:
        # Control FPS
        dt = clock.tick(60)/1000

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update entities
        updatables.update(dt)

        # Draw Screen
        screen.fill(pygame.Color(0,0,0))
        # We iterate drawables manually to avoid using pygames group draw method 
        # which requires additionaly parameters we have not covered yet.
        for drawable in drawables:
            drawable.draw(screen)

        display.flip()


if __name__ == "__main__":
    main()


