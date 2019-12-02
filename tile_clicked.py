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
display_creation_buttons1 = False
display_creation_buttons2 = False
display_creation_buttons3 = False
display_creation_buttons4 = False
display_creation_buttons5 = False
display_creation_buttons6 = False

beige_pressed = False
blue_pressed = False
green_pressed = False
cancel_pressed = False
#mode 1-6 for tiles, 7-9 for tower creation,
MODE = 99
tile1_obj = None
tile2_obj = None
tile3_obj = None
tile4_obj = None
tile5_obj = None
tile6_obj = None
mouse_pos = pygame.mouse.get_pos()
def button_pressed(button, nextmode):
    global MODE
    for events in pygame.event.get():
        if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1] and events.type == pygame.MOUSEBUTTONDOWN:
            if nextmode == 7:
                MODE = 7

            #will be tower blue
            if nextmode == 8:
                MODE = 8
                pass
            #just blit over screen to get rid of buttons. will happen regardless of any button you choose. cancel
            if nextmode == 9:
                MODE = 9
                pass
            #upgrades tower. replaces current with newly upgraded (in list).
            if nextmode == 10:
                MODE = 10
                pass
            #sells tower. removes from list
            if nextmode == 11:
                MODE = 11
                pass
def tower_created_buttons(x, y, towerobj):
    upgrade_button = (x, y, 75, 20)
    pygame.draw.rect(settings.display, (210, 180, 140), pygame.Rect(upgrade_button))
    upgrade_label = pygame.font.SysFont('comicsans', 20).render(str(towerobj.upgrade), 1, (0, 0, 0))
    settings.display.blit(upgrade_label, (x, y))
    # action when clicked
    button_pressed(upgrade_button, 10)
    sell_button = (x - 64, y + 32, 75, 20)
    pygame.draw.rect(settings.display, (210, 180, 140), pygame.Rect(sell_button))
    sell_label = pygame.font.SysFont('comicsans', 20).render(str(towerobj.resell), 1, (0, 0, 0))
    settings.display.blit(sell_label, (x - 64, y + 32))
    # action when clicked
    button_pressed(sell_button, 11)
    cancel_button = (x + 64, y + 32, 75, 20)
    pygame.draw.rect(settings.display, (210, 180, 140), pygame.Rect(upgrade_button))
    cancel_label = pygame.font.SysFont('comicsans', 20).render('cancel', 1, (0, 0, 0))
    settings.display.blit(cancel_label, (x + 64, y + 32))
    #action when clicked
    button_pressed(cancel_button, 9)
def tower_creation_buttons(x, y):
    beige_tower_button = (x, y, 75, 20)
    pygame.draw.rect(settings.display, (210, 180, 140), pygame.Rect(beige_tower_button))
    beige_tower_label = pygame.font.SysFont('comicsans', 20).render('beige [$100]', 1, (0, 0, 0))
    settings.display.blit(beige_tower_label, (x, y))
    # action when clicked
    button_pressed(beige_tower_button, 7)
    blue_tower_button = (x + 64, y + 32, 70, 20)
    pygame.draw.rect(settings.display, (0, 0, 255), pygame.Rect(blue_tower_button))
    blue_tower_label = pygame.font.SysFont('comicsans', 20).render('blue [$125]', 1, (0, 0, 0))
    settings.display.blit(blue_tower_label, (x + 64, y + 32))
    # action when clicked
    button_pressed(blue_tower_button, 8)
    cancel_button = (x, y + 64, 50, 20)
    pygame.draw.rect(settings.display, (255, 0, 0), pygame.Rect(cancel_button))
    cancel_button_label = pygame.font.SysFont('comicsans', 20).render('cancel', 1, (0, 0, 0))
    settings.display.blit(cancel_button_label, (x, y + 64))
    # action when clicked
    button_pressed(cancel_button, 9)
def click_tile():
    global MODE

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if tile1.x < mouse_pos[0] < tile1.x + 64 and tile1.y < mouse_pos[1] < tile1.y + 64 and event.type == pygame.MOUSEBUTTONDOWN:
            # calls this method which displays buttons
            MODE = 1

        if tile2.x < mouse_pos[0] < tile2.x + 64 and tile2.y < mouse_pos[1] < tile2.y + 64 and event.type == pygame.MOUSEBUTTONDOWN:
            # calls this method which displays buttons
            MODE = 2

        if tile3.x < mouse_pos[0] < tile3.x + 64 and tile3.y < mouse_pos[1] < tile3.y + 64 and event.type == pygame.MOUSEBUTTONDOWN:
            # calls this method which displays buttons
            MODE = 3

        if tile4.x < mouse_pos[0] < tile4.x + 64 and tile4.y < mouse_pos[1] < tile4.y + 64 and event.type == pygame.MOUSEBUTTONDOWN:
            # calls this method which displays buttons
            MODE = 4

        if tile5.x < mouse_pos[0] < tile5.x + 64 and tile5.y < mouse_pos[1] < tile5.y + 64 and event.type == pygame.MOUSEBUTTONDOWN:
            # calls this method which displays buttons
            MODE = 5

        if tile1.x < mouse_pos[0] < tile1.x + 64 and tile1.y < mouse_pos[1] < tile1.y + 64 and event.type == pygame.MOUSEBUTTONDOWN:
            # calls this method which displays buttons
            MODE = 6


