from car import input_car_data, Car
from person import input_client_data, Client
from log_gen import log
from db import addData

if __name__ == "__main__":
    print('-------------------Bem vindo-------------------')
    choice = input('Deseja adicionar um cliente[1] ou um veiculo[2]? ')
    
    if choice == '1':
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
    elif choice == '2':
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
    else:
        print('Ate mais ver')
