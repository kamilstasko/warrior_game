import pygame, os, datetime, sys
from data import image_pause, wielkosc_bloku, image_ground, image_wood, tree_1, tree_2, bush_1, bush_2, flower_1, flower_2, flower_3, flower_4, flower_5, image_finish, image_check
from base_level import Level
from objects import Platform
from menu import Pause_menu

# runda 1
class Level_1(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.position = [3 * wielkosc_bloku, self.player.screen_height - 2 * wielkosc_bloku]
        self.player.rect.center = self.position
        self.max_crystal = 5

        # platformy
        # pozycja:        szerokość             wysokość              położenie_x             położenie_y             obraz       ruch    rozmiar_ruchu
        self.wp = [
                   [ 17 * wielkosc_bloku,   2 * wielkosc_bloku,  -1 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   2 * wielkosc_bloku,  20 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   5 * wielkosc_bloku,  25 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   2 * wielkosc_bloku,  30 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  38 * wielkosc_bloku, self.player.screen_height -  18 * wielkosc_bloku,   image_wood, 1,  16 * wielkosc_bloku],
                   [  6 * wielkosc_bloku,  10 * wielkosc_bloku,  47 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  43 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 2,  10 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   7 * wielkosc_bloku,  56 * wielkosc_bloku, self.player.screen_height -   6 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   7 * wielkosc_bloku,  63 * wielkosc_bloku, self.player.screen_height -   6 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,  10 * wielkosc_bloku,  70 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,  13 * wielkosc_bloku, 100 * wielkosc_bloku, self.player.screen_height -  12 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  56 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 2,   8 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  69 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku,   image_wood, 2,  12 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  86 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 2,   8 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 107 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku,   image_wood, 1,   8 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 114 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku,   image_wood, 1,   3 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 121 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku,   image_wood, 1,   8 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 128 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku,   image_wood, 1,   3 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,  11 * wielkosc_bloku, 136 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,  21 * wielkosc_bloku, 135 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,  14 * wielkosc_bloku, 142 * wielkosc_bloku, self.player.screen_height -  13 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   2 * wielkosc_bloku, 144 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   2 * wielkosc_bloku, 150 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   2 * wielkosc_bloku, 156 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   4 * wielkosc_bloku, 159 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   6 * wielkosc_bloku, 162 * wielkosc_bloku, self.player.screen_height -   5 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   8 * wielkosc_bloku, 165 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,  10 * wielkosc_bloku, 168 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,  12 * wielkosc_bloku, 171 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 179 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 186 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 193 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 200 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,  13 * wielkosc_bloku, 206 * wielkosc_bloku, self.player.screen_height -  12 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 20 * wielkosc_bloku,   2 * wielkosc_bloku, 225 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                  ]

        # obiekty statyczne tła
        # pozycja:     położenie_x                                położenie_y                 obraz
        self.so = [
                   [  -1 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [   5 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [  11 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [  25 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku, tree_2],
                   [  48 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, bush_1],
                   [  71 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, bush_2],
                   [ 136 * wielkosc_bloku, self.player.screen_height -  21 * wielkosc_bloku, flower_1],
                   [ 143 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, flower_2],
                   [ 151 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_2],
                   [ 172 * wielkosc_bloku, self.player.screen_height -  12 * wielkosc_bloku, flower_3],
                   [ 207 * wielkosc_bloku, self.player.screen_height -  13 * wielkosc_bloku, flower_4],
                   [ 227 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_5],
                   [ 238 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, tree_2],
                   [ 242 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, tree_2],
                  ]

        # kryształy
        self.cr = [
                   [ self,  57 * wielkosc_bloku, self.player.screen_height -  7 * wielkosc_bloku, True],
                   [ self, 122 * wielkosc_bloku, self.player.screen_height - 12 * wielkosc_bloku, True],
                   [ self, 138 * wielkosc_bloku, self.player.screen_height - 11 * wielkosc_bloku, True],
                   [ self, 145 * wielkosc_bloku, self.player.screen_height -  2 * wielkosc_bloku, True],
                   [ self, 187 * wielkosc_bloku, self.player.screen_height - 12 * wielkosc_bloku, True],
                  ]
        
        self.load()
        self.info = True

    def load(self):
        # checkpointer
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 102 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, image_check, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        # finish
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 235 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, image_finish, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        super().load()
            
    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_level = Pause_menu(self.player, image_pause, self.player.level, 'Pause_menu')
                self.player.level = current_level

# runda 2
class Level_2(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.position = [3 * wielkosc_bloku, self.player.screen_height - 2 * wielkosc_bloku]
        self.player.rect.center = self.position
        self.max_crystal = 4

        # platformy
        # pozycja:        szerokość             wysokość              położenie_x                          położenie_y                   obraz       ruch    rozmiar_ruchu
        self.wp = [
                   [ 19 * wielkosc_bloku,   2 * wielkosc_bloku,  -1 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   3 * wielkosc_bloku,  18 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   4 * wielkosc_bloku,  20 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   5 * wielkosc_bloku,  22 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   6 * wielkosc_bloku,  24 * wielkosc_bloku, self.player.screen_height -   5 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   7 * wielkosc_bloku,  26 * wielkosc_bloku, self.player.screen_height -   6 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   8 * wielkosc_bloku,  28 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 18 * wielkosc_bloku,   2 * wielkosc_bloku,  30 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  9 * wielkosc_bloku,   1 * wielkosc_bloku,  35 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  52 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku,   image_wood, 1,  10 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,  12 * wielkosc_bloku,  58 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 20 * wielkosc_bloku,  14 * wielkosc_bloku,  63 * wielkosc_bloku, self.player.screen_height -  13 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   1 * wielkosc_bloku,  88 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   1 * wielkosc_bloku,  94 * wielkosc_bloku, self.player.screen_height -  16 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   1 * wielkosc_bloku, 100 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  2 * wielkosc_bloku,   1 * wielkosc_bloku, 106 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,  18 * wielkosc_bloku, 112 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,   1 * wielkosc_bloku, 117 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,   1 * wielkosc_bloku, 125 * wielkosc_bloku, self.player.screen_height -  13 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [  4 * wielkosc_bloku,   1 * wielkosc_bloku, 117 * wielkosc_bloku, self.player.screen_height -   6 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,   1 * wielkosc_bloku, 133 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [ 30 * wielkosc_bloku,   4 * wielkosc_bloku, 123 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 157 * wielkosc_bloku, self.player.screen_height -   5 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 164 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 171 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 178 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 185 * wielkosc_bloku, self.player.screen_height -  13 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [ 15 * wielkosc_bloku,  16 * wielkosc_bloku, 192 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                  ]

        # obiekty statyczne tła
        # pozycja:     położenie_x                                położenie_y                 obraz
        self.so = [
                   [   0 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, tree_2],
                   [   5 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, tree_2],
                   [  12 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, tree_2],
                   [  32 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_1],
                   [  47 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_2],
                   [  58 * wielkosc_bloku, self.player.screen_height -  18 * wielkosc_bloku, tree_1],
                   [ 127 * wielkosc_bloku, self.player.screen_height -   5 * wielkosc_bloku, bush_2],
                   [ 140 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku, tree_1],
                   [ 194 * wielkosc_bloku, self.player.screen_height -  21 * wielkosc_bloku, tree_2],
                   [ 200 * wielkosc_bloku, self.player.screen_height -  21 * wielkosc_bloku, tree_2],
                  ]

        # kryształy
        self.cr = [
                   [ self,  39 * wielkosc_bloku, self.player.screen_height -  2 * wielkosc_bloku, True],
                   [ self,  70 * wielkosc_bloku, self.player.screen_height - 14 * wielkosc_bloku, True],
                   [ self, 117 * wielkosc_bloku, self.player.screen_height -  7 * wielkosc_bloku, True],
                   [ self, 144 * wielkosc_bloku, self.player.screen_height -  4 * wielkosc_bloku, True],
                  ]

        # przeciwnicy
        self.op = [
                   [ self,  30 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, '1_ORK'],
                   [ self,  37 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, '2_ORK'],
                   [ self,  64 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku, '3_ORK'],
                   [ self,  67 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku, '3_ORK'],
                   [ self,  70 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku, '3_ORK'],
                   [ self, 195 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, '1_ORK'],
                  ]
        
        self.load()
        self.info = True

    def load(self):
        # checkpointer
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 114 * wielkosc_bloku, self.player.screen_height -  19 * wielkosc_bloku, image_check, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        # finish
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 198 * wielkosc_bloku, self.player.screen_height -   17 * wielkosc_bloku, image_finish, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        super().load()
            
    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_level = Pause_menu(self.player, image_pause, self.player.level, 'Pause_menu')
                self.player.level = current_level

# runda 3
class Level_3(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.position = [3 * wielkosc_bloku, self.player.screen_height - 2 * wielkosc_bloku]
        self.player.rect.center = self.position
        self.max_crystal = 5

        # platformy
        # pozycja:        szerokość             wysokość              położenie_x                          położenie_y                   obraz       ruch    rozmiar_ruchu
        self.wp = [
                   [ 22 * wielkosc_bloku,   2 * wielkosc_bloku,  -1 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku,  25 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku,   image_wood, 1,   6 * wielkosc_bloku],
                   [ 23 * wielkosc_bloku,  10 * wielkosc_bloku,  31 * wielkosc_bloku, self.player.screen_height -  22 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 20 * wielkosc_bloku,   8 * wielkosc_bloku,  31 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 66 * wielkosc_bloku,  20 * wielkosc_bloku,  54 * wielkosc_bloku, self.player.screen_height -  31 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 17 * wielkosc_bloku,   5 * wielkosc_bloku,  51 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 12 * wielkosc_bloku,   7 * wielkosc_bloku,  68 * wielkosc_bloku, self.player.screen_height -   6 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 40 * wielkosc_bloku,   5 * wielkosc_bloku,  80 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 121 * wielkosc_bloku, self.player.screen_height -  25 * wielkosc_bloku,   image_wood, 1,  19 * wielkosc_bloku],
                   [ 12 * wielkosc_bloku,   5 * wielkosc_bloku, 120 * wielkosc_bloku, self.player.screen_height -  33 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 12 * wielkosc_bloku,  13 * wielkosc_bloku, 132 * wielkosc_bloku, self.player.screen_height -  33 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 37 * wielkosc_bloku,   5 * wielkosc_bloku, 125 * wielkosc_bloku, self.player.screen_height -  25 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 10 * wielkosc_bloku,  15 * wielkosc_bloku, 125 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 20 * wielkosc_bloku,  13 * wielkosc_bloku, 135 * wielkosc_bloku, self.player.screen_height -  12 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  7 * wielkosc_bloku,  15 * wielkosc_bloku, 155 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 164 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku,   image_wood, 2,   8 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 178 * wielkosc_bloku, self.player.screen_height -  16 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  3 * wielkosc_bloku,   1 * wielkosc_bloku, 184 * wielkosc_bloku, self.player.screen_height -  18 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  5 * wielkosc_bloku,  21 * wielkosc_bloku, 190 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 14 * wielkosc_bloku,   9 * wielkosc_bloku, 212 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                  ]

        # obiekty statyczne tła
        # pozycja:     położenie_x                                położenie_y                 obraz
        self.so = [
                   [  -1 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [   6 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_1],
                   [  11 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [ 212 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, flower_1],
                   [ 215 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, flower_2],
                   [ 218 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, flower_3],
                   [ 222 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, flower_4],
                   [ 225 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku, flower_5],
                  ]

        # kryształy
        self.cr = [
                   [ self,  64 * wielkosc_bloku, self.player.screen_height -  5 * wielkosc_bloku, True],
                   [ self, 110 * wielkosc_bloku, self.player.screen_height -  5 * wielkosc_bloku, True],
                   [ self, 130 * wielkosc_bloku, self.player.screen_height - 26 * wielkosc_bloku, True],
                   [ self, 158 * wielkosc_bloku, self.player.screen_height - 15 * wielkosc_bloku, True],
                   [ self, 192 * wielkosc_bloku, self.player.screen_height - 21 * wielkosc_bloku, True],
                  ]

        # przeciwnicy
        self.op = [
                   [ self,  72 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, '2_ORK'],
                   [ self, 137 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, '1_ORK'],
                   [ self, 140 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, '2_ORK'],
                   [ self, 143 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, '3_ORK'],
                  ]

        # kolce
        self.sp = [
                   [ self,  59 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku],
                   [ self,  86 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku],
                   [ self,  90 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku],
                   [ self,  94 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku],
                   [ self,  98 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku],
                   [ self, 102 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku],
                  ]
        
        self.load()
        self.info = True

    def load(self):
        # checkpointer
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 113 * wielkosc_bloku, self.player.screen_height -   6 * wielkosc_bloku, image_check, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        # finish
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 220 * wielkosc_bloku, self.player.screen_height -   10 * wielkosc_bloku, image_finish, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        super().load()
            
    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_level = Pause_menu(self.player, image_pause, self.player.level, 'Pause_menu')
                self.player.level = current_level

# runda 4
class Level_4(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.position = [3 * wielkosc_bloku, self.player.screen_height - 2 * wielkosc_bloku]
        self.player.rect.center = self.position
        self.max_crystal = 5

        # platformy
        # pozycja:        szerokość             wysokość              położenie_x                          położenie_y                   obraz       ruch    rozmiar_ruchu
        self.wp = [
                   [  45 * wielkosc_bloku,   2 * wielkosc_bloku,  -1 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  16 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku,   image_wood, 1,   7 * wielkosc_bloku],
                   [  10 * wielkosc_bloku,   1 * wielkosc_bloku,  20 * wielkosc_bloku, self.player.screen_height -  12 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [  10 * wielkosc_bloku,   1 * wielkosc_bloku,  25 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [  30 * wielkosc_bloku,   3 * wielkosc_bloku,  44 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [ 100 * wielkosc_bloku,   2 * wielkosc_bloku,  74 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   1 * wielkosc_bloku,   1 * wielkosc_bloku,  76 * wielkosc_bloku, self.player.screen_height -   5 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   1 * wielkosc_bloku,   1 * wielkosc_bloku,  79 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  34 * wielkosc_bloku,   2 * wielkosc_bloku,  83 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   1 * wielkosc_bloku,   1 * wielkosc_bloku, 125 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   1 * wielkosc_bloku,   1 * wielkosc_bloku, 128 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   1 * wielkosc_bloku,   1 * wielkosc_bloku, 131 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   1 * wielkosc_bloku,   1 * wielkosc_bloku, 134 * wielkosc_bloku, self.player.screen_height -  13 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  25 * wielkosc_bloku,   1 * wielkosc_bloku, 137 * wielkosc_bloku, self.player.screen_height -  16 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [  20 * wielkosc_bloku,  17 * wielkosc_bloku, 167 * wielkosc_bloku, self.player.screen_height -  16 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 190 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 197 * wielkosc_bloku, self.player.screen_height -  12 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 204 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 211 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   7 * wielkosc_bloku,   1 * wielkosc_bloku, 218 * wielkosc_bloku, self.player.screen_height -  16 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                  ]

        # obiekty statyczne tła
        # pozycja:     położenie_x                                położenie_y                 obraz
        self.so = [
                   [  -1 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_1],
                   [   6 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_2],
                   [  12 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_2],
                   [  19 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_2],
                   [  29 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, bush_1],
                   [  37 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [  48 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_2],
                   [  60 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_2],
                   [ 137 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, flower_1],
                   [ 142 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, flower_2],
                   [ 147 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, flower_3],
                   [ 152 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, flower_4],
                   [ 157 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku, flower_5],
                   [ 171 * wielkosc_bloku, self.player.screen_height -  23 * wielkosc_bloku, tree_1],
                   [ 180 * wielkosc_bloku, self.player.screen_height -  23 * wielkosc_bloku, tree_1],
                  ]

        # kryształy
        self.cr = [
                   [ self,  27 * wielkosc_bloku, self.player.screen_height -  9 * wielkosc_bloku, True],
                   [ self, 100 * wielkosc_bloku, self.player.screen_height - 11 * wielkosc_bloku, True],
                   [ self, 109 * wielkosc_bloku, self.player.screen_height -  2 * wielkosc_bloku, True],
                   [ self, 164 * wielkosc_bloku, self.player.screen_height -  8 * wielkosc_bloku, True],
                   [ self, 177 * wielkosc_bloku, self.player.screen_height - 17 * wielkosc_bloku, True],
                  ]

        # przeciwnicy
        self.op = [
                   [ self,  22 * wielkosc_bloku, self.player.screen_height -  14 * wielkosc_bloku, '1_TROLL'],
                   [ self,  29 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku, '2_TROLL'],
                   [ self,  46 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, '3_TROLL'],
                   [ self,  49 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, '3_TROLL'],
                   [ self,  52 * wielkosc_bloku, self.player.screen_height -   4 * wielkosc_bloku, '3_TROLL'],
                   [ self, 169 * wielkosc_bloku, self.player.screen_height -  18 * wielkosc_bloku, '1_TROLL'],
                  ]

        # kolce
        self.sp = [
                   [ self,  87 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku],
                   [ self,  90 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku],
                   [ self,  93 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku],
                   [ self,  96 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku],
                   [ self,  99 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku],
                   [ self, 102 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku],
                  ]
        
        self.load()
        self.info = True

    def load(self):
        # checkpointer
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 113 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, image_check, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        # finish
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 221 * wielkosc_bloku, self.player.screen_height -   18 * wielkosc_bloku, image_finish, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        super().load()
            
    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_level = Pause_menu(self.player, image_pause, self.player.level, 'Pause_menu')
                self.player.level = current_level

# runda 5
class Level_5(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.position = [3 * wielkosc_bloku, self.player.screen_height - 2 * wielkosc_bloku]
        self.player.rect.center = self.position
        self.max_crystal = 5

        # platformy
        # pozycja:        szerokość             wysokość              położenie_x                          położenie_y                   obraz       ruch    rozmiar_ruchu
        self.wp = [
                   [  17 * wielkosc_bloku,   2 * wielkosc_bloku,  -1 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  18 * wielkosc_bloku, self.player.screen_height -  10 * wielkosc_bloku,   image_wood, 1,   8 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  24 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 1,  10 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  30 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  36 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 2,   8 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  44 * wielkosc_bloku, self.player.screen_height -  15 * wielkosc_bloku,   image_wood, 2,  14 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  66 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 2,   7 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  79 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  85 * wielkosc_bloku, self.player.screen_height -  20 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  79 * wielkosc_bloku, self.player.screen_height -  23 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  85 * wielkosc_bloku, self.player.screen_height -  26 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  79 * wielkosc_bloku, self.player.screen_height -  29 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  85 * wielkosc_bloku, self.player.screen_height -  32 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku,  91 * wielkosc_bloku, self.player.screen_height -  32 * wielkosc_bloku,   image_wood, 2,  15 * wielkosc_bloku],
                   [   5 * wielkosc_bloku,   1 * wielkosc_bloku, 112 * wielkosc_bloku, self.player.screen_height -  32 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 120 * wielkosc_bloku, self.player.screen_height -  32 * wielkosc_bloku,   image_wood, 1,  12 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 126 * wielkosc_bloku, self.player.screen_height -  29 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 135 * wielkosc_bloku, self.player.screen_height -  29 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 144 * wielkosc_bloku, self.player.screen_height -  29 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 150 * wielkosc_bloku, self.player.screen_height -  29 * wielkosc_bloku,   image_wood, 1,   6 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 156 * wielkosc_bloku, self.player.screen_height -  23 * wielkosc_bloku,   image_wood, 1,   6 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 162 * wielkosc_bloku, self.player.screen_height -  17 * wielkosc_bloku,   image_wood, 1,   6 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 168 * wielkosc_bloku, self.player.screen_height -  11 * wielkosc_bloku,   image_wood, 2,   8 * wielkosc_bloku],
                   [   5 * wielkosc_bloku,   1 * wielkosc_bloku, 182 * wielkosc_bloku, self.player.screen_height -   9 * wielkosc_bloku,   image_wood, 0,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 193 * wielkosc_bloku, self.player.screen_height -   7 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 202 * wielkosc_bloku, self.player.screen_height -   5 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [   3 * wielkosc_bloku,   1 * wielkosc_bloku, 211 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku,   image_wood, 3,   0 * wielkosc_bloku],
                   [  20 * wielkosc_bloku,   2 * wielkosc_bloku, 220 * wielkosc_bloku, self.player.screen_height -   1 * wielkosc_bloku, image_ground, 0,   0 * wielkosc_bloku],
                  ]

        # obiekty statyczne tła
        # pozycja:     położenie_x                                położenie_y                 obraz
        self.so = [
                   [   1 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_1],
                   [   3 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_2],
                   [   5 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_3],
                   [   7 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_4],
                   [   9 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_5],
                   [  11 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_1],
                   [  13 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_2],
                   [  15 * wielkosc_bloku, self.player.screen_height -   2 * wielkosc_bloku, flower_3],
                   [ 222 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [ 229 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                   [ 236 * wielkosc_bloku, self.player.screen_height -   8 * wielkosc_bloku, tree_1],
                  ]

        # kryształy
        self.cr = [
                   [ self,  31 * wielkosc_bloku, self.player.screen_height - 18 * wielkosc_bloku, True],
                   [ self,  86 * wielkosc_bloku, self.player.screen_height - 33 * wielkosc_bloku, True],
                   [ self, 100 * wielkosc_bloku, self.player.screen_height - 37 * wielkosc_bloku, True],
                   [ self, 121 * wielkosc_bloku, self.player.screen_height - 22 * wielkosc_bloku, True],
                   [ self, 184 * wielkosc_bloku, self.player.screen_height - 10 * wielkosc_bloku, True],
                  ]
        
        self.load()
        self.info = True

    def load(self):
        # checkpointer
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 114 * wielkosc_bloku, self.player.screen_height -  34 * wielkosc_bloku, image_check, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        # finish
        platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, 230 * wielkosc_bloku, self.player.screen_height -   3 * wielkosc_bloku, image_finish, 0,   0 * wielkosc_bloku)
        self.special_objects.add(platform)

        super().load()
            
    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_level = Pause_menu(self.player, image_pause, self.player.level, 'Pause_menu')
                self.player.level = current_level
