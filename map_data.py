import pygame
import pytmx
import data_location
import buttons

# import enemy_info
# import enemies
pygame.init()

# might want to put display up here, not sure.
current_mode = None
xmas_map = None


class map_reader:

    # map_type comes from either christmas_map or thanksgiving_map in data_location file
    def __init__(self, map_type):

        # pixelalpha true for transparency
        self.map = pytmx.load_pygame(map_type, pixelalpha=True)

        # this info applies to both maps, so values don't have to be passed in
        self.enemy_Path_map_layer = self.map.get_layer_by_name('enemy_Path')
        self.non_tower_Zone_map_layer = self.map.get_layer_by_name("non_tower_Zone")

        # dimensions of each tile
        self.width = self.map.width * self.map.tilewidth
        self.height = self.map.height * self.map.tilewidth

        # used in read_map_data() function
        self.enemy_path_list_x = []
        self.enemy_path_list_y = []
        self.non_tower_zone_list = []

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
        for tower_null in self.non_tower_Zone_map_layer:
            # tuple data thrown into list
            self.non_tower_zone_list.append(tower_null)
        print(self.non_tower_zone_list)
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
        self.map_img = self.make_map()
        self.map_rect = self.map_img.get_rect()

        # surface, from make_map, used as the surface to be displayed, dimensions, map_rect, used from make_map()'s surface rec area

        data_location.display.blit(self.map_img, self.map_rect)
        buttons.Game_Buttons().wave_button()
        buttons.Game_Buttons().stats_game_label()

        '''enemy_list = [buttons.modes.enemy_amnt_list[buttons.player_obj.current_wave]]
        print(enemy_list)
        enemy_type_list = [[], [], []]
        enemy_obj_list = [[], [], []]
        if buttons.modes.MODE == 0 or buttons.modes.MODE == 1 or buttons.modes.MODE == 2:

            for i in len(enemy_list[0[0]]):
                enemy_type_list[0][0].append(i + 1)
                enemy_type_list[0][0][i] = enemies.Enemy_Type(enemy_info.enemy1_tg)

                enemy_obj_list[0][0].append(enemies.Enemy(enemy_type_list[0][0][i]))
            for i in len(enemy_list[0[1]]):
                enemy_type_list[1][1].append(i + 1)
                enemy_type_list[1][1][i] = enemies.Enemy_Type(enemy_info.enemy2_tg)

                enemy_obj_list[1][1].append(enemies.Enemy(enemy_type_list[1][1][i]))
            for i in len(enemy_list[0[2]]):
                enemy_type_list[2][2].append(i + 1)
                enemy_type_list[2][2][i] = enemies.Enemy_Type(enemy_info.enemy3_tg)

                enemy_obj_list[2][2].append(enemies.Enemy(enemy_type_list[2][2][i]))

            #enemy_type_list = [enemy_list[0][0] * enemy_info.enemy1_tg, enemy_list[1][1] * enemy_info.enemy2_tg, enemy_list[2][2] * enemy_info.enemy3_tg]

        if buttons.modes.MODE == 3 or buttons.modes.MODE == 4 or buttons.modes.MODE == 5:

            for i in len(enemy_list[0[0]]):
                enemy_type_list[0][0].append(i + 1)
                enemy_type_list[0][0][i] = enemies.Enemy_Type(enemy_info.enemy1_xmas)

                enemy_obj_list[0][0].append(enemies.Enemy(enemy_type_list[0][0][i]))
            for i in len(enemy_list[0[1]]):
                enemy_type_list[1][1].append(i + 1)
                enemy_type_list[1][1][i] = enemies.Enemy_Type(enemy_info.enemy2_xmas)

                enemy_obj_list[1][1].append(enemies.Enemy(enemy_type_list[1][1][i]))
            for i in len(enemy_list[0[2]]):
                enemy_type_list[2][2].append(i + 1)
                enemy_type_list[2][2][i] = enemies.Enemy_Type(enemy_info.enemy3_xmas)

                enemy_obj_list[2][2].append(enemies.Enemy(enemy_type_list[2][2][i]))

            print('ENEMY TYPE LIST:', enemy_type_list)
            print('ENEMY OBJ LIST: ', enemy_obj_list)'''


def display():

    global xmas_map
    if buttons.MODE == 0 or buttons.MODE == 1 or buttons.MODE == 2:
        xmas_map = map_reader(data_location.xmas_map)
        xmas_map.display_map()
