import sys
import pygame

from settings import GameSettings
from player import Player
from projectile import Projectile


class RocketGame():
    """Rocket Game class to manage game assets and game logic."""

    def __init__(self):
        """Initialize the game and initial settings/resources."""
        pygame.init()
        pygame.display.set_caption('Rocket Game')
        self.settings = GameSettings()
        self._set_windowed_mode()
        self.player = Player(self)
        self.projectiles = pygame.sprite.Group()

    def game_loop(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_window()
            self._update_projectile()
            self.player.update()

    def _check_events(self):
        """Check for keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                # print log key
                # print(event.key)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                # print log key
                # print(event.key)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        if event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_s:
            self.player.moving_down = True
        if event.key == pygame.K_SPACE:
            self._shoot()
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False
        if event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False

    def _shoot(self):
        """Shoot projectile."""
        if len(self.projectiles) < self.settings.projectiles_allowed:
            new_projectile = Projectile(self)
            self.projectiles.add(new_projectile)

    def _update_projectile(self):
        """Update position of projectile and get rid of old projectiles."""
        # Update projectile positions.
        self.projectiles.update()

        # Delete projectiles that have disappeared.
        for projectile in self.projectiles.copy():
            if projectile.rect.bottom <= 0:
                self.projectiles.remove(projectile)

    def _update_window(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for projectile in self.projectiles.sprites():
            projectile.draw_projectile()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _set_windowed_mode(self):
        """Run the game in a window."""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_width))


if __name__ == "__main__":
    # Create an instance of a game and run the game.
    game = RocketGame()
    game.game_loop()
