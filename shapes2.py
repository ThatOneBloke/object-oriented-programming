import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

class Rectangle():
    def __init__ (self, color, dimensions):
        self.color = color
        self.dimensions = dimensions
        self.surface = screen
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.dimensions)

bluerectangle = Rectangle("blue", (100, 100, 50, 100))
redsquare = Rectangle("red", (200, 200, 50, 50))

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")
    bluerectangle.draw()
    redsquare.draw()
    pygame.display.update()