# ThermoShield

<p align="center">
  <strong>Physics-Informed AI for Thermal Sensor Security</strong>
  <br>
  Detección de sensores falsificados mediante modelos físicos de difusión de calor.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Physics-Heat%20Equation-DA5B35?style=flat-square" alt="Physics">
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-7057FF?style=flat-square" alt="Cybersecurity">
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square" alt="In development">
</p>

---

## Overview

ThermoShield explora cómo detectar lecturas de temperatura potencialmente falsificadas en un centro de datos mediante las propiedades físicas de la difusión del calor.

El proyecto simula un campo térmico, genera mediciones de sensores, introduce ataques sintéticos y analiza las inconsistencias para identificar posibles manipulaciones.

## Pipeline

```mermaid
flowchart TD
    A["Thermal Simulation"] --> B["Sensor Sampling"]
    B --> C["Attack Injection"]
    C --> D["Physics-Based Detection"]
    D --> E["Metrics & Evaluation"]

    style A fill:#172554,stroke:#3B82F6,color:#FFFFFF
    style B fill:#172554,stroke:#3B82F6,color:#FFFFFF
    style C fill:#451A03,stroke:#F59E0B,color:#FFFFFF
    style D fill:#312E81,stroke:#818CF8,color:#FFFFFF
    style E fill:#064E3B,stroke:#10B981,color:#FFFFFF
```

## Architecture Contracts

Las siguientes interfaces están **congeladas**. Las implementaciones deben respetar sus firmas y formatos de salida.

| Function | Contract | Owner |
|:--|:--|:--:|
| `simular(pasos)` | `array [tiempo, y, x]` | A |
| `sample_sensors(malla)` | `DataFrame[t, sensor_id, x, y, temp_medida]` | B |
| `inject_attack(df, tipo, sensor_id, t_inicio)` | `df + es_ataque` | B |
| `detect(df)` | `df + residual, alerta` | A |
| `calcular_metricas(df)` | `dict` | B |

## Workflow

1. Crear una rama por tarea.
2. Implementar sin modificar los contratos congelados.
3. Abrir un Pull Request hacia `main`.
4. Revisar los cambios del compañero antes de integrar.

```text
feature/<task>
      |
      v
 Pull Request
      |
      v
   Review
      |
      v
    main
```

## Project Scope

- Simulación de difusión térmica.
- Muestreo de sensores virtuales.
- Inyección de ataques sintéticos.
- Detección basada en residuos físicos.
- Evaluación mediante métricas.

---

<p align="center">
  <sub>ThermoShield · Physics × AI × Cybersecurity</sub>
</p>