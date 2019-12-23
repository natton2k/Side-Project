import pygame


class Piece:
    def __init__(self, color: str, pos: tuple, size):
        self.color = color
        self.pos = pos
        self.name = self.getName()
        self.size = size

    def getName(self):
        return str(self.__class__)[24:][:-2]

    def __str__(self):
        return f'{self.color} {self.name}'

    def getMove(self, x_range: list = None, y_range: list = None, L_shape=False):
        if not x_range or not y_range:
            x_range = []
            y_range = []
        moves = []
        if not L_shape:
            for x, y in zip(x_range, y_range):
                if x in range(1, 9) and y in range(1, 9):
                    moves.append((x, y))
        else:
            for x, y in self.LShape():
                if x in range(1, 9) and y in range(1, 9):
                    moves.append((x, y))
        return moves

    def North(self, step):
        x, y = self.pos
        if self.color == 'black':
            y_range = range(y - 1, y - step - 1, -1)
        else:
            y_range = range(y + 1, y + step + 1)
        x_range = [x] * 8
        return x_range, y_range

    def NorthEast(self, step):
        x, y = self.pos
        if self.color == 'black':
            y_range = range(y - 1, y - step - 1, -1)
            x_range = range(x + 1, x + step + 1)
        else:
            y_range = range(y + 1, y + step + 1)
            x_range = range(x - 1, x - step - 1, -1)
        return x_range, y_range

    def East(self, step):
        x, y = self.pos
        if self.color == 'black':
            x_range = range(x + 1, x + step + 1)
        else:
            x_range = range(x - 1, x - step - 1, -1)
        y_range = [y] * len(x_range)
        return x_range, y_range

    def SouthEast(self, step):
        x, y = self.pos
        if self.color == 'black':
            y_range = range(y + 1, y + step + 1)
            x_range = range(x + 1, x + step + 1)
        else:
            y_range = range(y - 1, y - step - 1, -1)
            x_range = range(x - 1, x - step - 1, -1)
        return x_range, y_range

    def South(self, step):
        x, y = self.pos
        if self.color == 'black':
            y_range = range(y + 1, y + step + 1)
        else:
            y_range = range(y - 1, y - step - 1, -1)
        x_range = [x] * len(y_range)
        return x_range, y_range

    def SouthWest(self, step):
        x, y = self.pos
        if self.color == 'black':
            y_range = range(y + 1, y + step + 1)
            x_range = range(x - 1, x - step - 1, -1)
        else:
            y_range = range(y - 1, y - step - 1, -1)
            x_range = range(x + 1, x + step + 1)
        return x_range, y_range

    def West(self, step):
        x, y = self.pos
        if self.color == 'black':
            x_range = range(x - 1, x - step - 1, -1)
        else:
            x_range = range(x + 1, x + step + 1)
        y_range = [y] * len(x_range)
        return x_range, y_range

    def NorthWest(self, step):
        x, y = self.pos
        if self.color == 'black':
            y_range = range(y - 1, y - step - 1, -1)
            x_range = range(x - 1, x - step - 1, -1)
        else:
            y_range = range(y + 1, y + step + 1)
            x_range = range(x + 1, x + step + 1)
        return x_range, y_range

    def LShape(self):
        moves = [
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
            (-2, 1),
            (-1, 2)
        ]
        x, y = self.pos
        for index, value in enumerate(moves):
            next_x, next_y = value
            moves[index] = (x + next_x, y + next_y)
        return moves


class King(Piece):
    def __init__(self, color: str, pos: tuple, size):
        Piece.__init__(self, color, pos, size)
        self.img = pygame.image.load('Pieces/' + color + '_king' + '.png').convert()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.img.set_colorkey((255, 255, 255))
        self.move = {
            'North': 1,
            'NorthEast': 1,
            'East': 1,
            'SouthEast': 1,
            'South': 1,
            'SouthWest': 1,
            'West': 1,
            'NorthWest': 1,
        }
        self.check = {
            'North': 7,
            'NorthEast': 7,
            'East': 7,
            'SouthEast': 7,
            'South': 7,
            'SouthWest': 7,
            'West': 7,
            'NorthWest': 7,
        }


class Queen(Piece):
    def __init__(self, color: str, pos: tuple, size):
        Piece.__init__(self, color, pos, size)
        self.img = pygame.image.load('Pieces/' + color + '_queen' + '.png').convert()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        # remove white background
        self.img.set_colorkey((255, 255, 255))

        self.move = {
            'North': 7,
            'NorthEast': 7,
            'East': 7,
            'SouthEast': 7,
            'South': 7,
            'SouthWest': 7,
            'West': 7,
            'NorthWest': 7,
        }


class Rook(Piece):
    def __init__(self, color: str, pos: tuple, size):
        Piece.__init__(self, color, pos, size)
        self.img = pygame.image.load('Pieces/' + color + '_rook' + '.png').convert()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        # remove white background
        self.img.set_colorkey((255, 255, 255))

        self.move = {
            'North': 7,
            'East': 7,
            'South': 7,
            'West': 7,
        }


class Knight(Piece):
    def __init__(self, color: str, pos: tuple, size):
        Piece.__init__(self, color, pos, size)
        self.img = pygame.image.load('Pieces/' + color + '_knight' + '.png').convert()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        # remove white background
        self.img.set_colorkey((255, 255, 255))
        self.move = {
            'LShape': 0
        }


class Bishop(Piece):
    def __init__(self, color: str, pos: tuple, size):
        Piece.__init__(self, color, pos, size)
        self.img = pygame.image.load('Pieces/' + color + '_bishop' + '.png').convert()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        # remove white background
        self.img.set_colorkey((255, 255, 255))
        self.move = {
            'NorthEast': 7,
            'SouthEast': 7,
            'SouthWest': 7,
            'NorthWest': 7,
        }


class Pawn(Piece):
    def __init__(self, color: str, pos: tuple, size):
        Piece.__init__(self, color, pos, size)
        self.img = pygame.image.load('Pieces/' + color + '_pawn' + '.png').convert()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        # remove white background
        self.img.set_colorkey((255, 255, 255))

        self.first_move = True

    @property
    def move(self):
        if self.first_move:
            return {
                'North': 2,
            }
        else:
            return {
                'North': 1,
            }

    @property
    def eat(self):
        return {
            'NorthEast': 1,
            'NorthWest': 1,
        }


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0))
    knight = Knight('white', (1, 1), 60)
    print(knight.move)
    for direction, step in knight.move.items():
        if direction == 'LShape':
            for x in knight.getMove(L_shape=True):
                print(x)
        else:
            f = getattr(knight, direction)
            range_x, range_y = f(step)
            print(f.__name__)
            for x in knight.getMove(range_x, range_y):
                print(x)