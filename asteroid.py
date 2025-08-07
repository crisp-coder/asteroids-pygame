from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = None

    def setImage(self, image):
        self.image = image

    def getImage(self, image):
        if self.image:
            return self.image
        else:
            return None

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255, 255),
            (self.position.x, self.position.y),
            self.radius, 2
            )
        if self.image:
            screen.blit(self.image, self.position - (18, 16))

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid1.setImage(self.image)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
        asteroid2.setImage(self.image)


