"""Persona B: muestrea la malla simulada y agrega ruido."""
import numpy as np
import pandas as pd

def sample_sensors(malla: np.ndarray, n_sensores: int = 10, ruido: float = 0.3) -> pd.DataFrame:
    """Devuelve DataFrame[t, sensor_id, x, y, temp_medida]."""
    raise NotImplementedError
