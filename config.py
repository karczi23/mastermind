import pygame as pg

def init():
    global menu
    global winner
    global drawable_prediction
    global count
    global index
    global predictions
    global theme_color
    global drawable_winnings
    global winning_set
    global mem1
    global mem2
    global mem3
    global turns

    # drawable prediction width
    global dp_w

    # init values, will change during program
    menu = True
    winner = False
    drawable_prediction = ''
    drawable_winnings = ''
    dp_w = 0
    count = 0
    index = []
    predictions = []
    theme_color = (30, 30, 180)
    winning_set = []
    mem1 = pg.Surface((0, 0))
    mem2 = pg.Surface((0, 0))
    mem3 = pg.Surface((0, 0))
    turns = 0

def get_menu():
    return menu

def get_winner():
    return winner

def get_drawable_prediction():
    return drawable_prediction

def get_dp_w():
    return dp_w

def get_count():
    return count

def get_index():
    return index

def get_predictions():
    return predictions

def get_theme_color():
    return theme_color

def get_drawable_winnings():
    return drawable_winnings

def get_winning_set():
    return winning_set

def get_mem1():
    return mem1

def get_mem2():
    return mem2

def get_mem3():
    return mem3

def get_turns():
    return turns