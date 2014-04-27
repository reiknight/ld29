# -*- coding: utf-8 -*-
import random, pygame
from constants import *
from cell import Cell

class Level:
    def __init__(self, cell_size, rows, cols):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.font = pygame.font.SysFont("Verdana", 30)

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                cell = self.buildCellAt(i, j)
                row.append(cell)
            self.cells.append(row)

    def update(self, camera):
        camerax, cameray = camera.getPosition()
        row, col, cell = self.getCellAt(camerax, cameray)

        if (col + (WINDOW_WIDTH / CELL_SIZE) >= len(self.cells[0])): # Spawn new column from right
            for i in range(self.rows):
                cell = self.buildCellAt(i, col + (WINDOW_WIDTH / CELL_SIZE))
                self.cells[i].append(cell)
            self.cols += 1

        if (row + (WINDOW_HEIGHT / CELL_SIZE) >= len(self.cells)):
            new_row = []
            for j in range(self.cols):
                cell = self.buildCellAt(row + (WINDOW_HEIGHT / CELL_SIZE), j)
                new_row.append(cell)
            self.cells.append(new_row)
            self.rows += 1

        for i in range(row, row + (WINDOW_HEIGHT / CELL_SIZE) + 1):
            for j in range(col, col + (WINDOW_WIDTH / CELL_SIZE) + 1):
                try:
                    self.cells[i][j].update
                except:
                    pass

    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        row, col, cell = self.getCellAt(camerax, cameray)

        for i in range(row, row + (WINDOW_HEIGHT / CELL_SIZE) + 1):
            for j in range(col, col + (WINDOW_WIDTH / CELL_SIZE) + 1):
                try:
                    self.cells[i][j].draw(surface, camerax, cameray)
                except:
                    pass

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
        if (col == 0):
            return OBSIDIAN

        tier_level = row // TIER_LEVEL_MULTIPLY
        tier_level = MAX_TIER_LEVEL if tier_level > MAX_TIER_LEVEL else tier_level

        prob = random.randrange(1, 100)
        acc_prob = 0

        for material in CELL_MATERIALS:
            acc_prob += CELL_MATERIAL_SPAWN_PROB[material][tier_level]
            if (prob <= acc_prob):
                return material
