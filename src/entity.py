# -*- coding: utf-8 -*-
class Entity:
    """Base class, for all entities"""
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y)