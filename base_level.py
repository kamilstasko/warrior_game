import pygame, os, datetime, sys
from data import screen, image_info_health, image_info_crystal, image_info_time, wielkosc_bloku, image_ground
from opponent import Opponent
from objects import Platform, Static_object, Spike, Crystal

# klasa rund
class Level:
    def __init__(self, player, background_image, name):
        self.name = name
        self.set_of_platforms = set()
        self.special_objects = set()
        self.static_objects = set()
        self.opponents = set()
        self.opponents_weapon = set()
        self.spikes = set()
        self.crystals = set()
        self.player = player
        self.player.reset_data()
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.background_image = background_image
        self.image_w = self.player.screen_width
        self.image_h = self.player.screen_height
        self.info = False
        self.time = datetime.datetime.now()
        self.save_time = 0
        self.change_time = False
        self.max_crystal = 0
        screen.blit(pygame.transform.scale(self.background_image,(self.image_w, self.image_h)),(0,0))
        self.remove_opponent = []
        self.wp = []
        self.so = []
        self.op = []
        self.rm = []
        self.sp = []
        self.cr = []

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.image_w, self.image_h)),(0,0))
        
        for o in self.static_objects:
            o.draw(surface)
        
        for p in self.set_of_platforms:
            p.draw(surface)

        for s in self.special_objects:
            s.draw(surface)

        for x in self.opponents:
            x.draw(surface)

        for s in self.spikes:
            s.draw(surface)

        for c in self.crystals:
            c.draw(surface)

        for w in self.opponents_weapon:
            w.draw(surface)

        if self.info:
            if self.save_time and self.change_time:
                time_now = (datetime.datetime.now() - self.time).seconds + self.save_time
            else:
                time_now = (datetime.datetime.now() - self.time).seconds
            time_sec = time_now % 60
            time_min = int((time_now - time_sec) / 60)
            if time_sec < 10:
                time = str(time_min) + ':0' + str(time_sec)
            else:
                time = str(time_min) + ':' + str(time_sec)

            surface.blit(pygame.transform.scale(image_info_health,(140, 70)),(10,10))
            surface.blit(pygame.transform.scale(image_info_crystal,(180, 70)),(160,10))
            surface.blit(pygame.transform.scale(image_info_time,(210, 70)),(350,10))
            surface.blit(pygame.font.SysFont(None, 70).render(str(self.player.live), True, (0,121,177)), [95, 25])
            surface.blit(pygame.font.SysFont(None, 70).render(str(self.player.crystal) + "/" + str(self.max_crystal), True, (0,121,177)), [245, 25])
            surface.blit(pygame.font.SysFont(None, 70).render(time, True, (0,121,177)), [440, 25])

    def update(self):
        if not self.player.die and not self.player.opponent_attack:
            for x in self.remove_opponent:
                if x in self.opponents:
                    self.opponents.remove(x)
            
            # sprawdzamy czy gracz zblizyl sie do prawej krawedzi ekranu
            if self.player.rect.right >= self.player.screen_width - self.player.screen_width//2:
                diff = self.player.rect.right - (self.player.screen_width - self.player.screen_width//2)
                self.player.rect.right = (self.player.screen_width - self.player.screen_width//2)
                self._shift_world_x(-diff)
                
            # sprawdzamy czy gracz zblizyl sie do lewej krawedzi ekranu
            if self.world_shift_x < 0 and self.player.rect.left <= self.player.screen_width//4:
                diff = self.player.screen_width//4 - self.player.rect.left
                self.player.rect.left = self.player.screen_width//4
                self._shift_world_x(diff)
            elif self.world_shift_x > 0 and self.player.rect.left <= self.player.screen_width//4:
                diff = -self.world_shift_x
                self._shift_world_x(diff)

            # sprawdzamy czy gracz zblizyl sie do gornej krawedzi ekranu
            if self.player.rect.top <= self.player.screen_height//4:
                diff = self.player.screen_height//4 - self.player.rect.top
                self.player.rect.top = self.player.screen_height//4
                self._shift_world_y(diff)

            # sprawdzamy czy gracz zblizyl sie do dolnej krawedzi ekranu
            if self.world_shift_y > 0 and self.player.rect.bottom >= self.player.screen_height - self.player.screen_height//2:
                diff = self.player.rect.bottom - (self.player.screen_height - self.player.screen_height//2)
                self.player.rect.bottom = (self.player.screen_height - self.player.screen_height//2)
                self._shift_world_y(-diff)
            elif self.world_shift_y < 0:
                diff = -self.world_shift_y
                self._shift_world_y(diff, True)

            for p in self.set_of_platforms:
                p.update()

            for x in self.opponents:
                x.update()

            for s in self.spikes:
                s.update()

            for c in self.crystals:
                c.update()

            # kolizja i update broni przeciwnika
            remove = []
            for w in self.opponents_weapon:
                if w.rect.x < self.player.screen_width and w.rect.x > 0 and w.rect.y + 35 < self.player.screen_height and w.rect.y > 0:
                    w.update()

                    if pygame.sprite.spritecollide(w, self.set_of_platforms, False) or pygame.sprite.spritecollide(w, self.opponents, False):
                        w.opponent.weapon = False
                        remove.append(w)
                    
                else:
                    w.opponent.weapon = False
                    remove.append(w)    

            for x in range(len(remove)):
                if remove[x] in self.opponents_weapon:
                    self.opponents_weapon.remove(remove[x])

    def _shift_world_x(self, diff):
        self.world_shift_x += diff

        for p in self.set_of_platforms:
            p.rect.x += diff

        for s in self.special_objects:
            s.rect.x += diff

        for o in self.static_objects:
            o.rect.x += diff

        for x in self.opponents:
            x.rect.x += diff
            x.platform_beg += diff
            x.platform_end += diff

        for s in self.spikes:
            s.rect.x += diff

        for c in self.crystals:
            c.rect.x += diff

        for w in self.opponents_weapon:
            w.rect.x += diff

    def _shift_world_y(self, diff, drive = False):
        self.world_shift_y += diff
        self.image_h += diff
        
        for p in self.set_of_platforms:
            p.rect.y += diff
            if p.move == 1 and drive:
                p.rect.y -= diff

        for s in self.special_objects:
            s.rect.y += diff

        for o in self.static_objects:
            o.rect.y += diff

        for x in self.opponents:
            x.rect.y += diff

        for s in self.spikes:
            s.rect.y += diff

        for c in self.crystals:
            c.rect.y += diff

        for w in self.opponents_weapon:
            w.rect.y += diff

        for b in self.player.list_bullet:
            b.rect.y += diff

    def get_events(self, event):
        pass

    def resize(self, surface, w, h):
        surface.blit(pygame.transform.scale(self.background_image, (w, h)),(0,0))

    def load(self):
        for x in range(0, 2800, 70):
            platform = Platform(self.player, wielkosc_bloku, wielkosc_bloku, -wielkosc_bloku, self.player.screen_height - wielkosc_bloku - x, image_ground, 0,   0 * wielkosc_bloku)
            self.set_of_platforms.add(platform) 

        for p in self.wp:
            platform = Platform(self.player, *p)
            self.set_of_platforms.add(platform)

        tmp = 0
        for y in self.op:
            try:
                opponent = Opponent(y[0], self.rm[tmp][1], y[2], y[3], self.rm[tmp][0])
            except:
                self.rm.append([False, False])
                opponent = Opponent(*y)
            finally:
                tmp += 1
                self.opponents.add(opponent)

        for o in self.so:
            static_object = Static_object(*o)
            self.static_objects.add(static_object)

        for s in self.sp:
            spike = Spike(s[0], s[1], s[2])
            self.spikes.add(spike)

        for c in self.cr:
            if c[3]:
                crystal = Crystal(*c)
                self.crystals.add(crystal)
