from constants import*
from circleshape import*

class Shot(CircleShape):

    def __init__(self, x, y ,radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation
        if hasattr(Shot, "containers") and len(Shot.containers) > 0:
            for i in Shot.containers:
                i.add(self)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

