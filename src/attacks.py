"""Persona B: inyecta ataques a las lecturas."""
import pandas as pd

def inject_attack(df: pd.DataFrame, tipo: str, sensor_id: int, t_inicio: int) -> pd.DataFrame:
    """tipo: 'fijo' | 'deriva' | 'replay'. Devuelve df con columna es_ataque."""
    raise NotImplementedError
