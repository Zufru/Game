# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:26:01 2020

@author: Tenkkeys
"""

import pygame
pygame.init()
bullets = []

game_items = [
    pygame.image.load('Sprites/items/used/ring_02d.png')
    ]

key_img_instructions = [
    pygame.image.load('Sprites/misc/w_key_img.png'),
    pygame.image.load('Sprites/misc/a_key_img.png'),
    pygame.image.load('Sprites/misc/d_key_img.png'),
    pygame.image.load('Sprites/misc/space_key_img.png'),
    pygame.image.load('Sprites/misc/e_key_img.png'),
    ]

g_over = pygame.image.load("Sprites/backgrounds/gameover.png")

bg = pygame.image.load('Sprites/backgrounds/background1.png')
instruction_scroll = pygame.image.load('Sprites/backgrounds/instruction_scroll.png')
title_screen_img = pygame.image.load('Sprites/backgrounds/title_screen.png')

clouds = [
    pygame.image.load('Sprites/backgrounds/clouds_front_fc.png'),
    pygame.image.load('Sprites/backgrounds/clouds_mid_fc.png')
    ]

energy_ball_player = [
    pygame.image.load('Sprites/energy_ball/EnergyBall1.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall2.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall3.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall4.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall5.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall6.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall7.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall8.png'),
    pygame.image.load('Sprites/energy_ball/EnergyBall9.png')
    ]

health_gfx = [
    #pygame.image.load('Sprites/healthbars/health_bg.png'),
    #pygame.image.load('Sprites/healthbars/health_border.png'),
    pygame.image.load('Sprites/healthbars/hp_value_0.png'),
    pygame.image.load('Sprites/healthbars/hp_value_1.png'),
    pygame.image.load('Sprites/healthbars/hp_value_2.png'),
    pygame.image.load('Sprites/healthbars/hp_value_3.png'),
    pygame.image.load('Sprites/healthbars/hp_value_4.png'),
    pygame.image.load('Sprites/healthbars/hp_value_5.png')
    # pygame.image.load('Sprites/healthbars/health -6.png'),
    # pygame.image.load('Sprites/healthbars/health -7.png'),
    # pygame.image.load('Sprites/healthbars/health -8.png'),
    # pygame.image.load('Sprites/healthbars/health -9.png')
    ]

props = [
    pygame.image.load('Sprites/props/box.png'),
    pygame.image.load('Sprites/props/tree01 (2).png'),
    pygame.image.load('Sprites/props/concrete_with_woodbridge.png'),
    pygame.image.load('Sprites/props/stairsup1t.png'),
    pygame.image.load('Sprites/props/stairsup2t.png'),
    pygame.image.load('Sprites/props/stairsup3t.png'),
    pygame.image.load('Sprites/props/pillar1.png'),
    pygame.image.load('Sprites/props/pillar2.png'),
    pygame.image.load('Sprites/props/platform1.png'),
    pygame.image.load('Sprites/props/platform2.png'),
    pygame.image.load('Sprites/props/pillar3.png'),
    pygame.image.load('Sprites/props/pillar4.png'),
    pygame.image.load('Sprites/props/platform3.png'),
    pygame.image.load('Sprites/props/platform4.png'),
    pygame.image.load('Sprites/props/pillar5.png'),
    pygame.image.load("Sprites/props/flooring1.png")
    ]

torches = [
    pygame.image.load("Sprites/props/torches/groundtorch3.png")
    ]

torchesfire1 = [
    pygame.image.load("Sprites/props/torches/grndtorchflameani3.png"),
    pygame.image.load("Sprites/props/torches/grndtorchflameani4.png"),
    pygame.image.load("Sprites/props/torches/grndtorchflameani5.png"),
    pygame.image.load("Sprites/props/torches/grndtorchflameani6.png"),
    pygame.image.load("Sprites/props/torches/grndtorchflameani7.png"),
    pygame.image.load("Sprites/props/torches/grndtorchflameani8.png"),
    pygame.image.load("Sprites/props/torches/grndtorchflameani9.png")
    ]

walkRight = [
    pygame.image.load('Sprites/player/Player_movement/walkR_1.png'), 
    pygame.image.load('Sprites/player/Player_movement/walkR_2.png'), 
    pygame.image.load('Sprites/player/Player_movement/walkR_3.png'), 
    pygame.image.load('Sprites/player/Player_movement/walkR_4.png')
    ]

#player movement
walkLeft = [
    pygame.image.load('Sprites/player/Player_movement/walkL_1.png'), 
    pygame.image.load('Sprites/player/Player_movement/walkL_2.png'), 
    pygame.image.load('Sprites/player/Player_movement/walkL_3.png'), 
    pygame.image.load('Sprites/player/Player_movement/walkL_4.png')
    ]

player_attackR = [
    pygame.image.load('Sprites/player/player_attack/attackR2.png'),
    pygame.image.load('Sprites/player/player_attack/attackR3.png'),
    pygame.image.load('Sprites/player/player_attack/attackR4.png'),
    pygame.image.load('Sprites/player/player_attack/attackR5.png'),
    pygame.image.load('Sprites/player/player_attack/attackR6.png'),
    pygame.image.load('Sprites/player/player_attack/attackR7.png'),
    pygame.image.load('Sprites/player/player_attack/attackR8.png'),
    pygame.image.load('Sprites/player/player_attack/attackR9.png'),
    pygame.image.load('Sprites/player/player_attack/attackR10.png')
    ]

player_attackL = [
    pygame.image.load('Sprites/player/player_attack/attackL2.png'),
    pygame.image.load('Sprites/player/player_attack/attackL3.png'),
    pygame.image.load('Sprites/player/player_attack/attackL4.png'),
    pygame.image.load('Sprites/player/player_attack/attackL5.png'),
    pygame.image.load('Sprites/player/player_attack/attackL6.png'),
    pygame.image.load('Sprites/player/player_attack/attackL7.png'),
    pygame.image.load('Sprites/player/player_attack/attackL8.png'),
    pygame.image.load('Sprites/player/player_attack/attackL9.png'),
    pygame.image.load('Sprites/player/player_attack/attackL10.png')
    ]

player_death = [
    pygame.image.load('Sprites/player/player_death/dead_1.png'), 
    pygame.image.load('Sprites/player/player_death/dead_2.png'), 
    pygame.image.load('Sprites/player/player_death/dead_3.png'), 
    pygame.image.load('Sprites/player/player_death/dead_4.png')
    ]

female_npc_chaticon = pygame.image.load('Sprites/NPC_level1/chat_icon.png')

female_npc_level1 = [
    pygame.image.load('Sprites/NPC_level1/idle01.png'),
    pygame.image.load('Sprites/NPC_level1/idle02.png'),
    pygame.image.load('Sprites/NPC_level1/idle03.png'),
    pygame.image.load('Sprites/NPC_level1/idle04.png'),
    pygame.image.load('Sprites/NPC_level1/idle05.png'),
    pygame.image.load('Sprites/NPC_level1/idle06.png'),
    pygame.image.load('Sprites/NPC_level1/idle07.png'),
    pygame.image.load('Sprites/NPC_level1/idle08.png'),
    pygame.image.load('Sprites/NPC_level1/idle09.png')
    ]

female_npc_level1_left = [
    pygame.image.load('Sprites/NPC_level1/facingLeft01.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft02.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft03.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft04.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft05.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft06.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft07.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft08.png'),
    pygame.image.load('Sprites/NPC_level1/facingLeft09.png')
    ]

doors = [
    pygame.image.load('Sprites/props/door.png')
    ]
# CHARACTER IDLE IMAGE
char = [
    pygame.image.load('Sprites/player/Player_idle/idle_1.png'),
    pygame.image.load('Sprites/player/Player_idle/idle_2.png'),
    pygame.image.load('Sprites/player/Player_idle/idle_3.png'),
    pygame.image.load('Sprites/player/Player_idle/idle_4.png')
    ]

charL = [
    pygame.image.load('Sprites/player/Player_idle/idleL_1.png'),
    pygame.image.load('Sprites/player/Player_idle/idleL_2.png'),
    pygame.image.load('Sprites/player/Player_idle/idleL_3.png'),
    pygame.image.load('Sprites/player/Player_idle/idleL_4.png')
    ]

hell_beast = [
    pygame.image.load('Sprites/Hell_beast/hellb1.png'),
    pygame.image.load('Sprites/Hell_beast/hellb2.png'),
    pygame.image.load('Sprites/Hell_beast/hellb3.png'),
    pygame.image.load('Sprites/Hell_beast/hellb4.png'),
    pygame.image.load('Sprites/Hell_beast/hellb5.png'),
    pygame.image.load('Sprites/Hell_beast/hellb6.png')
    ]

hell_beast_breath = [
    pygame.image.load('Sprites/Hell_beast/hellb_breath1.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath2.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath3.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath4.png')
    ]

hell_beast_fireball = [
    pygame.image.load('Sprites/Hell_beast/fire-ball1.png'),
    pygame.image.load('Sprites/Hell_beast/fire-ball2.png'),
    pygame.image.load('Sprites/Hell_beast/fire-ball3.png')
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

walkRightgoblin2 = [
    pygame.image.load('Sprites/goblin2/goblin run1.png'),
    pygame.image.load('Sprites/goblin2/goblin run2.png'),
    pygame.image.load('Sprites/goblin2/goblin run3.png'),
    pygame.image.load('Sprites/goblin2/goblin run4.png'),
    pygame.image.load('Sprites/goblin2/goblin run5.png'),
    pygame.image.load('Sprites/goblin2/goblin run6.png')
    ]

walkLeftgoblin2 = [
    pygame.image.load('Sprites/goblin2/goblin runLeft1.png'),
    pygame.image.load('Sprites/goblin2/goblin runLeft2.png'),
    pygame.image.load('Sprites/goblin2/goblin runLeft3.png'),
    pygame.image.load('Sprites/goblin2/goblin runLeft4.png'),
    pygame.image.load('Sprites/goblin2/goblin runLeft5.png'),
    pygame.image.load('Sprites/goblin2/goblin runLeft6.png')
    ]

masked_enemy_walkRight = [
    pygame.image.load('Sprites/masked_enemy/walkRight/walk01.png'),
    pygame.image.load('Sprites/masked_enemy/walkRight/walk02.png'),
    pygame.image.load('Sprites/masked_enemy/walkRight/walk03.png'),
    pygame.image.load('Sprites/masked_enemy/walkRight/walk04.png'),
    pygame.image.load('Sprites/masked_enemy/walkRight/walk05.png'),
    pygame.image.load('Sprites/masked_enemy/walkRight/walk06.png')
    ]

masked_enemy_walkLeft = [
    pygame.image.load('Sprites/masked_enemy/walkLeft/walkLeft01.png'),
    pygame.image.load('Sprites/masked_enemy/walkLeft/walkLeft02.png'),
    pygame.image.load('Sprites/masked_enemy/walkLeft/walkLeft03.png'),
    pygame.image.load('Sprites/masked_enemy/walkLeft/walkLeft04.png'),
    pygame.image.load('Sprites/masked_enemy/walkLeft/walkLeft05.png'),
    pygame.image.load('Sprites/masked_enemy/walkLeft/walkLeft06.png')
    ]

masked_enemy_idle = [
    pygame.image.load('Sprites/masked_enemy/idle/idle01.png'),
    pygame.image.load('Sprites/masked_enemy/idle/idle02.png'),
    pygame.image.load('Sprites/masked_enemy/idle/idle03.png'),
    pygame.image.load('Sprites/masked_enemy/idle/idle04.png'),
    pygame.image.load('Sprites/masked_enemy/idle/idle05.png'),
    pygame.image.load('Sprites/masked_enemy/idle/idle06.png'),
    pygame.image.load('Sprites/masked_enemy/idle/idle07.png')
    ]

masked_enemy_attack = [
    pygame.image.load('Sprites/masked_enemy/attack/attack01.png'),
    pygame.image.load('Sprites/masked_enemy/attack/attack02.png'),
    pygame.image.load('Sprites/masked_enemy/attack/attack03.png'),
    pygame.image.load('Sprites/masked_enemy/attack/attack04.png'),
    pygame.image.load('Sprites/masked_enemy/attack/attack05.png'),
    pygame.image.load('Sprites/masked_enemy/attack/attack06.png'),
    pygame.image.load('Sprites/masked_enemy/attack/attack07.png')
    ]

masked_enemy_hitR = [
    pygame.image.load('Sprites/masked_enemy/hit/hitR01.png'),
    pygame.image.load('Sprites/masked_enemy/hit/hitR02.png'),
    pygame.image.load('Sprites/masked_enemy/hit/hitR03.png')
    ]

masked_enemy_hitL = [
    pygame.image.load('Sprites/masked_enemy/hit/hitL01.png'),
    pygame.image.load('Sprites/masked_enemy/hit/hitL02.png'),
    pygame.image.load('Sprites/masked_enemy/hit/hitL03.png')
    ]
# BULLET SOUND EFFECT WHEN SHOT
#bullet_sfx = [
#    pygame.mixer.sound('Sound/bullet.wav'),
#    ]
# BULLET SOUND EFECT WHEN HITS TARGET
#hit_sfx = [
#    pygame.mixer.sound('Sound/hit.wav')
#    ]
ping_sound = pygame.mixer.Sound('misc/Sound/ping_sound.wav')
door_sfx = pygame.mixer.Sound('misc/Sound/door_sfx.wav')
# BACKGROUND MUSIC
music = pygame.mixer.music.load('misc/Sound/background_music.mp3')
pygame.mixer.music.play(-1)
