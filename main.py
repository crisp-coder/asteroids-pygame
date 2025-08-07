import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from scoreboard import *
from collisions import *

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

    print(f"Loading images...")

    asteroid_img_surface = pygame.image.load("images/asteroid.png")
    pygame.Surface.convert_alpha(asteroid_img_surface)

    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    # Asteroid
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    # Asteroid Field
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()
    asteroid_field.image = asteroid_img_surface
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
            if triangle_circle_collision(player, asteroid):
                print(f'Game Over!')
                print(f'Score: {scoreboard.get_score()}')
                return

        for shot in shots:
            for asteroid in asteroids:
                if circle_circle_collision(shot, asteroid):
                    shot.kill()
                    asteroid.split()
                    scoreboard.update_score(10)

        # Draw Screen
        screen.fill(pygame.Color(0,0,0))

        for drawable in drawables:
            drawable.draw(screen)

        # Draw score to screen last.
        score_surface = font.render(
            f"Score: {scoreboard.get_score()}",
            True,
            (255, 255, 255, 255))
        screen.blit(score_surface, (0, 0))

        # Show screen
        display.flip()

if __name__ == "__main__":
    main()


