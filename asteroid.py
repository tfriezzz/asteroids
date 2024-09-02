from circleshape import*
from constants import*


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        if hasattr(Asteroid, "containers") and len(Asteroid.containers) > 0:
                for i in Asteroid.containers:
                    i.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * TEMP_ASTEROID_SPEED * dt

        
