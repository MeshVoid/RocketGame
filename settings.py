class GameSettings():
    """Class to store all game settings"""

    def __init__(self):
        """Initialize all game settings here."""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 100)
        self.ship_speed = 1.0
        self.ship_rotation_speed = 1.0