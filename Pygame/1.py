import pygame
from tkinter import messagebox
messagebox.showinfo("Привіт!","Вітаю! Ви можете натискати чисоа від 1 до 9 і колір вікно буде змінюватия.")
pygame.init()
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("color")
mode = True
while mode:
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            mode = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1:
                screen.fill((255, 3, 24))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_2:
                screen.fill((255, 74, 3))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_3:
                screen.fill((255, 238, 3))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_4:
                screen.fill((58, 255, 3))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_5:
                screen.fill((3, 255, 247))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_6:
                screen.fill((3, 58, 255))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_7:
                screen.fill((204, 0, 255))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_8:
                screen.fill((254, 252, 255))
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_9:
                screen.fill((0,0,0))