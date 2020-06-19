import pygame, os, datetime, sys
from data import image_stars, image_lock, screen, image_lock_play, hi_scores_data, image_play, image_profile, image_exit, image_accept, image_back, image_resume, image_home, image_restart, image_help, image_records, image_left, image_right, image_next_level, image_level_1, image_level_2, image_level_3, image_level_4, image_level_5
from button import Button
from base_level import Level

# klasa wyboru postaci gracza
class Select_your_hero(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.button_hero_1 = Button(player, 'Hero_1', image_accept, self.player.screen_width*0.288, self.player.screen_height*0.272, self.player.screen_height, self.player.screen_height, 12, 12)
        self.button_hero_2 = Button(player, 'Hero_2', image_accept, self.player.screen_width*0.48, self.player.screen_height*0.272, self.player.screen_height, self.player.screen_height, 12, 12)
        self.button_hero_3 = Button(player, 'Hero_3', image_accept, self.player.screen_width*0.668, self.player.screen_height*0.272, self.player.screen_height, self.player.screen_height, 12, 12)
        self.button_hero_back = Button(player, 'Hero_back', image_back, self.player.screen_width*0.46, self.player.screen_height*5.55//7, self.player.screen_height, self.player.screen_height, 6, 6)
        self.info = False

    def get_events(self, event):
        self.button_hero_1.get_events(event)
        self.button_hero_2.get_events(event)
        self.button_hero_3.get_events(event)
        self.button_hero_back.get_events(event)

    def draw(self, surface):
        self.button_hero_1.draw(surface)
        self.button_hero_2.draw(surface)
        self.button_hero_3.draw(surface)
        self.button_hero_back.draw(surface)

    def update(self):    
        self.button_hero_1.update()
        self.button_hero_2.update()
        self.button_hero_3.update()
        self.button_hero_back.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_hero_1.resize(w*0.288, h*0.272, h, h)
        self.button_hero_2.resize(w*0.48, h*0.272, h, h)
        self.button_hero_3.resize(w*0.668, h*0.272, h, h)
        self.button_hero_back.resize(w*0.46, h*5.55//7, h, h)

# klasa informacji o sterowaniu
class Help(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.button_back = Button(player, 'Back', image_back, self.player.screen_width*0.46, self.player.screen_height*5.55//7, self.player.screen_height, self.player.screen_height, 6, 6)
        self.info = False

    def get_events(self, event):
        self.button_back.get_events(event)

    def draw(self, surface):
        self.button_back.draw(surface)

    def update(self):    
        self.button_back.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_back.resize(w*0.46, h*5.55//7, h, h)

# klasa menu start
class Start_menu(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.button_play = Button(player, 'Play', image_play, self.player.screen_width*0.09, self.player.screen_height*5.1//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.button_records = Button(player, 'Records', image_records, self.player.screen_width*0.26, self.player.screen_height*5.1//7, self.player.screen_height, self.player.screen_height, 4, 4)  
        self.button_profile = Button(player, 'Profile', image_profile, self.player.screen_width*0.43, self.player.screen_height*5.1//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.button_help = Button(player, 'Help', image_help, self.player.screen_width*0.6, self.player.screen_height*5.1//7, self.player.screen_height, self.player.screen_height, 4, 4)  
        self.button_exit = Button(player, 'Exit', image_exit, self.player.screen_width*0.77, self.player.screen_height*5.1//7, self.player.screen_height, self.player.screen_height, 4, 4)     
        self.info = False

    def get_events(self, event):
        self.button_play.get_events(event)
        self.button_profile.get_events(event)
        self.button_exit.get_events(event)
        self.button_records.get_events(event)
        self.button_help.get_events(event)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.player.screen_width, self.player.screen_height)),(0,0))
        self.button_play.draw(surface)
        self.button_profile.draw(surface)
        self.button_exit.draw(surface)
        self.button_records.draw(surface)
        self.button_help.draw(surface)

    def update(self):
        self.button_play.update()
        self.button_profile.update()
        self.button_exit.update()
        self.button_records.update()
        self.button_help.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_play.resize(w*0.09, h*5.1//7, h, h)
        self.button_profile.resize(w*0.43, h*5.1//7, h, h)
        self.button_exit.resize(w*0.77, h*5.1//7, h, h)
        self.button_records.resize(w*0.26, h*5.1//7, h, h)
        self.button_help.resize(w*0.6, h*5.1//7, h, h)

# klasa wyboru rundy
class Select_level(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.button_back = Button(player, 'Back', image_back, self.player.screen_width*0.448, self.player.screen_height*5.2//7, self.player.screen_height, self.player.screen_height, 5, 5)
        self.button_level_1 = Button(player, 'Level_1', image_level_1, self.player.screen_width*0.22, self.player.screen_height*0.4, self.player.screen_height, self.player.screen_height, 6, 6)
        self._read_stars()

        if self.list_line[0*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.34, self.player.screen_height*0.4))
        else:
            self.button_level_2 = Button(player, 'Level_2', image_level_2, self.player.screen_width*0.34, self.player.screen_height*0.4, self.player.screen_height, self.player.screen_height, 6, 6)

        if self.list_line[1*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.46, self.player.screen_height*0.4))
        else:
            self.button_level_3 = Button(player, 'Level_3', image_level_3, self.player.screen_width*0.46, self.player.screen_height*0.4, self.player.screen_height, self.player.screen_height, 6, 6)

        if self.list_line[2*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.58, self.player.screen_height*0.4))
        else:
            self.button_level_4 = Button(player, 'Level_4', image_level_4, self.player.screen_width*0.58, self.player.screen_height*0.4, self.player.screen_height, self.player.screen_height, 6, 6)

        if self.list_line[3*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.70, self.player.screen_height*0.4))
        else:
            self.button_level_5 = Button(player, 'Level_5', image_level_5, self.player.screen_width*0.70, self.player.screen_height*0.4, self.player.screen_height, self.player.screen_height, 6, 6)

        self.info = False

    def get_events(self, event):
        self.button_back.get_events(event)
        self.button_level_1.get_events(event)
        
        if self.list_line[0*4+3] != '0:00':
            self.button_level_2.get_events(event)

        if self.list_line[1*4+3] != '0:00':
            self.button_level_3.get_events(event)

        if self.list_line[2*4+3] != '0:00':
            self.button_level_4.get_events(event)

        if self.list_line[3*4+3] != '0:00':
            self.button_level_5.get_events(event)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.player.screen_width, self.player.screen_height)),(0,0))
        self.button_back.draw(surface)
        self.button_level_1.draw(surface)
        surface.blit(pygame.transform.scale(image_stars[int(self.list_line[0*4+1])],(int(self.player.screen_height/6), int(self.player.screen_height/10))),(self.player.screen_width*0.22, self.player.screen_height*0.52))
        
        if self.list_line[0*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.34, self.player.screen_height*0.4))
        else:
            self.button_level_2.draw(surface)
            surface.blit(pygame.transform.scale(image_stars[int(self.list_line[1*4+1])],(int(self.player.screen_height/6), int(self.player.screen_height/10))),(self.player.screen_width*0.34, self.player.screen_height*0.52))

        if self.list_line[1*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.46, self.player.screen_height*0.4))
        else:
            self.button_level_3.draw(surface)
            surface.blit(pygame.transform.scale(image_stars[int(self.list_line[2*4+1])],(int(self.player.screen_height/6), int(self.player.screen_height/10))),(self.player.screen_width*0.46, self.player.screen_height*0.52))

        if self.list_line[2*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.58, self.player.screen_height*0.4))
        else:
            self.button_level_4.draw(surface)
            surface.blit(pygame.transform.scale(image_stars[int(self.list_line[3*4+1])],(int(self.player.screen_height/6), int(self.player.screen_height/10))),(self.player.screen_width*0.58, self.player.screen_height*0.52))

        if self.list_line[3*4+3] == '0:00':
            screen.blit(pygame.transform.scale(image_lock, (self.player.screen_height//6, self.player.screen_height//6)),(self.player.screen_width*0.70, self.player.screen_height*0.4))
        else:
            self.button_level_5.draw(surface)
            surface.blit(pygame.transform.scale(image_stars[int(self.list_line[4*4+1])],(int(self.player.screen_height/6), int(self.player.screen_height/10))),(self.player.screen_width*0.70, self.player.screen_height*0.52))

    def update(self):
        self.button_back.update()
        self.button_level_1.update()

        if self.list_line[0*4+3] != '0:00':
            self.button_level_2.update()

        if self.list_line[1*4+3] != '0:00':
            self.button_level_3.update()

        if self.list_line[2*4+3] != '0:00':
            self.button_level_4.update()

        if self.list_line[3*4+3] != '0:00':
            self.button_level_5.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_back.resize(w*0.44, h*4.96//7, h, h)
        self.button_level_1.resize(w*0.22, h*0.4, h, h)

        if self.list_line[0*4+3] != '0:00':
            self.button_level_2.resize(w*0.34, h*0.4, h, h)

        if self.list_line[1*4+3] != '0:00':
            self.button_level_3.resize(w*0.46, h*0.4, h, h)

        if self.list_line[2*4+3] != '0:00':
            self.button_level_4.resize(w*0.58, h*0.4, h, h)

        if self.list_line[3*4+3] != '0:00':
            self.button_level_5.resize(w*0.70, h*0.4, h, h)

    def _read_stars(self):
        try:
            plik = open(hi_scores_data, 'r')
            self.list_line = [line.rstrip( "\n" ) for line in plik]
            plik.close()
        except:
            self.list_line = []

# klasa menu zatrzymania trwania rundy
class Pause_menu(Level):
    def __init__(self, player, background_image, current_level, name):
        super().__init__(player, background_image, name)
        self.current_level = current_level
        self.player.draw_player = False
        self.rect = self.player.rect
        self.button_resume = Button(player, 'Resume', image_resume, self.player.screen_width*0.264, self.player.screen_height*2.7//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.button_home = Button(player, 'Home', image_home, self.player.screen_width*0.43, self.player.screen_height*2.7//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.button_restart = Button(player, 'Restart', image_restart, self.player.screen_width*0.6, self.player.screen_height*2.7//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.info = False
        self.player.music.pause()

    def get_events(self, event):
        self.button_resume.get_events(event)
        self.button_home.get_events(event)
        self.button_restart.get_events(event)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.player.screen_width, self.player.screen_height)),(0,0))
        self.button_resume.draw(surface)
        self.button_home.draw(surface)
        self.button_restart.draw(surface)

    def update(self):
        self.button_resume.update()
        self.button_home.update()
        self.button_restart.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_resume.resize(w*0.264, h*2.7//7, h, h)
        self.button_home.resize(w*0.43, h*2.7//7, h, h)
        self.button_restart.resize(w*0.6, h*2.7//7, h, h)

# klasa porażki w rundzie
class Game_over(Level):
    def __init__(self, player, background_image, current_level, name):
        super().__init__(player, background_image, name)
        self.current_level = current_level
        self.player.draw_player = False
        self.rect = self.player.rect
        self.button_home = Button(player, 'Home', image_home, self.player.screen_width*0.35, self.player.screen_height*2.7//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.button_restart = Button(player, 'Restart', image_restart, self.player.screen_width*0.52, self.player.screen_height*2.7//7, self.player.screen_height, self.player.screen_height, 4, 4)
        self.info = False

    def get_events(self, event):
        self.button_home.get_events(event)
        self.button_restart.get_events(event)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.player.screen_width, self.player.screen_height)),(0,0))
        self.button_home.draw(surface)
        self.button_restart.draw(surface)

    def update(self):
        self.button_home.update()
        self.button_restart.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_home.resize(w*0.35, h*3.5//7, h, h)
        self.button_restart.resize(w*0.52, h*3.5//7, h, h)

# klasa najlepszych wyników
class Hi_scores(Level):
    def __init__(self, player, background_image, name):
        super().__init__(player, background_image, name)
        self.button_back = Button(player, 'Hero_back', image_back, self.player.screen_width*0.46, self.player.screen_height*5.3//7, self.player.screen_height, self.player.screen_height, 7, 7)
        self.button_left = Button(player, 'Left', image_left, self.player.screen_width*0.36, self.player.screen_height*5.3//7, self.player.screen_height, self.player.screen_height, 7, 7)
        self.button_right = Button(player, 'Right', image_right, self.player.screen_width*0.56, self.player.screen_height*5.3//7, self.player.screen_height, self.player.screen_height, 7, 7)
        self.info = False
        self.nr_list = 0
        self._read_data()

    def get_events(self, event):
        self.button_back.get_events(event)
        self.button_left.get_events(event)
        self.button_right.get_events(event)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.image_w, self.image_h)),(0,0))
        
        if len(self.list_line) > self.nr_list + 3:
            surface.blit(pygame.font.SysFont(None, 100).render(self.list_line[self.nr_list], True, (0,121,177)), [self.player.screen_width*0.42, self.player.screen_height*0.39])
            surface.blit(pygame.font.SysFont(None, 100).render(self.list_line[self.nr_list + 2], True, (0,121,177)), [self.player.screen_width*0.36, self.player.screen_height*0.55])
            surface.blit(pygame.font.SysFont(None, 100).render(self.list_line[self.nr_list + 3], True, (0,121,177)), [self.player.screen_width*0.63, self.player.screen_height*0.55])
        
        self.button_back.draw(surface)

        if self.nr_list > 0:
            self.button_left.draw(surface)

        if len(self.list_line) > self.nr_list + 4:
            self.button_right.draw(surface)

    def update(self):    
        self.button_back.update()
        self.button_left.update()
        self.button_right.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_back.resize(w*0.46, h*5.53//7, h, h)
        self.button_left.resize(w*0.36, h*5.3//7, h, h)
        self.button_right.resize(w*0.56, h*5.3//7, h, h)

    def _read_data(self):
        try:
            plik = open(hi_scores_data, 'r')
            self.list_line = [line.rstrip( "\n" ) for line in plik]
            plik.close()
        except:
            self.list_line = []
            print('no')

# klasa zakończenia rundy
class Level_complete(Level):
    def __init__(self, player, background_image, current_level, name, stars, time, crystals):
        super().__init__(player, background_image, name)
        self.current_level = current_level
        self.stars = int(stars)
        self.time = time
        self.diamond = crystals
        self.player.draw_player = False
        self.rect = self.player.rect
        self.button_home = Button(player, 'Home', image_home, self.player.screen_width*0.315, self.player.screen_height*5.13//7, self.player.screen_height, self.player.screen_height, 5, 5)
        self.button_restart = Button(player, 'Restart', image_restart, self.player.screen_width*0.448, self.player.screen_height*5.13//7, self.player.screen_height, self.player.screen_height, 5, 5)

        if self.current_level.name != 'Level 5':
            self.button_next_level = Button(player, 'Next_level', image_next_level, self.player.screen_width*0.585, self.player.screen_height*5.13//7, self.player.screen_height, self.player.screen_height, 5, 5)

        self.info = False

    def get_events(self, event):
        self.button_home.get_events(event)
        self.button_restart.get_events(event)

        if self.current_level.name != 'Level 5':
            self.button_next_level.get_events(event)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_image,(self.player.screen_width, self.player.screen_height)),(0,0))
        self.button_home.draw(surface)
        self.button_restart.draw(surface)

        if self.current_level.name != 'Level 5':
            self.button_next_level.draw(surface)
        else:
            surface.blit(pygame.transform.scale(image_lock_play, (self.player.screen_height//5, self.player.screen_height//5)),(self.player.screen_width*0.585, self.player.screen_height*0.733))

        surface.blit(pygame.transform.scale(image_stars[self.stars],(int(self.player.screen_height/2), int(self.player.screen_height/7))),(self.player.screen_width*0.37, self.player.screen_height*0.31))
        surface.blit(pygame.font.SysFont(None, 55).render(str(self.diamond) + "/" + str(self.current_level.max_crystal), True, (0,121,177)), [self.player.screen_width*0.54, self.player.screen_height*0.56])
        surface.blit(pygame.font.SysFont(None, 55).render(self.time, True, (0,121,177)), [self.player.screen_width*0.53, self.player.screen_height*0.48])

    def update(self):
        self.button_home.update()
        self.button_restart.update()

        if self.current_level.name != 'Level 5':
            self.button_next_level.update()

    def resize(self, surface, w, h):
        super().resize(surface, w, h)
        self.button_home.resize(w*0.315, h*5.13//7, h, h)
        self.button_restart.resize(w*0.448, h*5.13//7, h, h)

        if self.current_level.name != 'Level 5':
            self.button_next_level.resize(w*0.585, h*5.13//7, h, h)
        else:
            surface.blit(pygame.transform.scale(image_lock_play, (h//5, h//5)),(w*0.585, h*0.733))
