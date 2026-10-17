# ThermoShield

Deteccion de sensores falsificados en un centro de datos usando fisica (ecuacion de calor).

## Contratos (congelados)
- `simular(pasos) -> array [tiempo, y, x]`  (A)
- `sample_sensors(malla) -> DataFrame[t, sensor_id, x, y, temp_medida]`  (B)
- `inject_attack(df, tipo, sensor_id, t_inicio) -> df + es_ataque`  (B)
- `detect(df) -> df + residual, alerta`  (A)
- `calcular_metricas(df) -> dict`  (B)

## Flujo de trabajo
Una rama por tarea, PR hacia `main`, el otro revisa.
