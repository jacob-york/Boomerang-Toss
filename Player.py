from constants import *
from Entity import Entity
from momods100 import colors


class Player(Entity):

    def __init__(self, pos):
        super().__init__(colors.paint(P_ICON, "cyan"), pos)
        self.visible = True

        self.down_force = 0
        self.up_force = 0
        self.y_vel = 0

    def touching_floor(self, game_map):
        return (self.pos.y + self.down_force) >= game_map.floor

    def jump(self, strength):
        self.up_force = strength

    def motion(self, game_map):

        self.y_vel = self.down_force - self.up_force

        self.pos.y += self.y_vel  # 1

        if self.touching_floor(game_map):
            self.up_force = 0
            self.down_force = 0

        # gravity
        if not self.touching_floor(game_map):
            self.pos.y += self.down_force  # 2
            self.down_force += GRAV  # accelerating downwards (note: When I first coded this, I for whatever reason wrote it so self.pos.y is being incremented twice per GAME loop: once at #1 and once at #2.
            # On the basis that the program works really well, I'll leave it as is. But know that I don't think it makes any sense.)
        elif self.touching_floor(game_map):
            self.down_force = 0
            self.up_force = 0
