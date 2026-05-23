
import random
from app.config import settings
from app.models.snake import Snake
from app.models.food import Food
from app.utils.geometry import wrap_pos


class GameService:
    def __init__(self):
        self.grid_w = settings.WINDOW_W // settings.CELL
        self.grid_h = settings.WINDOW_H // settings.CELL
        self.score = 0
        self.game_over = False
        self.paused = False
        self.snake = None
        self.food = None
        self.reset()

    def reset(self):
        self.score = 0
        self.game_over = False
        self.paused = False
        cx = self.grid_w // 2
        cy = self.grid_h // 2
        body = []
        for i in range(settings.START_LEN):
            body.append((cx - i, cy))
        self.snake = Snake(body=body, dir=(1, 0))
        self.food = Food(pos=self._random_free_cell())

    def _random_free_cell(self):
        # intenta varias veces
        for _ in range(999):
            x = random.randint(0, self.grid_w - 1)
            y = random.randint(0, self.grid_h - 1)
            if (x, y) not in self.snake.body:
                return (x, y)
        return (0, 0)

    def tick(self):
        if self.game_over or self.paused:
            return

        # mover
        head_before = self.snake.head()
        self.snake.move(grow=False)

        # wrap
        hx, hy = self.snake.head()
        hx, hy = wrap_pos(hx, hy, self.grid_w, self.grid_h)
        self.snake.body[0] = (hx, hy)

        # comer
        if self.snake.head() == self.food.pos:
            self.score += 1
            # crecer: mueve una vez más "creciendo" reinsertando el head anterior
            # (no es la forma más elegante, pero funciona)
            self.snake.body.insert(1, head_before)
            self.food.pos = self._random_free_cell()

        # colisión
        if self.snake.hits_self():
            self.game_over = True

    def set_dir(self, dx, dy):
        if not self.game_over:
            self.snake.set_dir(dx, dy)

    def toggle_pause(self):
        self.paused = not self.paused
