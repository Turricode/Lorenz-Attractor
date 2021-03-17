import pygame
import math

WIDTH = 800
HEIGHT = 600

X_SHIFT = 500
Y_SHIFT = 500

MAX_POINTS = 100
POINT_SCALE = 7

window = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

sigma = 10
beta = 8 / 3
rho = 28

BACKGROUND_COLOR = (220, 220, 220)
DT = 0.001

points = [(0.0, 0.1, 0.0)]

def step(point):

    px = (sigma * (point[1] - point[0])) * DT
    py = (point[0] * (rho - point[2]) - point[1]) * DT
    pz = (point[0] * point[1] - beta * point[2]) * DT

    p = (point[0] + px, point[1] + py, point[2] + pz)

    return p

def mapColor(point):
    return (point[2] / math.sqrt(point[0] * point[0] + point[1] * point[1] + point[2] * point[2]) + 1) * 255 / 4

def mapToScreen(point):
    return (int(point[0] * POINT_SCALE) + int(WIDTH / 2), int(point[1] * POINT_SCALE) + int(HEIGHT / 2)), 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    if len(points) == MAX_POINTS:
        points.pop(0) 

    cp = step(points[-1])
    points.append(cp)
    
    for i in range(1, len(points)):
        s = mapToScreen(points[i - 1])
        e = mapToScreen(points[i])
        c = mapColor(points[i - 1])
        pygame.draw.aaline(window, (c, c, c), s, e)
    pygame.display.flip()