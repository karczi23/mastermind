from os.path import dirname
import RandomBall, os, pygame, Image, config, Text

class Game:
    def __init__(self, w = 640, h = 640) -> None:

        self.SCREEN_W = w
        self.SCREEN_H = h

        # vars
        self.RandomBall = RandomBall.RandomBall()
        self.img = Image.Image()
        self.text = Text.Text()

        # lists needed for saving 
        self.possiblities = []
        self.imgs = []
        self.predictions = []
        self.index = []
        self.win_balls = []
        self.win_balls_imgs = []

        dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

        # get images for balls
        for file in os.listdir(dirname):
            if file.endswith('_ball.png'):
                self.possiblities.append(file)
                self.imgs.append(self.img.create_image(file))
        # and for winning balls
            elif file.endswith('_win.png'):
                self.win_balls.append(file)
                self.win_balls_imgs.append(self.img.create_image(file))
        
    def start_new_game(self, count):
        # generate winning list on start
        self.winning_set = self.RandomBall.generate(count, self.possiblities)

        # change list items from 'some_name.png' to index
        for element in range(len(self.winning_set)):
            for j in range(len(self.possiblities)):
                if self.winning_set[element] == self.possiblities[j]:
                    self.winning_set[element] = j
                    break

        # set winning list to globals
        self.set_winning_set(self.winning_set)

        # fill lists with nothing
        for i in range(count):
            self.index.append(0)
            self.predictions.append(0)
        
        self.set_menu(False)

        # create surface for balls depending on ow many we choose
        self.w = 64 * count
        self.prediction_box = pygame.Surface((self.w, 64))
        self.prediction_box.fill(config.get_theme_color())

        # same but for winning balls
        self.trial = pygame.Surface((self.w, 64))
        self.trial.fill(config.get_theme_color())
        
        # setters
        self.set_drawable_winnings(self.trial)
        self.set_drawable_prediction(self.prediction_box)
        self.set_dp_w(self.w)
        self.set_index(self.index)
        self.set_predictions(self.predictions)
        
    def draw_prediction(self, count):
        # prepare and draw our prediction
        self.prediction_box = config.get_drawable_prediction()
        self.index = config.get_index()
        self.predictions = config.get_predictions()

        for i in range(count):
            self.prediction_box.blit(self.imgs[int(self.index[i]%8)], (i * 64, 0))
            self.predictions[i] = self.imgs[int(self.index[i%count]%8)].get_rect(
                left = (self.SCREEN_W/2 - 32*count + i * 64),
                top = 320
            )
        
        # set current guess
        self.set_drawable_prediction(self.prediction_box)


    def mem_write(self):
        # write history
        self.set_mem3(config.get_mem2().copy())
        self.set_mem2(config.get_mem1().copy())
        self.set_mem1(config.get_drawable_prediction().copy())


    def draw_winnings(self, count):
        # draw prediction but now to screen
        self.trial = config.get_drawable_winnings()

        for i in range(count):
            self.trial.blit(self.win_balls_imgs[1], (i * 64, 0))
        self.set_drawable_winnings(self.trial)
    
    def check_white(self):
        # self explanatory
        self.winning_set = config.get_winning_set()
        value = 0
        for i in range(len(self.index)):
            self.index[i] %= 8

        for element in set(self.index):
            if self.winning_set.count(element) > self.index.count(element):
                value += self.winning_set.count(element) - (self.winning_set.count(element) - self.index.count(element))  
            else: 
                value += self.winning_set.count(element)
        
        self.trial = config.get_drawable_winnings()

        for i in range(value):
            self.trial.blit(self.win_balls_imgs[2], (i * 64, 0))

        self.set_drawable_winnings(self.trial)

    def check_black(self):
        #self explanatory
        self.winning_set = config.get_winning_set()
        value = 0
        for element in range(len(self.index)):
            if self.index[element] == self.winning_set[element]:
                value += 1
        self.trial = config.get_drawable_winnings()

        for i in range(value):
            self.trial.blit(self.win_balls_imgs[0], (i * 64, 0))

        if value == len(self.winning_set):
            self.set_winner(True)

        self.set_drawable_winnings(self.trial)


    
    def display(self, screen, prediction_box, width, count, 
        drawable_winnings,
        # previous guess (up to 3)
        mem1 = pygame.Surface((0, 0)),
        mem2 = pygame.Surface((0, 0)),
        mem3 = pygame.Surface((0, 0))):
        # draw history to screen
        self.draw_prediction(count)
        
        screen.blit(prediction_box, (self.SCREEN_W/2 - width/2, 320))
        screen.blit(drawable_winnings, (self.SCREEN_W/2 - width/2, 400))
        screen.blit(mem1, (self.SCREEN_W/2 - width/2, 240))
        screen.blit(mem2, (self.SCREEN_W/2 - width/2, 160))
        screen.blit(mem3, (self.SCREEN_W/2 - width/2, 80))

    def display_winner(self, screen):
        # display if winner
        self.text.display_winner(screen, config.get_turns())

    # setters
        
    def set_mem1(self, value):
        config.mem1 = value
    
    def set_mem2(self, value):
        config.mem2 = value

    def set_mem3(self, value):
        config.mem3 = value

    def set_winner(self, value):
        config.winner = value

    def set_turns(self, value):
        config.turns = value
    
    def set_drawable_winnings(self, value):
        config.drawable_winnings = value
    
    def set_drawable_prediction(self, value):
        config.drawable_prediction = value

    def set_dp_w(self, value):
        config.dp_w = value

    def set_count(self, value):
        config.count = value

    def set_winning_set(self, value):
        config.winning_set = value

    def set_menu(self, value):
        config.menu = value

    def set_index(self, value):
        config.index = value

    def set_predictions(self, value):
        config.predictions = value