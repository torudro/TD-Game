import pygame
import settings
import enemy_track
pygame.init()
class Enemy_Type:
    def __init__(self, *args):
        self.health = args[0][0]
        self.worth = args[0][1]
        self.speed = args[0][2]
        self.image = args[0][3]
# list_counter = 0
class Enemy:
    def __init__(self, enemy_type):
        # again, depending on settings, will either be XMAS or TG
        self.list_counter = 0
        self.dead = False
        self.worth = enemy_type.worth
        self.speed = enemy_type.speed
        self.health = enemy_type.health
        self.image = enemy_type.image
        self.rotated_image = self.image
        self.image_display_dimensions = None
        # can't go left in this game due to layout of maps
        self.direction_left = False
        self.direction_right = False
        self.direction_up = False
        self.direction_down = False
        self.stop_list_count = False
        self.cont_list_count = False
        # to be able to go through lists
        self.enemy_path_list_x = enemy_track.enemy_path_list_x
        self.enemy_path_list_y = enemy_track.enemy_path_list_y

    def continue_list_counter(self):
        self.stop_list_count = False
        self.cont_list_count = True
        self.list_counter += 1
    def stop_list_counter(self):
        self.stop_list_count = False
        self.stop_list_count = True
    def draw(self):
        # print('LIST COUNTER: ',self.list_counter)
        # used for loops - current position in enemy_path_list_x or _y
        # self.list_counter = 0
        self.incr_x = self.enemy_path_list_x[self.list_counter] + enemy_track.dist_x_list[self.list_counter] * (1 / self.speed)
        self.incr_y = self.enemy_path_list_y[self.list_counter] + enemy_track.dist_y_list[self.list_counter] * (1 / self.speed)
        self.decr_y = self.enemy_path_list_y[self.list_counter] - enemy_track.dist_y_list[self.list_counter] * (1 / self.speed)
        # image drawn to surface with tuple as dimensions
        self.image_display_dimensions = pygame.Surface((59, 64))
        # gives enemy a collision area that's the same location of the image so it can be hit/know if at endpoint
        self.image_display_dimensions.get_rect(center=(self.enemy_path_list_x[self.list_counter], self.enemy_path_list_y[self.list_counter]))
        # subtracts 59 from x and 64 from y because they have to adapt to the location of the points on the map
        settings.display.blit(self.rotated_image, (
        self.enemy_path_list_x[self.list_counter] - 59, self.enemy_path_list_y[self.list_counter] - 64))
        # print(enemy_track.enemy_path_list_x[list_counter])
        # doesn't need to be called in for loop because it's only necessary for each central tile point (not fractions of it)
        if self.enemy_path_list_x[self.list_counter] < self.enemy_path_list_x[len(self.enemy_path_list_x) - 1] \
                and self.enemy_path_list_x[self.list_counter + 1] >= self.enemy_path_list_x[self.list_counter] \
                and self.enemy_path_list_y[self.list_counter] == self.enemy_path_list_y[self.list_counter]:
            self.direction_up = False
            self.direction_down = False
            self.direction_right = True
            # orientates facing right
            self.rotated_image = pygame.transform.rotate(self.image, 0)
        # first condition can be x or y, doesn't matter. if next y pos is less than, then the enemy is going up
        if self.enemy_path_list_x[self.list_counter] < self.enemy_path_list_x[len(self.enemy_path_list_x) - 1] \
                and self.enemy_path_list_y[self.list_counter + 1] < self.enemy_path_list_y[self.list_counter]:
            self.direction_right = False
            self.direction_down = False
            self.direction_up = True
            # orientates facing up
            self.rotated_image = pygame.transform.rotate(self.image, 90)
        # down direction because greater than sign
        if self.enemy_path_list_x[self.list_counter] < self.enemy_path_list_x[len(self.enemy_path_list_x) - 1] \
                and self.enemy_path_list_y[self.list_counter + 1] > self.enemy_path_list_y[self.list_counter]:
            self.direction_right = False
            self.direction_up = False
            self.direction_down = True
            # orientates facing down
            self.rotated_image = pygame.transform.rotate(self.image, 270)
        # Makes it so the enemy does not move anymore.
        if self.list_counter < 28:
            self.continue_list_counter()
        if self.list_counter == 28:
            self.stop_list_counter()
        # loop dependent on how many tiles the enemy moves per second. goes speed-1 times because don't want to draw to same tile point twice
# might be okay to add this before the for loop
# self.list_counter += 1
