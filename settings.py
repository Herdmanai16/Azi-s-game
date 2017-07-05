import random

# game options/settings
TITLE = "Best Thing Since Sliced Bread"
WIDTH = 750
HEIGHT = 700
FPS = 69
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
WIDTH1 = 70.98
WIDTH2 = 120


# player properties
PLAYER_ACC = 8
PLAYER_FRICTION = -0.2
PLAYER_GRAV = 0.8
PLAYER_JUMP = 30

# starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 10),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DEEP_BLUE = (0, 100, 200)
PLATFORM = (0, 180, 100)
RANDOM = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
PLAT_RANDOM = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
BACKGROUND = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
