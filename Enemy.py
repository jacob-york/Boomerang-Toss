from Entity import Entity
from constants import *
from momods100 import colors


class Enemy(Entity):

    def __init__(self, pos):
        super().__init__(colors.paint(E_ICON, "red"), pos)

    def remove(self, bg):
        super().remove(bg)
        self.icon = colors.paint(E_ICON, "red")

    def touching(self, boomerang):
        bmrang_horis_pos = round(boomerang.pos.x + settings[BMRANG_SPD][ACTIVE])
        self_horiz_pos = round(self.pos.x - BG_SPD)

        hitbox = range((self_horiz_pos - 1), (self_horiz_pos + 2))

        return boomerang.visible and (bmrang_horis_pos in hitbox) and \
            (round(boomerang.pos.y) == round(self.pos.y))
