from random import Random
from constants.game_level import GameLevel
from constants.game_status import GameStatus
from constants.square_status import SquareStatus
from player.player import Player


class Computer(Player):
    def __init__(self, board):
        super().__init__(board)
        self.__game_level = GameLevel.MEDIUM

    def set_game_level(self, game_level):
        self.__game_level = game_level

    def get_game_level(self):
        return self.__game_level

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

    def __select_square_medium(self):
        is_selected = self.__select_horizontal()
        if not is_selected:
            is_selected = self.__select_vertical()
        if not is_selected:
            is_selected = self.__select_diagonal()
        if not is_selected:
            self.__select_random()

    def __select_square_hard(self):
        best = -10
        move = [-1, -1]

        for i in range(1, 4):
            for j in range(1, 4):
                if self.get_board().get_square(i, j) == SquareStatus.EMPTY:
                    self.mark_square(i, j)
                    value = self.__minimax(self.get_board(), False)
                    if value > best:
                        best = value
                        move = [i, j]
                    self.get_board().set_square(i, j, SquareStatus.EMPTY)

        self.mark_square(move[0], move[1])

    def __select_square_easy(self):
        self.__select_random()

    def __minimax(self, board, return_max):
        game_status = self.__check_game_status()
        if game_status == GameStatus.TIE:
            return 0
        if game_status == GameStatus.COMPUTER_WIN:
            return 1
        if game_status == GameStatus.PLAYER_WIN:
            return -1

        if return_max:
            result = -10
        else:
            result = 10

        for i in range(1, 4):
            for j in range(1, 4):
                if board.get_square(i, j) == SquareStatus.EMPTY and return_max:
                    board.set_square(i, j, SquareStatus.COMPUTER)
                    result = max(result, self.__minimax(board, not return_max))
                    board.set_square(i, j, SquareStatus.EMPTY)
                if board.get_square(i, j) == SquareStatus.EMPTY and not return_max:
                    board.set_square(i, j, SquareStatus.PLAYER)
                    result = min(result, self.__minimax(board, not return_max))
                    board.set_square(i, j, SquareStatus.EMPTY)
        return result

    @staticmethod
    def __check_squares_match(square1, square2, square3):
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.COMPUTER:
            return GameStatus.COMPUTER_WIN
        if square1 == square2 and square1 == square3 and square1 == SquareStatus.PLAYER:
            return GameStatus.PLAYER_WIN
        return GameStatus.CONTINUE

    def __check_game_status(self):
        for row in range(1, 4):
            squares = self.get_board().get_row(row)
            game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
            if game_status != GameStatus.CONTINUE:
                return game_status

        for column in range(1, 4):
            squares = self.get_board().get_column(column)
            game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
            if game_status != GameStatus.CONTINUE:
                return game_status

        squares = self.get_board().get_left_to_right_diagonal()
        game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
        if game_status != GameStatus.CONTINUE:
            return game_status

        squares = self.get_board().get_right_to_left_diagonal()
        game_status = self.__check_squares_match(squares[0], squares[1], squares[2])
        if game_status != GameStatus.CONTINUE:
            return game_status

        if self.get_board().is_board_full():
            return GameStatus.TIE
        return GameStatus.CONTINUE

    def select_square(self):
        if self.__game_level == GameLevel.EASY:
            self.__select_square_easy()
        if self.__game_level == GameLevel.MEDIUM:
            self.__select_square_medium()
        if self.__game_level == GameLevel.HARD:
            self.__select_square_hard()

    @staticmethod
    def __is_player_or_computer(square1, square2):
        if square1 == square2 == SquareStatus.COMPUTER:
            return True
        elif square1 == square2 == SquareStatus.PLAYER:
            return True
        else:
            return False
