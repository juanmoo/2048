import random, time

class Board:
    def __init__(self,  size):
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.empty = set((i//self.size, i%self.size) for i in range(self.size * self.size))

        print("initialization done!")
        print("started with", len(self.empty), "empty spaces!")

    def board_str(self):
        board_strings = [  ' | '.join(str(n) if n != 0 else ' ' for n in row) for row in self.board]
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
        settings = { # row_start, row_end, row_step, col_start, col_end, col_step, dr, dc
            "up": [0, self.size, 1, 0, self.size, 1, -1, 0],
            "down":[self.size - 1, -1, -1, 0, self.size, 1, 1, 0],
            "left": [0, self.size, 1, 0, self.size, 1, 0, -1],
            "right": [0, self.size, 1, self.size - 1, -1, -1, 0, 1]
        }

        if dir not in settings:
            Exception("Invalid Direction.")
        
        row_start, row_end, row_step, col_start, col_end, col_step, dr, dc = settings[dir]

        moved = False
        merged = set()
        for _ in range(self.size - 1):
            for r in range(row_start, row_end, row_step):
                new_r = r + dr
                if 0 <= new_r < self.size:
                    for c in range(col_start, col_end, col_step):
                        new_c = c + dc

                        if 0 <= new_c < self.size and self.board[r][c] != 0 and (r, c) not in merged:
                            if (new_r, new_c) in self.empty:
                                assert(self.board[new_r][new_c] == 0)
                                moved = True
                                self.board[new_r][new_c] = self.board[r][c]
                                self.board[r][c] = 0
                                self.empty.add((r, c))
                                self.empty.remove((new_r, new_c))

                            elif self.board[r][c] == self.board[new_r][new_c] and (new_r, new_c) not in merged:
                                moved = True
                                self.board[r][c] = 0
                                self.board[new_r][new_c] *= 2
                                self.empty.add((r, c))
                                merged.add((new_r, new_c))
            if not moved: break
        return moved
                        

    def step(self, dir):
        moved = self.transition(dir)

        if moved:
            self.add_new_piece()
