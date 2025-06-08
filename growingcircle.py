import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

class Circle():
    def __init__ (self, radius, color, pos, width):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.width = width
        self.surface = screen
    
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)
    
    def grow(self, R):
        self.radius = self.radius + R
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)

bluecircle = Circle(10, "blue", (250, 250), 0)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            bluecircle.draw()
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            bluecircle.grow(10)
