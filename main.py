import tkinter as tk
from constants.game_level import GameLevel
from game import Game


def start_hard_game():
    start_menu.destroy()
    game = Game(GameLevel.HARD)
    game.run()


def start_medium_game():
    start_menu.destroy()
    game = Game(GameLevel.MEDIUM)
    game.run()


def start_easy_game():
    start_menu.destroy()
    game = Game(GameLevel.EASY)
    game.run()


start_menu = tk.Tk()
easy = tk.Button(master=start_menu, text="easy", command=start_easy_game)
medium = tk.Button(master=start_menu, text="medium", command=start_medium_game)
hard = tk.Button(master=start_menu, text="hard", command=start_hard_game)
easy.pack()
medium.pack()
hard.pack()

start_menu.mainloop()
