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

initialise = True

while (initialise):
    font = pygame.font.SysFont("Century", 100, bold=True)
    text = font.render('Introspection', True, blue)
    textRect = text.get_rect()
    textRect.center = (width//2, height//3)
    running = True
    initialise = False

while (running):
    screen.fill(white)
    screen.blit(text, textRect)
    start = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\start.png")
    start_small = pygame.transform.scale(start, (150, 100))
    screen.blit(start_small, (400, 700))
    settings = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\settings.png")
    settings_small = pygame.transform.scale(settings, (150, 100))
    screen.blit(settings_small, (600, 700))
    leave = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\leave.png")
    leave_small = pygame.transform.scale(leave, (150, 100))
    screen.blit(leave_small, (800, 700))
    pygame.display.flip()
    time.sleep(0.005)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if pygame.Rect(400, 700, 150, 100).collidepoint(x, y):
                import Instructions
            if pygame.Rect(600, 700, 150, 100).collidepoint(x, y):
                import Settings
            if pygame.Rect(800, 700, 150, 100).collidepoint(x, y):
                pygame.quit()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
