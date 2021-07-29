import sys
import tkinter as tk
from random import Random
from tkinter.constants import CENTER

from board.board import Board
from constants.game_level import GameLevel
from constants.game_status import GameStatus
from constants.square_status import SquareStatus
from player.computer import Computer
from player.player import Player


class Game:
    def __init__(self):
        self.__board = Board()
        self.__computer = Computer(self.__board)
        self.__player = Player(self.__board)
        self.__game_status = GameStatus.CONTINUE

    def __init_window(self):
        self.window = tk.Tk()
        self.window.title(self.__computer.get_game_level())
        self.window.geometry("400x400")
        self.window.config(bg="#272927")
        self.window.minsize(width=400, height=400)
        self.window.maxsize(width=400, height=400)

    def __init_buttons(self):
        self.buttons = list()
        self.buttons.append(
            tk.Button(master=self.window, text=1, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_1))
        self.buttons.append(
            tk.Button(master=self.window, text=2, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_2))
        self.buttons.append(
            tk.Button(master=self.window, text=3, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_3))
        self.buttons.append(
            tk.Button(master=self.window, text=4, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_4))
        self.buttons.append(
            tk.Button(master=self.window, text=5, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_5))
        self.buttons.append(
            tk.Button(master=self.window, text=6, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_6))
        self.buttons.append(
            tk.Button(master=self.window, text=7, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_7))
        self.buttons.append(
            tk.Button(master=self.window, text=8, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_8))
        self.buttons.append(
            tk.Button(master=self.window, text=9, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_9))

        self.buttons[0].place(relx=0.25, rely=0.25, anchor=CENTER)
        self.buttons[1].place(relx=0.5, rely=0.25, anchor=CENTER)
        self.buttons[2].place(relx=0.75, rely=0.25, anchor=CENTER)
        self.buttons[3].place(relx=0.25, rely=0.5, anchor=CENTER)
        self.buttons[4].place(relx=0.5, rely=0.5, anchor=CENTER)
        self.buttons[5].place(relx=0.75, rely=0.5, anchor=CENTER)
        self.buttons[6].place(relx=0.25, rely=0.75, anchor=CENTER)
        self.buttons[7].place(relx=0.5, rely=0.75, anchor=CENTER)
        self.buttons[8].place(relx=0.75, rely=0.75, anchor=CENTER)

    def __init_labels(self):
        self.labels = list()

    def __init_images(self):
        self.images = dict()
        self.images['cross'] = tk.PhotoImage(file="images/cross.png")
        self.images['circle'] = tk.PhotoImage(file="images/circle.png")
        self.images['win'] = tk.PhotoImage(file="images/win.png")
        self.images['lose'] = tk.PhotoImage(file="images/lose.png")
        self.images['tie'] = tk.PhotoImage(file="images/tie.png")
        self.images['restart'] = tk.PhotoImage(file="images/restart.png")
        self.images['menu'] = tk.PhotoImage(file="images/menu.png")
        self.images['exit'] = tk.PhotoImage(file="images/exit.png")

        self.images['cross'] = self.images['cross'].subsample(30)
        self.images['circle'] = self.images['circle'].subsample(18)
        self.images['win'] = self.images['win'].subsample(5)
        self.images['lose'] = self.images['lose'].subsample(5)
        self.images['tie'] = self.images['tie'].subsample(2)
        self.images['restart'] = self.images['restart'].subsample(15)
        self.images['menu'] = self.images['menu'].subsample(15)
        self.images['exit'] = self.images['exit'].subsample(60)

    def __check_game_status(self):
        for row in range(1, 4):
            squares = self.__board.get_row(row)
            self.__game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
            if self.__game_status != GameStatus.CONTINUE:
                return

        for column in range(1, 4):
            squares = self.__board.get_column(column)
            self.__game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
            if self.__game_status != GameStatus.CONTINUE:
                return

        squares = self.__board.get_left_to_right_diagonal()
        self.__game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
        if self.__game_status != GameStatus.CONTINUE:
            return

        squares = self.__board.get_right_to_left_diagonal()
        self.__game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
        if self.__game_status != GameStatus.CONTINUE:
            return

        if self.__board.is_board_full():
            self.__game_status = GameStatus.TIE

    def __do_selects(self, row, column):
        print(self.__computer.get_game_level())
        self.__player.mark_square(row, column)
        self.__board.print_board()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__clean_window()
            self.__print_result()
            self.__init_restart_button()
            self.__init_menu_button()
            self.__init_exit_button()
            self.window.mainloop()

        self.__computer.select_square()
        self.__board.print_board()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__clean_window()
            self.__print_result()
            self.__init_restart_button()
            self.__init_menu_button()
            self.__init_exit_button()
            self.window.mainloop()

    def __press_1(self):
        self.__do_selects(1, 1)
        self.__update_gui()

    def __press_2(self):
        self.__do_selects(1, 2)
        self.__update_gui()

    def __press_3(self):
        self.__do_selects(1, 3)
        self.__update_gui()

    def __press_4(self):
        self.__do_selects(2, 1)
        self.__update_gui()

    def __press_5(self):
        self.__do_selects(2, 2)
        self.__update_gui()

    def __press_6(self):
        self.__do_selects(2, 3)
        self.__update_gui()

    def __press_7(self):
        self.__do_selects(3, 1)
        self.__update_gui()

    def __press_8(self):
        self.__do_selects(3, 2)
        self.__update_gui()

    def __press_9(self):
        self.__do_selects(3, 3)
        self.__update_gui()

    def __update_gui(self):
        for row in range(1, 4):
            for column in range(1, 4):
                if self.__board.get_square(row, column) != SquareStatus.EMPTY:
                    self.__delete_button((row - 1) * 3 + column)
                    if self.__board.get_square(row, column) == SquareStatus.COMPUTER:
                        label = tk.Label(master=self.window, image=self.images['cross'], background="#272927")
                        label.place(relx=column * 0.25, rely=row * 0.25, anchor=CENTER)
                        self.labels.append(label)
                    else:
                        label = tk.Label(master=self.window, image=self.images['circle'], background="#272927")
                        label.place(relx=column * 0.25, rely=row * 0.25, anchor=CENTER)
                        self.labels.append(label)
        self.window.mainloop()

    def __delete_button(self, button_id):
        self.buttons[button_id - 1].destroy()

    def start_hard_game(self):
        self.start_menu.destroy()
        self.__computer.set_game_level(GameLevel.HARD)
        self.run()

    def start_medium_game(self):
        self.start_menu.destroy()
        self.__computer.set_game_level(GameLevel.MEDIUM)
        self.run()

    def start_easy_game(self):
        self.start_menu.destroy()
        self.__computer.set_game_level(GameLevel.EASY)
        self.run()

    def __init_menu(self):
        self.start_menu = tk.Tk()
        self.start_menu.title("XO")
        self.start_menu.geometry("400x400")
        self.start_menu.config(bg="#272927")
        self.start_menu.minsize(width=400, height=400)
        self.start_menu.maxsize(width=400, height=400)

        easy = tk.Button(master=self.start_menu, text="easy", command=self.start_easy_game)
        medium = tk.Button(master=self.start_menu, text="medium", command=self.start_medium_game)
        hard = tk.Button(master=self.start_menu, text="hard", command=self.start_hard_game)

        easy.config(width=20, height=2)
        medium.config(width=20, height=2)
        hard.config(width=20, height=2)

        easy.place(relx=0.5, rely=0.3, anchor=CENTER)
        medium.place(relx=0.5, rely=0.5, anchor=CENTER)
        hard.place(relx=0.5, rely=0.7, anchor=CENTER)

    def run_menu(self):
        self.__init_menu()
        self.start_menu.mainloop()

    def run(self):
        self.__init_window()
        self.__init_buttons()
        self.__init_labels()
        self.__init_images()
        self.__board.clean_board()

        if Random().randint(0, 1) == 0:
            self.__computer.select_square()

        self.__update_gui()
        self.window.mainloop()

    def __clean_window(self):
        for label in self.labels:
            label.destroy()
        self.labels.clear()

        for button in self.buttons:
            button.destroy()
        self.buttons.clear()

    def __print_result(self):
        label = tk.Label(master=self.window, background="#272927")
        if self.__game_status == GameStatus.PLAYER_WIN:
            label.config(image=self.images['win'])
        if self.__game_status == GameStatus.COMPUTER_WIN:
            label.config(image=self.images['lose'])
        if self.__game_status == GameStatus.TIE:
            label.config(image=self.images['tie'])

        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.labels.append(label)

    def __init_restart_button(self):
        restart_button = tk.Button(master=self.window, image=self.images['restart'], width=0, height=0,
                                   background="#272927", foreground="#f5d442", highlightthickness=0, bd=0,
                                   command=self.restart)
        restart_button.place(relx=0.7, rely=0.9, anchor=CENTER)
        self.buttons.append(restart_button)

    def __init_menu_button(self):
        menu_button = tk.Button(master=self.window, image=self.images['menu'], width=0, height=0,
                                background="#272927", foreground="#f5d442", highlightthickness=0, bd=0,
                                command=self.__press_menu_button)
        menu_button.place(relx=0.3, rely=0.9, anchor=CENTER)
        self.buttons.append(menu_button)

    def __init_exit_button(self):
        exit_button = tk.Button(master=self.window, image=self.images['exit'], width=0, height=0,
                                background="#272927", foreground="#f5d442", highlightthickness=0, bd=0,
                                command=sys.exit)
        exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.buttons.append(exit_button)

    def __press_menu_button(self):
        self.window.destroy()
        self.run_menu()

    @staticmethod
    def __check_squares_match(square1, square2, square3):
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.COMPUTER:
            return GameStatus.COMPUTER_WIN
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.PLAYER:
            return GameStatus.PLAYER_WIN
        return GameStatus.CONTINUE

    def restart(self):
        self.__board.clean_board()
        self.window.destroy()
        self.run()
