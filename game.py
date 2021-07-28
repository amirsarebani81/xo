from board import Board
import tkinter as tk
from computer import Computer
from player import Player
from square_status import SquareStatus
from game_status import GameStatus
from random import Random
import sys


class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.labels = list()
        self.button9 = tk.Button(master=self.window, text="9", width=2, height=2, command=self.press_9)
        self.button8 = tk.Button(master=self.window, text="8", width=2, height=2, command=self.press_8)
        self.button7 = tk.Button(master=self.window, text="7", width=2, height=2, command=self.press_7)
        self.button6 = tk.Button(master=self.window, text="6", width=2, height=2, command=self.press_6)
        self.button5 = tk.Button(master=self.window, text="5", width=2, height=2, command=self.press_5)
        self.button4 = tk.Button(master=self.window, text="4", width=2, height=2, command=self.press_4)
        self.button3 = tk.Button(master=self.window, text="3", width=2, height=2, command=self.press_3)
        self.button2 = tk.Button(master=self.window, text="2", width=2, height=2, command=self.press_2)
        self.button1 = tk.Button(master=self.window, text="1", width=2, height=2, command=self.press_1)
        self.__board = Board()
        self.__computer = Computer(self.__board)
        self.__player = Player(self.__board)
        self.__game_status = GameStatus.CONTINUE

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

    def do_selects(self, row, column):
        self.__player.mark_square(row, column)
        self.__board.print_board()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__print_result()
            sys.exit(0)

        self.__computer.select_square()
        self.__board.print_board()
        self.__check_game_status()

        if self.__game_status != GameStatus.CONTINUE:
            self.__print_result()
            sys.exit(0)

    def press_1(self):
        self.do_selects(1, 1)
        self.update_gui()

    def press_2(self):
        self.do_selects(1, 2)
        self.update_gui()

    def press_3(self):
        self.do_selects(1, 3)
        self.update_gui()

    def press_4(self):
        self.do_selects(2, 1)
        self.update_gui()

    def press_5(self):
        self.do_selects(2, 2)
        self.update_gui()

    def press_6(self):
        self.do_selects(2, 3)
        self.update_gui()

    def press_7(self):
        self.do_selects(3, 1)
        self.update_gui()

    def press_8(self):
        self.do_selects(3, 2)
        self.update_gui()

    def press_9(self):
        self.do_selects(3, 3)
        self.update_gui()

    def update_gui(self):
        cross = tk.PhotoImage(file="cross.png")
        cross = cross.subsample(50)
        circle = tk.PhotoImage(file="circle.png")
        circle = circle.subsample(50)
        for row in range(1, 4):
            for column in range(1, 4):
                if self.__board.get_square(row, column) != SquareStatus.EMPTY:
                    self.delete_button((row - 1) * 3 + column)
                    if self.__board.get_square(row, column) == SquareStatus.COMPUTER:
                        print("cross")
                        label = tk.Label(master=self.window, image=cross)
                        label.place(x=(column-1)*50, y=(row-1)*50)
                        self.labels.append(label)
                    else:
                        print("circle")
                        label = tk.Label(master=self.window, image=circle)
                        label.place(x=(column-1)*50, y=(row-1)*50)
                        self.labels.append(label)
        self.window.mainloop()

    def delete_button(self, button_id):
        if button_id == 1:
            self.button1.destroy()
        if button_id == 2:
            self.button2.destroy()
        if button_id == 3:
            self.button3.destroy()
        if button_id == 4:
            self.button4.destroy()
        if button_id == 5:
            self.button5.destroy()
        if button_id == 6:
            self.button6.destroy()
        if button_id == 7:
            self.button7.destroy()
        if button_id == 8:
            self.button8.destroy()
        if button_id == 9:
            self.button9.destroy()

    def run(self):
        if Random().randint(0, 1) == 0:
            self.__computer.select_square()

        self.button1.place(x=0, y=0)
        self.button2.place(x=50, y=0)
        self.button3.place(x=100, y=0)
        self.button4.place(x=0, y=50)
        self.button5.place(x=50, y=50)
        self.button6.place(x=100, y=50)
        self.button7.place(x=0, y=100)
        self.button8.place(x=50, y=100)
        self.button9.place(x=100, y=100)

        self.update_gui()
        self.window.mainloop()

    def update_status(self):
        print("updated")
        self.window.update()

    def __print_result(self):
        print('*****************************************')
        if self.__game_status == GameStatus.TIE:
            print("tie!")
        elif self.__game_status == GameStatus.PLAYER_WIN:
            print("player win!")
        elif self.__game_status == GameStatus.COMPUTER_WIN:
            print("computer win!")

    @staticmethod
    def __check_squares_match(square1, square2, square3):
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.COMPUTER:
            return GameStatus.COMPUTER_WIN
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.PLAYER:
            return GameStatus.PLAYER_WIN
        return GameStatus.CONTINUE
