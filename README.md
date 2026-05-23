
# Snake (Tkinter) - Proyecto simple (sin API)

Juego **Snake** básico hecho en Python usando **Tkinter** (solo librería estándar). Incluye una arquitectura mínima con:
- `controllers/` (manejo de input + loop)
- `services/` (reglas del juego)
- `models/` (Snake, Food)
- `utils/` (helpers)
- `config/` (configuración)

## Requisitos
- Python 3.9+ (Tkinter incluido en la mayoría de instalaciones)

## Ejecutar
```bash
python run.py
```

## Controles
- Flechas: mover
- P: pausar
- R: reiniciar
- Esc: salir

## Notas
- Persistencia de high score: NO (intencionalmente simple).
- Tests: solo un smoke test mínimo.
