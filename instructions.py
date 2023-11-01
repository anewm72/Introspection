import pygame
import time
import random

pygame.init()
width = 1240
height = 1000

white = (255, 255, 255)
blue = (0, 0, 128)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))

class Text():
    def __init__(self, writing, center_x, center_y):
        self.writing = writing
        self.center_x = center_x
        self.center_y = center_y
    def display(self):
        self.text = font.render(self.writing, True, white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.center_x, self.center_y)
        screen.blit(self.text, self.textRect)

while True:
    screen.fill(black)
    font = pygame.font.SysFont("Century", 25)
    first = Text('Welcome to INTROSPECTION. I will be your guide from now on, so you should listen to me.', 620, 330)
    second = Text("First, basic controls.  Use 'W', 'A', 'S' and 'D' to move.", 620, 380)
    third = Text("Open your inventory by pressing space.", 620, 430)
    fourth = Text("Close your inventory by pressing enter.", 620, 480)
    fifth = Text("Talk by people you meet by clicking on them.", 620, 530)
    sixth = Text("Now, get out of this forest.", 620, 580)
    first.display()
    pygame.display.flip()
    time.sleep(3)
    second.display()
    pygame.display.flip()
    time.sleep(3)
    third.display()
    pygame.display.flip()
    time.sleep(3)
    fourth.display()
    pygame.display.flip()
    time.sleep(3)
    fifth.display()
    pygame.display.flip()
    time.sleep(3)
    sixth.display()
    pygame.display.flip()
    import Main_Game
    time.sleep(0.005)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.quit()
