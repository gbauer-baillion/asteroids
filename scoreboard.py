import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        # Join the 'drawable' group if it exists
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.score = 0
        self.font = pygame.font.SysFont("monospace", 35)

        # This creates the actual "image" of the text
        self.image = self.font.render(f"Score: {self.score}", True, "white")
        self.rect = self.image.get_rect()

        # Position it 20 pixels from the top-right corner
        self.rect.topright = (1260, 20)

    def add_score(self, points):
        self.score += points
        # Every time the score changes, we must "re-draw" the text image
        self.image = self.font.render(f"Score: {self.score}", True, "white")
        self.rect = self.image.get_rect()
        self.rect.topright = (1260, 20)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
