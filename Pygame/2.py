import pygame
pygame.init()
screen = pygame.display.set_mode((350,200))
pygame.display.set_caption("mini")
square = pygame.Surface((75,75))
screen.fill("blue")
square.fill("Lime")
mode = True
x = 175
y = 100
while mode:
    pygame.display.update()
    screen.blit(square,(x,y))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            mode = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                square.fill("blue")
                screen.blit(square,(x,y))
                y = y-10
                screen.blit(square,(x,y))
            if i.key == pygame.K_DOWN:
                square.fill("blue")
                screen.blit(square, (x, y))
                square.fill("Lime")
                y = y + 10
                screen.blit(square, (x, y))
            if i.key == pygame.K_RIGHT:
                square.fill("blue")
                screen.blit(square, (x, y))
                square.fill("Lime")
                x = x + 10
                screen.blit(square, (x, y))
            if i.key == pygame.K_LEFT:
                square.fill("blue")
                screen.blit(square, (x, y))
                square.fill("Lime")
                x = x - 10
                screen.blit(square, (x, y))
