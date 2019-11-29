

#IMAGES FOR ENEMIES. ALL HAVE DIMENSIONS OF 59, 64
snowman_image = 'images/enemies/snowman.png'
gbm_image = 'images/enemies/gingerbreadman.png'
santa_image = 'images/enemies/santa.png'
#snowman moves 1/8th tile per second
snowman_speed = 1000
snowman_health = 20
#snowman worth 40 dollars
snowman_worth = 40

gbm_speed = 1
gbm_health = 30
gbm_worth = 60

santa_speed = 1000
santa_health = 55
santa_worth = 90

#Tuples to be passed into Enemy_Type class
enemy1_xmas = (snowman_health, snowman_worth, snowman_speed, snowman_image)
enemy2_xmas = (gbm_health, gbm_worth, gbm_speed, gbm_image)
enemy3_xmas = (santa_health, santa_worth, santa_speed, santa_image)