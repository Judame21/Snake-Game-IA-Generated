
from dataclasses import dataclass


@dataclass
class Snake:
    body: list  # lista de (x,y)
    dir: tuple  # (dx,dy)

    def head(self):
        return self.body[0]

    def move(self, grow=False):
        hx, hy = self.body[0]
        dx, dy = self.dir
        nx, ny = hx + dx, hy + dy
        self.body.insert(0, (nx, ny))
        if not grow:
            self.body.pop()

    def set_dir(self, dx, dy):
        # evita reversa inmediata
        cdx, cdy = self.dir
        if (dx, dy) == (-cdx, -cdy):
            return
        self.dir = (dx, dy)

    def hits_self(self):
        h = self.body[0]
        return h in self.body[1:]
