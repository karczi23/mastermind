from sys import path
import pygame, Image, os

# inherit from pygame sprite
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        img = Image.Image()

        self.image = img.create_image('cursor.png')

        pygame.mouse.set_visible(False)

    # draw our cursor wherever we have our windows cursor
    def update(self, screen):
        pos = pygame.mouse.get_pos()
        screen.blit(self.image, (pos[0] - 15, pos[1] -  15))
