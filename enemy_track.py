import pygame
import buttons
import pytmx
import data_location
pygame.init()
#gets enemy path list from map_data to negate circular dependencies
enemy_path_list_x = []
enemy_path_list_y = []
dist_x_list = []
dist_y_list = []


'''IF MAP IS XMAS'''
def game_xmas():
    #if buttons.MODE == 3 or buttons.MODE == 4 or buttons.MODE == 5:
    xmas_map = pytmx.load_pygame(data_location.xmas_map, pixelalpha=True)
    enemy_Path_map_layer = xmas_map.get_layer_by_name('enemy_Path')
    # reads through layer in map_type file and appends info from that to lists
    for enemy_path in enemy_Path_map_layer:
        enemy_path_list_x.append(enemy_path.x)
        #print(enemy_path_list_x.append(enemy_path.x))
        enemy_path_list_y.append(enemy_path.y)

    # assigns distances of each tile to dist_x and dist_y lists
    for i in range(len(enemy_path_list_x)):

        while len(dist_x_list) < len(enemy_path_list_x):
            # no shenanigans with distance formula because proceeding tile is never negative
            dist_x_list.append(enemy_path_list_x[i + 1] - enemy_path_list_x[i])
            dist_y_list.append(enemy_path_list_y[i + 1] - enemy_path_list_y[i])
