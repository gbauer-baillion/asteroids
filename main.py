import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")  # 1. Fill the background

        for obj in drawable:
            obj.draw(screen)  # 2. Draw objects

        pygame.display.flip()  # 3. Refresh the screen

        # 4. Handle timing
        # Limit the framerate to 60 FPS and calculate delta time
        dt = (
            clock.tick(60) / 1000
        )  # .tick(60) returns the milliseconds since the last call and divide by 1000 to convert to seconds


if __name__ == "__main__":
    main()
