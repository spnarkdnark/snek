from Snake import Snake
from Board import Board

class Game:
    """
    The Game Object
    """

    def __init__(self):
        self.control = {'W': (-1,0), 'S': (1,0), 'A': (0, -1), 'D': (0, 1)}
        self.snake = Snake([(5, 5), (6, 5), (7, 5), (7, 6)], (0, 1))
        self.board = Board(10, 10)

    def make_move(self):
        player_input = input().upper()
        head = self.snake.head()
        position = self.snake.get_position()
        print(game1.snake.body, head, game1.snake.direction, position)
        if player_input in self.control:
            self.snake.set_direction(self.control[player_input])
            self.snake.take_step()
            self.board.next_state(self.snake.body,head)
        else:
            print('not a valid move!')
        print(game1.snake.body, head, game1.snake.direction, position)
game1 = Game()
game1.board.next_state(game1.snake.body,[game1.snake.head])

def game_loop():

    game1.board.next_state(game1.snake.body, [game1.snake.head])
    position = game1.snake.get_position()
    head = game1.snake.head()
    print(game1.snake.body,head,game1.snake.direction,position)
    while True:


        game1.make_move()


game_loop()