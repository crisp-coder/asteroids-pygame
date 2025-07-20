import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from scoreboard import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialization
    pygame.init()
    font = pygame.font.Font("fp9b8a.otf", 24)
    display = pygame.display
    display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = display.get_surface()
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    # Asteroid
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    # Asteroid Field
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()
    # Shot
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatables, drawables)
    # Player
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Scoreboard
    scoreboard = Scoreboard()

    while True:
        # Control FPS
        dt = clock.tick(60)/1000

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update entities
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                print(f"Final score is {scoreboard.get_score()}")
                return

        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    scoreboard.update_score(10)
        
        # Draw Screen
        screen.fill(pygame.Color(0,0,0))
        # We iterate drawables manually to avoid using pygames group draw method 
        # which requires additionaly parameters we have not covered yet.
        for drawable in drawables:
            drawable.draw(screen)

        score_surface = font.render(
            f"Score: {scoreboard.get_score()}",
            True,
            (255, 255, 255, 255))
        screen.blit(score_surface, (0, 0))

        display.flip()




if __name__ == "__main__":
    main()


