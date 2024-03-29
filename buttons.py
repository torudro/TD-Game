import pygame
import settings
import enemies
import map_data
import tower_enemy_info
pygame.init()
# to be used in main game loop, but must be edited inside here
crashed = False
display_map = False
wave_counter = -1
mouse_pos = pygame.mouse.get_pos()
# If STATE is == 6 through 11, the purpose is to edit MODE in order to select the type of mode and display the corresponding map
STATE = 0
MODE = 99
BUTTON_ACTION = 200
map_obj = None
# If mode selection buttons are already clicked, then this is ran for the game maps to be able to be displayed
def button_clicked(button, state_next):
    global map_obj
    global STATE
    global wave_counter
    mouse_pos = pygame.mouse.get_pos()
    for events in pygame.event.get():
        # mouse_pos = pygame.mouse.get_pos()
        if button[0] < mouse_pos[0] < button[0] + button[2] and button[1] < mouse_pos[1] < button[1] + button[3]:
            if STATE == 0 and state_next == 1 and events.type == pygame.MOUSEBUTTONDOWN:
                print('PLAY CLICKED')
                STATE = state_next
                global display_map
                display_map = True
                map_obj = map_data.map_reader(settings.xmas_map)
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_TAB:
                STATE = state_next
                if wave_counter < len(level_settings_obj.enemy_amnt_list):
                    wave_counter += 1
                    spawn_next_wave_enemies()

# depending on state, will draw buttons corresponding to state
class TitleButtons:
    def __init__(self):
        global crashed
        global STATE
        self.pressed = False
        self.mode_button = None
        if STATE == 0:
            self.display_title()
            self.title_button()
        # State that correlates with the game mode. Game buttons are displayed during this state.
        if STATE == 1:
            pass
        # quit button
        if STATE == 99:
            crashed = True
    def title_button(self):
        # play button
        play_button_dimension = (settings.WIDTH * 0.45, settings.HEIGHT * 0.6, 150, 40)
        pygame.draw.rect(settings.display, (0, 255, 0), pygame.Rect(play_button_dimension))
        play_label = pygame.font.SysFont('comicsans', 40).render('PLAY', 1, (0, 0, 0))
        settings.display.blit(play_label, (settings.WIDTH * 0.45, settings.HEIGHT * 0.6))
        button_clicked(play_button_dimension, 1)
    def display_title(self):
        # STATE = 0
        settings.display.blit(pygame.image.load('background_images/title/title_screen.png'), (0, 0))
class Game_Buttons:
    def __init__(self):
        global STATE
        global BUTTON_ACTION
        global button_clicked
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
        lives_label = pygame.font.SysFont('comicsans', 20).render('Lives: ' + str(level_settings_obj.lives), 1,(0, 0, 0))
        settings.display.blit(lives_label, (0, 60))
    def wave_button(self):
        next_wave_button = (settings.WIDTH - 115, settings.HEIGHT - 40, 115, 40)
        pygame.draw.rect(settings.display, (255, 20, 147), pygame.Rect(next_wave_button))
        next_wave_button_label = pygame.font.SysFont('comicsans', 20).render('begin_wave [TAB]', 1, (0, 0, 0))
        settings.display.blit(next_wave_button_label, (settings.WIDTH - 115, settings.HEIGHT - 40))
        button_clicked(next_wave_button, 105)
    # method for turning true and false - use pygame.time.wait()
    def quit(self):
        button = (0, 0, 896, 576)
        pygame.draw.rect(settings.display, (255, 0, 255), pygame.Rect(button))
        button_label = pygame.font.SysFont('comicsans', 35).render('QUIT [DOWN ARROW]', 1, (0, 0, 0))
        settings.display.blit(button_label, (0, 0))

class LevelSettings:
    def __init__(self):
        self.waves = 20
        self.spawn_rate = 1000
        self.cash = 500
        self.lives = 60
        self.enemy_amnt_list = [[1, 0, 0], [2, 0, 0], [3, 1, 0], [5, 3, 0], [4, 7, 0],
                                [4, 9, 0], [5, 10, 0], [4, 5, 1], [4, 7, 1], [7, 10, 2],
                                [8, 12, 0], [10, 15, 0], [15, 12, 0], [18, 22, 5], [20, 26, 7],
                                [12, 15, 0], [17, 22, 2], [18, 27, 4], [28, 24, 4], [30, 30, 15]]
level_settings_obj = LevelSettings()
enemy1_obj_list = []
enemy2_obj_list = []
enemy3_obj_list = []
ENEMY_OBJ_LIST = []
# called every time the next_wave button is clicked
def spawn_next_wave_enemies():
    global enemy1_obj_list
    global enemy2_obj_list
    global enemy3_obj_list
    global ENEMY_OBJ_LIST
    #enemy list set to current wave list
    enemy_list = level_settings_obj.enemy_amnt_list[wave_counter]
    temp_list = []
    print('ENEMY LIST:', enemy_list)
    # Goes through first index of current wave
    for a in range(enemy_list[0]):
        temp_list.append(enemies.Enemy(enemies.Enemy_Type(tower_enemy_info.enemy1_xmas)))
    #Enemy 1 list set to enemy1 objects found
    enemy1_obj_list = temp_list
    temp_list = []

    for b in range(enemy_list[1]):
        temp_list.append(enemies.Enemy(enemies.Enemy_Type(tower_enemy_info.enemy2_xmas)))
    enemy2_obj_list = temp_list

    temp_list = []

    for c in range(enemy_list[2]):
        temp_list.append(enemies.Enemy(enemies.Enemy_Type(tower_enemy_info.enemy3_xmas)))
    enemy3_obj_list = temp_list
    ENEMY_OBJ_LIST = enemy1_obj_list
    if len(enemy2_obj_list) > 0:
        ENEMY_OBJ_LIST.extend(enemy2_obj_list)
    if len(enemy3_obj_list) > 0:
        ENEMY_OBJ_LIST.extend(enemy3_obj_list)