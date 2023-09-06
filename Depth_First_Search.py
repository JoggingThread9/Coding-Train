# Maze Generator
import random

import pygame
import sys
from random import choice

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)

WIDTH, HEIGHT = 800, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

size = 50


rows, cols = WIDTH // size, HEIGHT // size

clock = pygame.time.Clock()


class cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {
            'top': [True],
            'right': [True],
            'bottom': [True],
            'left': [True]
        }

        self.visited = False
        self.thickness = 2

    def current_cell(self):
        x, y = self.x * size, self.y * size
        pygame.draw.rect(WIN, white, (x + 2, y + 2, size - 2, size - 2))

    def draw(self):
        x, y = self.x * size, self.y * size

        if self.walls['top']:
            pygame.draw.line(WIN, grey, (x, y), (x + size, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(WIN, grey, (x + size, y), (x + size, y + size), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(WIN, grey, (x + size, y + size), (x, y + size), self.thickness)
        if self.walls['left']:
            pygame.draw.line(WIN, grey, (x, y + size), (x, y), self.thickness)

    def check_cell(self, x, y):
        find_index = lambda y, x: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return self.grid_cells[find_index(x, y)]

    def check_neighbors(self, gird_cells):
        self.grid_cells = grid_cells
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        return choice(neighbors) if neighbors else False


def remove_wall(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False

    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


grid_cells = [cell(row, col) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []

count = 1

while count != len(grid_cells):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    WIN.fill(black)
    [CELL.draw() for CELL in grid_cells]

    current_cell.visited = True
    current_cell.current_cell()

    next_cell = current_cell.check_neighbors(grid_cells)

    if next_cell:
        next_cell.visited = True
        count += 1
        stack.append(current_cell)
        remove_wall(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()

    pygame.display.update()
    clock.tick(20)
