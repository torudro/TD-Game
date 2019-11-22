import pygame
import pytmx
import data_location

pygame.init()

#might want to put display up here, not sure.

display = pygame.display.set_mode((data_location.WIDTH, data_location.HEIGHT))
clock = pygame.time.Clock()

class map_reader():

    #map_type comes from either christmas_map or thanksgiving_map in data_location file
    def __init__(self, map_type):

        #so can use display
        global display

        #pixelalpha true for transparency
        self.map = pytmx.load_pygame(map_type, pixelalpha = True)

        #this info applies to both maps, so values don't have to be passed in
        self.enemy_Path_map_layer = self.map.get_layer_by_name('enemy_Path')
        self.non_tower_Zone_map_layer = self.map.get_layer_by_name("non_tower_Zone")

        #dimensions of each tile
        self.width = self.map.width * self.map.tilewidth
        self.height = self.map.height * self.map.tilewidth

        #used in read_map_data() function
        self.enemy_path_list_x = []
        self.enemy_path_list_y = []
        self.non_tower_zone_list = []

        #for getting distance between tiles. used in enemy 
        self.dist_x = []
        self.dist_y = []

        
        
    def read_map_data(self):

        #reads through layer in map_type file and appends info from that to lists
        for enemy_path in enemy_Path_map_layer:
            
            self.enemy_path_list_x.append(enemy_path.x)
            
            self.enemy_path_list_y.append(enemy_path.y)

        #reads through layer that doesn't allow towers to be
        for tower_null in non_tower_Zone_map_layer:

            #tuple data thrown into list
            self.non_tower_zone_list.append(tower_null)

        #assigns distances of each tile to dist_x and dist_y lists
        for i in range(len(self.enemy_path_list_x)):
            
            if self.enemy_path_list_x[i] < len(self.enemy_path_list_x):
                #no shennanigans with distance formula because proceeding tile is never negative
                self.dist_x.append(self.enemy_path_list_x[i + 1] - self.enemy_path_list_x[i])
                self.dist_y.append(self.enemy_path_list_y[i + 1] - self.enemy_path_list_y[i])
                

    #used to render map data
    def render_map(self, temp_surface):
        tile_images = tiled_map.get_tile_image_by_gid

        for layer in tiled_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    self.tile = tile_images(gid)
                    if tile:
                        surface.blit(self.tile, (x * self.map.tilewidth, y * self.map.tileheight))

    #creates a tempory surface (maps will frequently be written over with a new one to get rid of images displayed on previous frame)
    def make_map(self):
        self.temp_surface = pygame.Surface((self.width, self.height))
        render_map(temp_surface)
        return self.temp_surface

    #displays map to screen. Will be called a lot, meaning that methods it uses will also be called a lot
    def display_map(self):
        self.map_img = make_map()
        self.map_rect = map_img.get_rect()

        #surface, from make_map, used as the surface to be displayed, dimensions, map_rect, used from make_map()'s surface rec area
        display.blit(self.map_img, self.map_rect)



        
