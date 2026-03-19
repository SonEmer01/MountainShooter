#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import case

from code.background import Background
from code.player1 import Player1
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
            return Player1('Player1', (10, WIN_HEIGHT/2))
    return None