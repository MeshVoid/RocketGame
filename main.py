import sys
import pygame

from settings import GameSettings
from player import Player


class RocketGame():
    """Rocket Game class to manage game assets and game logic."""

    def __init__(self):
        """Initialize the game and initial settings/resources."""
        pygame.init()
        self.settings = GameSettings()

        self._set_windowed_mode()

        pygame.display.set_caption('Rocket Game')

        self.player = Player(self)

    def start_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_window()
            self.player.update()

    def _check_events(self):
        """Check for keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

    def _update_window(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
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
    game.start_game()
