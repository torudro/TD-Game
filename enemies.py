import pygame

import data_location
import enemy_track
pygame.init()
class Enemy_Type:
    def __init__(self, *args):

         self.health = args[0][0]
         self.worth = args[0][1]
         self.speed = args[0][2]
         self.image = args[0][3]



list_counter = 0
class Enemy:

    def __init__(self, enemy_type):
        
        #again, depending on settings, will either be XMAS or TG

        global list_counter
        self.dead = False
        self.worth = enemy_type.worth
        self.speed = enemy_type.speed
        self.health = enemy_type.health
        self.image = enemy_type.image

        self.enemy_image = pygame.image.load(self.image)

        self.image_display_dimensions = None

        self.rotated_image = self.enemy_image

        #can't go left in this game due to layout of maps
        self.direction_left = False
        
        self.direction_right = False
        self.direction_up = False
        self.direction_down = False

        #to be able to go through lists


        self.enemy_path_list_x = enemy_track.enemy_path_list_x
        self.enemy_path_list_y = enemy_track.enemy_path_list_y

    def draw(self):
        global list_counter
        print('LIST COUNTER: ',list_counter)
        #used for loops - current position in enemy_path_list_x or _y
        #self.list_counter = 0
        self.incr_x = enemy_track.enemy_path_list_x[list_counter] + enemy_track.dist_x_list[list_counter] * (1/self.speed)

        self.incr_y = enemy_track.enemy_path_list_y[list_counter] + enemy_track.dist_y_list[list_counter] * (1/self.speed)
        self.decr_y = enemy_track.enemy_path_list_y[list_counter] - enemy_track.dist_y_list[list_counter] * (1/self.speed)

        
        #image drawn to surface with tuple as dimensions
        self.image_display_dimensions = pygame.Surface((59, 64))

        #gives enemy a collision area that's the same location of the image so it can be hit/know if at endpoint
        self.image_display_dimensions.get_rect(center = (enemy_track.enemy_path_list_x[list_counter], enemy_track.enemy_path_list_y[list_counter]))
        
        #subtracts 59 from x and 64 from y because they have to adapt to the location of the points on the map
        data_location.display.blit(self.rotated_image, (enemy_track.enemy_path_list_x[list_counter] - 59, enemy_track.enemy_path_list_y[list_counter] - 64))

        #doesn't need to be called in for loop because it's only necessary for each central tile point (not fractions of it)
        if enemy_track.enemy_path_list_x[list_counter] < enemy_track.enemy_path_list_x[len(enemy_track.enemy_path_list_x) - 1] \
                and enemy_track.enemy_path_list_x[list_counter + 1] >= enemy_track.enemy_path_list_x[list_counter] \
                and enemy_track.enemy_path_list_y[list_counter] == enemy_track.enemy_path_list_y[list_counter]:
            self.direction_up = False
            self.direction_down = False
            self.direction_right = True


            #orientates facing right
            self.rotated_image = pygame.transform.rotate(self.enemy_image, 0)
        #first condition can be x or y, doesn't matter. if next y pos is less than, then the enemy is going up
        if enemy_track.enemy_path_list_x[list_counter] < enemy_track.enemy_path_list_x[len(enemy_track.enemy_path_list_x) - 1] \
                and enemy_track.enemy_path_list_y[list_counter + 1] < enemy_track.enemy_path_list_y[list_counter]:
            self.direction_right = False
            self.direction_down = False
            self.direction_up = True


               #orientates facing up

            self.rotated_image = pygame.transform.rotate(self.enemy_image, 90)
        #down direction because greater than sign       
        if enemy_track.enemy_path_list_x[list_counter] < enemy_track.enemy_path_list_x[len(enemy_track.enemy_path_list_x) - 1] \
                and enemy_track.enemy_path_list_y[list_counter + 1] > enemy_track.enemy_path_list_y[list_counter]:
            self.direction_right = False
            self.direction_up = False
            self.direction_down = True


               #orientates facing down
            self.rotated_image = pygame.transform.rotate(self.enemy_image, 270)
        #loop dependent on how many tiles the enemy moves per second. goes speed-1 times because don't want to draw to same tile point twice
        '''for i in range(1, self.speed):


            #important because every iteration we want to display new map to get rid of old enemy img files from previous location
            #enemy_track.display_map()


            #self.map_data_object.enemy_path_list_x[self.list_counter] - 59
            if self.direction_right == True:

                self.image_display_dimensions.get_rect(center = (self.incr_x, enemy_track.enemy_path_list_y[list_counter]))
                data_location.display.blit(self.rotated_image, ( (self.incr_x - 59), enemy_track.enemy_path_list_y[list_counter] - 59))
            if self.direction_up == True:

                self.image_display_dimensions.get_rect(center = (enemy_track.enemy_path_list_x[list_counter], self.decr_y))
                data_location.display.blit(self.rotated_image, ( (enemy_track.enemy_path_list_x[list_counter] - 59), self.decr_y - 59))
            if self.direction_down == True:

                self.image_display_dimensions.get_rect(center = (enemy_track.enemy_path_list_x[list_counter], self.incr_y))
                data_location.display.blit(self.rotated_image, ( (enemy_track.enemy_path_list_x[list_counter] - 59), self.incr_y - 59))
'''
            
        #might be okay to add this before the for loop    
        list_counter +=1
            
            
