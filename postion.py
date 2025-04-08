from dataclasses import dataclass
from verify import get_input
import verify


@dataclass
class Position:
    position: str
    wage: float
    workload: float
    commission: float = 0
    
    def __post_init__(self):
        if self.wage <= 0:
            raise ValueError('O salário não pode ser negativo ou zero.')
    
    def position_to_dict(self):
        return {
            'position': self.position,
            'wage': self.wage,
            'workload': self.workload,
            'commission': self.commission
        }
        
def input_postion_data() -> Position:
    print('\n--- Cadastro de cargo ---')
    position = get_input('Cargo: ', verify.none_word)
    wage = get_input('Salario: ', lambda x: verify.is_num(x, float))
    workload = get_input('Carga horaria: ', lambda x: verify.is_num(x, int))
    commission = get_input('Comissao por venda: ', lambda x: verify.is_num(x, float)) #criar validacao, permitindo apenas comissao menor que 10%
    commission = float(commission)
    wage = float(wage)
    return Position(position=position, wage=wage, workload=workload, commission=commission)