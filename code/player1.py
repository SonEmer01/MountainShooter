#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity

class Player1(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 1
        pass
