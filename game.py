from board import Board
from computer import Computer
from player import Player
from square_status import SquareStatus
from game_status import GameStatus
from random import Random


class Game:
    def __init__(self):
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

    def run(self):
        if Random().randint(0, 1) == 0:
            first_turn = Player(self.__board)
            second_turn = Computer(self.__board)
        else:
            first_turn = Computer(self.__board)
            second_turn = Player(self.__board)

        while self.__game_status == GameStatus.CONTINUE:
            first_turn.select_square()
            self.__board.print_ground()
            self.__check_game_status()

            if self.__game_status != GameStatus.CONTINUE:
                break

            second_turn.select_square()
            self.__board.print_ground()
            self.__check_game_status()

        self.__print_result()

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
        if square1 == square2 == square3 == SquareStatus.COMPUTER:
            return GameStatus.COMPUTER_WIN
        if square1 == square2 == square3 == SquareStatus.PLAYER:
            return GameStatus.PLAYER_WIN
        return GameStatus.CONTINUE
