import pygame
pygame.init()
screen = pygame.display.set_mode((350,200))
pygame.display.set_caption("mini")
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (70, 100)) # Змінюємо розмір
grass = pygame.Surface((350,40))
grass.fill("green")
screen.fill((66, 224, 245))
mode = True
x = 175
y = 100
while mode:
    pygame.display.update()
    screen.blit(grass,(0,160))
    screen.blit(player,(x,y))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            mode = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                screen.fill((66, 224, 245))
                y = y-10
                if y<0:
                    y = y + 10
                screen.blit(player,(x,y))
            if i.key == pygame.K_DOWN:
                screen.fill((66, 224, 245))
                y = y + 10
                if y + 100>200 :
                    y = y - 10
                screen.blit(player, (x, y))
            if i.key == pygame.K_RIGHT:
                screen.fill((66, 224, 245))
                x = x + 10
                if x+50>350:
                    x = x - 10
                screen.blit(player, (x, y))
            if i.key == pygame.K_LEFT:
                screen.fill((66, 224, 245))
                x = x - 10
                if x< -7:
                    x = x + 10
                screen.blit(player, (x, y))
