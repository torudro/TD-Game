import pygame
import settings
pygame.init()
class Tower_Type:
    def __init__(self, *args):
        self.price = args[0][0]
        self.upgrade = args[0][1]
        self.resell = args[0][2]
        self.attack_stat = args[0][3]
        self.speed = args[0][4]
        self.radius = args[0][5]
        self.image = args[0][6]
        self.attack_img = args[0][7]
class Tower:
    def __init__(self, tower_type):
        self.destroy = False
        self.price = tower_type.price
        self.upgrade = tower_type.upgrade
        self.resell = tower_type.resell
        self.attack_stat = tower_type.attack_stat
        self.speed = tower_type.speed
        self.radius = tower_type.radius
        self.image = tower_type.image
        self.attack_img = tower_type.attack_img
    # each time a tower is upgrades, a new object will just be created in it's place in the same location.
    def draw(self, x, y):
        settings.display.blit(self.image, (x, y))
    #shoots attack at nearest enemy. x and y are nearest enemies coordinates
    def attack(self, x, y):
        settings.display.blit(self.attack_img, (x, y))