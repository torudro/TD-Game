import pygame
import pytmx
import data_location
pygame.init()



beige_alien_1_image = 'images/towers/tower_sprites/beige_1.png'
beige_alien_2_image = 'images/towers/tower_sprites/beige_2.png'
beige_alien_3_image = 'images/towers/tower_sprites/beige_3.png'

blue_alien_1 = 'images/towers/tower_sprites/blue_1.png'
blue_alien_2 = 'images/towers/tower_sprites/blue_2.png'
blue_alien_3 = 'images/towers/tower_sprites/blue_3.png'

green_alien_1 = 'images/towers/tower_sprites/green_1.png'
green_alien_2 = 'images/towers/tower_sprites/green_2.png'
green_alien_3 = 'images/towers/tower_sprites/green_3.png'

#NORMAL MODE

beige_alien_1_price = 200
beige_alien_1_resell = 75

beige_alien_1_upgrade = 150
beige_alien_1_attack = 5
beige_alien_1_speed = 0.5
beige_alien_1_radius = 128

beige_alien_2_upgrade = 300
beige_alien_2_resell = 200
beige_alien_2_attack = 10
beige_alien_2_speed = 1
beige_alien_2_radius = 192

beige_alien_3_resell = 310
beige_alien_3_attack = 15
beige_alien_3_speed = 3
beige_alien_3_radius = 256


#HARD MODE

#PSYCHOTIC MODE

beige_tower_1 = (beige_alien_1_price, beige_alien_2_upgrade, beige_alien_1_resell, beige_alien_1_attack, beige_alien_1_speed, beige_alien_1_radius, beige_alien_1_image)
beige_tower_2 = (None, beige_alien_2_upgrade, beige_alien_2_resell, beige_alien_2_attack, beige_alien_2_speed, beige_alien_2_radius, beige_alien_2_image)
beige_tower_3 = (None, None, beige_alien_3_resell, beige_alien_3_attack, beige_alien_3_speed, beige_alien_3_radius, beige_alien_3_image)
tower_zones_list = []
#Process Tower zones:
def tower_zones_available():
    xmas_map = pytmx.load_pygame(data_location.xmas_map, pixelalpha=True)
    tower_Zone_layer = xmas_map.get_layer_by_name('tower_Zone')
    for i in tower_Zone_layer:
        tower_zones_list.append(i)

