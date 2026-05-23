
def clamp(v, lo, hi):
    if v < lo:
        return lo
    if v > hi:
        return hi
    return v


def wrap_pos(x, y, max_x, max_y):
    # wrap-around clásico de snake
    if x < 0:
        x = max_x - 1
    if y < 0:
        y = max_y - 1
    if x >= max_x:
        x = 0
    if y >= max_y:
        y = 0
    return x, y
