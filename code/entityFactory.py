#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from unittest import case
from code.background import Background
from code.enemy import Enemy
from code.player1 import Player
from const import WIN_WIDTH, WIN_HEIGHT

def get_entity(entity_name: str, position=tuple):
    match entity_name:
        case 'Level1Bg':
            list_bg = []
            for i in range(7):
                list_bg.append(Background(f'Level1Bg{i}', position=(0,0)))
                list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
            return list_bg
        case 'Player1':
            return Player('Player1', (10, WIN_HEIGHT/2 - 30))
        case 'Player2':
            return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
        case 'Enemy1':
            return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        case 'Enemy2':
            return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
    return None