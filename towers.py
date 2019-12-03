import pygame
import settings
pygame.init()
class Tower_Type:
    def __init__(self, *args):
        self.price = args[0][0]
        self.upgrade = args[0][1]
        self.resell = args[0][2]
        self.attack = args[0][3]
        self.speed = args[0][4]
        self.radius = args[0][5]
        self.image = args[0][6]
        self.image = pygame.image.load(self.image)
class Tower:
    def __init__(self, tower_type):
        self.destroy = False
        self.price = tower_type.price
        self.upgrade = tower_type.upgrade
        self.resell = tower_type.resell
        self.attack = tower_type.attack
        self.speed = tower_type.speed
        self.radius = tower_type.radius
        self.image = tower_type.image
    # each time a tower is upgrades, a new object will just be created in it's place in the same location.
    def draw(self, x, y):
        settings.display.blit(self.image, (x, y))