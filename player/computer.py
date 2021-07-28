from constants.square_status import SquareStatus
from random import Random
from player.player import Player


class Computer(Player):
    def __init__(self, board):
        super().__init__(board)

    def mark_square(self, row, column):
        super().get_board().set_square(row, column, SquareStatus.COMPUTER)

    def __select_horizontal(self):
        for row in range(1, 4):
            squares = super().get_board().get_row(row)
            if self.__is_player_or_computer(squares[0], squares[1]) and super().is_selecting_possible(squares[2]):
                self.mark_square(row, 3)
                return True
            if self.__is_player_or_computer(squares[0], squares[2]) and super().is_selecting_possible(squares[1]):
                self.mark_square(row, 2)
                return True
            if self.__is_player_or_computer(squares[1], squares[2]) and super().is_selecting_possible(squares[0]):
                self.mark_square(row, 1)
                return True
        return False

    def __select_vertical(self):
        for column in range(1, 4):
            squares = super().get_board().get_column(column)
            if self.__is_player_or_computer(squares[0], squares[1]) and super().is_selecting_possible(squares[2]):
                self.mark_square(3, column)
                return True
            if self.__is_player_or_computer(squares[0], squares[2]) and super().is_selecting_possible(squares[1]):
                self.mark_square(2, column)
                return True
            if self.__is_player_or_computer(squares[1], squares[2]) and super().is_selecting_possible(squares[0]):
                self.mark_square(1, column)
                return True
        return False

    def __select_diagonal(self):
        squares = super().get_board().get_left_to_right_diagonal()
        if self.__is_player_or_computer(squares[0], squares[1]) and super().is_selecting_possible(squares[2]):
            self.mark_square(3, 3)
            return True
        if self.__is_player_or_computer(squares[0], squares[2]) and super().is_selecting_possible(squares[1]):
            self.mark_square(2, 2)
            return True
        if self.__is_player_or_computer(squares[1], squares[2]) and super().is_selecting_possible(squares[0]):
            self.mark_square(1, 1)
            return True

        squares = super().get_board().get_right_to_left_diagonal()
        if self.__is_player_or_computer(squares[0], squares[1]) and super().is_selecting_possible(squares[2]):
            self.mark_square(3, 1)
            return True
        if self.__is_player_or_computer(squares[0], squares[2]) and super().is_selecting_possible(squares[1]):
            self.mark_square(2, 2)
            return True
        if self.__is_player_or_computer(squares[1], squares[2]) and super().is_selecting_possible(squares[0]):
            self.mark_square(1, 3)
            return True
        return False

    def __select_random(self):
        while True:
            row, column = Random().randint(1, 3), Random().randint(1, 3)
            if super().is_selecting_possible(super().get_board().get_square(row, column)):
                self.mark_square(row, column)
                return True

    def select_square(self):
        is_selected = self.__select_horizontal()
        if not is_selected:
            is_selected = self.__select_vertical()
        if not is_selected:
            is_selected = self.__select_diagonal()
        if not is_selected:
            self.__select_random()

    @staticmethod
    def __is_player_or_computer(square1, square2):
        if square1 == square2 == SquareStatus.COMPUTER:
            return True
        elif square1 == square2 == SquareStatus.PLAYER:
            return True
        else:
            return False
