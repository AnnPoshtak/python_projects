import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(":)")
screen.fill((20,50,120))

square = pygame.Surface((50,170))
square.fill("red")
font = pygame.font.Font("Tagesschrift-Regular.ttf",40)
text = font.render("Hi!", False,"black")

mode = True
while mode:
    screen.blit(square, (0,0))
    pygame.display.update()
    screen.blit(text,(300,10))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            mode = False
