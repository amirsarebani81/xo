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
        self.__window = tk.Tk()
        if self.__computer.get_game_level() == GameLevel.EASY:
            title = "Easy mode"
        if self.__computer.get_game_level() == GameLevel.MEDIUM:
            title = "Medium mode"
        if self.__computer.get_game_level() == GameLevel.HARD:
            title = "Hard mode"
        self.__window.title(title)
        self.__window.geometry("400x400")
        self.__window.config(bg="#272927")
        self.__window.minsize(width=300, height=300)
        self.__window.maxsize(width=500, height=500)

    def __init_buttons(self):
        self.__buttons = list()
        self.__buttons.append(
            tk.Button(master=self.__window, text=1, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_1))
        self.__buttons.append(
            tk.Button(master=self.__window, text=2, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_2))
        self.__buttons.append(
            tk.Button(master=self.__window, text=3, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_3))
        self.__buttons.append(
            tk.Button(master=self.__window, text=4, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_4))
        self.__buttons.append(
            tk.Button(master=self.__window, text=5, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_5))
        self.__buttons.append(
            tk.Button(master=self.__window, text=6, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_6))
        self.__buttons.append(
            tk.Button(master=self.__window, text=7, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_7))
        self.__buttons.append(
            tk.Button(master=self.__window, text=8, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_8))
        self.__buttons.append(
            tk.Button(master=self.__window, text=9, width=5, height=4, background="#272927", highlightthickness=0, bd=0,
                      command=self.__press_9))

        self.__buttons[0].place(relx=0.25, rely=0.25, anchor=CENTER)
        self.__buttons[1].place(relx=0.5, rely=0.25, anchor=CENTER)
        self.__buttons[2].place(relx=0.75, rely=0.25, anchor=CENTER)
        self.__buttons[3].place(relx=0.25, rely=0.5, anchor=CENTER)
        self.__buttons[4].place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__buttons[5].place(relx=0.75, rely=0.5, anchor=CENTER)
        self.__buttons[6].place(relx=0.25, rely=0.75, anchor=CENTER)
        self.__buttons[7].place(relx=0.5, rely=0.75, anchor=CENTER)
        self.__buttons[8].place(relx=0.75, rely=0.75, anchor=CENTER)

    def __init_labels(self):
        self.__labels = list()

    def __init_images(self):
        self.__images = dict()
        self.__images['cross'] = tk.PhotoImage(file="images/cross.png")
        self.__images['circle'] = tk.PhotoImage(file="images/circle.png")
        self.__images['win'] = tk.PhotoImage(file="images/win.png")
        self.__images['lose'] = tk.PhotoImage(file="images/lose.png")
        self.__images['tie'] = tk.PhotoImage(file="images/tie.png")
        self.__images['restart'] = tk.PhotoImage(file="images/restart.png")
        self.__images['menu'] = tk.PhotoImage(file="images/menu.png")
        self.__images['exit'] = tk.PhotoImage(file="images/exit.png")

        self.__images['cross'] = self.__images['cross'].subsample(30)
        self.__images['circle'] = self.__images['circle'].subsample(18)
        self.__images['win'] = self.__images['win'].subsample(5)
        self.__images['lose'] = self.__images['lose'].subsample(5)
        self.__images['tie'] = self.__images['tie'].subsample(2)
        self.__images['restart'] = self.__images['restart'].subsample(15)
        self.__images['menu'] = self.__images['menu'].subsample(15)
        self.__images['exit'] = self.__images['exit'].subsample(60)

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
        self.__player.mark_square(row, column)
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__clean_window()
            self.__print_result()
            self.__init_restart_button()
            self.__init_menu_button()
            self.__init_exit_button()
            self.__window.mainloop()

        self.__computer.select_square()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__clean_window()
            self.__print_result()
            self.__init_restart_button()
            self.__init_menu_button()
            self.__init_exit_button()
            self.__window.mainloop()

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
                        label = tk.Label(master=self.__window, image=self.__images['cross'], background="#272927")
                        label.place(relx=column * 0.25, rely=row * 0.25, anchor=CENTER)
                        self.__labels.append(label)
                    else:
                        label = tk.Label(master=self.__window, image=self.__images['circle'], background="#272927")
                        label.place(relx=column * 0.25, rely=row * 0.25, anchor=CENTER)
                        self.__labels.append(label)
        self.__window.mainloop()

    def __delete_button(self, button_id):
        self.__buttons[button_id - 1].destroy()

    def __start_hard_game(self):
        self.__start_menu.destroy()
        self.__computer.set_game_level(GameLevel.HARD)
        self.__run()

    def __start_medium_game(self):
        self.__start_menu.destroy()
        self.__computer.set_game_level(GameLevel.MEDIUM)
        self.__run()

    def __start_easy_game(self):
        self.__start_menu.destroy()
        self.__computer.set_game_level(GameLevel.EASY)
        self.__run()

    def __init_menu(self):
        self.__start_menu = tk.Tk()
        self.__start_menu.title("XO")
        self.__start_menu.geometry("400x400")
        self.__start_menu.config(bg="#272927")
        self.__start_menu.minsize(width=200, height=250)
        self.__start_menu.maxsize(width=400, height=400)

        easy = tk.Button(master=self.__start_menu, text="easy", command=self.__start_easy_game)
        medium = tk.Button(master=self.__start_menu, text="medium", command=self.__start_medium_game)
        hard = tk.Button(master=self.__start_menu, text="hard", command=self.__start_hard_game)

        easy.config(width=20, height=2)
        medium.config(width=20, height=2)
        hard.config(width=20, height=2)

        easy.place(relx=0.5, rely=0.3, anchor=CENTER)
        medium.place(relx=0.5, rely=0.5, anchor=CENTER)
        hard.place(relx=0.5, rely=0.7, anchor=CENTER)

    def run_menu(self):
        self.__init_menu()
        self.__start_menu.mainloop()

    def __run(self):
        self.__init_window()
        self.__init_buttons()
        self.__init_labels()
        self.__init_images()
        self.__board.clean_board()

        if Random().randint(0, 1) == 0:
            self.__computer.select_square()

        self.__update_gui()
        self.__window.mainloop()

    def __clean_window(self):
        for label in self.__labels:
            label.destroy()
        self.__labels.clear()

        for button in self.__buttons:
            button.destroy()
        self.__buttons.clear()

    def __print_result(self):
        label = tk.Label(master=self.__window, background="#272927")
        if self.__game_status == GameStatus.PLAYER_WIN:
            label.config(image=self.__images['win'])
        if self.__game_status == GameStatus.COMPUTER_WIN:
            label.config(image=self.__images['lose'])
        if self.__game_status == GameStatus.TIE:
            label.config(image=self.__images['tie'])

        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__labels.append(label)

    def __init_restart_button(self):
        restart_button = tk.Button(master=self.__window, image=self.__images['restart'], width=0, height=0,
                                   background="#272927", foreground="#f5d442", highlightthickness=0, bd=0,
                                   command=self.__restart)
        restart_button.place(relx=0.7, rely=0.9, anchor=CENTER)
        self.__buttons.append(restart_button)

    def __init_menu_button(self):
        menu_button = tk.Button(master=self.__window, image=self.__images['menu'], width=0, height=0,
                                background="#272927", foreground="#f5d442", highlightthickness=0, bd=0,
                                command=self.__press_menu_button)
        menu_button.place(relx=0.3, rely=0.9, anchor=CENTER)
        self.__buttons.append(menu_button)

    def __init_exit_button(self):
        exit_button = tk.Button(master=self.__window, image=self.__images['exit'], width=0, height=0,
                                background="#272927", foreground="#f5d442", highlightthickness=0, bd=0,
                                command=sys.exit)
        exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.__buttons.append(exit_button)

    def __press_menu_button(self):
        self.__window.destroy()
        self.run_menu()

    @staticmethod
    def __check_squares_match(square1, square2, square3):
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.COMPUTER:
            return GameStatus.COMPUTER_WIN
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.PLAYER:
            return GameStatus.PLAYER_WIN
        return GameStatus.CONTINUE

    def __restart(self):
        self.__board.clean_board()
        self.__window.destroy()
        self.__run()
