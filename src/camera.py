# -*- coding: utf-8 -*-

from constants import *

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, player):
        playerCenterx, playerCentery = player.getCenter()
        if (self.x + HALF_WINDOW_WIDTH) - playerCenterx > CAMERA_SLACK:
            self.x = playerCenterx + CAMERA_SLACK - HALF_WINDOW_WIDTH
        elif playerCenterx - (self.x + HALF_WINDOW_WIDTH) > CAMERA_SLACK:
            self.x = playerCenterx - CAMERA_SLACK - HALF_WINDOW_WIDTH
        if (self.y + HALF_WINDOW_HEIGHT) - playerCentery > CAMERA_SLACK:
            self.y = playerCentery + CAMERA_SLACK - HALF_WINDOW_HEIGHT
        elif playerCentery - (self.y + HALF_WINDOW_HEIGHT) > CAMERA_SLACK:
            self.y = playerCentery - CAMERA_SLACK - HALF_WINDOW_HEIGHT

        if (self.x <= 0):
            self.x = 0

    def getPosition(self):
        return (self.x, self.y)
