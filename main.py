import pygame
from cell import Cell
# Constants
WIDTH = 400
HEIGHT = 400
W = 10

# Colors
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cols = WIDTH // W
rows = HEIGHT // W

# Create the grid
grid = []
for j in range(rows):
    for i in range(cols):
        cell = Cell(i, j, W, cols, rows)
        grid.append(cell)

current = grid[0]
stack = []

# Main loop
running = True
while running:
    clock.tick(12)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for cell in grid:
        cell.show(screen)

    current.visited = True
    current.highlight(screen)
    next_cell = current.checkNeighbours(grid)
    if next_cell:
        current.removeWall(next_cell)
        next_cell.visited = True
        stack.append(current)
        current = next_cell
    elif len(stack) > 0:
        current = stack.pop()

    pygame.display.flip()

pygame.quit()
