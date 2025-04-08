from uuid import uuid4
from address import Address, input_address_data
from verify import get_input
from postion import Position, input_postion_data
import verify

class Person:
    def __init__(self, name: str, birthday: str, cpf: str, gender: str, phone: str, email: str, address: Address):
        self.__name = name
        self.__birthday = birthday
        self.__cpf = cpf
        self.__gender = gender
        self.__address = address
        self.__phone = phone
        self.__email = email
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    @property
    def birthday(self) -> str:
        return self.__birthday
    
    @birthday.setter
    def birthday(self, birthday: str):
        self.__birthday = birthday
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @property
    def gender(self) -> str:
        return self.__gender
    
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender
    
    @property
    def address(self) -> Address:
        return self.__address
    
    @address.setter
    def address(self, address: Address):
        self.__address = address
    
    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email

class Client(Person):
    def __init__(self, name:str, birthday:str, cpf:str, gender:str, phone:str, email:str, address: Address, income: float = 0):
        super().__init__(name, birthday, cpf, gender, phone, email, address)
        self.__client_id = str(uuid4())
        self.__income = income
        self.__car_rented = None
        
    @property
    def client_id(self) -> str:
        return self.__client_id
    
    @client_id.setter
    def client_id(self, client_id: str):
        self.__client_id = client_id
    
    @property
    def income(self) -> float:
        return self.__income
    
    @income.setter
    def income(self, income: float):
        self.__income = income
    
    @property
    def car_rented(self):
        return self.__car_rented
    
    @car_rented.setter
    def car_rented(self, car):
        self.__car_rented = car
    
    def __str__(self):
        return (f'Client(name={self.name} \nbirthday={self.birthday} \ncpf={self.cpf} \ngender={self.gender} \naddress={self.address.to_dict()})'
                f'phone={self.phone} \nemail={self.client_id} \nincome={self.income} \ncar_rented={self.car_rented}')
    
    def client_dict(self): 
        return {   "name": self.name,
            "birthday": self.birthday,
            "cpf": self.cpf,
            "gender": self.gender,
            "address": self.address.to_dict(),
            "phone": self.phone,
            "email": self.email,
            "client_id": self.client_id,
            "income": self.income,
            "car_rented": self.car_rented}

def input_client_data() -> Client:
    print('\n--- Cadastro de Cliente ---')
    name = get_input('Nome: ', verify.none_word)
    birthday = get_input('Data de nascimento: ', verify.is_date)
    cpf = get_input('CPF: ', verify.is_cpf)
    gender = get_input('Genero (M/F): ', verify.none_word)
    phone = get_input('Celular (sem parenteses, hifen ou pontos ex: 18997791500): ', verify.is_phone)
    email = get_input('email: ', verify.is_email)
    income = get_input('Renda mensal: ', lambda x: verify.is_num(x, float))
    address = input_address_data()
    return Client(name=name, 
                  birthday=birthday, 
                  cpf=cpf, 
                  gender=gender.upper(), 
                  phone=phone, 
                  email=email, 
                  address=address, 
                  income=income)
    

class Employee(Person):
    def __init__(self, name: str, birthday: str, cpf: str, gender: str, phone: str, email: str, position: Position,address: Address):
        super().__init__(name, birthday, cpf, gender, phone, email, address)
        self.__employee_id = str(uuid4())
        self.__position = position
    
    @property
    def employee_id(self) -> str:
        return self.__employee_id
    
    @employee_id.setter
    def employee_id(self, employee_id: str):
        self.__employee_id = employee_id

    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, position: Position):
        self.position = position

    def empolyee_to_dict(self):
        return {"name": self.name,
            "birthday": self.birthday,
            "cpf": self.cpf,
            "gender": self.gender,
            "address": self.address.to_dict(),
            "phone": self.phone,
            "email": self.email,
            "Employee_id": self.employee_id,
            "Position": self.position
            }
        
def input_employee_data() -> Employee:
    print('\n--- Cadastro de Funcionario ---')
    name = get_input('Nome: ', verify.none_word)
    birthday = get_input('Data de nascimento: ', verify.is_date)
    cpf = get_input('CPF: ', verify.is_cpf)
    gender = get_input('Genero (M/F): ', verify.none_word)
    phone = get_input('Celular (sem parenteses, hifen ou pontos ex: 18997791500): ', verify.is_phone)
    email = get_input('email: ', verify.is_email)
    address = input_address_data()
    position = get_input('Cargo: ', verify.none_word)
    return Employee(name=name, 
                  birthday=birthday, 
                  cpf=cpf, 
                  gender=gender.upper(), 
                  address=address,
                  phone=phone, 
                  email=email,
                  position= position,)
    
# empregado = input_employee_data()
# print(Employee.empolyee_to_dict(empregado))
