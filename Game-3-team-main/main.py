# 1. Імпортувати модуль pygame
import pygame 
#
import modules.area as area
import modules.settings as settings
import modules.sprites as sprites
import modules.enemy as enemy
import modules.heart as heart
import modules.button as button
# 3. Ініціалізувати налаштування pygame
pygame.init()

win_height = 800
win_width = 800

start_game = True
  
# 4.Cтворюємо ігровое вікно з ім'ям win 
win = pygame.display.set_mode((win_width,win_height))
# 5. Задаємо назву ігрового вікна
pygame.display.set_caption("Advanture of man")
# 6. Створюємо основну функцію гри run_game:
def run_game():

    global start_game

    clock = pygame.time.Clock()
    
    # - задаємо змінну game, що відповідає за роботу циклу   
    game = True
    # - задаємо ігровий цикл while, 
    while game:
    # - задаємо умову закриття ігрового вікна,
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start_game:
                mouse_cor = pygame.mouse.get_pos()
                if button.check_mouse_cor(button.play_button, mouse_cor):
                    start_game = False
                # elif button.check_mouse_cor(button.settings_button, mouse_cor):
                #     settings_win_height = 800
                #     settings_win_width = 800
                #     win2 = pygame.display.set_mode((settings_win_width,settings_win_height))
                #     pygame.display.set_caption("Advanture of man")

        if start_game:
            settings.start.blit_sprite(win)
            button.play_button.blit_sprite(win)
            # button.settings_button.blit_sprite(win)
    # - задіємо об'єкт sprite і викликаємо його метод blit_sprite(), малюємо зображення на ігровому вікні, в центрі екрану
        if not heart.game_over and not start_game:

            settings.fon1.blit_sprite(win)

            for el in area.list_create_area:
                # pygame.draw.rect(win, el.COLOR, el.RECT)
                el.blit_sprite(win)
            #
            # sprites.sprite.draw_rect(win)
            # enemy.enemy2.draw_rect(win)
            #
            area.change_level()
            heart.show_hearts(win)
            sprites.sprite.blit_sprite(win)
            enemy.enemy1.blit_sprite(win)
            enemy.enemy2.blit_sprite(win)
            enemy.enemy3.blit_sprite(win)
            enemy.enemy4.blit_sprite(win)
            #
            sprites.sprite.can_move_right(area.list_rect)
            sprites.sprite.can_move_left(area.list_rect)

            #
            sprites.sprite.move_sprite(area.list_rect)
            enemy.enemy1.move_enemy(area.list_rect, name_folder="robot_move", count_while= 2, last_img= 15, first_img= 2)
            enemy.enemy4.move_enemy(area.list_rect, name_folder="robot_shoot", count_while=4, last_img=13, first_img=2)
            #
            sprites.sprite.jump(area.list_rect)
            #
            sprites.sprite.gravity(list_rect= area.list_rect)
            enemy.enemy1.gravity(list_rect= area.list_rect)
            enemy.enemy2.gravity(list_rect= area.list_rect)
            enemy.enemy3.gravity(list_rect= area.list_rect)
            enemy.enemy4.gravity(list_rect= area.list_rect)

            enemy.enemy2.shoot(win, 200, list_rect= area.list_rect, width=80, height=25, name_sprite= sprites.sprite)
            enemy.enemy3.shoot(win, 200, list_rect= area.list_rect, width=80, height= 25, name_sprite= sprites.sprite)
            enemy.enemy4.shoot(win, 100, list_rect= area.list_rect, width= 55, height= 37, name_sprite= sprites.sprite)
            
        elif heart.game_over:
            settings.end.blit_sprite(win)
        area.change_level()
    # - задаємо оновлення ігрового екрану
        clock.tick(60)
        pygame.display.flip()
# 11. І найголовніше – викликаємо основну функцію гри
run_game()