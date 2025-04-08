from car import input_car_data, Car
from person import input_client_data, Client, Employee, input_employee_data
from postion import Position, input_postion_data
from log_gen import log
from db import addData

if __name__ == "__main__":
    print('-------------------Bem vindo-------------------')
    choice = int(input('Deseja adicionar um: \ncliente   1️⃣ \nveiculo   2️⃣ \nempregado 3️⃣ \ncargo     4️⃣ \n'))
    
    if choice == 1:
        while True:
            try:
                client = input_client_data()  
                client = Client.client_dict(client)
                addData('db/client.json', client)
                print("\n Cliente cadastrado com sucesso!")
                log('Cliente foi adicionado')
                another = input("\nCadastrar outro cliente? (s/n): ").strip().lower()
                if another != 's':
                    break

            except ValueError as e:
                print(f"\nErro: {e}. Tente novamente!")
            except KeyError:
                print("\nErro: Tipo ou status inválido. Use os valores disponíveis.")
    elif choice == 2:
        while True:
            try:
                car = input_car_data()  
                cars = Car.car_dict(car)
                addData('db/car.json', cars)
                print("\nVeículo cadastrado com sucesso!")
                log('carro foi adicionado')
                another = input("\nCadastrar outro veículo? (s/n): ").strip().lower()
                if another != 's':
                    break

            except ValueError as e:
                print(f"\nErro: {e}. Tente novamente!")
            except KeyError:
                print("\nErro: Tipo ou status inválido. Use os valores disponíveis.")
    elif choice == 3:
        while True:
            try:
                employee = input_employee_data()  
                employee = Employee.empolyee_to_dict(employee)
                addData('db/funcionario.json', employee)
                print("\nFuncionario cadastrado com sucesso!")
                log('Funcionario foi adicionado')
                another = input("\nCadastrar outro Funcionario? (s/n): ").strip().lower()
                if another != 's':
                    break

            except ValueError as e:
                print(f"\nErro: {e}. Tente novamente!")
            except KeyError:
                print("\nErro: Tipo ou status inválido. Use os valores disponíveis.")
    elif choice == 4:
        while True:
            try:
                position = input_postion_data()
                position = Position.position_to_dict(position)
                addData('db/Cargos.json', position)
                print("Cargo cadastrado com sucesso!")
                log('Cargo foi adicionado')
                another = input("\nCadastrar outro Cargo? (s/n): ").strip().lower()
                if another != 's':
                    break

            except ValueError as e:
                print(f"\nErro: {e}. Tente novamente!")
            except KeyError:
                print("\nErro: Tipo ou status inválido. Use os valores disponíveis.")
    else:
        print('Ate mais ver')
