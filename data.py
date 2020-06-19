import pygame, os, datetime, sys

# stałe
katalog_z_obrazami = 'images'
wielkosc_bloku = 70
hi_scores_data = 'hiscores.txt'

# obrazy tła
image_start = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/start.png'))
image_select_hero = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/select_hero.png'))
image_select_level = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/select_level.png'))
image_background_level = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/level.png'))
image_pause = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/pause.png'))
image_game_over = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/game_over.png'))
image_hi_scores = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/hi_scores.png'))
image_info_health = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/health.png'))
image_info_time = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/time.png'))
image_info_crystal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/crystal.png'))
image_check = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/pointer.png'))
image_finish = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/scarecrow.png'))
image_crystal = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/crystal.png'))
image_level_complete = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/level_complete.png'))
image_lost_life = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/lost_life.png'))
image_help_info = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/backgrounds/help.png'))

#obrazy przycisków
image_play_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/play.png'))
image_play_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/play.png'))
image_play_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/play.png'))
image_play_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/play.png'))
image_exit_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/cancel.png'))
image_exit_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/cancel.png'))
image_exit_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/cancel.png'))
image_exit_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/exit.png'))
image_profile_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/profile.png'))
image_profile_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/profile.png'))
image_profile_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/profile.png'))
image_profile_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/profile.png'))
image_accept_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/accept.png'))
image_accept_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/accept.png'))
image_accept_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/accept.png'))
image_level_1_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/lvl_1.png'))
image_level_1_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/lvl_1.png'))
image_level_1_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/lvl_1.png'))
image_level_2_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/lvl_2.png'))
image_level_2_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/lvl_2.png'))
image_level_2_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/lvl_2.png'))
image_level_3_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/lvl_3.png'))
image_level_3_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/lvl_3.png'))
image_level_3_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/lvl_3.png'))
image_level_4_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/lvl_4.png'))
image_level_4_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/lvl_4.png'))
image_level_4_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/lvl_4.png'))
image_level_5_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/lvl_5.png'))
image_level_5_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/lvl_5.png'))
image_level_5_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/lvl_5.png'))
image_home_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/home.png'))
image_home_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/home.png'))
image_home_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/home.png'))
image_home_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/home.png'))
image_restart_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/restart.png'))
image_restart_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/restart.png'))
image_restart_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/restart.png'))
image_restart_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/restart.png'))
image_resume_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/resume.png'))
image_help_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/help.png'))
image_help_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/help.png'))
image_help_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/help.png'))
image_help_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/help.png'))
image_records_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/records.png'))
image_records_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/records.png'))
image_records_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/records.png'))
image_records_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/records.png'))
image_left_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/left.png'))
image_left_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/left.png'))
image_left_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/left.png'))
image_right_normal = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/normal/right.png'))
image_right_hover = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/hover/right.png'))
image_right_click = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/click/right.png'))
image_lock = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/lock/lock_level.png'))
image_next_level_text = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/text/next_level.png'))
image_lock_play = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/buttons/lock/lock_play.png'))

# listy obrazów przycisków
image_play = [image_play_normal, image_play_hover, image_play_click, image_play_text]
image_profile = [image_profile_normal, image_profile_hover, image_profile_click, image_profile_text]
image_exit = [image_exit_normal, image_exit_hover, image_exit_click, image_exit_text]
image_accept = [image_accept_normal, image_accept_hover, image_accept_click, False]
image_back = [image_exit_normal, image_exit_hover, image_exit_click, False]
image_level_1 = [image_level_1_normal, image_level_1_hover, image_level_1_click, False]
image_level_2 = [image_level_2_normal, image_level_2_hover, image_level_2_click, False]
image_level_3 = [image_level_3_normal, image_level_3_hover, image_level_3_click, False]
image_level_4 = [image_level_4_normal, image_level_4_hover, image_level_4_click, False]
image_level_5 = [image_level_5_normal, image_level_5_hover, image_level_5_click, False]
image_resume = [image_play_normal, image_play_hover, image_play_click, image_resume_text]
image_home = [image_home_normal, image_home_hover, image_home_click, image_home_text]
image_restart = [image_restart_normal, image_restart_hover, image_restart_click, image_restart_text]
image_help = [image_help_normal, image_help_hover, image_help_click, image_help_text]
image_records = [image_records_normal, image_records_hover, image_records_click, image_records_text]
image_left = [image_left_normal, image_left_hover, image_left_click, False]
image_right = [image_right_normal, image_right_hover, image_right_click, False]
image_next_level = [image_play_normal, image_play_hover, image_play_click, image_next_level_text]

# obrazy bloków
ground_0 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/00.png'))
ground_1 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/01.png'))
ground_2 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/02.png'))
ground_3 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/03.png'))
ground_4 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/04.png'))
ground_5 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/05.png'))
ground_6 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/06.png'))
wood_1 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/24.png'))
wood_2 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/25.png'))
wood_3 = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Tiles/26.png'))
spikes = pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/spikes.png'))

# tablice obrazów bloków
image_ground = [ground_0, ground_1, ground_2, ground_3, ground_4, ground_5, ground_6]
image_wood = [wood_1, wood_2, wood_3]

# obrazy gwiazdek
image_star_0 = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/0_stars.png'))
image_star_1 = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/1_stars.png'))
image_star_2 = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/2_stars.png'))
image_star_3 = pygame.image.load(os.path.join(katalog_z_obrazami,'Gui/info/3_stars.png'))
image_stars = [image_star_0, image_star_1, image_star_2, image_star_3]

# obrazy obiektów statycznych
bush_1 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/bush1.png')), 3 * wielkosc_bloku, 2 * wielkosc_bloku]
bush_2 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/bush2.png')), 3 * wielkosc_bloku, 2 * wielkosc_bloku]
flower_1 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/flower1.png')), 1 * wielkosc_bloku, 1 * wielkosc_bloku]
flower_2 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/flower2.png')), 1 * wielkosc_bloku, 1 * wielkosc_bloku]
flower_3 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/flower3.png')), 1 * wielkosc_bloku, 1 * wielkosc_bloku]
flower_4 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/flower4.png')), 1 * wielkosc_bloku, 1 * wielkosc_bloku]
flower_5 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/flower5.png')), 1 * wielkosc_bloku, 1 * wielkosc_bloku]
tree_1 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/tree1.png')), 5 * wielkosc_bloku, 7 * wielkosc_bloku]
tree_2 = [pygame.image.load(os.path.join(katalog_z_obrazami,'Block/Elements/tree2.png')), 4 * wielkosc_bloku, 6 * wielkosc_bloku]

screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)#pygame.FULLSCREEN)
SCREENSIZE = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
pygame.display.set_caption("My game")
