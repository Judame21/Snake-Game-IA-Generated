
import tkinter as tk
from app.config import settings
from app.services.game_service import GameService
from app.utils import logger


class GameController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Snake (Tkinter)')
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=settings.WINDOW_W, height=settings.WINDOW_H, bg=settings.BG, highlightthickness=0)
        self.canvas.pack()

        self.svc = GameService()
        self._job = None

        self.root.bind('<KeyPress>', self.on_key)
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

        logger.log('Game started')

    def on_close(self):
        try:
            if self._job:
                self.root.after_cancel(self._job)
        except Exception:
            pass
        self.root.destroy()

    def on_key(self, e):
        k = e.keysym
        if k == 'Up':
            self.svc.set_dir(0, -1)
        elif k == 'Down':
            self.svc.set_dir(0, 1)
        elif k == 'Left':
            self.svc.set_dir(-1, 0)
        elif k == 'Right':
            self.svc.set_dir(1, 0)
        elif k in ('p', 'P'):
            self.svc.toggle_pause()
        elif k in ('r', 'R'):
            self.svc.reset()
        elif k == 'Escape':
            self.on_close()

    def draw(self):
        self.canvas.delete('all')

        # grid (opcional)
        # for x in range(0, settings.WINDOW_W, settings.CELL):
        #     self.canvas.create_line(x, 0, x, settings.WINDOW_H, fill=settings.GRID_COLOR)
        # for y in range(0, settings.WINDOW_H, settings.CELL):
        #     self.canvas.create_line(0, y, settings.WINDOW_W, y, fill=settings.GRID_COLOR)

        # snake
        for i, (x, y) in enumerate(self.svc.snake.body):
            px = x * settings.CELL
            py = y * settings.CELL
            c = settings.SNAKE_COLOR
            self.canvas.create_rectangle(px, py, px + settings.CELL, py + settings.CELL, fill=c, outline='')

        # food
        fx, fy = self.svc.food.pos
        px = fx * settings.CELL
        py = fy * settings.CELL
        self.canvas.create_oval(px + 2, py + 2, px + settings.CELL - 2, py + settings.CELL - 2, fill=settings.FOOD_COLOR, outline='')

        # HUD
        status = f"Score: {self.svc.score}"
        if self.svc.paused:
            status += '  (PAUSA)'
        if self.svc.game_over:
            status += '  (GAME OVER - presiona R)'
        self.canvas.create_text(10, 10, anchor='nw', fill='white', text=status, font=('Consolas', 12))

    def loop(self):
        self.svc.tick()
        self.draw()
        delay_ms = int(1000 / settings.FPS)
        self._job = self.root.after(delay_ms, self.loop)

    def run(self):
        self.loop()
        self.root.mainloop()
