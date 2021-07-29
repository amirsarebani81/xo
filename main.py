import tkinter as tk
from game import Game


def start_program():
    start_menu.destroy()
    game = Game()
    game.run()


start_menu = tk.Tk()
start_button = tk.Button(master=start_menu, text="Start", command=start_program)
start_button.pack()

start_menu.mainloop()
