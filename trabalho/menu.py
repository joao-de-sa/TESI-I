import tkinter as tk


class Tela:
    def banco(self):
        self.top_banco = tk.Toplevel()
        self.top_banco.title("Banco")
        self.top_banco.geometry('300x150')
        self.janela.grab_set()

        #Botões
        self.btn_cadastrar = tk.Button(self.top_banco, text="Cadastrar")
        self.btn_cadastrar.grid(column=0, row=0)

        self.btn_mostrar = tk.Button(self.top_banco, text="Mostrar")
        self.btn_mostrar.grid(column=1, row=0)

        self.btn_atualizar = tk.Button(self.top_banco, text="Atualizar")
        self.btn_atualizar.grid(column=2, row=0)
    def conta(self):
        self.conta = tk.Toplevel()
        self.conta.title("Conta")
        self.conta.geometry('800x650')
        self.janela.grab_set()

        self.frm_contaCorrente = tk.Frame()
        self.frm_contaCorrente.pack(side=tk.RIGHT)
        self.btn_contaCorrente = tk.Button(self.frm_contaCorrente, text="Conta Corrente")
        self.btn_contaCorrente.pack()

        self.frm_contaPoupanca = tk.Frame()
        self.frm_contaPoupanca.pack(side=tk.RIGHT)
        self.btn_contaPoupanca = tk.Button(self.frm_contaPoupanca, text="Conta Corrente")
        self.btn_contaPoupanca.pack()


    def cliente(self):
        self.btn_cliente = tk.Toplevel()
        self.btn_cliente.title("Banco")
        self.btn_cliente.geometry('300x150')
        self.janela.grab_set()

    def __init__(self, master):
        self.janela = master
        self.janela.title("Menu")
        self.janela.geometry("500x300")
        self.frame_botoes = tk.Frame()
        self.frame_botoes.grid(column=0, row=0)

        #botões
        self.btn_banco = tk.Button(self.janela, text="Banco", command=self.banco)
        self.btn_banco.grid(column=0, row=0)

        self.btn_conta = tk.Button(self.janela, text="Conta", command=self.conta)
        self.btn_conta.grid(column=1, row=0)

        self.btn_cliente = tk.Button(self.janela, text="Cliente", command=self.cliente)
        self.btn_cliente.grid(column=2, row=0)

app = tk.Tk()
Tela(app)
app.mainloop()