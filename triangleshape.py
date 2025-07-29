import pygame

class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        # Radius of the circle that is centered on the triangle.
        self.radius = radius
        self.points = []

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def calc_points(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius + right
        c = self.position - forward * self.radius - right
        self.points = [a, b, c]
        return self.points

