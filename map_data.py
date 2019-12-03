import pygame
import pytmx
import settings
import buttons
import tile_clicked
import tower_enemy_info
pygame.init()
current_mode = None
xmas_map = None
wave_counter = 0
count = 0
can_create_towers = False
MODE = 99
STATE = 99
#if 1 gets added, then the first button sets for the towers can no longer be shown (until a tower is sold)
tile1_set = 0
tile2_set = 0
tile3_set = 0
tile4_set = 0
tile5_set = 0
tile6_set = 0
tile1_beige = 0
tile2_beige = 0
tile3_beige = 0
tile4_beige = 0
tile5_beige = 0
tile6_beige = 0
tile1_blue = 0
tile2_blue = 0
tile3_blue = 0
tile4_blue = 0
tile5_blue = 0
tile6_blue = 0
class map_reader:
    # map_type comes from either christmas_map or thanksgiving_map in data_location file
    def __init__(self, map_type):
        # pixelalpha true for transparency
        self.map = pytmx.load_pygame(map_type, pixelalpha=True)

        # this info applies to both maps, so values don't have to be passed in
        self.enemy_Path_map_layer = self.map.get_layer_by_name('enemy_Path')
        self.tower_Zone_layer = self.map.get_layer_by_name("tower_Zone")

        # dimensions of each tile
        self.width = self.map.width * self.map.tilewidth

        self.height = self.map.height * self.map.tilewidth

        # used in read_map_data() function
        self.enemy_path_list_x = []
        self.enemy_path_list_y = []
        self.tower_zone_list = []

        # for getting distance between tiles. used in enemy
        self.dist_x = []
        self.dist_y = []
    def read_map_data(self):
        # reads through layer in map_type file and appends info from that to lists

        for enemy_path in self.enemy_Path_map_layer:
            self.enemy_path_list_x.append(enemy_path.x)
            print(self.enemy_path_list_x.append(enemy_path.x))
            self.enemy_path_list_y.append(enemy_path.y)

        # reads through layer that doesn't allow towers to be
        for tower_Zone in self.tower_Zone_layer:
            # tuple data thrown into list
            self.tower_zone_list.append(tower_Zone)

        # assigns distances of each tile to dist_x and dist_y lists
        for i in range(len(self.enemy_path_list_x)):

            while len(self.dist_x) < len(self.enemy_path_list_x):
                # no shennanigans with distance formula because proceeding tile is never negative
                self.dist_x.append(self.enemy_path_list_x[i + 1] - self.enemy_path_list_x[i])
                self.dist_y.append(self.enemy_path_list_y[i + 1] - self.enemy_path_list_y[i])
    # used to render map data
    def render_map(self, temp_surface):
        self.tile_images = self.map.get_tile_image_by_gid

        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.tile_images(gid)
                    if tile:
                        temp_surface.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))
    # creates a tempory surface (maps will frequently be written over with a new one to get rid of images displayed on previous frame)
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render_map(temp_surface)
        return temp_surface
    # displays map to screen. Will be called a lot, meaning that methods it uses will also be called a lot
    def display_map(self):
        global current_mode
        global wave_counter
        global buttons_wave_counter_copy
        global temp_enemy_list
        global count
        global can_create_towers
        global MODE
        global TOWERMODE
        global STATE
        global button_set1
        global button_set2
        global tile1_set
        global tile2_set
        global tile3_set
        global tile4_set
        global tile5_set
        global tile6_set
        global tile1_beige
        global tile2_beige
        global tile3_beige
        global tile4_beige
        global tile5_beige
        global tile6_beige
        global tile1_blue
        global tile2_blue
        global tile3_blue
        global tile4_blue
        global tile5_blue
        global tile6_blue
        self.map_img = self.make_map()
        self.map_rect = self.map_img.get_rect()
        # surface, from make_map, used as the surface to be displayed, dimensions, map_rect, used from make_map()'s surface rec area
        settings.display.blit(self.map_img, self.map_rect)
        buttons.Game_Buttons().wave_button()
        buttons.Game_Buttons().stats_game_label()
        # For Towers:

        if pygame.key.get_pressed()[pygame.K_1] and tile1_set == 0:
            MODE = 1
        if pygame.key.get_pressed()[pygame.K_2] and tile2_set == 0:
            MODE = 2
        if pygame.key.get_pressed()[pygame.K_3] and tile3_set == 0:
            MODE = 3
        if pygame.key.get_pressed()[pygame.K_4] and tile4_set == 0:
            MODE = 4
        if pygame.key.get_pressed()[pygame.K_5] and tile5_set == 0:
            MODE = 5
        if pygame.key.get_pressed()[pygame.K_6] and tile6_set == 0:
            MODE = 6

        if pygame.key.get_pressed()[pygame.K_1] and tile1_set == 1:
            print('1 STATE ',STATE)
            STATE = 1
        if pygame.key.get_pressed()[pygame.K_2] and tile2_set == 1:
            print('2 STATE ',STATE)
            STATE = 2

        if pygame.key.get_pressed()[pygame.K_3] and tile3_set == 1:
            STATE = 3
        if pygame.key.get_pressed()[pygame.K_4] and tile4_set == 1:
            STATE = 4
        if pygame.key.get_pressed()[pygame.K_5] and tile5_set == 1:
            STATE = 5
        if pygame.key.get_pressed()[pygame.K_6] and tile6_set == 1:
            STATE = 6
        # For upgrading towers:
        # upgrades
        #Cancel button
        if pygame.key.get_pressed()[pygame.K_c] and (MODE == 1 or MODE == 2 or MODE == 3 or MODE == 4 or MODE == 5 or MODE == 6):
            MODE = 99
        if pygame.key.get_pressed()[pygame.K_c] and (STATE == 1 or STATE == 2 or STATE == 3 or STATE == 4 or STATE == 5 or STATE == 6):
            STATE = 99
        #buy beige
        if pygame.key.get_pressed()[pygame.K_a] and MODE == 1 and buttons.level_settings_obj.cash >= 150:
            #Set mode = 99 so that the set1 buttons no longer appear
            MODE = 99
            tile1_set = 1
            buttons.level_settings_obj.cash -= 150
            tile1_beige = 1
            tile1_blue = 0
            tile_clicked.tile1_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.beige_tower1))
        #buy blue
        if pygame.key.get_pressed()[pygame.K_s] and MODE == 1 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile1_set = 1
            buttons.level_settings_obj.cash -= 150
            tile1_beige = 0
            tile1_blue = 1

            tile_clicked.tile1_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.blue_tower1))
            print('test')
        if pygame.key.get_pressed()[pygame.K_a] and MODE == 2 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile2_set = 1
            buttons.level_settings_obj.cash -= 150
            tile2_beige = 1
            tile2_blue = 0
            tile_clicked.tile2_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.beige_tower1))
        if pygame.key.get_pressed()[pygame.K_s] and MODE == 2 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile2_set = 1
            buttons.level_settings_obj.cash -= 150
            tile2_beige = 0
            tile2_blue = 1
            tile_clicked.tile2_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.blue_tower1))

        if pygame.key.get_pressed()[pygame.K_a] and MODE == 3 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile3_set = 1
            buttons.level_settings_obj.cash -= 150
            tile3_beige = 1
            tile3_blue = 0
            tile_clicked.tile3_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.beige_tower1))
        if pygame.key.get_pressed()[pygame.K_s] and MODE == 3 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            #blits over screen so buttons disappear
            tile3_set = 1
            buttons.level_settings_obj.cash -= 150
            tile3_beige = 0
            tile3_blue = 1
            #new tower obj
            tile_clicked.tile3_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.blue_tower1))
        if pygame.key.get_pressed()[pygame.K_a] and MODE == 4 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            #blits over screen so buttons disappear
            tile4_set = 1
            buttons.level_settings_obj.cash -= 150
            tile4_beige = 1
            tile4_blue = 0
            tile_clicked.tile4_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.beige_tower1))
        if pygame.key.get_pressed()[pygame.K_s] and MODE == 4 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile4_set = 1
            buttons.level_settings_obj.cash -= 150
            tile4_beige = 0
            tile4_blue = 1
            tile_clicked.tile4_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.blue_tower1))
        if pygame.key.get_pressed()[pygame.K_a] and MODE == 5 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile5_set = 1
            buttons.level_settings_obj.cash -= 150
            tile5_beige = 1
            tile5_blue = 0
            tile_clicked.tile5_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.beige_tower1))
        if pygame.key.get_pressed()[pygame.K_s] and MODE == 5 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile5_set = 1
            buttons.level_settings_obj.cash -= 150
            tile5_beige = 0
            tile5_blue = 1
            tile_clicked.tile5_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.blue_tower1))
        if pygame.key.get_pressed()[pygame.K_a] and MODE == 6 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile6_set = 1
            buttons.level_settings_obj.cash -= 150
            tile6_beige = 1
            tile6_blue = 0
            tile_clicked.tile6_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.beige_tower1))
        if pygame.key.get_pressed()[pygame.K_s] and MODE == 6 and buttons.level_settings_obj.cash >= 150:
            MODE = 99
            tile6_set = 1
            buttons.level_settings_obj.cash -= 150
            tile6_beige = 0
            tile6_blue = 1
            tile_clicked.tile6_obj = tile_clicked.towers.Tower(tile_clicked.towers.Tower_Type(tower_enemy_info.blue_tower1))

        #Sell
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 1 and tile1_beige == 1:
            tile1_set = 0
            tile1_beige = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile1_obj.resell
            tile_clicked.tile1_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 1 and tile1_blue == 1:
            tile1_set = 0
            tile1_blue = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile1_obj.resell
            tile_clicked.tile1_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 2:
            print('BIEGE TEST')
            tile2_set = 0
            tile2_beige = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile2_obj.resell
            tile_clicked.tile2_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 2:
            tile2_set = 0
            tile2_blue = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile2_obj.resell
            tile_clicked.tile2_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 3:
            tile3_set = 0
            tile3_beige = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile3_obj.resell
            tile_clicked.tile3_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 3:
            tile3_set = 0
            tile3_blue = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile3_obj.resell
            tile_clicked.tile3_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 4:
            tile4_set = 0
            tile4_beige = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile4_obj.resell
            tile_clicked.tile4_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 4:
            tile4_set = 0
            tile4_blue = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile4_obj.resell
            tile_clicked.tile4_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 5:
            tile5_set = 0
            tile5_beige = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile5_obj.resell
            tile_clicked.tile5_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 5:
            tile5_set = 0
            tile5_blue = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile5_obj.resell
            tile_clicked.tile5_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 6:
            tile6_set = 0
            tile6_beige = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile6_obj.resell
            tile_clicked.tile6_obj = None
        if pygame.key.get_pressed()[pygame.K_x] and STATE == 6:
            tile6_set = 0
            tile6_blue = 0
            MODE = 99
            STATE = 99
            buttons.level_settings_obj.cash += tile_clicked.tile6_obj.resell
            tile_clicked.tile6_obj = None
        #cancel buttons
        if STATE == 99:
            settings.display.blit(self.map_img, self.map_rect)
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
        if MODE == 99:
            settings.display.blit(self.map_img, self.map_rect)
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
        # Depeneding on the mode, call methods that correspond to the mode.
        if MODE == 1:
            tile_clicked.beige_buy_button(tile_clicked.tile1.x, tile_clicked.tile1.y)
            tile_clicked.blue_buy_button(tile_clicked.tile1.x, tile_clicked.tile1.y)
            tile_clicked.cancel_button(tile_clicked.tile1.x, tile_clicked.tile1.y)
        if MODE == 2:
            tile_clicked.beige_buy_button(tile_clicked.tile2.x, tile_clicked.tile2.y)
            tile_clicked.blue_buy_button(tile_clicked.tile2.x, tile_clicked.tile2.y)
            tile_clicked.cancel_button(tile_clicked.tile2.x, tile_clicked.tile2.y)
        if MODE == 3:
            tile_clicked.beige_buy_button(tile_clicked.tile3.x, tile_clicked.tile3.y)
            tile_clicked.blue_buy_button(tile_clicked.tile3.x, tile_clicked.tile3.y)
            tile_clicked.cancel_button(tile_clicked.tile3.x, tile_clicked.tile3.y)
        if MODE == 4:
            tile_clicked.beige_buy_button(tile_clicked.tile4.x, tile_clicked.tile4.y)
            tile_clicked.blue_buy_button(tile_clicked.tile4.x, tile_clicked.tile4.y)
            tile_clicked.cancel_button(tile_clicked.tile4.x, tile_clicked.tile4.y)
        if MODE == 5:
            tile_clicked.beige_buy_button(tile_clicked.tile5.x, tile_clicked.tile5.y)
            tile_clicked.blue_buy_button(tile_clicked.tile5.x, tile_clicked.tile5.y)
            tile_clicked.cancel_button(tile_clicked.tile5.x, tile_clicked.tile5.y)
        if MODE == 6:
            tile_clicked.beige_buy_button(tile_clicked.tile6.x, tile_clicked.tile6.y)
            tile_clicked.blue_buy_button(tile_clicked.tile6.x, tile_clicked.tile6.y)
            tile_clicked.cancel_button(tile_clicked.tile6.x, tile_clicked.tile6.y)
        # blit before hand because you are going to screen that requires previous buttons to not be presents
        if STATE == 1:
            tile_clicked.cancel_button(tile_clicked.tile1.x, tile_clicked.tile1.y)
            tile_clicked.sell_button(tile_clicked.tile1.x, tile_clicked.tile1.y, tile_clicked.tile1_obj)
        if STATE == 2:
            tile_clicked.cancel_button(tile_clicked.tile2.x, tile_clicked.tile2.y)
            tile_clicked.sell_button(tile_clicked.tile2.x, tile_clicked.tile2.y, tile_clicked.tile2_obj)
        if STATE == 3:
            tile_clicked.cancel_button(tile_clicked.tile3.x, tile_clicked.tile3.y)
            tile_clicked.sell_button(tile_clicked.tile3.x, tile_clicked.tile3.y, tile_clicked.tile3_obj)
        if STATE == 4:
            tile_clicked.cancel_button(tile_clicked.tile4.x, tile_clicked.tile4.y)
            tile_clicked.sell_button(tile_clicked.tile4.x, tile_clicked.tile4.y, tile_clicked.tile4_obj)
        if STATE == 5:
            tile_clicked.cancel_button(tile_clicked.tile5.x, tile_clicked.tile5.y)
            tile_clicked.sell_button(tile_clicked.tile5.x, tile_clicked.tile5.y, tile_clicked.tile5_obj)
        if STATE == 6:
            tile_clicked.cancel_button(tile_clicked.tile6.x, tile_clicked.tile6.y)
            tile_clicked.sell_button(tile_clicked.tile6.x, tile_clicked.tile6.y, tile_clicked.tile6_obj)

        # Draws an object in a tile if the object exists
        if tile_clicked.tile1_obj != None:
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
            tile_clicked.tile1_obj.draw(tile_clicked.tile1.x, tile_clicked.tile1.y)

        if tile_clicked.tile2_obj != None:
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
            tile_clicked.tile2_obj.draw(tile_clicked.tile2.x, tile_clicked.tile2.y)
        if tile_clicked.tile3_obj != None:
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
            tile_clicked.tile3_obj.draw(tile_clicked.tile3.x, tile_clicked.tile3.y)
        if tile_clicked.tile4_obj != None:
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
            tile_clicked.tile4_obj.draw(tile_clicked.tile4.x, tile_clicked.tile4.y)
        if tile_clicked.tile5_obj != None:
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
            tile_clicked.tile5_obj.draw(tile_clicked.tile5.x, tile_clicked.tile5.y)
        if tile_clicked.tile6_obj != None:
            buttons.Game_Buttons().wave_button()
            buttons.Game_Buttons().stats_game_label()
            tile_clicked.tile6_obj.draw(tile_clicked.tile6.x, tile_clicked.tile6.y)

        # print('tile6',tile_clicked.tile6_buttons)
        # if length of list that contains enemies is less than the amount of waves, then you can create towers.

        # iterates the following if the next wave button has been clicked. Important because enemy_obj_list doesn't fill until next wave button has been clicked.
        if buttons.wave_counter > - 1:
            loop_count = 0
            #print('ENEMY LIST 1',buttons.enemy1_obj_list)
            #print('ENEMY LIST 2', buttons.enemy2_obj_list)
            #print('ENEMY LIST 3', buttons.enemy3_obj_list)
            print(buttons.ENEMY_OBJ_LIST)

            for i in buttons.ENEMY_OBJ_LIST:

                if len(buttons.ENEMY_OBJ_LIST) == 1:
                    i.draw()
                    print('HEALTH:',i.health)
                    if tile_clicked.tile1_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile1.x) **2) <= tile_clicked.tile1_obj.radius:
                            tile_clicked.tile1_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile1_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile2_obj != None:
                        if ((i.enemy_path_list_x[
                                 i.list_counter] - tile_clicked.tile2.x) ** 2) <= tile_clicked.tile2_obj.radius:
                            tile_clicked.tile2_obj.attack(i.enemy_path_list_x[i.list_counter],
                                                          i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile2_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile3_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile3.x) **2) <= tile_clicked.tile3_obj.radius:
                            tile_clicked.tile3_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile3_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile4_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile4.x) **2) <= tile_clicked.tile4_obj.radius:
                            tile_clicked.tile4_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile4_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile5_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile5.x) **2) <= tile_clicked.tile5_obj.radius:
                            tile_clicked.tile5_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile5_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile6_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile6.x) **2) <= tile_clicked.tile6_obj.radius:
                            tile_clicked.tile6_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile6_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth

                    if i.list_counter == 28:
                        buttons.level_settings_obj.lives -= 1
                        settings.display.blit(settings.end_point, (settings.WIDTH - 64, 64))
                        del buttons.ENEMY_OBJ_LIST[loop_count]
                if len(buttons.ENEMY_OBJ_LIST) > 1:

                    i.draw()

                    if tile_clicked.tile1_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile1.x) **2) <= tile_clicked.tile1_obj.radius:
                            tile_clicked.tile1_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile1_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile2_obj != None:
                        if ((i.enemy_path_list_x[
                                 i.list_counter] - tile_clicked.tile2.x) ** 2) <= tile_clicked.tile2_obj.radius:
                            tile_clicked.tile2_obj.attack(i.enemy_path_list_x[i.list_counter],
                                                          i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile2_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile3_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile3.x) **2) <= tile_clicked.tile3_obj.radius:
                            tile_clicked.tile3_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile3_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile4_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile4.x) **2) <= tile_clicked.tile4_obj.radius:
                            tile_clicked.tile4_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile4_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile5_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile5.x) **2) <= tile_clicked.tile5_obj.radius:
                            tile_clicked.tile5_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile5_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if tile_clicked.tile6_obj != None:
                        if ((i.enemy_path_list_x[i.list_counter] - tile_clicked.tile6.x) **2) <= tile_clicked.tile6_obj.radius:
                            tile_clicked.tile6_obj.attack(i.enemy_path_list_x[i.list_counter], i.enemy_path_list_y[i.list_counter])
                            i.health -= tile_clicked.tile6_obj.attack_stat
                            if i.health <= 0:
                                del buttons.ENEMY_OBJ_LIST[loop_count]
                            buttons.level_settings_obj.cash += i.worth
                    if i.list_counter == 28:
                        buttons.level_settings_obj.lives -= 1
                        settings.display.blit(settings.end_point, (settings.WIDTH - 64, 64))
                        del buttons.ENEMY_OBJ_LIST[loop_count]
            if buttons.level_settings_obj.lives <= 0:
                buttons.Game_Buttons().quit()
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    pygame.quit()
                    quit()
            loop_count += 1


    def display(self):
        settings.display.blit(self.map_img, self.map_rect)
        buttons.Game_Buttons().wave_button()
        buttons.Game_Buttons().stats_game_label()
