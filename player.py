import pygame, os, datetime, sys
from data import image_level_complete, image_game_over, screen, katalog_z_obrazami, image_lost_life, image_check, image_finish, image_pause, hi_scores_data
from menu import Level_complete, Game_over
from objects import Bullet

# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, hero, width, height):
        super().__init__()
        self.music = pygame.mixer.music
        self.window_open = True
        self.screen_width = width
        self.screen_height = height
        self.hero = hero
        self.image = None
        self.load_hero(hero)
        self.level = None
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.count_m = 0
        self.count_r = 0
        self.count_t = 0
        self.count_b = 0
        self.count_d = 0
        self.direction_of_movement = 'right'
        self.draw_player = False
        self.speed = False
        self.speed_jump = False
        self.live = 3
        self.crystal = 0
        self.save_crystal = 0
        self.save_position = False
        self.end_level = False
        self.list_bullet = set()
        self.throwing = False
        self.remove_bullet = False
        self.die = False
        self.opponent_attack = False
        self.music.load("music/menu.mp3")
        self.music.play(-1, 0.0)

    def reset_data(self):
        self.movement_x = 0
        self.movement_y = 0
        self.count_m = 0
        self.count_r = 0
        self.count_t = 0
        self.count_b = 0
        self.count_d = 0
        self.direction_of_movement = 'right'
        self.speed = False
        self.speed_jump = False
        self.live = 3
        self.crystal = 0
        self.save_crystal = 0
        self.save_position = False
        self.end_level = False
        self.list_bullet = set()
        self.throwing = False
        self.remove_bullet = False
        self.die = False
        self.opponent_attack = False

    def draw(self, surface):
        if self.draw_player:
            surface.blit(self.image, self.rect)

            for b in self.list_bullet:
                b.draw(surface)

    def turn_left(self):
        if self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
        self.movement_x = -6

    def turn_right(self):
        if self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'
        self.movement_x = 6

    def jump(self):
        if self.speed:
            self.speed_jump = True
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        self.rect.y -= 2
        if colliding_platforms:
            self.movement_y = -12

    def throw(self):
        if not self.throwing:
            self.throwing = True
    
    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y += 1
        else:
            self.movement_y += 0.35

    def stop_x(self):
        self.movement_x = 0

    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                self.speed = True
            elif event.key == pygame.K_d:
                self.turn_right()
            elif event.key == pygame.K_a:
                self.turn_left()
            elif event.key == pygame.K_w:
                self.jump()
            elif event.key == pygame.K_SPACE:
                self.throw()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                self.speed = False
            elif event.key == pygame.K_d and self.movement_x > 0:
                self.stop_x()
            elif event.key == pygame.K_a and self.movement_x < 0:
                self.stop_x()

    def update(self):
        if self.die:
            self.throwing = False
            self.count_b = 0
            
            if self.direction_of_movement == 'right':
                self._dieing(self.image_die_R)
            else:
                self._dieing(self.image_die_L)

        elif not self.opponent_attack:        
            # pociski
            for b in self.list_bullet:
                b.update()

                if b.rect.x > self.screen_width or b.rect.x < 0 or pygame.sprite.spritecollide(b, self.level.set_of_platforms, False) or pygame.sprite.spritecollide(b, self.level.opponents, False):
                    self.remove_bullet = b

            for x in self.level.opponents:
                if pygame.sprite.spritecollide(x, self.list_bullet, False):
                    x.remove_opponent()

            if self.remove_bullet:
                self.list_bullet.remove(self.remove_bullet)
                self.remove_bullet = False
                
            # ruchome obiekty poziome kolizja
            colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
            
            for p in colliding_platforms:
                if p.move == 2:
                    if p.go[0]:
                        self.rect.x += 4
                    else:
                        self.rect.x -= 4

            # bieganie i skakanie
            if self.movement_y == 0:
                self.speed_jump = False

            # rysowanie gracza i grawitacja
            if self.draw_player:
                self._gravitation()
            else:
                self.movement_y = 0

            # bieganie
            if self.speed_jump or self.speed and self.rect.y + self.movement_y == self.rect.y + 1:
                if self.movement_x > 0:
                    self.movement_x = 12
                elif self.movement_x < 0:
                    self.movement_x = -12
            else:
                if self.movement_x > 0:
                    self.movement_x = 8
                elif self.movement_x < 0:
                    self.movement_x = -8
            
            # ruch w poziomie
            self.rect.x += self.movement_x

            colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms | self.level.spikes, False)

            for p in colliding_platforms:
                if hasattr(p, 'down') and p.down:
                    self.die = True
                    p.down = False
                else:
                    if self.movement_x < 0:
                        self.rect.left = p.rect.right
                    if self.movement_x > 0:
                        self.rect.right = p.rect.left

            # animacja poziomo
            if self.movement_x > 0:
                if self.speed:
                    self._run(self.image_run_R)
                else:
                    self._move(self.image_walk_R)
            if self.movement_x < 0:
                if self.speed:
                    self._run(self.image_run_L)
                else:
                    self._move(self.image_walk_L)


            # ruch w pionie
            self.rect.y += self.movement_y

            colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms | self.level.spikes, False)

            for p in colliding_platforms:
                if hasattr(p, 'down') and p.down:
                    self.die = True
                    p.down = False
                else:
                    if hasattr(p, 'move') and p.move == 2 and self.movement_x == 0:
                        self.rect.x += p.movement_x
                    if hasattr(p, 'move') and p.move == 3:
                        p.fall = True
                    if self.movement_y > 0:
                        self.rect.bottom = p.rect.top
                    if self.movement_y < 0:
                        self.rect.top = p.rect.bottom
                    
                self.movement_y = 0

            # animacja pionowo
            if self.movement_y != 0:
                if self.direction_of_movement == 'right':
                    self._jumping(self.image_jump_R)
                else:
                    self._jumping(self.image_jump_L)

            # stan bezczynności
            if self.movement_x == 0 and self.movement_y == 0:
                if self.direction_of_movement == 'right':
                    self._stand(self.image_idle_R)
                else:
                    self._stand(self.image_idle_L)
            else:
                self.count_t = 0

            # obiekty specjalne kolizja
            colliding_platforms = pygame.sprite.spritecollide(self, self.level.special_objects, False)

            for p in colliding_platforms:
                if not isinstance(p.image_list, list):
                    if p.image_list == image_check and not self.save_position:
                        effect = pygame.mixer.Sound("music/checkpoint.wav")
                        effect.play()
                        
                        self.save_crystal = self.crystal
                        self.save_position = [p.rect.x, p.rect.y, p.start_x, p.start_y]

                        for c in self.level.crystals:
                            if c.collected:
                                self.level.cr[self.level.cr.index([c.level, c.start_x, c.start_y, True])] = [c.level, c.start_x, c.start_y, False]
                        
                    elif p.image_list == image_finish and not self.end_level:
                        self.music.pause()
                        effect = pygame.mixer.Sound("music/finish.wav")
                        effect.play()
                        
                        self.end_level = True
                        self._save_result(datetime.datetime.now())

            # rzucanie
            if self.throwing:
                if self.direction_of_movement == 'right':
                    self._throwing(self.image_throw_R)
                else:
                    self._throwing(self.image_throw_L)

            # spadanie kolcy
            for s in self.level.spikes:
                if s.rect.x + 185 >= self.rect.x >= s.rect.x and self.rect.y > s.rect.y + 35:
                    if not s.down:
                        s.down = True
                        
                colliding_platform = pygame.sprite.spritecollide(s, self.level.set_of_platforms, False)

                for x in colliding_platform:
                    if s.down:
                        s.rect.y = x.rect.y - s.rect.h
                        s.down = False
                        s.change = True

            # zebranie diamentu
            colliding_crystal = pygame.sprite.spritecollide(self, self.level.crystals, False)

            for c in colliding_crystal:
                if not c.collected:
                    effect = pygame.mixer.Sound("music/coin.wav")
                    effect.play()
                    
                    self.crystal += 1
                    c.collected = True

            # śmierć poza ekranem
            if self.draw_player and self.rect.y > self.screen_height:
                self.die = True
                self.count_d = 12
                self.music.pause()
                effect = pygame.mixer.Sound("music/game_over.wav")
                effect.play()

            # śmierć po kontakcie z przeciwnikiem
            colliding_platforms = pygame.sprite.spritecollide(self, self.level.opponents, False)

            for p in colliding_platforms:
                self.music.pause()
                effect = pygame.mixer.Sound("music/game_over.wav")
                effect.play()
                
                if self.rect.x < p.rect.x:
                    p.turn = False
                else:
                    p.turn = True
                
                p.attack = True
                self.opponent_attack = p
            
            # śmierć od broni przeciwnika
            if pygame.sprite.spritecollide(self, self.level.opponents_weapon, False):
                self.die = True
                self.music.pause()
                effect = pygame.mixer.Sound("music/game_over.wav")
                effect.play()

        else:
            self.opponent_attack.update()

    # działania związane z zakończeniem rundy
    def _save_result(self, end_time):
        finish_time = (end_time - self.level.time).seconds + self.level.save_time
        finish_sec = finish_time % 60
        finish_min = int((finish_time - finish_sec) / 60)

        if finish_sec < 10:
            finish_time = str(finish_min) + ":0" + str(finish_sec)
        else:
            finish_time = str(finish_min) + ":" + str(finish_sec)

        if finish_min < 3 and self.crystal == self.level.max_crystal:
            finish_stars = str(3)
        elif finish_min < 5 and self.crystal + 2 >= self.level.max_crystal:
            finish_stars = str(2)
        else:
            finish_stars = str(1)
        
        try:
            file = open(hi_scores_data, 'r')
            list_line = [line.rstrip( "\n" ) for line in file]
            file.close()
        except:
            list_line = []

        change = False
        for x in range(0, len(list_line), 4):
            if list_line[x] == self.level.name:
                crystal, max_crystal = list_line[x+2].split('/')
                hi_min, hi_sec = list_line[x+3].split(':')
                if self.crystal > int(crystal):
                    change = True
                    list_line[x+1] = finish_stars    
                    list_line[x+2] = str(self.crystal) + "/" + str(self.level.max_crystal)
                    list_line[x+3] = finish_time                
                        
                elif self.crystal == int(crystal) and int(hi_min) == 0 and int(hi_sec) == 0 or int(hi_min) > finish_min or int(hi_min) == finish_min and int(hi_sec) > finish_sec:
                    change = True
                    list_line[x+1] = finish_stars
                    list_line[x+3] = finish_time  
                        
        if change:
            with open(hi_scores_data, 'w') as file:
                for x in range(len(list_line)):
                    file.write(list_line[x]+'\n')

        self.end_level = False
        
        current_level = Level_complete(self, image_level_complete, self.level, 'Level_complete', finish_stars, finish_time, self.crystal)
        self.level = current_level

    def _dieing(self, image_list):
        if self.count_d < 2:
            self.image = image_list[0]
        elif self.count_d < 4:
            self.image = image_list[1]
        elif self.count_d < 6:
            self.image = image_list[2]
        elif self.count_d < 8:
            self.image = image_list[3]
        elif self.count_d < 10:
            self.image = image_list[4]
        elif self.count_d < 12:
            self.image = image_list[5]
        elif self.count_d < 30:
            self.live -= 1
            if self.live > 0:
                screen.blit(pygame.transform.scale(image_lost_life,(self.screen_width, self.screen_height)),(0,0))
                self.level.world_shift_x = 0
                self.level.world_shift_y = 0
                self.level.set_of_platforms = set()
                self.level.special_objects = set()
                self.level.static_objects = set()
                self.level.opponents = set()
                self.level.opponents_weapon = set()
                self.level.spikes = set()
                self.level.crystals = set()
                self.movement_x = 0
                self.movement_y = 0
                if self.save_position:
                    self.level.load()
                    self.rect.x = self.save_position[0]
                    self.rect.y = self.save_position[1]
                    self.level._shift_world_x(self.save_position[0] - self.save_position[2])
                    self.level._shift_world_y(self.save_position[1] - self.save_position[3])
                    self.crystal = self.save_crystal
                else:
                    for s in self.level.sp:
                        s[2] = s[3]
                    for c in self.level.cr:
                        c[3] = True
                    self.level.rm = []
                    self.level.load()
                    self.rect.center = self.level.position
                    self.crystal = 0
                self.level.change_time = True
                self.level.save_time += (datetime.datetime.now() - self.level.time).seconds
                pygame.display.flip()
                pygame.time.delay(3000)
                self.level.time = datetime.datetime.now()
                self.music.play(-1, 0.0)
            else:
                current_level = Game_over(self, image_game_over, self.level, 'Game_over')
                self.level = current_level
            self.die = False
            self.count_d = 0
            self.list_bullet = set()

        if self.count_d == 8:
            self.rect.y += 30

        if self.count_d == 10:
            self.rect.y +=  70
     
        self.count_d += 0.5

    def _throwing(self, image_list):
        if self.count_b < 3:
            self.image = image_list[0]
        elif self.count_b < 6:
            self.image = image_list[1]
        elif self.count_b < 9:
            self.image = image_list[2]

        if self.count_b == 6:
            self.list_bullet.add(Bullet(self))

        if self.count_b == 9:
            self.count_b = 0
            self.throwing = False
        else:
            self.count_b += 1

    def _run(self, image_list):
        if self.count_r < 3:
            self.image = image_list[0]
        elif self.count_r < 6:
            self.image = image_list[1]
        elif self.count_r < 9:
            self.image = image_list[2]
        elif self.count_r < 12:
            self.image = image_list[3]
        elif self.count_r < 15:
            self.image = image_list[4]
        elif self.count_r < 18:
            self.image = image_list[5]

        if self.count_r >= 18:
            self.count_r = 0
        else:
            self.count_r += 1

    def _stand(self, image_list):
        if self.count_t < 5:
            self.image = image_list[0]
        elif self.count_t < 10:
            self.image = image_list[1]
        elif self.count_t < 15:
            self.image = image_list[2]
        elif self.count_t < 20:
            self.image = image_list[3]

        if self.count_t >= 20:
            self.count_t = 0
        else:
            self.count_t += 1

    def _move(self, image_list):
        if self.count_m < 3:
            self.image = image_list[0]
        elif self.count_m < 6:
            self.image = image_list[1]
        elif self.count_m < 9:
            self.image = image_list[2]
        elif self.count_m < 12:
            self.image = image_list[3]
        elif self.count_m < 15:
            self.image = image_list[4]
        elif self.count_m < 18:
            self.image = image_list[5]

        if self.count_m >= 18:
            self.count_m = 0
        else:
            self.count_m += 1

    def _jumping(self, image_list):
        if self.movement_y < -11:
            self.image = image_list[0]
        elif self.movement_y < -10:
            self.image = image_list[1]
        elif self.movement_y < 0:
            self.image = image_list[2]
        elif self.movement_y < 10:
            self.image = image_list[3]
        elif self.movement_y < 11:
            self.image = image_list[4]
        else:
            self.image = image_list[5]

    # ładowanie grafik postaci
    def load_hero(self, hero):
        self.hero = hero
        faint_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_L/1.png'))
        faint_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_L/2.png'))
        faint_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_L/3.png'))
        faint_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_L/4.png'))
        hurt_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Hurt_L/1.png'))
        hurt_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Hurt_L/2.png'))
        faint_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_R/1.png'))
        faint_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_R/2.png'))
        faint_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_R/3.png'))
        faint_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Faint_R/4.png'))
        hurt_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Hurt_R/1.png'))
        hurt_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Hurt_R/2.png'))
        idle_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_L/1.png'))
        idle_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_L/2.png'))
        idle_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_L/3.png'))
        idle_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_L/4.png'))
        idle_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_R/1.png'))
        idle_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_R/2.png'))
        idle_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_R/3.png'))
        idle_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Idle_R/4.png'))
        jump_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_L/1.png'))
        jump_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_L/2.png'))
        jump_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_L/3.png'))
        jump_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_L/4.png'))
        jump_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_L/5.png'))
        jump_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_L/6.png'))
        jump_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_R/1.png'))
        jump_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_R/2.png'))
        jump_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_R/3.png'))
        jump_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_R/4.png'))
        jump_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_R/5.png'))
        jump_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Jump_R/6.png'))
        run_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_L/1.png'))
        run_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_L/2.png'))
        run_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_L/3.png'))
        run_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_L/4.png'))
        run_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_L/5.png'))
        run_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_L/6.png'))
        run_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_R/1.png'))
        run_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_R/2.png'))
        run_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_R/3.png'))
        run_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_R/4.png'))
        run_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_R/5.png'))
        run_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Run_R/6.png'))
        throw_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Throw_L/1.png'))
        throw_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Throw_L/2.png'))
        throw_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Throw_L/3.png'))
        throw_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Throw_R/1.png'))
        throw_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Throw_R/2.png'))
        throw_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Throw_R/3.png'))
        walk_1_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_L/1.png'))
        walk_2_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_L/2.png'))
        walk_3_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_L/3.png'))
        walk_4_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_L/4.png'))
        walk_5_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_L/5.png'))
        walk_6_L = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_L/6.png'))
        walk_1_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_R/1.png'))
        walk_2_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_R/2.png'))
        walk_3_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_R/3.png'))
        walk_4_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_R/4.png'))
        walk_5_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_R/5.png'))
        walk_6_R = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Walk_R/6.png'))
        bullet_1 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/1.png'))
        bullet_2 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/2.png'))
        bullet_3 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/3.png'))
        bullet_4 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/4.png'))
        bullet_5 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/5.png'))
        bullet_6 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/6.png'))
        bullet_7 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/7.png'))
        bullet_8 = pygame.image.load(os.path.join(katalog_z_obrazami,'Hero',hero,'Bullet/8.png'))

        self.image_die_L = [hurt_1_L, hurt_2_L, faint_1_L, faint_2_L, faint_3_L, faint_4_L]
        self.image_die_R = [hurt_1_R, hurt_2_R, faint_1_R, faint_2_R, faint_3_R, faint_4_R]
        self.image_idle_L = [idle_1_L, idle_2_L, idle_3_L, idle_4_L]
        self.image_idle_R = [idle_1_R, idle_2_R, idle_3_R, idle_4_R]
        self.image_jump_L = [jump_1_L, jump_2_L, jump_3_L, jump_4_L, jump_5_L, jump_6_L]
        self.image_jump_R = [jump_1_R, jump_2_R, jump_3_R, jump_4_R, jump_5_R, jump_6_R]
        self.image_run_L = [run_1_L, run_2_L, run_3_L, run_4_L, run_5_L, run_6_L]
        self.image_run_R = [run_1_R, run_2_R, run_3_R, run_4_R, run_5_R, run_6_R]
        self.image_throw_L = [throw_1_L, throw_2_L, throw_3_L]
        self.image_throw_R = [throw_1_R, throw_2_R, throw_3_R]
        self.image_walk_L = [walk_1_L, walk_2_L, walk_3_L, walk_4_L, walk_5_L, walk_6_L]
        self.image_walk_R = [walk_1_R, walk_2_R, walk_3_R, walk_4_R, walk_5_R, walk_6_R]
        self.image_bullet = [bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6, bullet_7, bullet_8]

        self.image = self.image_idle_R[0]
