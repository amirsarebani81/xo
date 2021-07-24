from board import Board
from game import Game
from player import Player
from computer import Computer

board = Board()
computer = Computer(board)
player = Player(board)

game = Game()
game.run()
