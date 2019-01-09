import operator
UP = (0,1)


class Snake:
    """
    A Snake Object
    """
    def __init__(self,body,direction):
        """
        Initialize the snake with a body and direction
        :param body: an array of tuples containing snakes position during game
        :param direction: UP,DOWN,LEFT, or RIGHT
        """
        self.body = body
        self.direction = direction
        self.length = len(body)
        self.control = {'UP': (0, 1), 'DOWN': (0, -1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
        self.alive = True

    def get_position(self):
        """
        add the head and direction to return the snakes next position
        :return: a tuple which will be appended to the snake's body
        """
        head = self.head()
        return tuple(map(operator.add, head, self.direction))

    def take_step(self):
        """
        add the new position to snake body and pop the last segment off
        :return: nothing, mutates self.body
        """
        position = self.get_position()
        self.body.append(position)
        self.body.pop(0)

    def set_direction(self,direction):
        """
        set the snake's direction value
        :param direction: a direction tuple
        :return: nothing, mutates snake direction value
        """
        self.direction = direction

    def head(self):
        """
        get the current co-ord value of the snake's head
        :return: last element on the body array
        """
        return self.body[-1]

    def check_self_collide(self):
        """
        check if the snake has collided with itself
        :return: set the snake's self.alive property to False, securing his untimely demise
        """
        if len(self.body) != len(set(self.body)):
            self.alive = False


#testuple = tuple(map(lambda x: x%10,snek.position))  # This will give you the coordinate to use for wraparound

