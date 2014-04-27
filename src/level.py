# -*- coding: utf-8 -*-
import random
from constants import *
from cell import Cell

class Level:
    def __init__(self, cell_size, rows, cols):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.cells = []

        for i in range(rows):
            row = []
            for j in range(cols):
                cell_type_id = SKY if i < SURFACE_LEVEL else GROUND
                cell = Cell(cell_type_id, i, j, self.cell_size)
                if (cell_type_id == GROUND):
                    cell.setMaterial(materialAt(i, j))
                row.append(cell)
            self.cells.append(row)

    def update(self):
        for row in self.cells:
            for cell in row:
                cell.update()

    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        for row in self.cells:
            for cell in row:
                cell.draw(surface, camerax, cameray)

    def getCellAt(self, x, y):
        col = int(x / self.cell_size)
        row = int(y / self.cell_size)
        return (row, col, self.cells[row][col])

    def materialAt(self, row, col):
        if (row < 5):
            return DIRT
        else
            return CELL_MATERIALS[random.randint(0, len(CELL_MATERIALS))]

