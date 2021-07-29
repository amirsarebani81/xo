from tkinter.constants import ANCHOR, CENTER
from board.board import Board
import tkinter as tk
from player.computer import Computer
from player.player import Player
from constants.square_status import SquareStatus
from constants.game_status import GameStatus
from random import Random


class Game:
    def __init__(self, game_level):
        self.__init_window()
        self.labels = list()
        self.buttons = list()
        self.__board = Board()
        self.__computer = Computer(self.__board, game_level)
        self.__player = Player(self.__board)
        self.__game_status = GameStatus.CONTINUE

        self.__init_buttons()

    def __init_window(self):
        self.window = tk.Tk()
        self.window.title("XO")
        self.window.geometry("400x400")
        self.window.config(bg="#272927")
        self.window.minsize(width=400, height=400)
        self.window.maxsize(width=400, height=400)

    def __init_buttons(self):
        self.buttons.append(tk.Button(master=self.window, text=1, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_1))
        self.buttons.append(tk.Button(master=self.window, text=2, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_2))
        self.buttons.append(tk.Button(master=self.window, text=3, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_3))
        self.buttons.append(tk.Button(master=self.window, text=4, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_4))
        self.buttons.append(tk.Button(master=self.window, text=5, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_5))
        self.buttons.append(tk.Button(master=self.window, text=6, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_6))
        self.buttons.append(tk.Button(master=self.window, text=7, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_7))
        self.buttons.append(tk.Button(master=self.window, text=8, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_8))
        self.buttons.append(tk.Button(master=self.window, text=9, width=5, height=4, background="#272927", highlightthickness=0, bd=0, command=self.__press_9))

        self.buttons[0].place(relx=0.25, rely=0.25, anchor=CENTER)
        self.buttons[1].place(relx=0.5, rely=0.25, anchor=CENTER)
        self.buttons[2].place(relx=0.75, rely=0.25, anchor=CENTER)
        self.buttons[3].place(relx=0.25, rely=0.5, anchor=CENTER)
        self.buttons[4].place(relx=0.5, rely=0.5, anchor=CENTER)
        self.buttons[5].place(relx=0.75, rely=0.5, anchor=CENTER)
        self.buttons[6].place(relx=0.25, rely=0.75, anchor=CENTER)
        self.buttons[7].place(relx=0.5, rely=0.75, anchor=CENTER)
        self.buttons[8].place(relx=0.75, rely=0.75, anchor=CENTER)

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
        self.__board.print_board()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__clean_window()
            self.__print_result()
            self.__init_restart_button()
            self.window.mainloop()

        self.__computer.select_square()
        self.__board.print_board()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__clean_window()
            self.__print_result()
            self.__init_restart_button()
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
        cross = tk.PhotoImage(file="images/cross.png")
        circle = tk.PhotoImage(file="images/circle.png")
        cross = cross.subsample(30)
        circle = circle.subsample(18)

        for row in range(1, 4):
            for column in range(1, 4):
                if self.__board.get_square(row, column) != SquareStatus.EMPTY:
                    self.__delete_button((row - 1) * 3 + column)
                    if self.__board.get_square(row, column) == SquareStatus.COMPUTER:
                        label = tk.Label(master=self.window, image=cross, background="#272927")
                        label.place(relx=column*0.25, rely=row*0.25, anchor=CENTER)
                        self.labels.append(label)
                    else:
                        label = tk.Label(master=self.window, image=circle, background="#272927")
                        label.place(relx=column*0.25, rely=row*0.25, anchor=CENTER)
                        self.labels.append(label)
        self.window.mainloop()

    def __delete_button(self, button_id):
        self.buttons[button_id - 1].destroy()

    def run(self):
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
        label = tk.Label()
        if self.__game_status == GameStatus.PLAYER_WIN:
            label.config(text="player win")
        if self.__game_status == GameStatus.COMPUTER_WIN:
            label.config(text="computer win")
        if self.__game_status == GameStatus.TIE:
            label.config(text="tie")

        label.place(x=0, y=0)
        self.labels.append(label)

    def __init_restart_button(self):
        restart_button = tk.Button(text="restart", command=self.restart)
        restart_button.place(x=100, y=100)
        self.buttons.append(restart_button)

    @staticmethod
    def __check_squares_match(square1, square2, square3):
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.COMPUTER:
            return GameStatus.COMPUTER_WIN
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.PLAYER:
            return GameStatus.PLAYER_WIN
        return GameStatus.CONTINUE

    def restart(self):
        self.__board.clean_board()
        self.__clean_window()
        self.__init_buttons()
        self.run()