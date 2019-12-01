import pygame
import map_data
import data_location
# import player
import enemies
import enemy_info
import towers
import tower_info

pygame.init()

# to be used in main game loop, but must be edited inside here
crashed = False
display_map = False
display_xmas_map = False
map_reader_obj = map_data.map_reader(data_location.xmas_map)

clicked_normal = False
clicked_hard = False
clicked_psycho = False
wave_counter = -1
# If STATE is == 6 through 11, the purpose is to edit MODE in order to select the type of mode and display the corresponding map
STATE = 0
MODE = 99
BUTTON_ACTION = 200
# Title, Settings, Level Selection, xmas selector, tg selection
SCREENS = ['background_images/title/title_screen.png', None,
           'background_images/selection/christmas_selection.png']


# depending on state, will draw buttons corresponding to state
class Buttons:
    def __init__(self):
        global crashed
        global STATE
        global clicked_normal
        global clicked_hard
        global clicked_psycho

        self.pressed = False
        self.mode_button = None
        self.normal_button_dimension = None
        self.hard_button_dimension = None
        self.psycho_button_dimension = None

        if STATE == 0:
            self.display_title()
            self.title_buttons()
        if STATE == 1:
            self.display_settings()
            self.settings_buttons()
        if STATE == 2:
            self.display_selection_christmas()
            self.mode_buttons()

        # if STATE == 5:

        # State that correlates with the game mode. Game buttons are displayed during this state.
        if STATE == 98:
            pass
        # quit button
        if STATE == 99:
            crashed = True
        # nothing occurs, just a placeholder
        if STATE == 100:
            pass

    def title_buttons(self):
        # play button
        play_button_dimension = (data_location.WIDTH * 0.30, data_location.HEIGHT * 0.6, 150, 40)
        pygame.draw.rect(data_location.display, (0, 255, 0), pygame.Rect(play_button_dimension))
        play_label = pygame.font.SysFont('comicsans', 40).render('PLAY', 1, (0, 0, 0))
        data_location.display.blit(play_label, (data_location.WIDTH * 0.30, data_location.HEIGHT * 0.6))
        check_if_clicked(play_button_dimension, 2)

        # settings
        settings_button_dimension = (data_location.WIDTH * 0.50, data_location.HEIGHT * 0.6, 150, 40)
        pygame.draw.rect(data_location.display, (0, 255, 0), pygame.Rect(settings_button_dimension))
        settings_label = pygame.font.SysFont('comicsans', 40).render('SETTINGS', 1, (0, 0, 0))
        data_location.display.blit(settings_label, (data_location.WIDTH * 0.50, data_location.HEIGHT * 0.6))
        check_if_clicked(settings_button_dimension, 1)
        # quit
        quit_button_dimension = data_location.WIDTH * 0.40, data_location.HEIGHT * 0.7, 150, 40
        pygame.draw.rect(data_location.display, (0, 255, 0), pygame.Rect(quit_button_dimension))
        quit_label = pygame.font.SysFont('comicsans', 40).render('QUIT', 1, (0, 0, 0))
        data_location.display.blit(quit_label, (data_location.WIDTH * 0.40, data_location.HEIGHT * 0.7))
        check_if_clicked(quit_button_dimension, 99)

    def settings_buttons(self):
        print('settings-button')

    def mode_buttons(self):
        #   global player_obj
        global MODE
        self.normal_button_dimension = (data_location.WIDTH - 210, 175, 210, 40)
        pygame.draw.rect(data_location.display, (0, 255, 255), pygame.Rect(self.normal_button_dimension))
        easy_label = pygame.font.SysFont('comicsans', 40).render('NORMAL', 1, (0, 0, 0))
        data_location.display.blit(easy_label, (data_location.WIDTH - 210, 175))

        self.check_if_mode_clicked(self.normal_button_dimension)

        self.hard_button_dimension = (data_location.WIDTH - 210, 235, 210, 40)
        pygame.draw.rect(data_location.display, (75, 0, 130), pygame.Rect(self.hard_button_dimension))
        hard_label = pygame.font.SysFont('comicsans', 40).render('HARD', 1, (0, 0, 0))
        data_location.display.blit(hard_label, (data_location.WIDTH - 210, 235))

        self.check_if_mode_clicked(self.hard_button_dimension)

        self.psycho_button_dimension = (data_location.WIDTH - 210, 295, 210, 40)
        pygame.draw.rect(data_location.display, (255, 20, 147), pygame.Rect(self.psycho_button_dimension))
        psycho_label = pygame.font.SysFont('comicsans', 40).render('PSYCHOTIC', 1, (0, 0, 0))
        data_location.display.blit(psycho_label, (data_location.WIDTH - 210, 295))

        self.check_if_mode_clicked(self.psycho_button_dimension)

        if STATE == 2:

            if clicked_normal:

                self.selection_is_over(self.normal_button_dimension, 98)

                MODE = 0

                mode_obj.set_normal()
            #                player_obj = player.Player(MODE, mode_obj.waves, mode_obj.spawn_rate, mode_obj.starting_cash)
            # print(modes.MODE, modes.mode_list)
            elif clicked_hard:
                self.selection_is_over(self.hard_button_dimension, 98)
                MODE = 1

                mode_obj.set_hard()
            #                player_obj = player.Player(MODE, mode_obj.waves, mode_obj.spawn_rate, mode_obj.starting_cash)
            # print(modes.MODE, modes.mode_list)
            elif clicked_psycho:
                self.selection_is_over(self.psycho_button_dimension, 98)
                MODE = 2
                mode_obj.set_psycho()
        #      player_obj = player.Player(MODE, mode_obj.waves, mode_obj.spawn_rate, mode_obj.starting_cash)
        # print(modes.MODE, modes.mode_list)

    def check_if_mode_clicked(self, button):
        global clicked_normal
        global clicked_hard
        global clicked_psycho
        mouse_pos = pygame.mouse.get_pos()

        if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1]:
            for event in pygame.event.get():
                if button == self.normal_button_dimension and event.type == pygame.MOUSEBUTTONDOWN:

                    clicked_normal = True
                    print(clicked_normal)
                elif button == self.hard_button_dimension and event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_hard = True
                elif button == self.psycho_button_dimension and event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_psycho = True

    # If mode selection buttons are already clicked, then this is ran for the game maps to be able to be displayed
    def selection_is_over(self, button, state_next):
        mouse_pos = pygame.mouse.get_pos()
        if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1]:
            # must be global if in an if for some reason
            global STATE
            global display_map
            global display_xmas_map

            if STATE == 2 and state_next == 98:
                print('PRINT TEST CLICKED_NORMAL')
                display_map = True
                display_xmas_map = True
                # player_obj = player.Player(modes.MODE, modes.mode_list)
                # print(modes.MODE, modes.mode_list)
                # modes.display()

    def display_title(self):
        # STATE = 0
        data_location.display.blit(pygame.image.load(SCREENS[STATE]), (0, 0))

    def display_settings(self):
        # STATE = 1
        data_location.display.blit(pygame.image.load(SCREENS[STATE]), (0, 0))

    def display_selection(self):
        # STATE = 2
        data_location.display.blit(pygame.image.load(SCREENS[STATE]), (0, 0))

    def display_selection_christmas(self):
        data_location.display.blit(pygame.image.load(SCREENS[STATE]), (0, 0))

    def set_mode_normal(self):
        global MODE
        MODE = 0

    def set_mode_hard(self):
        global MODE
        MODE = 1

    def set_mode_psychotic(self):
        global MODE
        MODE = 2

    # called when an area that can hold a tower is called. displays even more buttons
    def new_tower(self):
        print('test')

    def sell_tower(self):
        print('test')

    def upgrade_tower(self):
        print('test')

    def confirmation_yes(self):
        print('test')

    def confirmation_no(self):
        print('test')


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
        pygame.draw.rect(data_location.display, (32, 178, 170), pygame.Rect(self.stats_rect))
        waves_label = pygame.font.SysFont('comicsans', 20).render('Waves:', 1, (0, 0, 0))
        data_location.display.blit(waves_label, (0, 0))
        wave_count_label = pygame.font.SysFont('comicsans', 20).render(
            str(wave_counter + 1) + '/' + str(mode_obj.waves), 1, (0, 0, 0))
        data_location.display.blit(wave_count_label, (0, 20))
        # money stat
        money_label = pygame.font.SysFont('comicsans', 20).render('$' + str(mode_obj.cash), 1, (0, 0, 0))
        data_location.display.blit(money_label, (0, 40))
        # lives
        lives_label = pygame.font.SysFont('comicsans', 20).render('Lives: ' + str(mode_obj.lives), 1, (0, 0, 0))
        data_location.display.blit(lives_label, (0, 60))

    def wave_button(self):

        next_wave_button = (data_location.WIDTH - 75, data_location.HEIGHT - 40, 75, 40)
        pygame.draw.rect(data_location.display, (255, 20, 147), pygame.Rect(next_wave_button))
        next_wave_button_label = pygame.font.SysFont('comicsans', 20).render('begin_wave', 1, (0, 0, 0))
        data_location.display.blit(next_wave_button_label, (data_location.WIDTH - 75, data_location.HEIGHT - 40))
        check_if_clicked(next_wave_button, 105)

    def pause_play_buttons(self):
        print('test')

    # changes color of button if hovering. state_next is equal to whatever state conincides with the button press

    def game_button_over(self, button, button_action):
        mouse_pos = pygame.mouse.get_pos()
        if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1]:
            # must be global if in an if for some reason
            global STATE
            global display_map
            global display_xmas_map

            pygame.draw.rect(data_location.display, (255, 0, 0), button)

            # if button is pressed, change value of state. changing value of state will induce action.
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and STATE == 3 and button_action == 200:
                    pass
                    # self.player_obj.waves += 1


def check_if_clicked(button, state_next):
    mouse_pos = pygame.mouse.get_pos()
    if button[0] + button[2] > mouse_pos[0] > button[0] and button[1] + button[3] > mouse_pos[1] > button[1]:
        # must be global if in an if for some reason
        global STATE
        global wave_counter
        pygame.draw.rect(data_location.display, (255, 0, 0), button)

        # state 98 and 100 represents null.
        # next_wave button custom 105 STATE
        for event in pygame.event.get():
            if state_next != 98 and event.type == pygame.MOUSEBUTTONDOWN:
                STATE = state_next
            # STATE = 105 means that wave_button was pressed.
            if STATE == 105 and event.type == pygame.MOUSEBUTTONDOWN:
                if wave_counter < len(mode_obj.enemy_amnt_list):
                    wave_counter += 1
                    print('CLICK CONFIRMATION TEST - MODE SELECTED')
                    spawn_next_wave_enemies()


class Modes:
    def __init__(self):
        global MODE

        self.normal_waves = 20
        self.normal_spawn_rate = 1000
        self.normal_cash = 500
        self.normal_lives = 60
        self.normal_enemy_multiplier = [[1, 0, 0], [2, 0, 0], [3, 1, 0], [5, 3, 0], [4, 7, 0],
                                        [4, 9, 0], [5, 10, 0], [4, 5, 1], [4, 7, 1], [7, 10, 2],
                                        [8, 12, 0], [10, 15, 0], [15, 12, 0], [18, 22, 5], [20, 26, 7],
                                        [12, 15, 0], [17, 22, 2], [18, 27, 4], [28, 24, 4], [30, 30, 15]]

        # wave, index of that wave,
        # print(normal_enemy_multiplier[3][1][0])

        self.hard_waves = 30
        self.hard_spawn_rate = 2
        self.hard_cash = 425
        self.hard_lives = 45
        # 30 waves
        self.hard_enemy_multiplier = [[[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                      [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                      [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                      [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                      [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                      [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []]]
        self.psycho_waves = 55
        self.psycho_spawn_rate = 3
        self.psycho_cash = 350
        self.psycho_lives = 25
        # 50 waves
        self.psycho_enemy_multiplier = [[[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []],
                                        [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []]]
        self.waves = None
        self.spawn_rate = None
        self.cash = None
        self.lives = None
        self.enemy_amnt_list = []

    # 0-2 thanksgiving: 0 =  normal, 1 = hard, 2 = psycho, #3-5 christmas: 3 = normal, 4 = hard, 5 = psycho
    def set_normal(self):

        if MODE == 0:
            self.waves = self.normal_waves
            self.spawn_rate = self.normal_spawn_rate
            self.cash = self.normal_cash
            self.lives = self.normal_lives
            self.enemy_amnt_list = self.normal_enemy_multiplier
            # print(self.enemy_amnt_list)

    def set_hard(self):

        if MODE == 1:
            self.waves = self.hard_waves
            self.spawn_rate = self.hard_spawn_rate
            self.cash = self.hard_cash
            self.lives = self.hard_lives
            self.enemy_amnt_list = self.hard_enemy_multiplier


    def set_psycho(self):

        if MODE == 2:
            self.waves = self.psycho_waves
            self.spawn_rate = self.psycho_spawn_rate
            self.cash = self.psycho_cash
            self.lives = self.psycho_lives
            self.enemy_amnt_list = self.psycho_enemy_multiplier


mode_obj = Modes()

'''ENEMY PROCESSOR:'''
# contains list of enemies to be spawned according to the difficulty and current wave
# enemy_list = [mode_obj.enemy_amnt_list[wave_counter]]
# print(enemy_list)
enemy_obj_list = [[]]


# called every time the next_wave button is clicked
def spawn_next_wave_enemies():
    global enemy_obj_list
    # contains list of enemies to be spawned according to the difficulty and current wave
    print('ENEMY AMNT LIST FROM MODE_OBJ:', mode_obj.enemy_amnt_list)
    enemy_list = mode_obj.enemy_amnt_list[wave_counter]
    print('WAVE COUNTER: ', wave_counter)
    # loops through enemy amount values inside current wave
    '''unneccessary?'''
    # for i in enemy_list:

    temp_list = []
    print('ENEMY LIST:', enemy_list)
    # Goes through first index of current wave
    for a in range(enemy_list[0]):
        temp_list.append(enemies.Enemy(enemies.Enemy_Type(enemy_info.enemy1_xmas)))

    enemy_obj_list[0].append(temp_list)
    print('ENEMY 1 TYPE APPENDED - ',enemy_obj_list)
    # print(i)
    #print('1st enemy:', enemy_obj_list[0])

    temp_list = []
    # if has 2nd enemy type in wave, goes through 2nd index of current wave
    if enemy_list[1] > 0:
        for b in range(enemy_list[1]):
            temp_list.append(enemies.Enemy(enemies.Enemy_Type(enemy_info.enemy2_xmas)))
        enemy_obj_list[0].append(temp_list)
        print('ENEMY 2 TYPE APPENDED - ', enemy_obj_list)
        #print('2nd enemy:', enemy_obj_list[1])

    temp_list = []
    # if has 3rd enemy type in wave, goes through 3rd index of current wave
    if enemy_list[2] > 0:
        for c in range(enemy_list[2]):
            temp_list.append(enemies.Enemy(enemies.Enemy_Type(enemy_info.enemy3_xmas)))
        enemy_obj_list[0].append(temp_list)
        #print('3rd enemy:', enemy_obj_list[2])
        print('ENEMY 3 TYPE APPENDED - ',enemy_obj_list)

tower_info.tower_zones_available()
tower_list = []
for event in pygame.event.get():

    print(tower_info.tower_zones_list[0].y)
    rect_dimension = (tower_info.tower_zones_list[0].x, tower_info.tower_zones_list[0].y, 64, 64)
    rect = pygame.draw.rect(data_location.display, (75, 0, 130), pygame.Rect(rect_dimension))
    mouse_pos = pygame.mouse.get_pos()
    if rect[0] + rect[2] > mouse_pos[0] > rect[0] and rect[1] + rect[3] > mouse_pos[1] > rect[1] \
            and event.type == pygame.MOUSEBUTTONDOWN:

        print('test')
        pass
