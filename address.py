from verify import get_input
import verify


class Address:
    def __init__(self, street: str, district: str, number: int, city: str, cep: str, country: str, state: str):
        self.__street = street
        self.__district = district
        self.__number = number
        self.__city = city
        self.__cep = cep
        self.__country = country
        self.__state = state
    
    @property
    def street(self) -> str:
        return self.__street
    
    @street.setter
    def street(self, street: str):
        self.__street = street
    
    @property
    def district(self) -> str:
        return self.__district
    
    @district.setter
    def district(self, district: str):
        self.__district = district
    
    @property
    def number(self) -> int:
        return self.__number
    
    @number.setter
    def number(self, number: int):
        self.__number = number
    
    @property
    def city(self) -> str:
        return self.__city
    
    @city.setter
    def city(self, city: str):
        self.__city = city
    
    @property
    def cep(self) -> str:
        return self.__cep
    
    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep
    
    @property
    def country(self) -> str:
        return self.__country
    
    @country.setter
    def country(self, country: str):
        self.__country = country
    
    @property
    def state(self) -> str:
        return self.__state
    
    @state.setter
    def state(self, state: str):
        self.__state = state

    def to_dict(self) -> dict:
        return {
            "street": self.street,
            "district": self.district,
            "number": self.number,
            "city": self.city,
            "cep": self.cep,
            "country": self.country,
            "state": self.state
        }
        
        
def input_address_data() -> Address:
    print("\n--- Cadastro de Endereço ---")
    
    # Dados obrigatórios
    street = get_input("Rua: ", verify.none_word)
    district = get_input("Bairro: ", verify.none_word)
    number = int(get_input("Número: ", lambda x: verify.is_num(x, int)))
    city = get_input("Cidade: ", verify.none_word)
    cep = get_input("CEP (formato 00000-000): ", verify.none_word, 'Digite um CEP válido!') # criar validacao
    country = get_input("País: ", verify.none_word)
    state = get_input("Estado (sigla): ", verify.none_word, 'Digite uma sigla válida (2 caracteres)')
    return Address(
        street=street,
        district=district,
        number=number,
        city=city,
        cep=cep,
        country=country,
        state=state.upper()
    )