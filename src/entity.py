# -*- coding: utf-8 -*-
class Entity:
    """Base class, for all entities"""
    def draw(self, surface, camerax, cameray):
        self.sprite.draw(surface, self.x - camerax, self.y - cameray)
