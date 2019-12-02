import pygame
import pytmx
import settings
import buttons
import tile_clicked
import tower_enemy_info
# import enemies
pygame.init()

# might want to put display up here, not sure.
current_mode = None
xmas_map = None

wave_counter = 0
buttons_wave_counter_copy = None
temp_enemy_list = []
count = 0

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
        self.map_img = self.make_map()
        self.map_rect = self.map_img.get_rect()

        # surface, from make_map, used as the surface to be displayed, dimensions, map_rect, used from make_map()'s surface rec area

        settings.display.blit(self.map_img, self.map_rect)
        buttons.Game_Buttons().wave_button()
        buttons.Game_Buttons().stats_game_label()
        mouse_pos = pygame.mouse.get_pos()
        #For Towers:
        tile_clicked.click_tile()

        if tile_clicked.display_creation_buttons1:
            tile_clicked.tower_creation_buttons(tile_clicked.tile1.x, tile_clicked.tile1.y)
        if tile_clicked.display_creation_buttons2:
            tile_clicked.tower_creation_buttons(tile_clicked.tile2.x, tile_clicked.tile2.y)
        if tile_clicked.display_creation_buttons3:
            tile_clicked.tower_creation_buttons(tile_clicked.tile3.x, tile_clicked.tile3.y)
        if tile_clicked.display_creation_buttons4:
            tile_clicked.tower_creation_buttons(tile_clicked.tile4.x, tile_clicked.tile4.y)
        if tile_clicked.display_creation_buttons5:
            tile_clicked.tower_creation_buttons(tile_clicked.tile5.x, tile_clicked.tile5.y)
        if tile_clicked.display_creation_buttons6:
            tile_clicked.tower_creation_buttons(tile_clicked.tile6.x, tile_clicked.tile6.y)


        #iterates the following if the next wave button has been clicked. Important because enemy_obj_list doesn't fill until next wave button has been clicked.
        if buttons.wave_counter > -1:
            buttons_wave_counter_copy = buttons.wave_counter
            # The following is very important. You need to call .draw() each time the map is updated - this simulates movement for the enemies.

            # loops through the range of enemy_obj_list
            print('ENEMY OBJ LIST:',buttons.enemy_obj_list)
            for i in range(len(buttons.enemy_obj_list[0][buttons_wave_counter_copy])):
                # blits over old enemy images (because Pygame fucking sucks and you can't just delete an old image)
                data_location.display.blit(self.map_img, self.map_rect)
                buttons.Game_Buttons().wave_button()
                buttons.Game_Buttons().stats_game_label()

                # print('ENEMY OBJ LIST', buttons.enemy_obj_list[buttons_wave_counter_copy])

                if len(temp_enemy_list) < len(
                        buttons.enemy_obj_list[0][buttons_wave_counter_copy]) and temp_enemy_list != \
                        buttons.enemy_obj_list[0][buttons_wave_counter_copy]:
                    temp_enemy_list.append(buttons.enemy_obj_list[0][buttons_wave_counter_copy])

                pygame.time.delay(10)

                for u in range(len(temp_enemy_list)):

                    if len(temp_enemy_list[buttons_wave_counter_copy]) > 1:
                        temp_enemy_list[buttons_wave_counter_copy][u].draw()
                        # is the enemy objects list_counter variable is 28(on the black tile, the end point), then blit over the enemy
                        if temp_enemy_list[buttons_wave_counter_copy][u].list_counter == 28:
                            data_location.display.blit(pygame.image.load(data_location.end_point),
                                                       (data_location.WIDTH - 64, 64))
                        # removes 1 life per enemy if enemy is on x val that begins at start of final tile
                        if temp_enemy_list[buttons_wave_counter_copy][u].enemy_path_list_x[
                            temp_enemy_list[buttons_wave_counter_copy][u].list_counter] == data_location.WIDTH - 64:
                            del temp_enemy_list[buttons_wave_counter_copy][u]

                    # if only 1 enemy object in list

                    elif len(temp_enemy_list[buttons_wave_counter_copy]) == 1:
                        #print('COUNT AMNT TST:', temp_enemy_list[count])
                        temp_enemy_list[count][0].draw()
                        # is the enemy objects list_counter variable is 28(on the black tile, the end point), then blit over the enemy
                        if temp_enemy_list[count][buttons_wave_counter_copy].list_counter == 28:
                            data_location.display.blit(pygame.image.load(data_location.end_point),
                                                       (data_location.WIDTH - 64, 64))
                        # removes 1 life per enemy if enemy is on x val that begins at start of final tile
                        if temp_enemy_list[count][buttons_wave_counter_copy].enemy_path_list_x[
                            temp_enemy_list[count][buttons_wave_counter_copy].list_counter] == data_location.WIDTH - 64:
                            del temp_enemy_list[count][buttons_wave_counter_copy]
                    else:
                        break

                        buttons.mode_obj.lives -= 1

                if buttons_wave_counter_copy < buttons.wave_counter:
                    del temp_enemy_list[buttons_wave_counter_copy]
                    buttons_wave_counter_copy += 1
                    count += 1


def display():
    global xmas_map
    if buttons.MODE == 0 or buttons.MODE == 1 or buttons.MODE == 2:
        xmas_map = map_reader(data_location.xmas_map)
        xmas_map.display_map()
