import sys
import pygame

from settings import GameSettings
from player import Player
from projectile import Projectile
from star import Star

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

        # Spawn stars
        self.stars = pygame.sprite.Group()
        self._create_star_cloud()

    def game_loop(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.player.update()
            self._update_window()
            self._update_projectile()

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
        # Draw stars
        self.stars.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _set_windowed_mode(self):
        """Run the game in a window."""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_width))

    def _create_star_cloud(self):
        """Create the cloud of stars."""
        #Make an star
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (1 * star_width)
        number_stars_x = int(available_space_x // (1.5 * star_width))

        # Determine the number of rows of stars that fit on the screen
        player_height = self.player.rect.height
        available_space_y = (self.settings.screen_height -
                            ( 2* star_height)- player_height)
        number_rows = available_space_y // ( star_height)

        # Create the full grid of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)
    
    def _create_star(self, star_number, row_number):
        """Create star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)
       

if __name__ == "__main__":
    # Create an instance of a game and run the game.
    game = RocketGame()
    game.game_loop()
