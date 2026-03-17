#!/usr/bin/python
# -*- coding: utf-8 -*-
from code import background


class EntityFactory:

    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case "level1Bg":
                list_Bg = []
                for i in range(7):
                    list_Bg.append(background(name: f'Level1Bg{i}', position: (0, 0)))
