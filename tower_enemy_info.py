import pygame
import pytmx
import settings
pygame.init()
beige_tower_1_image = 'images/towers/tower_sprites/beige_1.png'
beige_tower_2_image = 'images/towers/tower_sprites/beige_2.png'
blue_tower_1_image = 'images/towers/tower_sprites/blue_1.png'
blue_tower_2_image = 'images/towers/tower_sprites/blue_2.png'
beige_tower_1_price = 150
beige_tower_1_resell = 75
beige_tower_1_upgrade = 150
beige_tower_1_attack = 5
beige_tower_1_speed = 0.5
beige_tower_1_radius = 128
beige_tower_2_price = 0
beige_tower_2_resell = 150
beige_tower_2_upgrade = 0
beige_tower_2_attack = 10
beige_tower_2_speed = 1
beige_tower_2_radius = 192
beige_tower1 = (beige_tower_1_price, beige_tower_1_upgrade, beige_tower_1_resell, beige_tower_1_attack, beige_tower_1_speed, beige_tower_1_radius, beige_tower_1_image)
beige_tower2 = (beige_tower_2_price, beige_tower_2_upgrade, beige_tower_2_resell, beige_tower_2_attack, beige_tower_2_speed, beige_tower_2_radius, beige_tower_2_image)
blue_tower_1_price = 150
blue_tower_1_resell = 75
blue_tower_1_upgrade = 150
blue_tower_1_attack = 5
blue_tower_1_speed = 0.5
blue_tower_1_radius = 128
blue_tower_2_price = 0
blue_tower_2_resell = 150
blue_tower_2_upgrade = 0
blue_tower_2_attack = 10
blue_tower_2_speed = 1
blue_tower_2_radius = 192
blue_tower1 = (blue_tower_1_price, blue_tower_1_upgrade, blue_tower_1_resell, blue_tower_1_attack, blue_tower_1_speed, blue_tower_1_radius, blue_tower_1_image)
blue_tower2 = (blue_tower_2_price, blue_tower_2_upgrade, blue_tower_2_resell, blue_tower_2_attack, blue_tower_2_speed, blue_tower_2_radius, blue_tower_2_image)
tower_zones_list = []
# Process Tower zones:
def tower_zones_available():
    xmas_map = pytmx.load_pygame(settings.xmas_map, pixelalpha=True)
    tower_Zone_layer = xmas_map.get_layer_by_name('tower_Zone')
    for i in tower_Zone_layer:
        tower_zones_list.append(i)
# IMAGES FOR ENEMIES. ALL HAVE DIMENSIONS OF 59, 64
snowman_image = 'images/enemies/snowman.png'
gbm_image = 'images/enemies/gingerbreadman.png'
santa_image = 'images/enemies/santa.png'
snowman_speed = 1000
snowman_health = 20
snowman_worth = 40
gbm_speed = 1
gbm_health = 30
gbm_worth = 60
santa_speed = 1000
santa_health = 55
santa_worth = 90
# Tuples to be passed into Enemy_Type class
enemy1_xmas = (snowman_health, snowman_worth, snowman_speed, snowman_image)
enemy2_xmas = (gbm_health, gbm_worth, gbm_speed, gbm_image)
enemy3_xmas = (santa_health, santa_worth, santa_speed, santa_image)