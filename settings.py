class GameSettings():
    """Class to store all game settings"""

    def __init__(self):
        """Initialize all game settings here."""
        # Game window settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 100)
        # Player ship settings
        self.ship_speed = 1.0
        self.ship_rotation_speed = 1.0
        # Projectile settings
        self.projectile_speed = 1.0
        self.projectile_width = 3
        self.projectile_height = 15
        self.projectile_color = (200, 200, 200)
        self.projectiles_allowed = 3