import tkinter as tk
from tkinter import ttk, messagebox
from postion import Position
from db import addData
from log_gen import log
import verify


def abrir_formulario_cargo(root):
    form = tk.Toplevel(root)
    form.title("Cadastro de Cargo")
    form.geometry("500x300")

    labels = ["Cargo", "Salário", "Carga Horária", "Comissão (%)"]
    entradas = {}

    for label in labels:
        linha = ttk.Frame(form)
        linha.pack(padx=10, pady=4, fill='x')

        ttk.Label(linha, text=label, width=18).grid(row=0, column=0, sticky="w")
        entrada = ttk.Entry(linha)
        entrada.grid(row=0, column=1, sticky="ew")
        linha.columnconfigure(1, weight=1)

        entradas[label] = entrada

    def salvar():
        try:
            cargo = entradas["Cargo"].get()
            salario = entradas["Salário"].get()
            carga = entradas["Carga Horária"].get()
            comissao = entradas["Comissão (%)"].get()

            # Validações
            if not verify.none_word(cargo): raise ValueError("Cargo inválido.")
            if not verify.is_num(salario, float) or float(salario) <= 0: raise ValueError("Salário inválido.")
            if not verify.is_num(carga, int): raise ValueError("Carga horária inválida.")
            if not verify.is_num(comissao, float) or float(comissao) > 10: raise ValueError("Comissão deve ser <= 10%.")

            position = Position(
                position=cargo,
                wage=float(salario),
                workload=int(carga),
                commission=float(comissao)
            )

            addData('db/Cargos.json', position.position_to_dict())
            log("Cargo foi adicionado")
            messagebox.showinfo("Sucesso", "Cargo cadastrado com sucesso!")
            form.destroy()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(form, text="Salvar", command=salvar).pack(pady=15)
