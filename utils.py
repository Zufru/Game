import pygame

window = pygame.display.set_mode((800, 500))

shoot_timing = 0
shootloop = 0
score = 0
bullets = []

#player movement
walkRight = [
    pygame.image.load('Sprites/player/knight iso char_run right_0.png'), 
    pygame.image.load('Sprites/player/knight iso char_run right_1.png'), 
    pygame.image.load('Sprites/player/knight iso char_run right_2.png'),
    pygame.image.load('Sprites/player/knight iso char_run right_3.png'),
    pygame.image.load('Sprites/player/knight iso char_run right_4.png'),
    pygame.image.load('Sprites/player/knight iso char_run right_5.png')
    ]

health_gfx = [
    #pygame.image.load('Sprites/healthbars/health_bg.png'),
    #pygame.image.load('Sprites/healthbars/health_border.png'),
    pygame.image.load('Sprites/healthbars/full_health.png'),
    pygame.image.load('Sprites/healthbars/health -1.png'),
    pygame.image.load('Sprites/healthbars/health -2.png'),
    pygame.image.load('Sprites/healthbars/health -3.png'),
    pygame.image.load('Sprites/healthbars/health -4.png'),
    pygame.image.load('Sprites/healthbars/health -5.png'),
    pygame.image.load('Sprites/healthbars/health -6.png'),
    pygame.image.load('Sprites/healthbars/health -7.png'),
    pygame.image.load('Sprites/healthbars/health -8.png'),
    pygame.image.load('Sprites/healthbars/health -9.png')
    ]

enviroment = [
    pygame.image.load('Sprites/box.png'),
    pygame.image.load('Sprites/backgrounds/tree01 (2).png')
    ]

#player movement
walkLeft = [
    pygame.image.load('Sprites/player/knight iso char_run left_0.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_1.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_2.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_3.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_4.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_5.png')
    ]

g_over = pygame.image.load("Sprites/gameover.png")

bg = pygame.image.load('Sprites/backgrounds/sky_fc.png')

clouds = [
    pygame.image.load('Sprites/backgrounds/clouds_front_fc.png'),
    pygame.image.load('Sprites/backgrounds/clouds_mid_fc.png')
    ]

trees = [
    pygame.image.load('Sprites/backgrounds/tree01.png')
    ]
# CHARACTER IDLE IMAGE
char = [
    pygame.image.load('Sprites/player/knight iso char_idle_0.png'),
    pygame.image.load('Sprites/player/knight iso char_idle_1.png'),
    pygame.image.load('Sprites/player/knight iso char_idle_2.png'),
    pygame.image.load('Sprites/player/knight iso char_idle_3.png')
    ]

hell_beast = [
    pygame.image.load('Sprites/Hell_beast/hellb1.png'),
    pygame.image.load('Sprites/Hell_beast/hellb2.png'),
    pygame.image.load('Sprites/Hell_beast/hellb3.png'),
    pygame.image.load('Sprites/Hell_beast/hellb4.png'),
    pygame.image.load('Sprites/Hell_beast/hellb5.png'),
    pygame.image.load('Sprites/Hell_beast/hellb6.png'),
    pygame.image.load('Sprites/Hell_beast/hellb1.png'),
    pygame.image.load('Sprites/Hell_beast/hellb2.png'),
    pygame.image.load('Sprites/Hell_beast/hellb3.png'),
    pygame.image.load('Sprites/Hell_beast/hellb4.png')
    ]

hell_beast_breath = [
    pygame.image.load('Sprites/Hell_beast/hellb_breath1.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath2.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath3.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath4.png')
    ]

walkLeftgoblin = [
    pygame.image.load('Sprites/e_goblin/L1E.png'),
    pygame.image.load('Sprites/e_goblin/L2E.png'),
    pygame.image.load('Sprites/e_goblin/L3E.png'),
    pygame.image.load('Sprites/e_goblin/L4E.png'),
    pygame.image.load('Sprites/e_goblin/L5E.png'),
    pygame.image.load('Sprites/e_goblin/L6E.png'),
    pygame.image.load('Sprites/e_goblin/L7E.png'),
    pygame.image.load('Sprites/e_goblin/L8E.png'),
    pygame.image.load('Sprites/e_goblin/L9E.png'),
    pygame.image.load('Sprites/e_goblin/L10E.png'),
    pygame.image.load('Sprites/e_goblin/L11E.png')
    ]
    
walkRightgoblin = [
    pygame.image.load('Sprites/e_goblin/R1E.png'),
    pygame.image.load('Sprites/e_goblin/R2E.png'),
    pygame.image.load('Sprites/e_goblin/R3E.png'),
    pygame.image.load('Sprites/e_goblin/R4E.png'),
    pygame.image.load('Sprites/e_goblin/R5E.png'),
    pygame.image.load('Sprites/e_goblin/R6E.png'),
    pygame.image.load('Sprites/e_goblin/R7E.png'),
    pygame.image.load('Sprites/e_goblin/R8E.png'),
    pygame.image.load('Sprites/e_goblin/R9E.png'),
    pygame.image.load('Sprites/e_goblin/R10E.png'),
    pygame.image.load('Sprites/e_goblin/R11E.png')
    ]

# BULLET SOUND EFFECT WHEN SHOT
#bullet_sfx = [
#    pygame.mixer.sound('Sound/bullet.wav'),
#    ]
# BULLET SOUND EFECT WHEN HITS TARGET
#hit_sfx = [
#    pygame.mixer.sound('Sound/hit.wav')
#    ]
# BACKGROUND MUSIC
#music = pygame.mixer.music.load('Sound/music.mp3')
#pygame.mixer.music.play(-1)