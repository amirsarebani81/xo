from square_status import SquareStatus


class Board:
    def __init__(self):
        self.__board = [[SquareStatus.EMPTY for _ in range(3)] for _ in range(3)]

    @staticmethod
    def __get_square_symbol(square_status):
        if square_status == SquareStatus.EMPTY:
            return '-'
        elif square_status == SquareStatus.COMPUTER:
            return 'c'
        else:
            return 'p'

    def set_square(self, row, column, square_status):
        self.__board[row - 1][column - 1] = square_status

    def get_square(self, row, column):
        return self.__board[row - 1][column - 1]

    def print_ground(self):
        print('_________________________________________')
        for i in range(3):
            for j in range(3):
                print(self.__get_square_symbol(self.__board[i][j]), end=" ")
            print("")
        print('_________________________________________')

    def get_row(self, row):
        return self.__board[row - 1]

    def get_column(self, column):
        column = [self.__board[0][column - 1], self.__board[1][column - 1], self.__board[2][column - 1]]
        return column

    def get_right_to_left_diagonal(self):
        diagonal = [self.__board[0][2], self.__board[1][1], self.__board[2][0]]
        return diagonal

    def get_left_to_right_diagonal(self):
        diagonal = [self.__board[0][0], self.__board[1][1], self.__board[2][2]]
        return diagonal

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == SquareStatus.EMPTY:
                    return False
        return True
