import pygame, sys, Game, config
from pygame.constants import K_ESCAPE

class EventHandler:

    def __init__(self, Text, screen):

        # vars
        self.Text = Text
        self.screen = screen
        self.text = ''
        self.Game = Game.Game()

    def handleKeyboardEvent(self, event):
        # turn off game
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif not config.get_winner():
            # remove text from input (if exists)
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                return self.text
            # start game
            elif event.key == pygame.K_RETURN and config.menu:
                if self.text != '' and not int(self.text) > 10:
                    self.Game.start_new_game(int(self.text))
                    self.Game.set_count(int(self.text))
                # if text > 10 dont accept
                else:
                    return self.text
            # check for winner
            elif event.key == pygame.K_RETURN and not config.menu:
                self.Game.draw_winnings(int(self.text))
                self.Game.check_white()
                self.Game.check_black()
                self.Game.mem_write()
                self.Game.set_turns(config.get_turns()+1)
            # add to input box
            else:
                try:
                    if int(event.unicode) >= 0 and int(event.unicode) <= 9: 
                        self.text += event.unicode
                        return self.text
                except:
                    return self.text

    def handleMouseEvent(self, event):
        # check if button in menu is clicked
        if self.Text.start_rect.collidepoint(event.pos) and config.menu:
            return True
        # unclick the button if pressed outside
        elif not self.Text.start_rect.collidepoint(event.pos) and config.menu:
            return False
        # change balls on click
        else:
            if not config.get_winner():
                for i in range(int(config.get_dp_w() / 64)):
                    if self.Game.predictions[i].collidepoint(event.pos):
                        self.Game.index[i] += 1