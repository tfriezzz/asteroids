import pygame
from constants import*
from player import*




def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)

    print(f"Updatable group size: {len(updatable)}")
    print(f"Drawable group size: {len(drawable)}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

        for updatable_object in updatable:
            updatable_object.update(dt)

if __name__ == "__main__":
    main()
