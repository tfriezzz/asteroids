from circleshape import*
from constants import*
from shot import*

class Player(CircleShape):

    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.cooldown_timer = 0
        self.rotation = 0
        if hasattr(Player, "containers") and len(Player.containers) > 0:
            for i in Player.containers:
                i.add(self)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.cooldown_timer < 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
            forward = pygame.Vector2(0, 1).rotate(shot.rotation)
            shot.position += forward * PLAYER_SHOOT_SPEED * dt
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN

