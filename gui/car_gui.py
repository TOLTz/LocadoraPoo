import tkinter as tk
from tkinter import ttk, messagebox
from car import Car, TipoVeiculo, StatusVeiculo
from db import addData
from log_gen import log
import verify

def abrir_formulario_carro(root):
    form = tk.Toplevel(root)
    form.title("Cadastro de Veículo")
    form.geometry("500x600")

    labels = [
        "Placa", "Marca", "Modelo", "Ano",
        "Cor", "Quilometragem", "Valor diário", "Valor de venda"
    ]
    entradas = {}

    for label in labels:
        linha = ttk.Frame(form)
        linha.pack(padx=10, pady=4, fill='x')

        ttk.Label(linha, text=label, width=18).grid(row=0, column=0, sticky="w")
        entrada = ttk.Entry(linha)
        entrada.grid(row=0, column=1, sticky="ew")
        linha.columnconfigure(1, weight=1)
        
        entradas[label] = entrada


    # Dropdowns para Tipo e Status
    linha_tipo = ttk.Frame(form)
    linha_tipo.pack(padx=10, pady=4, fill='x')

    ttk.Label(linha_tipo, text="Tipo", width=18).grid(row=0, column=0, sticky="w")
    tipo_var = tk.StringVar()
    tipo_menu = ttk.Combobox(linha_tipo, textvariable=tipo_var, values=[t.name for t in TipoVeiculo], state="readonly")
    tipo_menu.grid(row=0, column=1, sticky="ew")
    linha_tipo.columnconfigure(1, weight=1)

    # Status
    linha_status = ttk.Frame(form)
    linha_status.pack(padx=10, pady=4, fill='x')

    ttk.Label(linha_status, text="Status", width=18).grid(row=0, column=0, sticky="w")
    status_var = tk.StringVar()
    status_menu = ttk.Combobox(linha_status, textvariable=status_var, values=[s.name for s in StatusVeiculo], state="readonly")
    status_menu.grid(row=0, column=1, sticky="ew")
    linha_status.columnconfigure(1, weight=1)

    def salvar():
        try:
            plate = entradas["Placa"].get()
            mark = entradas["Marca"].get()
            model = entradas["Modelo"].get()
            year = entradas["Ano"].get()
            color = entradas["Cor"].get()
            mileage = entradas["Quilometragem"].get()
            daily_value = entradas["Valor diário"].get()
            sell_value = entradas["Valor de venda"].get()

            tipo = tipo_var.get()
            status = status_var.get()

            # Validação
            if not verify.is_valid_plate(plate): raise ValueError("Placa inválida.")
            if not verify.none_word(mark): raise ValueError("Marca inválida.")
            if not verify.none_word(model): raise ValueError("Modelo inválido.")
            if not verify.is_num(year, int): raise ValueError("Ano inválido.")
            if not verify.none_word(color): raise ValueError("Cor inválida.")
            if not verify.is_num(mileage, float): raise ValueError("Quilometragem inválida.")
            if not verify.is_num(daily_value, float): raise ValueError("Valor diário inválido.")
            if not verify.is_num(sell_value, float): raise ValueError("Valor de venda inválido.")

            tipo_enum = TipoVeiculo[tipo] if tipo else TipoVeiculo.CARRO
            status_enum = StatusVeiculo[status] if status else StatusVeiculo.DISPONIVEL

            carro = Car(
                plate=plate,
                mark=mark,
                model=model,
                year=int(year),
                color=color,
                mileage=float(mileage),
                daily_value=float(daily_value),
                sell_value=float(sell_value),
                type_v=tipo_enum,
                status=status_enum
            )

            addData('db/car.json', carro.car_dict())
            log("Carro foi adicionado")
            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
            form.destroy()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except KeyError:
            messagebox.showerror("Erro", "Tipo ou status inválido.")

    ttk.Button(form, text="Salvar", command=salvar).pack(pady=15)
