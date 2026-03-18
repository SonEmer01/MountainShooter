#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from typing import List

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, text_size=None):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        tempo = pygame.time.Clock()
        while True:
            tempo.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()

            #self.level_text(text_size: 14, text: f'{self.name} - Timeout:{self.timeout / 1000:.lf }s', COLOR_WHITE, text_pos: )10,5))

            pygame.display.flip()


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(self.name, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


