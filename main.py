import buttons
import pygame
import enemy_track
pygame.init()
title_buttons_obj = buttons.TitleButtons
clock = pygame.time.Clock()
enemy_track_run_count = 0
tower_list = []
def game_loop():
    # global so not creating new objects every iteration of loop
    global buttons_obj
    global tower_list
    while not buttons.crashed:
        title_buttons_obj()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                buttons.crashed = True
        pygame.display.flip()
        clock.tick(30)
        if buttons.display_map and not buttons.crashed:
            global enemy_track_run_count
            buttons.map_obj.display_map()
            # pygame.time.delay(100)
            # so the data doesn't process multiple times in this loop
            if enemy_track_run_count < 1:
                enemy_track.game_xmas()
                enemy_track_run_count += 1
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    buttons.crashed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                buttons.crashed = True
        pygame.display.flip()
        clock.tick(30)
game_loop()
pygame.quit()
quit()
