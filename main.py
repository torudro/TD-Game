import buttons
import pygame
import enemies
import enemy_info
import enemy_track
pygame.init()


#will eventually add enemies based on wave, probably a loop or something

buttons_obj = buttons.Buttons

clock = pygame.time.Clock()

enemy_track_run_count = 0
def game_loop():

    #global so not creating new objects every iteration of loop
    global buttons_obj

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
                buttons.map_data.display()
                #pygame.time.delay(100)
                for i in range(len(buttons.enemy_obj_list)):
                    #print(buttons.enemy_obj_list)
                    '''if buttons.enemy_obj_list[0][i].enemy_path_list_x[enemies.list_counter] == 832:
                        print('LOOP PRINTED:', buttons.enemy_obj_list)
                        del buttons.enemy_obj_list[i]
                        print('DELETED')'''
                #so the data doesn't process multiple times in this loop
                if enemy_track_run_count < 1:
                    enemy_track.game_xmas()
                    enemy_track_run_count += 1


                #pygame.display.flip()
                clock.tick(30)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        buttons.crashed = True

            '''if button is thanksgiving'''


            #pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    buttons.crashed = True

            pygame.display.flip()
            clock.tick(30)

game_loop()
pygame.quit()
quit()
