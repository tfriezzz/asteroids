from circleshape import*
from constants import*
import random


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

    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            vector = self.velocity.rotate(random_angle)
            angle = vector.as_polar()
            #vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.rotation = angle[1]
            asteroid_1.velocity = vector * 1.2

            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.rotation = -angle[1]
            asteroid_2.velocity = vector * 1.2


