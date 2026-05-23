
# Test mínimo (smoke). No abre UI.
from app.services.game_service import GameService


def test_game_ticks():
    g = GameService()
    for _ in range(5):
        g.tick()
    assert g.score >= 0
