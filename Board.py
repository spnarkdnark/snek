class Board:
    """
    A Class representing the 'map' that snake is played on.
    """
    def __init__(self,height,width):
        """
        initialize the board object
        :param height: height of the board
        :param width: width of the board
        """
        self.height = height
        self.width = width
        self.state = self.empty_state()  # self.state is initially set to a fully empty 2D array

    def empty_state(self):
        """
        called on __init__ to populate height x width array with NONE values before changing state
        :return: an empty height x width array
        """
        return [[None]*self.width for i in range(self.height)]

    def next_state(self, body, head, apple):
        """
        update the state of the board with location of body head and apple
        :param body: array of tuple values representing the snake's body
        :param head: single length array with the head's location tuple
        :param apple: single length array with apple's location tuple
        :return: an updated board state based on player input
        """
        for i in range(self.height):
            for j in range(self.width):
                if (i,j) in body:
                    self.state[i][j] = 'BODY'
                elif (i,j) in head:
                    self.state[i][j] = 'HEAD'
                elif (i,j) in apple:
                    self.state[i][j] = 'APPLE'
                else:
                    self.state[i][j] = None

    def render(self):
        """
        render the board state to the terminal
        :return: board state printed to the terminal
        """
        states = {'HEAD': '  X  ', 'BODY': '  O  ', 'APPLE': '  A  '}  # Dictionary of possible states
        for i in range(self.height):  # Loop through each row in self.state
            row = []  # Init empty printable row
            for j in range(self.width):  # Loop through each value in row
                if self.state[i][j] in states:  # If it is a head, body or apple (search states dictionary)
                    row.append(states[self.state[i][j]])  # append its symbol to row
                else:  # Or append an empty symbol
                    row.append("   ")
            print(''.join(row))  # Pretty print each row









board1 = Board(10,10)
board1.next_state([(1,1),(2,2),(3,3),(4,4)],[(5,5)],[(6,6)])
board1.render()