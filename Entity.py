from constants import *


class Entity:
    """The most fundamental object in the game. Nearly everything you see is a entity."""

    def __init__(self, icon, pos):
        self.icon = icon
        self.pos = pos
        self.visible = False

    def __str__(self):
        """entity is automatically made invisible based on the value of self.visible"""
        if self.visible:
            return self.icon
        else:
            return "  "

    def add(self, bg):
        bg.append(self)
        self.visible = True
        self.pos.x = MAP_WIDTH - 1

    def remove(self, bg):
        self.visible = False
        bg.pop(bg.index(self))

    def motion(self):
        self.pos.x -= BG_SPD

    # edge detectors
    def touching_lwall(self, game_map):
        return self.pos.x <= game_map.lwall

    def touching_rwall(self, game_map):
        return self.pos.x >= game_map.rwall

    def touching_ceiling(self, game_map):
        return self.pos.y <= game_map.ceiling

    def touching_floor(self, game_map):
        return self.pos.y >= game_map.floor
