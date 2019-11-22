import pygame
import pytmx
import enemy_info
import map_data
import data_location

pygame.init()




class Enemy():

    def __init__(self, enemy_type):
        #again, depending on settings, will either be XMAS or TG
        self.map_data_object = map_data.map_reader(data_location.christmas_map)
        self.dead = False
        self.worth = enemy_type + '_worth'
        self.speed = enemy_type + '_speed'
        self.health = enemy_type + '_health'
        self.image = enemy_type + '_images'

        self.image_display_dimensions = None

        #can't go left in this game due to layout of maps
        self.direction_left = False
        
        self.direction_right = False
        self.direction_up = False
        self.direction_down = False

        #to be able to go through lists
        self.list_counter = 0

        #for loop useage
        

    def draw(self):

        #used for loops - current position in enemy_path_list_x or _y
        self.list_counter = 0

        self.incr_x = self.map_data_object.enemy_path_list_x[list_counter] + self.map_data_object.dist_x[list_counter] * (1/self.speed)
        self.incr_y = self.map_data_object.enemy_path_list_y[list_counter] + self.map_data_object.dist_y[list_counter] * (1/self.speed)

        
        #loads enemy image
        pygame.image.load(self.image)
        #image drawn to surface with tuple as dimensions
        self.image_display_dimensions = pygame.Surface((59, 64))

        #gives enemy a collision area that's the same location of the image so it can be hit/know if at endpoint
        self.image_display_dimensions.get_rect(center = (self.map_data_object.enemy_path_list_x[list_counter], self.map_data_object.enemy_path_list_y[list_counter]))
        
        #subtracts 59 from x and 64 from y because they have to adapt to the location of the points on the map
        map_data.display.blit(self.image, ( (self.map_data_object.enemy_path_list_x[list_counter] - 59), self.map_data_object.enemy_path_list_y[list_counter] - 64))

        #doesn't need to be called in for loop because it's only necessary for each central tile point (not fractions of it)
        if self.map_data_object.enemy_path_list_x[list_counter] < len(self.map_data_object.enemy_path_list_x) and self.map_data_object.enemy_path_list_x[list_counter + 1] >= self.map_data_object.enemy_path_list_x[list_counter] and self.map_data_object.enemy_path_list_y[list_counter] == self.map_data_object.enemy_path_list_y[list_counter]:
            self.direction_up = False
            self.direction_down = False
            self.direction_right = True

                #orientates facing right
            self.image = pygame.transform(self.image, 0)
        #first condition can be x or y, doesn't matter. if next y pos is less than, then the enemy is going up
        if self.map_data_object.enemy_path_list_x[list_counter] < len(self.map_data_object.enemy_path_list_x) and self.map_data_object.enemy_path_list_y[list_counter + 1] < self.map_data_object.enemy_path_list_y[list_counter]:
            self.direction_right = False
            self.direction_down = False
            self.direction_up = True

               #orientates facing up
            self.image = pygame.transform(self.image, 90)
        #down direction because greater than sign       
        if self.map_data_object.enemy_path_list_x[list_counter] < len(self.map_data_object.enemy_path_list_x) and self.map_data_object.enemy_path_list_y[list_counter + 1] > self.map_data_object.enemy_path_list_y[list_counter]:
            self.direction_right = False
            self.direction_up = False
            self.direction_down = True

               #orientates facing down
            self.image = pygame.transform(self.image, 180)
        #loop dependent on how many tiles the enemy moves per second. goes speed-1 times because don't want to draw to same tile point twice
        for i in range(1, self.speed):
            #important because every iteration we want to display new map to get rid of old enemy img files from previous location
            self.map_data_object.display_map()
            #might change
            pygame.time.delay(500)

            self.image_display_dimensions.get_rect(center = (incr_x, self.map_data_object.enemy_path_list_y[list_counter]))
            map_data.display.blit(self.image, ( (self.map_data_object.enemy_path_list_x[list_counter] - 59), incr_y))

            
        #might be okay to add this before the for loop    
        self.list_counter +=1    
            
            
