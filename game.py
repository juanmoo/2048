import random, pygame, time 
from pygame.locals import *
from board import *

class Game:
    def __init__(self, size=4):
        self.board = Board(size)
        self.board.add_new_piece()

    def print_board(self):
        bstr = self.board.board_str()
        print(bstr + "\n" * 2)

    def start(self):

        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Pygame Keyboard Test')
        pygame.mouse.set_visible(0)

        self.print_board()

        while True:
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    if (event.key == pygame.K_UP):
                        self.board.step("up")
                        self.print_board()
                        time.sleep(0.2)
                    elif(event.key == pygame.K_DOWN):
                        self.board.step("down")
                        self.print_board()
                        time.sleep(0.2)
                    elif(event.key == pygame.K_LEFT):
                        self.board.step("left")
                        self.print_board()
                        time.sleep(0.2)
                    elif(event.key == pygame.K_RIGHT):
                        self.board.step("right")
                        self.print_board()
                        time.sleep(0.2)

if __name__ == '__main__':
    g = Game(5)
    g.start()