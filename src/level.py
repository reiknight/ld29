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

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                cell = self.buildCellAt(i, j)
                row.append(cell)
            self.cells.append(row)

    def update(self, camera):
        # Update cells
        for row in self.cells:
            for cell in row:
                cell.update()

        camerax, cameray = camera.getPosition()
        row, col, cell = self.getCellAt(camerax, cameray)

        if (col + (len(self.cells[0]) - LEVEL_INITIAL_COLS) < 0): # Spawn new column from left
            for i in range(self.rows):
                cell = self.buildCellAt(i, col)
                self.cells[i].insert(0, cell)

        if (col + (WINDOW_WIDTH / CELL_SIZE) >= len(self.cells[0])): # Spawn new column from right
            for i in range(self.rows):
                cell = self.buildCellAt(i, col + (WINDOW_WIDTH / CELL_SIZE))
                self.cells[i].append(cell)

    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        camera_row, camera_col, camera_cell = self.getCellAt(camerax, cameray)
        camera_col += (len(self.cells[0]) - LEVEL_INITIAL_COLS)

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if (j >= camera_col and j <= camera_col + (WINDOW_WIDTH / CELL_SIZE)):
                    self.cells[i][j].draw(surface, camerax, cameray)

    def getCellAt(self, x, y):
        row = int(y / self.cell_size)
        col = int(x / self.cell_size)
        return (row, col, self.cells[row][col])

    def buildCellAt(self, row, col):
        cell_type_id = SKY if row < SURFACE_LEVEL else GROUND
        cell = Cell(cell_type_id, row, col, self.cell_size)
        if (cell_type_id == GROUND):
            cell.setMaterial(self.materialAt(row, col))
        return cell

    def materialAt(self, row, col):
        if (row < SURFACE_LEVEL + 5):
            return CELL_MATERIALS[random.randint(0, 1)]
        elif(row < SURFACE_LEVEL + 15):
            return CELL_MATERIALS[random.randint(0, 2)]
        else:
            return CELL_MATERIALS[random.randint(0, len(CELL_MATERIALS) - 1)]

