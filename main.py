import sys

import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode((600, 480))
print("Setup Finish")

print("Loop Start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()