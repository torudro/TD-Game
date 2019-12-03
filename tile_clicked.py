import pygame
import settings
import tower_enemy_info
import towers
pygame.init()
tower_enemy_info.tower_zones_available()
tower_zones_list = tower_enemy_info.tower_zones_list
tile1 = tower_zones_list[0]
tile2 = tower_zones_list[1]
tile3 = tower_zones_list[2]
tile4 = tower_zones_list[3]
tile5 = tower_zones_list[4]
tile6 = tower_zones_list[5]
# mode 1-6 for tiles, 7-9 for tower creation,
MODE = 0
tile1_obj = None
tile2_obj = None
tile3_obj = None
tile4_obj = None
tile5_obj = None
tile6_obj = None
blit_again = False
#button set 1
tile1_b1 = False
tile2_b1 = False
tile3_b1 = False
tile4_b1 = False
tile5_b1 = False
tile6_b1 = False
#button set 2
tile1_b2 = False
tile2_b2 = False
tile3_b2 = False
tile4_b2 = False
tile5_b2 = False
tile6_b2 = False
def button_pressed(nextreference):
    global MODE
    global tile1_obj
    global tile2_obj
    global tile3_obj
    global tile4_obj
    global tile5_obj
    global tile6_obj
    global blit_again
    global tile1_b1
    global tile2_b1
    global tile3_b1
    global tile4_b1
    global tile5_b1
    global tile6_b1
def beige_buy_button(x, y):
    beige_tower_button = (x - 64, y - 32, 60, 40)
    pygame.draw.rect(settings.display, (210, 180, 140), pygame.Rect(beige_tower_button))
    beige_tower_label = pygame.font.SysFont('comicsans', 20).render('beige [a]', 1, (0, 0, 0))
    settings.display.blit(beige_tower_label, (x - 64, y - 32))
def blue_buy_button(x, y):
    blue_tower_button = (x - 64, y + 32, 60, 40)
    pygame.draw.rect(settings.display, (0, 0, 255), pygame.Rect(blue_tower_button))
    blue_tower_label = pygame.font.SysFont('comicsans', 20).render('blue [s]', 1, (0, 0, 0))
    settings.display.blit(blue_tower_label, (x - 64, y + 32))
def cancel_button(x, y):
    cancel_button = (x + 64, y, 60, 40)
    pygame.draw.rect(settings.display, (255, 0, 0), pygame.Rect(cancel_button))
    cancel_button_label = pygame.font.SysFont('comicsans', 20).render('cancel [c]', 1, (0, 0, 0))
    settings.display.blit(cancel_button_label, (x + 64, y))
def sell_button(x, y, towerobj):
    sell_button = (x + 35, y - 76, 60, 40)
    pygame.draw.rect(settings.display, (210, 180, 140), pygame.Rect(sell_button))
    sell_label = pygame.font.SysFont('comicsans', 20).render('sell $' + str(towerobj.resell) + ' [x]', 1, (0, 0, 0))
    settings.display.blit(sell_label, (x + 35, y - 76))