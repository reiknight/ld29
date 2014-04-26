# -*- coding: utf-8 -*-
import random
from cell import Cell

CELL_TYPES = 5

class Level:
    def __init__(self, cell_size = 50, rows = 12, cols = 16):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.cells = []

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Cell(int(CELL_TYPES * random.random()), i, j, self.cell_size))
            self.cells.append(row)

    def update(self):
        for row in self.cells:
            for cell in row:
                cell.update()

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)
