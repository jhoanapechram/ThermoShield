from src.physics import simular
from src.sensors import sample_sensors
from src.attacks import inject_attack
from src.detector import detect
from src.metrics import calcular_metricas

if __name__ == "__main__":
    malla = simular(500)
    df = sample_sensors(malla)
    df = inject_attack(df, "deriva", 7, 200)
    df = detect(df)
    print(calcular_metricas(df))
