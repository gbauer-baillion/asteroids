import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        log_state()

        pygame.display.flip()

        # 2. Limit the framerate to 60 FPS and calculate delta time
        ms_passed = clock.tick(
            60
        )  # .tick(60) returns the milliseconds since the last call
        dt = ms_passed / 1000  # divide by 1000 to convert to seconds


if __name__ == "__main__":
    main()
