import tkinter as tk
from tkinter.constants import CENTER
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
start_menu.title("XO")
start_menu.geometry("400x400")
start_menu.config(bg="#272927")
start_menu.minsize(width=400, height=400)
start_menu.maxsize(width=400, height=400)

easy = tk.Button(master=start_menu, text="easy", command=start_easy_game)
medium = tk.Button(master=start_menu, text="medium", command=start_medium_game)
hard = tk.Button(master=start_menu, text="hard", command=start_hard_game)

easy.config(width=20, height=2)
medium.config(width=20, height=2)
hard.config(width=20, height=2)

easy.place(relx=0.5, rely=0.3, anchor=CENTER)
medium.place(relx=0.5, rely=0.5, anchor=CENTER)
hard.place(relx=0.5, rely=0.7, anchor=CENTER)

start_menu.mainloop()
