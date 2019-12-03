import buttons
import enemies
import tower_enemy_info
# contains list of enemies to be spawned according to the difficulty and current wave
enemy_list = [buttons.mode_obj.enemy_amnt_list[buttons.wave_counter]]
# print(enemy_list)
enemy_type_list = [[], [], []]
enemy_obj_list = [[], [], []]
# needs to be a method that gets - called every time the next_wave button is clicked
def next_wave_enemies():
    # if buttons.MODE == 0 or buttons.MODE == 1 or buttons.MODE == 2:
    # loop that goes through the lists inside of the current wave
    for i in enemy_list[0][buttons.wave_counter]:
        # appends x enemies (depending on current wave) to enemy_obj_list[0][0], which is the 1st enemy slot
        enemy_obj_list[0][0].append(enemies.Enemy(enemy_list[0][i][0]) * enemy_info.enemy1_xmas)
        enemy_obj_list[0][1].append(enemies.Enemy(enemy_list[0][i][1]) * enemy_info.enemy2_xmas)
        enemy_obj_list[0][2].append(enemies.Enemy(enemy_list[0][i][2]) * enemy_info.enemy2_xmas)

    # Loops through enemy_obj_list, calling draw() for each of them.
    for i in range(len(enemy_obj_list[0])):
        enemy_obj_list[0][i].draw()
