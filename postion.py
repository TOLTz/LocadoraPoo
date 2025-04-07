from dataclasses import dataclass

@dataclass
class Position:
    position: str
    wage: float
    workload: float
    vacations: bool
    commision: float = 0