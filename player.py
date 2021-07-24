from square_status import SquareStatus


class Player:
    def __init__(self, board):
        self.__board = board

    @staticmethod
    def is_selecting_possible(square):
        return square == SquareStatus.EMPTY

    def select_square(self):
        row, column = int(input("Enter row: ")), int(input("Enter column: "))
        if self.is_selecting_possible(self.__board.get_square(row, column)):
            self.mark_square(row, column)
        else:
            self.select_square()

    def mark_square(self, row, column):
        self.__board.set_square(row, column, SquareStatus.PLAYER)

    def get_board(self):
        return self.__board
