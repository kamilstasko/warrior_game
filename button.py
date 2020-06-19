import pygame, os, datetime, sys
from data import image_help_info, image_start, image_select_hero, image_select_level, image_background_level, image_hi_scores, image_lost_life

# klasa przycisku
class Button(pygame.sprite.Sprite):
    def __init__(self, player, action, image_list, rect_x, rect_y, scale_x, scale_y, size_x, size_y):
        super().__init__()
        self.player = player
        self.image_list = image_list
        self.image = image_list[0]
        self.size_x = size_x
        self.size_y = size_y
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.rect = pygame.transform.scale(self.image,(self.scale_x//self.size_x, self.scale_y//self.size_y)).get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.action = action
        self.text = False

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.image,(self.scale_x//self.size_x, self.scale_y//self.size_y)),(self.rect.x,self.rect.y))
        if self.text:
            surface.blit(pygame.transform.scale(self.text,(self.scale_x//self.size_x, self.scale_y//20)),(self.rect.x,self.rect.y-pygame.transform.scale(self.text,(self.scale_x//self.size_x, self.scale_y//20)).get_rect().height-2))

    def get_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = self.image_list[1]
                self.text = self.image_list[3]
            else:
                self.image = self.image_list[0]
                self.text = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = self.image_list[2]
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = self.image_list[0]
                self.text = False
                if self.action == 'Play':
                    from menu import Select_level
                    current_level = Select_level(self.player, image_select_level, 'Select_level')
                    self.player.level = current_level
                elif self.action == 'Help':
                    from menu import Help
                    current_level = Help(self.player, image_help_info, 'Help')
                    self.player.level = current_level
                elif self.action == 'Profile':
                    from menu import Select_your_hero
                    current_level = Select_your_hero(self.player, image_select_hero, 'Select_your_hero')
                    self.player.level = current_level
                elif self.action == 'Exit':
                   self.player.window_open = False
                elif self.action == 'Home':
                    from menu import Select_level
                    current_level = Select_level(self.player, image_select_level, 'Select_level')
                    self.player.level = current_level
                    self.player.music.load("music/menu.mp3")
                    self.player.music.play(-1, 0.0)
                elif self.action == 'Resume':
                    self.player.rect = self.player.level.rect 
                    self.player.level = self.player.level.current_level
                    self.player.draw_player = True
                    self.player.music.unpause()
                elif self.action == 'Records':
                    from menu import Hi_scores
                    current_level = Hi_scores(self.player, image_hi_scores, 'Hi_scores')
                    self.player.level = current_level
                elif self.action == 'Left':
                    if self.player.level.nr_list > 0:
                        self.player.level.nr_list -= 4
                elif self.action == 'Right':
                    if len(self.player.level.list_line) > self.player.level.nr_list + 4:
                        self.player.level.nr_list += 4
                elif self.action == 'Restart':
                    self.player.reset_data()
                    if self.player.level.current_level.name == 'Level 1':
                        from levels import Level_1
                        current_level = Level_1(self.player, image_background_level, 'Level 1')
                        self.player.level = current_level
                        self.player.draw_player = True
                    elif self.player.level.current_level.name == 'Level 2':
                        from levels import Level_2
                        current_level = Level_2(self.player, image_background_level, 'Level 2')
                        self.player.level = current_level
                        self.player.draw_player = True
                    elif self.player.level.current_level.name == 'Level 3':
                        from levels import Level_3
                        current_level = Level_3(self.player, image_background_level, 'Level 3')
                        self.player.level = current_level
                        self.player.draw_player = True
                    elif self.player.level.current_level.name == 'Level 4':
                        from levels import Level_4
                        current_level = Level_4(self.player, image_background_level, 'Level 4')
                        self.player.level = current_level
                        self.player.draw_player = True
                    elif self.player.level.current_level.name == 'Level 5':
                        from levels import Level_5
                        current_level = Level_5(self.player, image_background_level, 'Level 5')
                        self.player.level = current_level
                        self.player.draw_player = True
                    self.player.music.play(-1, 0.0)
                elif self.action in ['Hero_back', 'Back']:
                    from menu import Start_menu
                    current_level = Start_menu(self.player, image_start, 'Start_menu')
                    self.player.level = current_level
                elif self.action in ['Hero_1', 'Hero_2', 'Hero_3']:
                    self.player.load_hero(self.action)
                    from menu import Start_menu
                    current_level = Start_menu(self.player, image_start, 'Start_menu')
                    self.player.level = current_level
                elif self.action == 'Level_1':
                    from levels import Level_1
                    current_level = Level_1(self.player, image_background_level, 'Level 1')
                    self.player.level = current_level
                    self.player.draw_player = True
                    self.player.music.load("music/level1.mp3")
                    self.player.music.play(-1, 0.0)
                elif self.action == 'Level_2':
                    from levels import Level_2
                    current_level = Level_2(self.player, image_background_level, 'Level 2')
                    self.player.level = current_level
                    self.player.draw_player = True
                    self.player.music.load("music/level2.mp3")
                    self.player.music.play(-1, 0.0)
                elif self.action == 'Level_3':
                    from levels import Level_3
                    current_level = Level_3(self.player, image_background_level, 'Level 3')
                    self.player.level = current_level
                    self.player.draw_player = True
                    self.player.music.load("music/level3.mp3")
                    self.player.music.play(-1, 0.0)
                elif self.action == 'Level_4':
                    from levels import Level_4
                    current_level = Level_4(self.player, image_background_level, 'Level 4')
                    self.player.level = current_level
                    self.player.draw_player = True
                    self.player.music.load("music/level4.mp3")
                    self.player.music.play(-1, 0.0)
                elif self.action == 'Level_5':
                    from levels import Level_5
                    current_level = Level_5(self.player, image_background_level, 'Level 5')
                    self.player.level = current_level
                    self.player.draw_player = True
                    self.player.music.load("music/level5.mp3")
                    self.player.music.play(-1, 0.0)
                elif self.action == 'Next_level':
                    self.player.reset_data()
                    if self.player.level.current_level.name == 'Level 1':
                        from levels import Level_2
                        current_level = Level_2(self.player, image_background_level, 'Level 2')
                        self.player.level = current_level
                        self.player.draw_player = True
                        self.player.music.load("music/level2.mp3")
                        self.player.music.play(-1, 0.0)
                    elif self.player.level.current_level.name == 'Level 2':
                        from levels import Level_3
                        current_level = Level_3(self.player, image_background_level, 'Level 3')
                        self.player.level = current_level
                        self.player.draw_player = True
                        self.player.music.load("music/level3.mp3")
                        self.player.music.play(-1, 0.0)
                    elif self.player.level.current_level.name == 'Level 3':
                        from levels import Level_4
                        current_level = Level_4(self.player, image_background_level, 'Level 4')
                        self.player.level = current_level
                        self.player.draw_player = True
                        self.player.music.load("music/level4.mp3")
                        self.player.music.play(-1, 0.0)
                    elif self.player.level.current_level.name == 'Level 4':
                        from levels import Level_5
                        current_level = Level_5(self.player, image_background_level, 'Level 5')
                        self.player.level = current_level
                        self.player.draw_player = True
                        self.player.music.load("music/level5.mp3")
                        self.player.music.play(-1, 0.0)

    def resize(self, rect_x, rect_y, scale_x, scale_y):
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.rect = pygame.transform.scale(self.image,(self.scale_x//self.size_x, self.scale_y//self.size_y)).get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
