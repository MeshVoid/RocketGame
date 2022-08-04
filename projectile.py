import pygame
from pygame.sprite import Sprite


class Projectile(Sprite):
    """A class to manage projectiles fired from the ship"""

    def __init__(self, game):
        """Create a projectile at the ship's current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.projectile_color

        # Create projectile rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.projectile_width, self.settings.projectile_height)
        self.rect.midtop = game.player.rect.midtop

        # Store projectile position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move projectiles up the screen."""
        # Update the decimal position of a projectile.
        self.y -= self.settings.projectile_speed
        # Update the rect position
        self.rect.y = self.y
    
    def draw_projectile(self):
        """Draw the projectile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)