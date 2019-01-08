from Snake import Snake
from Board import Board

class Game:
    """
    The Game Object
    """

    def __init__(self):
        self.control = {'W': (0, 1), 'S': (0, -1), 'A': (-1, 0), 'D': (1, 0)}
        self.snake = Snake([(5, 5), (6, 5), (7, 5), (7, 6)], (0, 1))
        self.board = Board(10, 10)

    def make_move(self):
        player_input = input().upper()
        if player_input in self.control:
            self.snake.set_direction(self.control[player_input])
            self.snake.take_step()
            self.board.next_state(self.snake.body,self.snake.head)

game1 = Game()
game1.board.next_state(game1.snake.body,[game1.snake.head])
print(game1.board.state)
game1.make_move()
print(game1.board.state)