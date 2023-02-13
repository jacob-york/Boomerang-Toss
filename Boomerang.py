from Entity import Entity
from constants import *
from momods100 import colors
from math import sqrt


class Boomerang(Entity):

    def __init__(self, pos):
        super().__init__(BMRANG_ICON, pos)
        self.reflected = False
        self.hit = False
        self.down = False
        self.up = False

        self.aim_up = None

    def __str__(self):
        if self.down:
            self.icon = BMRANG_DOWN if not self.reflected else BMRANG_UP
        elif self.up:
            self.icon = BMRANG_UP if not self.reflected else BMRANG_DOWN
        else:
            self.icon = BMRANG_ICON if not self.reflected else BMRANG_REVERSE
        return colors.paint(self.icon, "yellow")

    @staticmethod
    def diag(speed):
        return speed / sqrt(2)
    
    def touching_ceiling(self, game_map):
        return (self.pos.y - Boomerang.diag(settings[BMRANG_SPD][ACTIVE])) <= game_map.ceiling

    def touching_lwall(self, game_map):
        if not self.hit:
            return (self.pos.x - settings[BMRANG_SPD][ACTIVE]) <= game_map.lwall
        else:
            return (self.pos.x - Boomerang.diag(settings[BMRANG_SPD][ACTIVE])) <= game_map.lwall

    def touching_floor(self, game_map):
        return (self.pos.y + Boomerang.diag(settings[BMRANG_SPD][ACTIVE])) >= game_map.floor

    def touching_rwall(self, game_map):
        if not self.hit:
            return (self.pos.x + settings[BMRANG_SPD][ACTIVE]) >= game_map.rwall
        else:
            return (self.pos.x + Boomerang.diag(settings[BMRANG_SPD][ACTIVE])) >= game_map.rwall

    def motion(self, game_map, player):
        if not self.visible:
            self.pos.y = player.pos.y
        elif self.visible:
            if not self.reflected:
                if not self.hit:
                    self.pos.x += settings[BMRANG_SPD][ACTIVE]
                else:
                    self.pos.x += Boomerang.diag(settings[BMRANG_SPD][ACTIVE])
            elif self.reflected:
                if not self.hit:
                    self.pos.x -= settings[BMRANG_SPD][ACTIVE]
                else:
                    self.pos.x -= Boomerang.diag(settings[BMRANG_SPD][ACTIVE])
                    
        if self.down:
            self.pos.y += Boomerang.diag(settings[BMRANG_SPD][ACTIVE])
        elif self.up:
            self.pos.y -= Boomerang.diag(settings[BMRANG_SPD][ACTIVE])
        if self.touching_floor(game_map) and self.down:
            self.up = True
            self.down = False
        if self.touching_ceiling(game_map) and self.up:
            self.up = False
            self.down = True
        if self.touching_rwall(game_map):
            self.reflected = True
        if self.touching_lwall(game_map):
            self.visible = False
            self.reflected = False
            self.hit = False
            self.down = False
            self.up = False 
            self.pos.x = 6
            self.pos.y = 0
