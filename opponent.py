import pygame, os, datetime, sys
from data import katalog_z_obrazami
from objects import Weapon, Static_object

# klasa przeciwnika
class Opponent(pygame.sprite.Sprite):
    def __init__(self, level, rect_x, rect_y, select, remove = False):
        super().__init__()
        self._load_images(select)
        self.select = select
        self.image_list = self.image_walk_R
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.start_x = rect_x
        self.start_y = rect_y
        self.move_x = 0
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.level = level
        self.count_c = 0
        self.count_a = 0
        self.attack = False
        self.turn = True
        self.weapon = False
        self.platform_beg = 0
        self.platform_end = 0

        colliding = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for p in colliding:
            self.platform_beg = p.rect.x
            self.platform_end = p.rect.x + p.rect.w - self.rect.w

        self.rect.y -= 35

        if remove:
            self.remove_me = True
            self.rect.y += 35
            self.count_r = 27

            if remove == 1:
                self.movement_x = 6
            else:
                self.movement_x = -6
                
        else:
            self.count_r = 0
            self.remove_me = False
            self.movement_x = 6

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.attack:
            if self.turn:
                self.image_list = self.image_attack_R
            else:
                self.image_list = self.image_attack_L
            self._attacking()
        else:
            if self.remove_me:
                if self.movement_x > 0:
                    self.image_list = self.image_die_R
                else:
                    self.image_list = self.image_die_L
                self._removing()

            else:
                if not self.weapon:
                    if self.rect.x < self.level.player.screen_width and self.rect.x > 0 and self.rect.y + 175 < self.level.player.screen_height and self.rect.y > 0:
                        self._throw(self.movement_x)

                self.rect.x += self.movement_x

                colliding = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

                if not colliding:
                    if self.rect.x > self.platform_end or self.rect.x < self.platform_beg:
                        self.movement_x *= -1
                        self.rect.x += 2 * self.movement_x
                        self.count_c = 0
                else:
                    self.movement_x *= -1
                    self.rect.x += 2 * self.movement_x
                    self.count_c = 0

                if self.movement_x > 0:
                    self.image_list = self.image_walk_R
                    self.turn = True
                else:
                    self.image_list = self.image_walk_L
                    self.turn = False

                self.move_x += self.movement_x

                self._change_image()

    def remove_opponent(self):
        self.remove_me = True
        self._removing()

    def _throw(self, move):
        self.weapon = Weapon(self)
        self.level.opponents_weapon.add(self.weapon)

    def _attacking(self):
        if self.count_a < 3:
            self.image = self.image_list[0]
        elif self.count_a < 6:
            self.image = self.image_list[1]
        elif self.count_a < 9:
            self.image = self.image_list[2]
        elif self.count_a < 12:
            self.image = self.image_list[3]
        elif self.count_a < 15:
            self.image = self.image_list[4]
        elif self.count_a < 18:
            self.image = self.image_list[5]
        elif self.count_a < 21:
            self.image = self.image_list[6]
            self.level.player.opponent_attack = False
            self.level.player.die = True

        if self.count_a == 9:
            self.rect.y -= 35

        if self.count_a == 12:
            self.rect.y -= 20

        if self.count_a == 15:
            self.rect.y += 40

        if self.count_a == 18:
            self.rect.y += 15

        self.count_a += 1

    def _removing(self):
        if self.count_r < 2:
            self.image = self.image_list[0]
        elif self.count_r < 4:
            self.image = self.image_list[1]
        elif self.count_r < 6:
            self.image = self.image_list[2]
        elif self.count_r < 8:
            self.image = self.image_list[3]
        elif self.count_r < 10:
            self.image = self.image_list[4]
        elif self.count_r < 12:
            self.image = self.image_list[5]
        elif self.count_r < 14:
            self.image = self.image_list[6]
        elif self.count_r < 16:
            self.image = self.image_list[7]
        elif self.count_r < 18:
            self.image = self.image_list[8]
        elif self.count_r < 20:
            self.image = self.image_list[9]
        elif self.count_r < 22:
            self.image = self.image_list[10]
        elif self.count_r < 24:
            self.image = self.image_list[11]
        elif self.count_r < 26:
            self.image = self.image_list[12]
        elif self.count_r < 28:
            self.image = self.image_list[13]
            self.level.static_objects.add(Static_object(self.rect.x, self.rect.y, [self.image, self.image.get_rect().w, self.image.get_rect().h]))
            self.level.remove_opponent.append(self)

            if self.count_r != 27:
                if self.movement_x > 0:
                    self.level.rm[self.level.op.index([self.level, self.start_x, self.start_y, self.select])] = [1, self.start_x + self.move_x]
                else:
                    self.level.rm[self.level.op.index([self.level, self.start_x, self.start_y, self.select])] = [2, self.start_x + self.move_x]
            
        if self.count_r == 18:
            self.rect.y += 35 

        self.count_r += 1

    def _change_image(self):
        if self.count_c < 2:
            self.image = self.image_list[0]
        elif self.count_c < 4:
            self.image = self.image_list[1]
        elif self.count_c < 6:
            self.image = self.image_list[2]
        elif self.count_c < 8:
            self.image = self.image_list[3]
        elif self.count_c < 10:
            self.image = self.image_list[4]
        elif self.count_c < 12:
            self.image = self.image_list[5]
        elif self.count_c < 14:
            self.image = self.image_list[6]
        else:
            self.count_c = -1

        self.count_c += 1

    # ładowanie grafik przeciwnika
    def _load_images(self, select):
        walk_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/1.png'))
        walk_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/2.png'))
        walk_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/3.png'))
        walk_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/4.png'))
        walk_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/5.png'))
        walk_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/6.png'))
        walk_7_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_L/7.png'))
        walk_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/1.png'))
        walk_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/2.png'))
        walk_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/3.png'))
        walk_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/4.png'))
        walk_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/5.png'))
        walk_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/6.png'))
        walk_7_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'WALK_R/7.png'))
        hurt_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/1.png'))
        hurt_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/2.png'))
        hurt_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/3.png'))
        hurt_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/4.png'))
        hurt_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/5.png'))
        hurt_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/6.png'))
        hurt_7_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_L/7.png'))
        hurt_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/1.png'))
        hurt_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/2.png'))
        hurt_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/3.png'))
        hurt_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/4.png'))
        hurt_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/5.png'))
        hurt_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/6.png'))
        hurt_7_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'HURT_R/7.png'))
        die_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/1.png'))
        die_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/2.png'))
        die_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/3.png'))
        die_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/4.png'))
        die_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/5.png'))
        die_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/6.png'))
        die_7_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_L/7.png'))
        die_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/1.png'))
        die_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/2.png'))
        die_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/3.png'))
        die_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/4.png'))
        die_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/5.png'))
        die_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/6.png'))
        die_7_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'DIE_R/7.png'))
        attack_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/1.png'))
        attack_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/2.png'))
        attack_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/3.png'))
        attack_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/4.png'))
        attack_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/5.png'))
        attack_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/6.png'))
        attack_7_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_L/7.png'))
        attack_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/1.png'))
        attack_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/2.png'))
        attack_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/3.png'))
        attack_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/4.png'))
        attack_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/5.png'))
        attack_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/6.png'))
        attack_7_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent', select, 'ATTAK_R/7.png'))
        weapon_1 = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent/Weapon/1.png'))
        weapon_2 = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent/Weapon/2.png'))
        weapon_3 = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent/Weapon/3.png'))
        weapon_4 = pygame.image.load(os.path.join(katalog_z_obrazami,'Opponent/Weapon/4.png'))
        
        self.image_walk_L = [walk_1_L, walk_2_L, walk_3_L, walk_4_L, walk_5_L, walk_6_L, walk_7_L]
        self.image_walk_R = [walk_1_R, walk_2_R, walk_3_R, walk_4_R, walk_5_R, walk_6_R, walk_7_R]
        self.image_die_L = [hurt_1_L, hurt_2_L, hurt_3_L, hurt_4_L, hurt_5_L, hurt_6_L, hurt_7_L, die_1_L, die_2_L, die_3_L, die_4_L, die_5_L, die_6_L, die_7_L]
        self.image_die_R = [hurt_1_R, hurt_2_R, hurt_3_R, hurt_4_R, hurt_5_R, hurt_6_R, hurt_7_R, die_1_R, die_2_R, die_3_R, die_4_R, die_5_R, die_6_R, die_7_R]
        self.image_attack_L = [attack_1_L, attack_2_L, attack_3_L, attack_4_L, attack_5_L, attack_6_L, attack_7_L]
        self.image_attack_R = [attack_1_R, attack_2_R, attack_3_R, attack_4_R, attack_5_R, attack_6_R, attack_7_R]
        self.image_weapon = [weapon_1, weapon_2, weapon_3, weapon_4]
