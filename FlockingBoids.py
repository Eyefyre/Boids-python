import pygame
from Boid import Boid
import random


WIDTH,HEIGHT = 1000,1000
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Boids")
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (255,240,240)
BEIGE = (249,243,221)
RED = (255,0,0)
BLUE = (0,29,67)
FPS = 60

boids = []

for i in range(100):
    boids.append(Boid(random.randint(0,HEIGHT),random.randint(0,WIDTH),WHITE,WINDOW,4))
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                checkMouseClick()
        draw_all()
    pygame.quit()

def checkMouseClick():
    mouse_pos = pygame.mouse.get_pos()
    boids.append(Boid(mouse_pos[0],mouse_pos[1],WHITE,WINDOW,4))

def draw_all():
    draw_window()
    for boid in boids:
        boid.edges()
        boid.flock(boids)
    for boid in boids:
        boid.update()
        boid.draw()
    update_display()

def draw_window():
    WINDOW.fill(BLUE)

def update_display():
    pygame.display.update()

if __name__ == "__main__":
    main()