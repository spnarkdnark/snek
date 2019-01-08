import operator

UP = (0,1)
DOWN = (0,-1)
RIGHT = (1,0)
LEFT = (-1,0)




class Apple:
    """
    An Apple Object
    """
    def __init__(self,position):
        """
        Initialize the Apple Object
        :param position: tuple co-ord of the apple's position
        """
        self.position = position


class Board:
    """
    The Game Board Object
    """

    def __init(self,size):



class Game:
    """
    The Game OBject - Controlling basically everything
    """
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.snake = Snake([(5,5),(6,5),(7,5),(7,6)],UP)
        self.board = self.empty_board()
        self.update_board()

    def empty_board(self):
        return [['   ']*self.width for i in range(1,self.height)]

    def update_board(self):
        for y in range(self.height-1):
            for x in range(self.width-1):
                if(x,y) in self.snake.body:
                    self.board[y][x] = ' O '
                else:
                    self.board[y][x] = '   '

    def render(self):
        for row in self.board:
            print("|" + ''.join(row) + "|")

    def make_move(self):
        available_moves = {'W': UP, 'A': LEFT, 'S': DOWN, 'D': RIGHT}
        player_move = input('').upper()
        current_pos = self.snake.get_position()
        if player_move in available_moves:
            for i in available_moves:
                if player_move == i:
                    self.snake.set_direction(available_moves[player_move])
                    self.snake.take_step(current_pos)
                    self.update_board()


