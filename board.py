from square_status import SquareStatus


class Board:
    def __init__(self):
        self.__board = [[SquareStatus.EMPTY for i in range(3)] for j in range(3)]

    @staticmethod
    def __get_square_symbol(square_status):
        if square_status == SquareStatus.EMPTY:
            return '0'
        elif square_status == SquareStatus.COMPUTER:
            return 'c'
        else:
            return 'p'

    def set_square(self, row, column, square_status):
        self.__board[row - 1][column - 1] = square_status

    def get_square(self, row, column):
        return self.__board[row - 1][column - 1]

    def print_ground(self):
        for i in range(3):
            for j in range(3):
                print(f"{self.__get_square_symbol(self.__board[i][j])}", end=" ")
            print(f"")
