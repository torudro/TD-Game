import pygame
import map_data
import settings
# import player
import enemies

import towers
import tower_enemy_info

pygame.init()

# to be used in main game loop, but must be edited inside here
crashed = False
display_map = False
display_xmas_map = False
wave_counter = -1
mouse_pos = pygame.mouse.get_pos()
# If STATE is == 6 through 11, the purpose is to edit MODE in order to select the type of mode and display the corresponding map
STATE = 0
MODE = 99
BUTTON_ACTION = 200
# Title, Settings, Level Selection, xmas selector, tg selection



# depending on state, will draw buttons corresponding to state
class Buttons:
    def __init__(self):
        global crashed
        global STATE
        self.pressed = False
        self.mode_button = None

        if STATE == 0:
            self.display_title()
            self.title_buttons()

        # State that correlates with the game mode. Game buttons are displayed during this state.
        if STATE == 1:
            pass
        # quit button
        if STATE == 99:
            crashed = True
        # nothing occurs, just a placeholder
        if STATE == 100:
            pass

    def title_buttons(self):
        # play button
        play_button_dimension = (settings.WIDTH * 0.40, settings.HEIGHT * 0.6, 150, 40)
        pygame.draw.rect(settings.display, (0, 255, 0), pygame.Rect(play_button_dimension))
        play_label = pygame.font.SysFont('comicsans', 40).render('PLAY', 1, (0, 0, 0))
        settings.display.blit(play_label, (settings.WIDTH * 0.40, settings.HEIGHT * 0.6))
        self.button_clicked(play_button_dimension, 1)

        # quit
        quit_button_dimension = settings.WIDTH * 0.40, settings.HEIGHT * 0.7, 150, 40
        pygame.draw.rect(settings.display, (0, 255, 0), pygame.Rect(quit_button_dimension))
        quit_label = pygame.font.SysFont('comicsans', 40).render('QUIT', 1, (0, 0, 0))
        settings.display.blit(quit_label, (settings.WIDTH * 0.40, settings.HEIGHT * 0.7))
        self.button_clicked(quit_button_dimension, 99)

    def display_title(self):
        # STATE = 0
        settings.display.blit(pygame.image.load('background_images/title/title_screen.png'), (0, 0))
    # If mode selection buttons are already clicked, then this is ran for the game maps to be able to be displayed
    def button_clicked(self, button, state_next):

        for events in pygame.event.get():
            if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1] and events.type == pygame.MOUSEBUTTONDOWN:
                #change color of rectangle to show hovered over:
                color_change = button
                pygame.draw.rect(settings.display, (255, 0, 0), pygame.Rect(color_change))
                global display_map
                global display_xmas_map

                if STATE == 0 and state_next == 1:
                    print('PRINT TEST CLICKED_NORMAL')
                    display_map = True
                    display_xmas_map = True

class Game_Buttons:
    def __init__(self):
        global STATE
        global BUTTON_ACTION

        if BUTTON_ACTION == 200:
            self.wave_button()
        if BUTTON_ACTION == 201:
            self.pause_play_buttons()

    def stats_game_label(self):
        #   global player_obj
        global wave_counter
        self.stats_rect = (0, 0, 64, 80)
        pygame.draw.rect(settings.display, (32, 178, 170), pygame.Rect(self.stats_rect))
        waves_label = pygame.font.SysFont('comicsans', 20).render('Waves:', 1, (0, 0, 0))
        settings.display.blit(waves_label, (0, 0))
        wave_count_label = pygame.font.SysFont('comicsans', 20).render(
            str(wave_counter + 1) + '/' + str(level_settings_obj.waves), 1, (0, 0, 0))
        settings.display.blit(wave_count_label, (0, 20))
        # money stat
        money_label = pygame.font.SysFont('comicsans', 20).render('$' + str(level_settings_obj.cash), 1, (0, 0, 0))
        settings.display.blit(money_label, (0, 40))
        # lives
        lives_label = pygame.font.SysFont('comicsans', 20).render('Lives: ' + str(level_settings_obj.lives), 1, (0, 0, 0))
        settings.display.blit(lives_label, (0, 60))

    def wave_button(self):

        next_wave_button = (settings.WIDTH - 75, settings.HEIGHT - 40, 75, 40)
        pygame.draw.rect(settings.display, (255, 20, 147), pygame.Rect(next_wave_button))
        next_wave_button_label = pygame.font.SysFont('comicsans', 20).render('begin_wave', 1, (0, 0, 0))
        settings.display.blit(next_wave_button_label, (settings.WIDTH - 75, settings.HEIGHT - 40))
        check_if_clicked(next_wave_button, 105)

    #method for turning true and false - use pygame.time.wait()
    def pause_play_buttons(self):
        print('test')

def check_if_clicked(button, state_next):

    if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1]:
        # must be global if in an if for some reason
        global STATE
        global wave_counter
        pygame.draw.rect(settings.display, (255, 0, 0), button)

        # state 98 and 100 represents null.
        # next_wave button custom 105 STATE
        for event in pygame.event.get():
            if state_next != 98 and event.type == pygame.MOUSEBUTTONDOWN:
                STATE = state_next
            # STATE = 105 means that wave_button was pressed.
            if STATE == 105 and event.type == pygame.MOUSEBUTTONDOWN:
                if wave_counter < len(level_settings_obj.enemy_amnt_list):
                    wave_counter += 1
                    print('CLICK CONFIRMATION TEST - MODE SELECTED')
                    spawn_next_wave_enemies()


class LevelSettings:
    def __init__(self):
        global MODE

        self.waves = 20
        self.spawn_rate = 1000
        self.cash = 500
        self.lives = 60
        self.enemy_amnt_list = [[1, 0, 0], [2, 0, 0], [3, 1, 0], [5, 3, 0], [4, 7, 0],
                                        [4, 9, 0], [5, 10, 0], [4, 5, 1], [4, 7, 1], [7, 10, 2],
                                        [8, 12, 0], [10, 15, 0], [15, 12, 0], [18, 22, 5], [20, 26, 7],
                                        [12, 15, 0], [17, 22, 2], [18, 27, 4], [28, 24, 4], [30, 30, 15]]





level_settings_obj = LevelSettings()

enemy_obj_list = []


# called every time the next_wave button is clicked
def spawn_next_wave_enemies():
    global enemy_obj_list

    enemy_list = level_settings_obj.enemy_amnt_list[wave_counter]

    temp_list = []
    print('ENEMY LIST:', enemy_list)
    # Goes through first index of current wave
    for a in range(enemy_list[0]):
        temp_list.append(enemies.Enemy(enemies.Enemy_Type(tower_enemy_info.enemy1_xmas)))

    enemy_obj_list[0].append(temp_list)
    temp_list = []
    # if has 2nd enemy type in wave, goes through 2nd index of current wave
    if enemy_list[1] > 0:
        for b in range(enemy_list[1]):
            temp_list.append(enemies.Enemy(enemies.Enemy_Type(tower_enemy_info.enemy2_xmas)))
        enemy_obj_list[0].append(temp_list)
        print('ENEMY 2 TYPE APPENDED - ', enemy_obj_list)
        # print('2nd enemy:', enemy_obj_list[1])

    temp_list = []
    # if has 3rd enemy type in wave, goes through 3rd index of current wave
    if enemy_list[2] > 0:
        for c in range(enemy_list[2]):
            temp_list.append(enemies.Enemy(enemies.Enemy_Type(tower_enemy_info.enemy3_xmas)))
        enemy_obj_list[0].append(temp_list)

tower_enemy_info.tower_zones_available()
tower_list = []
for event in pygame.event.get():

    print(tower_enemy_info.tower_zones_list[0].y)
    rect_dimension = (tower_enemy_info.tower_zones_list[0].x, tower_enemy_info.tower_zones_list[0].y, 64, 64)
    rect = pygame.draw.rect(settings.display, (75, 0, 130), pygame.Rect(rect_dimension))
    mouse_pos = pygame.mouse.get_pos()
    if rect[0] + rect[2] > mouse_pos[0] > rect[0] and rect[1] + rect[3] > mouse_pos[1] > rect[1] \
            and event.type == pygame.MOUSEBUTTONDOWN:
        print('test')
        pass
