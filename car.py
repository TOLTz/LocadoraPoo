from enum import Enum, auto
from verify import get_input
import verify

class TipoVeiculo(Enum):
    CARRO = auto()
    MOTO = auto()
    CAMINHAO = auto()
    SUV = auto()

class StatusVeiculo(Enum):
    DISPONIVEL = auto()
    ALUGADO = auto()
    EM_MANUTENCAO = auto()
    VENDIDO = auto()

class Car:
    def __init__(
        self,
        plate: str,
        mark: str,
        model: str,
        year: int,
        color: str,
        mileage: float,
        daily_value: float,
        sell_value: float,
        type_v: TipoVeiculo = TipoVeiculo.CARRO,
        status: StatusVeiculo = StatusVeiculo.DISPONIVEL,
    ):
        self.__plate = plate
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__color = color
        self.__type_v = type_v
        self.__status = status
        self.__mileage = mileage
        self.__daily_value = daily_value
        self.__sell_value = sell_value


    @property
    def plate(self) -> str:
        return self.__plate

    @plate.setter
    def plate(self, value: str):
        self.__plate = value

    @property
    def mark(self) -> str:
        return self.__mark

    @mark.setter
    def mark(self, value: str):
        self.__mark = value

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str):
        self.__model = value

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int):
        self.__year = value

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str):
        self.__color = value

    @property
    def type_v(self) -> TipoVeiculo:
        return self.__type_v

    @type_v.setter
    def type_v(self, value: TipoVeiculo):
        self.__type_v = value

    @property
    def status(self) -> StatusVeiculo:
        return self.__status

    @status.setter
    def status(self, value: StatusVeiculo):
        self.__status = value

    @property
    def mileage(self) -> float:
        return self.__mileage

    @mileage.setter
    def mileage(self, value: float):
        self.__mileage = value

    @property
    def daily_value(self) -> float:
        return self.__daily_value

    @daily_value.setter
    def daily_value(self, value: float):
        self.__daily_value = value

    @property
    def sell_value(self) -> float:
        return self.__sell_value

    @sell_value.setter
    def sell_value(self, value: float):
        self.__sell_value = value

    def __str__(self):
        return (
            f"Car(plate={self.plate}, mark={self.mark}, model={self.model}, "
            f"year={self.year}, color={self.color}, type_v={self.type_v.name}, "
            f"status={self.__status.name}, mileage={self.__mileage}, "
            f"daily_value={self.daily_value}, sell_value={self.sell_value})"
        )
    
    def car_dict(self):
        car_dict = {
                'plate': self.plate,
                'mark': self.mark,
                'model': self.model,
                'year': self.year,
                'color': self.color,
                'type_v': self.type_v.name,
                'status': self.status.name,
                'mileage': self.mileage,
                'daily_value': self.daily_value,
                'sell_value': self.sell_value
            }
        return car_dict
def input_car_data() -> Car:
    print("\n--- Cadastro de Veículo ---")
    
    # Dados obrigatórios (com validação via setters)
    plate = get_input("Placa (formato ABC-1234 ou ABC1D23): ", verify.is_valid_plate, 'Digite uma placa valida!')
    mark = get_input("Marca: ", verify.none_word)
    model = get_input("Modelo: ", verify.none_word)
    year = get_input('Ano: ', lambda x: verify.is_num(x, int))
    color = get_input('Cor: ', verify.none_word)
    mileage = get_input("Quilometragem: ", lambda x: verify.is_num(x, float))
    daily_value = float(get_input("Valor diário de aluguel: ", lambda x: verify.is_num(x, float)))
    sell_value = float(get_input("Valor de venda: ", lambda x: verify.is_num(x, float)))
    type_input = input(f"Tipo ({'/'.join([t.name for t in TipoVeiculo])}): ").strip()
    type_v = TipoVeiculo[type_input.upper()] if type_input else TipoVeiculo.CARRO

    status_input = input(f"Status ({'/'.join([s.name for s in StatusVeiculo])}): ").strip()
    status = StatusVeiculo[status_input.upper()] if status_input else StatusVeiculo.DISPONIVEL

    # Cria e retorna o objeto
    return Car(
        plate=plate,
        mark=mark,
        model=model,
        year=year,
        color=color,
        mileage=mileage,
        daily_value=daily_value,
        sell_value=sell_value,
        type_v=type_v,
        status=status
    )
    
