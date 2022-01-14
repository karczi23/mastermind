import pygame, sys, os

class Image:
    def __init__(self):
        # if pygame doesnt work good, turn off
        if not pygame.image.get_extended():
            print("could not load PNG files required to run tis game")
            sys.exit()
    
    # create images with transparent background
    def create_image(self, path):
        dirname = os.path.join(os.path.dirname(__file__),'assets', path)

        image = pygame.image.load(dirname).convert_alpha()
        return image
