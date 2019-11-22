import map_data
import enemies
import data_location
#I don't think I need to import enemy_info

import pytmx
import pygame

#will eventually add selection so it will either be XMAS or TG map
map_ = map_data.map_reader(data_location.christmas_map)

#will eventually add enemies based on wave, probably a loop or something
enemy = enemies.Enemy('snowman')

#begins by displaying map
#map_.display_map()

def game_loop():
    crashed = False
    while not crashed:
        map_.display_map()
        enemy.draw()
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        pygame.map_.display.flip()
        map_.clock.tick(30)
