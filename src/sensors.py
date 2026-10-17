"""Persona B: muestrea la malla simulada y agrega ruido."""
import numpy as np
import pandas as pd


def sample_sensors(malla: np.ndarray, n_sensores: int = 10,
                   ruido: float = 0.3, seed: int = 42) -> pd.DataFrame:
    """Devuelve DataFrame[t, sensor_id, x, y, temp_medida]."""
    rng = np.random.default_rng(seed)
    n_t, n_y, n_x = malla.shape

    # posiciones fijas de los sensores (evitando los bordes)
    xs = rng.integers(2, n_x - 2, n_sensores)
    ys = rng.integers(2, n_y - 2, n_sensores)

    filas = []
    for sid, (x, y) in enumerate(zip(xs, ys)):
        serie = malla[:, y, x] + rng.normal(0, ruido, n_t)
        for t in range(n_t):
            filas.append((t, sid, int(x), int(y), serie[t]))

    return pd.DataFrame(filas, columns=["t", "sensor_id", "x", "y", "temp_medida"])


def malla_falsa(pasos: int = 500, n: int = 30) -> np.ndarray:
    """Malla inventada para probar mientras A termina physics.py."""
    rng = np.random.default_rng(0)
    base = 25 + 10 * np.exp(-((np.arange(n)[:, None] - 15) ** 2
                              + (np.arange(n)[None, :] - 15) ** 2) / 60)
    t = np.arange(pasos)[:, None, None]
    return base[None] + 0.5 * np.sin(t / 50) + rng.normal(0, 0.05, (pasos, n, n))