from Entity import Entity
from constants import *


class Effect(Entity):

    def __init__(self, icon, pos, duration):
        super().__init__(icon, pos)
        self.__clock = 0
        self.duration = duration

    def __str__(self):
        if self.visible:
            self.__clock += 1
            if (self.__clock * settings[TICK_SPD][ACTIVE]) == self.duration:
                self.visible = False
                self.__clock = 0
            return self.icon
        elif not self.visible:
            return "  "

    def add(self, bg):
        bg.append(self)
        self.visible = True
