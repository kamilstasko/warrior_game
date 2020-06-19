import pygame, os, datetime, sys
from data import spikes, image_crystal, wielkosc_bloku

# klasa zbieranych diamentów
class Crystal(pygame.sprite.Sprite):
    def __init__(self, level, rect_x, rect_y, active):
        super().__init__()
        self.level = level
        self.image = image_crystal
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y - 35
        self.start_x = rect_x
        self.start_y = rect_y
        self.collected = not active
        self.movement_y = -20
        self.move_y = 0

        if not active:
            self.rect.y += 2000
            self.move_y = -2001

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.collected:
            self.rect.y += self.movement_y
            self.move_y += self.movement_y

            if self.move_y < -2000:
                self.movement_y = 0

# klasa spadających kolcy
class Spike(pygame.sprite.Sprite):
    def __init__(self, level, rect_x, rect_y):
        super().__init__()
        self.level = level
        self.image = spikes
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.down = False
        self.speed = 10
        self.change = False
        self.start_x = rect_x
        self.start_y = rect_y
        self.move_y = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.down:
            self.rect.y += self.speed
            self.move_y += self.speed
            self.speed += 1

        if self.change:
            self.level.sp[self.level.sp.index([self.level, self.start_x, self.start_y, self.start_y])] = [self.level, self.start_x, self.start_y + self.move_y, self.start_y]
            self.change = False

# klasa statycznych obiektów tła
class Static_object(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y, image):
        super().__init__()
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.width = image[1]
        self.height = image[2]

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.image,(self.width, self.height)),(self.rect.x, self.rect.y))

# klasa broni przeciwnika
class Weapon(pygame.sprite.Sprite):
    def __init__(self, opponent):
        super().__init__()
        self.opponent = opponent
        self.image_nr = 0
        self.image = self.opponent.image_weapon[0]
        self.rect = self.image.get_rect()
        self.rect.y = self.opponent.rect.y + 75

        if self.opponent.movement_x > 0:
            self.rect.x = self.opponent.rect.x + 260
            self.move = 1
            self.speed = 12
        else:
            self.move = -1
            self.rect.x = self.opponent.rect.x - 42
            self.speed = -12

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += 3 * self.move + self.speed
        self.image_nr += self.move
        
        if self.image_nr > 3:
            self.image_nr = 0
        elif self.image_nr < 0:
            self.image_nr = 3

        if self.move > 0:
            self.speed += 0.2   
        else:
            self.speed -= 0.2

        self.image = self.opponent.image_weapon[self.image_nr]

# klasa broni gracza
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = self.player.image_bullet[0]
        self.image_nr = 0
        self.rect = self.image.get_rect()
        self.rect.y = self.player.rect.y + 50

        if self.player.direction_of_movement == 'right':
            self.rect.x = self.player.rect.x + 70
            self.move = 1
            self.speed = 12
        else:
            self.move = -1
            self.rect.x = self.player.rect.x
            self.speed = -12
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += 3 * self.move + self.speed
        self.image_nr += self.move
        
        if self.image_nr > 7:
            self.image_nr = 0
        elif self.image_nr < 0:
            self.image_nr = 7

        if self.move > 0:
            self.speed += 0.2   
        else:
            self.speed -= 0.2

        self.image = self.player.image_bullet[self.image_nr]

# klasa platformy
class Platform(pygame.sprite.Sprite):
    def __init__(self, player, width, height, rect_x, rect_y, image_list, move, size_move):
        super().__init__()
        self.player = player
        self.image = pygame.surface.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.image_list = image_list
        self.start_x = rect_x
        self.start_y = rect_y
        self.movement_x = 0
        self.movement_y = 0
        self.move = move
        self.size_move = size_move
        self.go = [1, rect_y]
        if move == 2:
            self.go = [1, rect_x]
        self.fall = False

    def draw(self, surface):
        if not isinstance(self.image_list, list):
            surface.blit(self.image_list, self.rect)
        else:
            if len(self.image_list) > 3:
                if self.rect.width == wielkosc_bloku:
                    surface.blit(self.image_list[0], self.rect)
                elif self.rect.height > wielkosc_bloku:
                    for i in range(0, self.rect.height - wielkosc_bloku + 1, wielkosc_bloku):
                        if i == 0:
                            x = 1
                        else:
                            x = 4
                                
                        surface.blit(self.image_list[x], [self.rect.x, self.rect.y + i])
                        for j in range(wielkosc_bloku, self.rect.width - wielkosc_bloku, wielkosc_bloku):
                            surface.blit(self.image_list[x+1], [self.rect.x + j, self.rect.y + i])
                        surface.blit(self.image_list[x+2], [self.rect.right - wielkosc_bloku, self.rect.y + i])
                else:
                    surface.blit(self.image_list[1], self.rect)
                    for i in range(wielkosc_bloku, self.rect.width - wielkosc_bloku, wielkosc_bloku):
                        surface.blit(self.image_list[2], [self.rect.x + i, self.rect.y])
                    surface.blit(self.image_list[3], [self.rect.right - wielkosc_bloku, self.rect.y])
            else:
                surface.blit(self.image_list[0], self.rect)
                for i in range(wielkosc_bloku, self.rect.width - wielkosc_bloku, wielkosc_bloku):
                    surface.blit(self.image_list[1], [self.rect.x + i, self.rect.y])
                surface.blit(self.image_list[2], [self.rect.right - wielkosc_bloku, self.rect.y])

    def update(self):
        if self.move == 1:
            if self.go[0] and self.go[1] <= self.start_y + self.size_move:
                self.movement_y = 4
            elif self.go[1] >= self.start_y:
                self.movement_y = -4
                self.go[0] = 0
            else:
                self.go[0] = 1

            if self.player.rect.y + 140 == self.rect.y and self.rect.x - wielkosc_bloku + 18 <= self.player.rect.x <= self.rect.x + self.rect.width:
                self.player.rect.y += self.movement_y
            self.rect.y += self.movement_y
            self.go[1] += self.movement_y
                
        elif self.move == 2:
            if self.go[0] and self.go[1] <= self.start_x + self.size_move:
                self.movement_x = 4
            elif self.go[1] >= self.start_x:
                self.movement_x = -4
                self.go[0] = 0
            else:
                self.go[0] = 1
                
            self.rect.x += self.movement_x
            self.go[1] += self.movement_x
            
        elif self.move == 3:
            if self.fall:
                if self.go[1] > 29:
                    self.rect.y += 2 + self.go[1] - 30
                self.go[1] += 1
            else:
                self.go[1] = 0
            if self.rect.y > 5000:
                self.fall = False
