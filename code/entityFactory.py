#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import case

from code import background
from code.background import Background
from const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=tuple):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
        return None