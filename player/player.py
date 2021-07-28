from constants.square_status import SquareStatus


class Player:
    def __init__(self, board):
        self.__board = board

    @staticmethod
    def is_selecting_possible(square):
        return square == SquareStatus.EMPTY

    def select_square(self):
        try:
            row, column = int(input("Enter row: ")), int(input("Enter column: "))
            if self.is_selecting_possible(self.__board.get_square(row, column)):
                self.mark_square(row, column)
            else:
                print("This square selected before!")
                self.select_square()
        except ValueError:
            print("Enter a valid integer in range 1 to 3")
            self.select_square()
        except IndexError:
            print("Invalid input!")
            self.select_square()

    def mark_square(self, row, column):
        self.__board.set_square(row, column, SquareStatus.PLAYER)

    def get_board(self):
        return self.__board
