import buttons
import pygame
import enemies
import enemy_info
import tower_info
import towers
import data_location
import enemy_track
pygame.init()


#will eventually add enemies based on wave, probably a loop or something

buttons_obj = buttons.Buttons

clock = pygame.time.Clock()

enemy_track_run_count = 0
tower_list = []
def game_loop():

    #global so not creating new objects every iteration of loop
    global buttons_obj
    global tower_list
    while not buttons.crashed:
        buttons_obj()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                buttons.crashed = True
        pygame.display.flip()
        clock.tick(30)

        while buttons.display_map and not buttons.crashed:

            '''if the modes display christmas map'''
            if buttons.display_xmas_map and not buttons.crashed:

                global enemy_track_run_count
                buttons.map_reader_obj.display_map()
                #pygame.time.delay(100)

                for event in pygame.event.get():

                    print(tower_info.tower_zones_list[0].y)
                    rect_dimension = (tower_info.tower_zones_list[0].x, tower_info.tower_zones_list[0].y, 64, 64)
                    rect = pygame.draw.rect(data_location.display, (0, 255, 0), pygame.Rect(rect_dimension))
                    mouse_pos = pygame.mouse.get_pos()
                    if rect[0] + rect[2] > mouse_pos[0] > rect[0] and rect[1] + rect[3] > mouse_pos[1] > rect[1] \
                            and event.type == pygame.MOUSEBUTTONDOWN:
                        tower_list.append(towers.Tower(towers.Tower_Type(tower_info.beige_tower_1)))
                        tower_list[0].create_tower(tower_info.tower_zones_list[0].x, tower_info.tower_zones_list[0].y)
                        print('test')
                        pass

                #so the data doesn't process multiple times in this loop
                if enemy_track_run_count < 1:
                    enemy_track.game_xmas()
                    enemy_track_run_count += 1


                #pygame.display.flip()
                clock.tick(30)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        buttons.crashed = True


            #pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    buttons.crashed = True

            pygame.display.flip()
            clock.tick(30)

game_loop()
pygame.quit()
quit()
