import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # 1. Kill the current asteroid

        if (
            self.radius <= ASTEROID_MIN_RADIUS
        ):  # 2. If it's small enough, just stop here
            return

        else:  # 3. Handle the split logic
            log_event("asteroid_split")

            random_angle = random.uniform(20, 50)

            # 4. Create 2 new velocity vectors by rotating the current one
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)

            # 5. Calculate radius of smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # 6. Instantiate 2 new smaller asteroids at current position
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            # 7. Assign the new velocities multiplied by 1.2 to make them faster
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2.velocity = new_velocity2 * 1.2
