from enum import Enum, auto

class TipoPagamento(Enum):
    CARTAO_CREDITO = auto()
    CARTAO_DEBITO = auto()
    PIX = auto()
    BOLETO = auto()
    DINHEIRO = auto()