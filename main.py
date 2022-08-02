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
        self.player = Player()

        self._set_windowed_mode()

        pygame.display.set_caption('Rocket Game')
    
    def start_game(self):
        """Start the main loop of the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _set_windowed_mode(self):
        """Run the game in a window."""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_width))

if __name__== "__main__":
    # Create an instance of a game and run the game.
    game = RocketGame()
    game.start_game()