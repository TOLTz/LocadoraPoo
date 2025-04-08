import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk, messagebox
from person import Client
from address import Address
from db import addData
from log_gen import log
import verify


def abrir_formulario_cliente(root):
    form = tk.Toplevel(root)
    form.title("Cadastro de Cliente")
    form.geometry("550x750")

    labels = [
        "Nome", "Data de nascimento (dd/mm/aaaa)",
        "CPF", "Gênero (M/F)", "Telefone", "Email", "Renda mensal",
        "Rua", "Bairro", "Número", "Cidade", "CEP", "País", "Estado (UF)"
    ]

    entradas = {}

    for label in labels:
        linha = ttk.Frame(form)
        linha.pack(padx=10, pady=4, fill='x')

        ttk.Label(linha, text=label, width=22).grid(row=0, column=0, sticky="w")
        entrada = ttk.Entry(linha)
        entrada.grid(row=0, column=1, sticky="ew")
        linha.columnconfigure(1, weight=1)

        entradas[label] = entrada

    def salvar():
        try:
            # Coletar dados
            nome = entradas["Nome"].get()
            nascimento = entradas["Data de nascimento (dd/mm/aaaa)"].get()
            cpf = entradas["CPF"].get()
            genero = entradas["Gênero (M/F)"].get().upper()
            telefone = entradas["Telefone"].get()
            email = entradas["Email"].get()
            renda = entradas["Renda mensal"].get()

            rua = entradas["Rua"].get()
            bairro = entradas["Bairro"].get()
            numero = entradas["Número"].get()
            cidade = entradas["Cidade"].get()
            cep = entradas["CEP"].get()
            pais = entradas["País"].get()
            estado = entradas["Estado (UF)"].get().upper()

            # Validações
            if not verify.none_word(nome): raise ValueError("Nome inválido.")
            if not verify.is_date(nascimento): raise ValueError("Data inválida.")
            if not verify.is_cpf(cpf): raise ValueError("CPF inválido.")
            if not verify.none_word(genero): raise ValueError("Gênero inválido.")
            if not verify.is_phone(telefone): raise ValueError("Telefone inválido.")
            if not verify.is_email(email): raise ValueError("Email inválido.")
            if not verify.is_num(renda, float): raise ValueError("Renda inválida.")
            if not verify.none_word(estado) or len(estado) != 2: raise ValueError("UF inválida.")

            if not verify.none_word(rua): raise ValueError("Rua inválida.")
            if not verify.none_word(bairro): raise ValueError("Bairro inválido.")
            if not verify.is_num(numero, int): raise ValueError("Número inválido.")
            if not verify.none_word(cidade): raise ValueError("Cidade inválida.")
            if not verify.none_word(cep): raise ValueError("CEP inválido.")
            if not verify.none_word(pais): raise ValueError("País inválido.")

            endereco = Address(
                street=rua,
                district=bairro,
                number=int(numero),
                city=cidade,
                cep=cep,
                country=pais,
                state=estado
            )

            cliente = Client(
                name=nome,
                birthday=nascimento,
                cpf=cpf,
                gender=genero,
                phone=telefone,
                email=email,
                address=endereco,
                income=float(renda)
            )

            addData('db/client.json', cliente.client_dict())
            log("Cliente foi adicionado")
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            form.destroy()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    ttk
