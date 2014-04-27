# -*- coding: utf-8 -*-
import random
from cell import Cell

SURFACE_LEVEL= 5

SKY = 0
GROUND = 1

DIRT = 0
STONE = 1
LIGHT_METAL = 2
HEAVY_METAL = 3
OBSIDIAN = 4

CELL_MATERIALS = (DIRT, STONE, LIGHT_METAL, HEAVY_METAL, OBSIDIAN)

class Level:
    def __init__(self, cell_size = 50, rows = 12, cols = 16):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.cells = []

        for i in range(rows):
            row = []
            for j in range(cols):
                cell_type_id = SKY if i < SURFACE_LEVEL else GROUND
                #int(CELL_TYPES * random.random())
                cell = Cell(cell_type_id, i, j, self.cell_size)
                row.append(cell)
            self.cells.append(row)

    def update(self):
        for row in self.cells:
            for cell in row:
                cell.update()

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)
