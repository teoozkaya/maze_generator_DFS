import pygame
import random


# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

class Cell:
    def __init__(self, i, j, w, cols, rows):
        self.i = i
        self.j = j
        self.w = w
        self.cols = cols
        self.rows = rows
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left
        self.visited = False

    def show(self, screen):

        x = self.i * self.w
        y = self.j * self.w
        if self.visited:
            pygame.draw.rect(screen, MAGENTA, (x, y, self.w, self.w))

        if self.walls[0]:
            pygame.draw.line(screen, WHITE, (x, y), (x + self.w, y))
        if self.walls[1]:
            pygame.draw.line(screen, WHITE, (x + self.w, y), (x + self.w, y + self.w))
        if self.walls[2]:
            pygame.draw.line(screen, WHITE, (x + self.w, y + self.w), (x, y + self.w))
        if self.walls[3]:
            pygame.draw.line(screen, WHITE, (x, y + self.w), (x, y))


    def highlight(self, screen):
        x = self.i * self.w
        y = self.j * self.w
        pygame.draw.rect(screen, BLUE, (x + 1, y + 1, self.w - 2, self.w - 2))

    def checkNeighbours(self, grid):
        neighbours = []
        top = self.get_neighbor(grid, self.i, self.j - 1)
        right = self.get_neighbor(grid, self.i + 1, self.j)
        bottom = self.get_neighbor(grid, self.i, self.j + 1)
        left = self.get_neighbor(grid, self.i - 1, self.j)

        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited :
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)

        if len(neighbours) > 0:
            return random.choice(neighbours)
        return None

    def get_neighbor(self, grid, i, j):
        index = self.calculate_index(i, j)
        if index is not None:
            return grid[index]
        return None

    def calculate_index(self, i, j):
        if i < 0 or i > self.cols-1 or j < 0 or j > self.rows - 1:
            return None
        return i + j * self.cols

    def removeWall(self, next):
        x = self.i - next.i
        y = self.j - next.j

        if x == 1:
            self.walls[3] = False
            next.walls[1] = False
        if x == -1:
            self.walls[1] = False
            next.walls[3] = False

        if y == 1:
            self.walls[0] = False
            next.walls[2] = False
        if y == -1:
            self.walls[2] = False
            next.walls[0] = False



