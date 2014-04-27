# -*- coding: utf-8 -*-
class Entity:
    """Base class, for all entities"""
    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        self.sprite.draw(surface, self.x - camerax, self.y - cameray)
