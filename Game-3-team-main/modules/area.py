import pygame
import os
import modules.settings as settings
import modules.sprites as sprits

win_height = 800
win_width = 800

area_w = 100
area_h = 75

level_counter = 1

list_area_1 = [
    "000000001",
    "000000001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110000001",
    "000110001",
    "000000011",
    "111111111"
]

list_area_2 = [
    "010001001",
    "001010001",
    "000010111",
    "110000011",
    "111011001",
    "000001001",
    "000001111",
    "110010001",
    "000110001",
    "000000011",
    "111111111"
]

list_area_3 = [
    "010010001",
    "001000101",
    "010010111",
    "110010011",
    "111000001",
    "000001001",
    "000101111",
    "110010001",
    "000110001",
    "010000011",
    "111111111"
]

list_area_4 = [
    "010001001",
    "000100101",
    "000010111",
    "110000011",
    "111000001",
    "010001001",
    "000101111",
    "110001001",
    "000110001",
    "000000011",
    "111111111"
]

list_area_5 = [
    "100010001",
    "010001001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110001001",
    "000110001",
    "000100011",
    "111111111"
]

list_area_6 = [
    "001001001",
    "010011001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110000101",
    "000110001",
    "000000011",
    "111111111"
]

list_area_7 = [
    "000110001",
    "001001001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110001001",
    "000110001",
    "011000011",
    "111111111"
]

list_area_8 = [
    "011000001",
    "000011001",
    "000010111",
    "110001011",
    "111000001",
    "000001001",
    "000101111",
    "110001001",
    "000110001",
    "000000011",
    "111111111"
]

list_area_9 = [
    "110000001",
    "000011001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110000001",
    "000110001",
    "000110011",
    "111111111"
]

list_area_10 = [
    "011000001",
    "000110001",
    "000010111",
    "010000011",
    "111000001",
    "000001001",
    "000101111",
    "110000001",
    "000110001",
    "000000011",
    "111111111"
]

list_area_11 = [
    "010010001",
    "000001101",
    "000010111",
    "110000011",
    "111011001",
    "000001001",
    "000101111",
    "110000001",
    "000110001",
    "010000011",
    "111111111"
]

list_area_12 = [
    "110001001",
    "001000001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110000001",
    "000110001",
    "00000011",
    "111111111"
]
list_create_area = []
list_rect = []
class Area(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def draw_rect(self, win, rect):
    #     pygame.draw.rect(win, self.COLOR, rect)

def create_area(level):
    x = 0
    y = 0
    for string in level:
        for el in string:
            if el == "1":
                area = Area(
                    x= x,
                    y= y,
                    width= area_w,
                    height= area_h,
                    color= (255, 165, 0),
                    name_image= ("images/platforms/pl4.png")
                )
                list_create_area.append(area)
                list_rect.append(area.RECT)
            x += area_w
        x = 0
        y += area_h



def change_level():
        if sprits.sprite.X == 650 and sprits.sprite.Y == 0:
            sprits.sprite.X = 91
            sprits.sprite.Y = 690
            level_counter += 1
            if level_counter == 2:
                create_area(list_area_2)
            if level_counter == 3:
                create_area(list_area_3)
            if level_counter == 4:
                create_area(list_area_4)
            if level_counter == 5:
                create_area(list_area_5)
            if level_counter == 6:
                create_area(list_area_6)
            if level_counter == 7:
                create_area(list_area_7)
            if level_counter == 8:
                create_area(list_area_8)
            if level_counter == 9:
                create_area(list_area_9)
            if level_counter == 10:
                create_area(list_area_10)
            if level_counter == 11:
                create_area(list_area_11)
            if level_counter == 12:
                create_area(list_area_12)
            print("Lf hf,jnftn")
create_area(list_area_1)





      

