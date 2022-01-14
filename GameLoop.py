import pygame, Cursor, EventHandler, sys, Text, Game, config, Image
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT

####################################################################
####                                                            ####
####                         MAIN  FILE                         ####
####                                                            ####
####                KAROL KOŹLINKA 3H MASTERMIND                ####
####                                                            ####
####################################################################

class GameLoop:
    def __init__(self, width = 640, height = 640, title = "Mastermind"):
        self.size = self.width, self.height = width, height
        self.title = title
        

    def initGameLoop(self):

        # if pygame doesnt work turn off
        if not pygame.get_init():
            pygame.init()
            print("pygame initialised")

        clock = pygame.time.Clock()
        self.img = Image.Image()

        self.screen = pygame.display.set_mode(self.size)
        
        self.icon = self.img.create_image('icon.png')

        # icon and title of window
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

        # used for while loop (render frames)
        running = True

        # vars
        self.text = Text.Text(self.width, self.height)
        self.Cursor = Cursor.Cursor()
        self.e = EventHandler.EventHandler(self.text, self.screen)
        self.Game = Game.Game(self.width, self.height)

        # init config vars
        config.init()

        self.themeColor = config.get_theme_color()

        # for input
        self.active = False

        self.input = 'Kule (max 10)'

        while running:
            
            # render menu or render game
            menu = config.get_menu()

            # event handling, more in EventHHandler.py
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.input = self.e.handleKeyboardEvent(event)
                elif event.type == MOUSEBUTTONDOWN:
                    self.active = self.e.handleMouseEvent(event)

            # background color
            self.screen.fill(self.themeColor)
            
            if menu:
                self.text.display_title_screen(self.screen)
                self.text.display_instructions(self.screen)

                if self.active:
                    self.text.display_input_box(self.screen, self.input)
            else:
                self.Game.display(
                    self.screen, 
                    config.get_drawable_prediction(), 
                    config.get_dp_w(), 
                    config.get_count(), 
                    config.get_drawable_winnings(),
                    config.get_mem1(),
                    config.get_mem2(),
                    config.get_mem3()
                )
                
                if config.get_winner():
                    self.Game.display_winner(self.screen)
            
            self.Cursor.update(self.screen)

            # refresh screen
            pygame.display.flip()
            
            # limit to 60 FPS
            clock.tick(60)


# exec
if __name__ == '__main__':
    try:
        app = GameLoop()
        app.initGameLoop()
    except KeyboardInterrupt:
        print("Exiting...")