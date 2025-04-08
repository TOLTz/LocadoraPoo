import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from client_gui import abrir_formulario_cliente 
from person import input_client_data, Client
from car_gui import abrir_formulario_carro
from employee_gui import abrir_formulario_funcionario
from position_gui import abrir_formulario_cargo

from db import addData
from log_gen import log

def cadastrar_cliente():
    try:
        cliente = input_client_data()
        cliente_dict = Client.client_dict(cliente)
        addData('db/client.json', cliente_dict)
        log('Cliente foi adicionado')
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {e}")

def main_gui():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro")
    janela.geometry("300x300")

    titulo = ttk.Label(janela, text="Menu de Cadastro", font=("Helvetica", 14))
    titulo.pack(pady=20)

    ttk.Button(janela, text="Cadastrar Cliente", command=lambda: abrir_formulario_cliente(janela)).pack(pady=5)
    ttk.Button(janela, text="Cadastrar Veículo", command=lambda: abrir_formulario_carro(janela)).pack(pady=5)
    ttk.Button(janela, text="Cadastrar Funcionário", command=lambda: abrir_formulario_funcionario(janela)).pack(pady=5)
    ttk.Button(janela, text="Cadastrar Cargo", command=lambda: abrir_formulario_cargo(janela)).pack(pady=5)


    janela.mainloop()

if __name__ == "__main__":
    main_gui()
