import random, pygame, time 
from pygame.locals import *
from model import *

class Game:
    def __init__(self):
        self.board = Board(4)
        self.board.add_new_piece()
    
    def start(self):

        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Pygame Keyboard Test')
        pygame.mouse.set_visible(0)

        while True:
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    if (event.key == pygame.K_UP):
                        self.board.step("up")
                        bstr = self.board.board_str()
                        print(bstr + "\n" * 2)
                        time.sleep(0.2)
                    elif(event.key == pygame.K_DOWN):
                        self.board.step("down")
                        bstr = self.board.board_str()
                        print(bstr + "\n" * 2)
                        time.sleep(0.2)
                    elif(event.key == pygame.K_LEFT):
                        self.board.step("left")
                        bstr = self.board.board_str()
                        print(bstr + "\n" * 2)
                        time.sleep(0.2)
                    elif(event.key == pygame.K_RIGHT):
                        self.board.step("right")
                        bstr = self.board.board_str()
                        print(bstr + "\n" * 2)
                        time.sleep(0.2)

if __name__ == '__main__':
    g = Game()
    g.start()