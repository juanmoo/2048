import random, pygame, time
from pygame.locals import *

class Board:
    def __init__(self,  size):
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.empty = set((i//self.size, i%self.size) for i in range(self.size * self.size))

    def board_str(self):
        board_strings = [  ' | '.join(str(n) for n in row) for row in self.board]
        board_string = ('\n' + '-' * (self.size * 4 - 3) + '\n').join(board_strings)
        return board_string

    def add_new_piece(self):
        # Select empty position at random
        if len(self.empty) == 0:
            raise Exception('No more spaces left in board.')
        p = random.sample(self.empty, 1)[0]
        self.empty.remove(p)
        r, c = p

        assert(self.board[r][c] == 0)

        if random.random() < 0.9:
            val = 2
        else:
            val = 4

        self.board[r][c] = val

        return True

    def transition(self, dir):
        # move tiles according to direction
        moved = False
        for _ in range(self.size - 1):
            count = 0
            if dir == 'up':
                for r in range(self.size):
                    for c in range(self.size):
                        if ( (r - 1) >= 0 and self.board[r][c] != 0 ):
                            # Above Cell is empty
                            if (r - 1, c) in self.empty:
                                count += 1
                                self.board[r - 1][c] = self.board[r][c]
                                self.board[r][c] = 0
                                self.empty.remove((r - 1, c))
                                self.empty.add((r, c))
                            
                            elif self.board[r - 1][c] == self.board[r][c]:
                                count += 1
                                self.board[r - 1][c] *= 2
                                self.board[r][c] = 0
                                self.empty.add((r, c))

            elif dir == 'down':
                for r in range(self.size - 1, -1, -1):
                    for c in range(self.size):
                        if ( (r + 1) < self.size and self.board[r][c] != 0 ):

                            # Below Cell is empty
                            if (r + 1, c) in self.empty:
                                count += 1
                                self.board[r + 1][c] = self.board[r][c]
                                self.board[r][c] = 0
                                self.empty.remove((r + 1, c))
                                self.empty.add((r, c))
                            
                            elif self.board[r + 1][c] == self.board[r][c]:
                                count += 1
                                self.board[r + 1][c] *= 2
                                self.board[r][c] = 0
                                self.empty.add((r, c))

            elif dir == 'left':
                for c in range(self.size):
                    for r in range(self.size):
                        if ( (c - 1) >= 0 and self.board[r][c] != 0 ):

                            # Cell to the left is empty
                            if (r, c - 1) in self.empty:
                                count += 1
                                self.board[r][c - 1] = self.board[r][c]
                                self.board[r][c] = 0
                                self.empty.remove((r, c - 1))
                                self.empty.add((r, c))
                            
                            elif self.board[r][c - 1] == self.board[r][c]:
                                count += 1
                                self.board[r][c - 1] *= 2
                                self.board[r][c] = 0
                                self.empty.add((r, c))

            elif dir == 'right':
                for c in range(self.size - 1, -1, -1):
                    for r in range(self.size):
                        if ( (c + 1) < self.size and self.board[r][c] != 0 ):
                            # Cell to the right is empty
                            if (r, c + 1) in self.empty:
                                count += 1
                                self.board[r][c + 1] = self.board[r][c]
                                self.board[r][c] = 0
                                self.empty.remove((r, c + 1))
                                self.empty.add((r, c))

                            elif self.board[r][c + 1] == self.board[r][c]:
                                count += 1
                                self.board[r][c + 1] *= 2
                                self.board[r][c] = 0
                                self.empty.add((r, c))
            else:
                raise Exception("Invalid Direction")

            if count == 0:
                break
            else:
                moved = True
        return moved

    def step(self, dir):
        moved = self.transition(dir)

        if moved:
            self.add_new_piece()
