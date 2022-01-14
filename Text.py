from os import path
import pygame, os, config

class Text:
    def __init__(self, w = 640, h = 640) -> None:

        self.SCREEN_W = w
        self.SCREEN_H = h

        # text strings
        self.title_text = 'Mastermind'
        self.button_text = 'Rozpocznij grę'
        
        # path
        dirname = os.path.join(os.path.dirname(__file__), 'bin\\font.ttf')

        # load fonts
        self.fontBig = pygame.font.Font(dirname, 48)
        self.fontMedium = pygame.font.Font(dirname, 30)
        self.fontSmall = pygame.font.Font(dirname, 20)
        self.fontVerySmall = pygame.font.Font(dirname, 14)
        self.winner = pygame.font.Font(dirname, 25)

        # header
        self.header = self.fontBig.render(self.title_text, True, (255, 255, 255))
        self.title_w, self.title_h = self.fontBig.size(self.title_text)

        # button
        self.button = self.fontMedium.render(self.button_text, True, (255, 255, 255))
        self.button_w, self.button_h = self.fontMedium.size(self.button_text)

        self.start = pygame.Surface((self.button_w+20, self.button_h+20))

        # rect to check for crossing
        self.start_rect = self.start.get_rect(
            left = (self.SCREEN_W/2 - self.button_w/2 - 10), 
            top = (self.SCREEN_H/2 - self.button_h/2 - 10)
        )

    def display_title_screen(self, screen):
        # title
        screen.blit(
            self.header,
            (self.SCREEN_W/2 - self.title_w/2, 
            self.SCREEN_H/4 - self.title_h/2)
        )

        # text into button
        self.start.blit(self.button, (10, 10))

        # button
        screen.blit(
            self.start, 
            (self.SCREEN_W/2 - self.button_w/2 - 10, 
            self.SCREEN_H/2 - self.button_h/2 - 10)
        )

    def get_start(self):
        return self.start

    def display_input_box(self, screen, input):
        # draw rectangle with theme color behind text
        self.input_box = pygame.Surface((self.SCREEN_W/4, self.SCREEN_H/10))
        self.input_box.fill(config.get_theme_color())

        # render text
        self.input = self.fontSmall.render(input, True, (255, 255, 255))
        self.input_box.blit(self.input, (10, 10))

        # render text on rectangle
        screen.blit(
            self.input_box,
            (self.SCREEN_W/2 - self.SCREEN_W/8,
            self.SCREEN_H/8 * 5)
        )

    def display_instructions(self, screen):

        self.instructions_text = 'ENTER - zatwierdzamy, LPM - przeklikujemy wybór'

        # render text and check its size
        self.instructions = self.fontVerySmall.render(self.instructions_text, True, (255, 255, 255))
        self.instructions_w, self.instructions_h = self.fontVerySmall.size(self.instructions_text)

        # draw rect behind
        self.instructions_box = pygame.Surface((self.instructions_w + 20, self.instructions_h + 20))
        self.instructions_box.fill(config.get_theme_color())

        # text on rect
        self.instructions_box.blit(self.instructions, (10, 10))
        
        # render on screen
        screen.blit(self.instructions, (self.SCREEN_W/2 - self.instructions_w/2, self.SCREEN_H/8*7  - self.instructions_h/2))


    def display_winner(self, screen, turns):

        # display winner messages depending on turns
        if turns == 1:
            self.winner_t = f'Gratulacje! Wygrałeś w {turns} ruchu!'
        else:
            self.winner_t = f'Gratulacje! Wygrałeś w {turns} ruchach!'

        # render text, check size
        self.winner_text = self.winner.render(self.winner_t, True, (255, 255, 255))
        self.winner_w, self.winner_h = self.winner.size(self.winner_t)

        # rect behind
        self.winner_surface = pygame.Surface((self.winner_w + 20, self.winner_h + 20))
        self.winner_surface.fill(config.get_theme_color())

        # text to rect
        self.winner_surface.blit(self.winner_text, (10, 10))

        # to screen
        screen.blit(self.winner_surface, (self.SCREEN_W/2 - self.winner_w/2, self.SCREEN_H/8*7  - self.winner_h/2))