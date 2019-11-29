import pygame
import pytmx
import math


pygame.init()



#for displaying enemies. global because if i want to edit it it has to be, if not inside a method it's own variable gets made


'''FOR ANOTHER CLASS'''
display = pygame.display.set_mode((896, 576))

tiled_map = pytmx.load_pygame('background_images/christmas/Christmas_Map.tsx.tmx', pixelalpha = True)

'''FOR ANOTHER CLASS'''
clock = pygame.time.Clock()

enemy_Path_map_layer = tiled_map.get_layer_by_name('enemy_Path')
non_tower_Zone_map_layer = tiled_map.get_layer_by_name("non_tower_Zone")

enemy_path_list_x = []
enemy_path_list_y = []

non_tower_zone_list = []

#length of map, 14, multiplied by length of tiles, 64 pixels
width = tiled_map.width * tiled_map.tilewidth
#9 * 64
height = tiled_map.height * tiled_map.tilewidth

#enemy_path_list is filled with all the enemy_path coordinates. TUPLES
for enemy_path in enemy_Path_map_layer:
    enemy_path_list_x.append(enemy_path.x)
    enemy_path_list_y.append(enemy_path.y)

'''print(enemy_path_list)'''
#non_tower_zone_list is filled with all coordinates that towers can not occupy.
for tower_null in non_tower_Zone_map_layer:

    non_tower_zone_list.append(tower_null)

'''print(non_tower_zone_list)'''
#render map
def render(surface):
    tile_images = tiled_map.get_tile_image_by_gid

    for layer in tiled_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tile_images(gid)
                if tile:
                    surface.blit(tile, (x * tiled_map.tilewidth, y * tiled_map.tileheight))

def make_map():
    temp_surface = pygame.Surface((width, height))
    render(temp_surface)
    return temp_surface

'''FOR ANOTHER CLASS'''
def display_christmas_map():
    map_img = make_map()
    map_rect = map_img.get_rect()

    display.blit(map_img, map_rect)

'''FOR ANOTHER CLASS'''
def game_loop():
    crashed = False
    global test
    while not crashed:
        #draws new screen to get rid of old enemy models/projectiles/etc.
        #display_christmas_map()
        #updates snowman position
        display_christmas_map()
        snowman_update()
        pygame.time.delay(100)
        #display_christmas_map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
        
        pygame.display.flip()
        clock.tick(30)

display_christmas_map()

'''FOR ANOTHER CLASS'''
spawn_point = [0 * tiled_map.tilewidth, 5 * tiled_map.tileheight]
end_point = [13 * tiled_map.tilewidth, 1 * tiled_map.tileheight]
#loads image, displays on surface, gives hitbox
snowman_img = pygame.image.load('images/enemies/snowman.png')
snowman_image_display = pygame.Surface((59, 64))
rotated_snowman = snowman_img

straight = False
up = False
down = False

snowman_rect_pos_x_list = []
snowman_rect_pos_y_list = []

snowman_display_pos_x_list = []
snowman_display_pos_y_list = []

snowman_velocity = [0, 0]
#moves 1/8 tile per sec
snowman_speed = 1/8

'''FOR ANOTHER CLASS'''
'''
for i in range( len( enemy_path_list_x)):
        #print(nextTile)
        #print(type(nextTile))

        snowman_rect_temp = snowman_image_display.get_rect(center = (enemy_path_list_x[i] - 64, enemy_path_list_y[i] - 59))
        
        #rectangle snowman x val = enemy_path_list_x[i] - 64 
        snowman_rect_x = snowman_rect_temp.x
        snowman_rect_pos_x_list.append(snowman_rect_x)

        #rectangle snowman y val = enemy_path_list_y[i] - 59
        snowman_rect_y = snowman_rect_temp.y
        snowman_rect_pos_y_list.append(snowman_rect_y)
        
        snowman_display_temp =(display.blit(snowman_img, (enemy_path_list_x[i] - 64, enemy_path_list_y[i] - 59)))

        snowman_display_x = snowman_display_temp.x
        snowman_display_pos_x_list.append(snowman_display_x)
        
        snowman_display_y = snowman_display_temp.y
        snowman_display_pos_y_list.append(snowman_display_y)

'''
#will use pos_list vals to creates snowman rect images
snowman_rect_list = []
snowman_display_list = []


#loop for assigning position values to snowman, 30 fps
'''for i in range(1,31):
        print(i)
        #nested loop 8 so 1/8 per tile, meaning 1 frame = 
        for a in range(28):
            
            #implement [i] instead of just zero - have to use a loop
            
            snowman_rect = snowman_image_display.get_rect(center = (enemy_path_list_x[a]/28, enemy_path_list_y[a]/28))
            snowman_rect_list.append(snowman_rect)
            
            snowman_display = display.blit(snowman_img, (snowman_display_pos_x_list[a]/28, snowman_display_pos_y_list[a]/28))
            snowman_display_list.append(snowman_display)
            
'''          

            
nested_holder = 8
incremented_x = 10
incremented_y = 10
list_counter_nested = 0
list_counter = 0
print(enemy_path_list_x)
'''UNNCESSARY
def distance_x(x1, x2):
    distance = ((x1 - x2) ** 2) ** 0.5
    return distance

def distance_y(y1, y2):
    distance = ((y1 - y2) ** 2) ** 0.5
    return distance
      '''
inc_x_count = 0.125
inc_y_up_count = 0.125
inc_y_down_count = 0.125

def snowman_update():
    #global so an instance variable isn't made here and I actually edit its values
    global list_counter
    global snowman_rect_pos_list
    global straight
    global up
    global down


    global nested_holder
    global snowman_img
    
    global rotated_snowman

    global incremented_x
    global incremented_y

    global list_counter_nested

    global inc_x_count
    global inc_y_up_count
    global inc_y_down_count
    
    dist_x = enemy_path_list_x[list_counter + 1] - enemy_path_list_x[list_counter]
    dist_y = enemy_path_list_y[list_counter + 1] - enemy_path_list_y[list_counter]

        #straight
    if enemy_path_list_x[list_counter] < enemy_path_list_x[list_counter + 1]:
        print('FIRST:',enemy_path_list_x[list_counter])
        straight = True
        down = False
        up = False
            #down
    if enemy_path_list_y[list_counter] < enemy_path_list_y[list_counter + 1]:
        straight = False
        down = True
        up = False
            #up
    if enemy_path_list_y[list_counter] > enemy_path_list_y[list_counter + 1]:
        straight = False
        down = False
        up = True

    if straight:
        print('straight')
        rotated_snowman = pygame.transform.rotate(snowman_img, 0)
    if up:
        print('up')
        rotated_snowman = pygame.transform.rotate(snowman_img, 90)
    if down:
        print('down')
        rotated_snowman = pygame.transform.rotate(snowman_img, 180)
                               
    #test:
    snowman_image_display.get_rect(center = (enemy_path_list_x[list_counter], enemy_path_list_y[list_counter]))
    
    #64 width of image, 59 height
    display.blit(rotated_snowman, ( (enemy_path_list_x[list_counter] - 64), (enemy_path_list_y[list_counter] - 59)) )

    
    #because moving at 8ths of a tile. divides by 8 decrementing each time until 1. Dividing by 8 to get eights
    for i in range(8, 1, -1):
        display_christmas_map()
        pygame.time.delay(500)
        
        while straight == True:
            pygame.display.flip()
            #display_christmas_map()
            pygame.time.delay(100)
            display_christmas_map()
            # subctract 1 because it was counting the next instead of current for some reason
            print('PATH',enemy_path_list_x[list_counter])
            incremented_x = enemy_path_list_x[list_counter] + dist_x * inc_x_count
            print(incremented_x)
            inc_x_count += 0.125
            
            snowman_image_display.get_rect(center = (incremented_x, enemy_path_list_y[list_counter]))
            display.blit(rotated_snowman, ( (incremented_x - 64, enemy_path_list_y[list_counter] - 59)))

            #probably should make into a method
            '''if enemy_path_list_x[list_counter + 1] < enemy_path_list_x[list_counter]:
                print('FIRST:',enemy_path_list_x[list_counter])
                straight = False'''
            if enemy_path_list_y[list_counter + 1] > enemy_path_list_y[list_counter] or enemy_path_list_y[list_counter + 2] > enemy_path_list_y[list_counter + 1] or enemy_path_list_y[list_counter + 3] > enemy_path_list_y[list_counter + 2] or enemy_path_list_y[list_counter + 4] > enemy_path_list_y[list_counter + 3]: 
                straight = False
                down = True
            if enemy_path_list_y[list_counter + 1] < enemy_path_list_y[list_counter] or enemy_path_list_y[list_counter + 2] < enemy_path_list_y[list_counter + 1] or enemy_path_list_y[list_counter + 3] < enemy_path_list_y[list_counter + 2] or enemy_path_list_y[list_counter + 4] < enemy_path_list_y[list_counter + 3]:
                straight = False
                up = True

            
            
        while up == True:
            print('SECOND')
            pygame.display.flip()
            #display_christmas_map()
            pygame.time.delay(100)
            display_christmas_map()
            incremented_y = enemy_path_list_y[list_counter] + dist_y * inc_y_up_count
            
            
            snowman_image_display.get_rect(center = (enemy_path_list_x[list_counter], incremented_y))
            display.blit(rotated_snowman, ( (enemy_path_list_x[list_counter] - 64, incremented_y - 59)))

            inc_y_up_count += 0.125

            if enemy_path_list_y[list_counter + 1] > enemy_path_list_y[list_counter]:
                up = False
            elif enemy_path_list_x[list_counter + 1] > enemy_path_list_x[list_counter]:
                straight = True
            else:
                down = True
                

            
        #maybe divide instead of just subtract
        while down == True:
            pygame.display.flip()
            #display_christmas_map()
            pygame.time.delay(100)
            display_christmas_map()
            incremented_y = enemy_path_list_y[list_counter] + dist_y * inc_y_down_count
            
            
            snowman_image_display.get_rect(center = (enemy_path_list_x[list_counter], incremented_y))
            display.blit(rotated_snowman, ( (enemy_path_list_x[list_counter] - 64, incremented_y - 59)))
            
            inc_y_down_count += 0.125

            if enemy_path_list_y[list_counter + 1] < enemy_path_list_y[list_counter]:
                down = False
            elif enemy_path_list_x[list_counter + 1] > enemy_path_list_x[list_counter]:
                straight = True
            else:
                down = True

            
        
        nested_holder -= 1
        if nested_holder <= 2:
            break
    #display.blit(snowman_img, (snowman_display_pos_x_list[list_counter] + 5 , snowman_display_pos_x_list[list_counter] + 5))
    
    if list_counter < len(enemy_path_list_x) -1:
        list_counter += 1
        

game_loop()
pygame.quit()
quit()
                
