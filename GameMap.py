from momods100.puc import C
from momods100 import colors


class GameMap:

    def __init__(self, rows, columns, graphic):
        self.rows = rows
        self.columns = columns
        self.graphic = graphic
        self.graph = []

        self.score = 0
        self.timer = 0
        
        # barriers:
        self.floor = self.rows - 8
        self.lwall = 0
        self.rwall = self.columns - 1
        self.ceiling = 0
        
        for x in range(self.rows):
            self.graph.append([])
        for each_row in self.graph:
            for i in range(self.columns):
                each_row.append(self.graphic)
        for bit_index in range(self.columns):
            self.decorate(C(bit_index, self.floor), "__")

    def __str__(self):
        rep = ""
        rep += "\n"*31
        rep += "(press <ESC> to pause game.)"
        rep += "\n"*3
        rep += "\t\t\t"
        rep += "{SCORE:" + ("0"*(4 - len(str(self.score)))) + str(self.score) + "}"
        rep += "\t"
        rep += "{" + str(self.timer) + "}"
        rep += "\n"
        y = 0
        x = 0
        for each_row in self.graph:
            rep += colors.paint(((str(y) + " ") if (len(str(y)) == 1) else str(y)), "dark gray")
            for each_graphic in each_row:
                rep += each_graphic
            rep += "\n"
            y += 1
        rep += "  "
        for each_column in self.graph[1]:
            rep += colors.paint(((str(x) + " ") if (len(str(x)) == 1) else str(x)), "dark gray")
            x += 1
        return rep

    # most likely soon to be deprecated in favor of update_ent_pos
    def decorate(self, location, item):
        y = round(location.y)
        x = round(location.x)
        self.graph[y][x] = str(item)

    def refresh_self(self):
        """wipe self.graph and redraw it."""
        self.graph = []
        for x in range(self.rows):
            self.graph.append([])
        for each_row in self.graph:
            for i in range(self.columns):
                each_row.append(self.graphic)
        for bit_index in range(self.columns):
            self.decorate(C(bit_index, self.floor), "__")

    def update_ent_pos(self, ent):
        y = round(ent.pos.y)
        x = round(ent.pos.x)
        self.graph[y][x] = str(ent)
