import os.path
import sys
import tkinter as tk
import tkinter.ttk as ttk
from calendar import month_name
from tkinter import messagebox

import PIL.Image
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas

_script = sys.argv[0]
_location = os.path.dirname(_script)
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

_style_code_ran = 0


def _style_code():
    global _style_code_ran
    if _style_code_ran:
        return
    style = ttk.Style()
    if sys.platform == "win32":
        style.theme_use('winnative')
    style.configure('.', background=_bgcolor)
    style.configure('.', foreground=_fgcolor)
    style.configure('.', font='TkDefaultFont')
    style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
    if _bgmode == 'dark':
        style.map('.', foreground=[('selected', 'white'), ('active', 'white')])
    else:
        style.map('.', foreground=[('selected', 'black'), ('active', 'black')])
    _style_code_ran = 1


def salvar_pdf(self):
    # Obter dados do formulário
    nome = self.entry_name.get()
    cpf_cnpjoto = self.entry_cpfcnpj.get()
    email = self.entry_email.get()
    adubo = self.entry_adubo.get()
    quantidade= self.entry_quantidade.get()
    valor = self.entry_valor.get()
    status = self.entry_status.get()
    emissão= self.entry_emissao.get()
    nf = self.entry_nf.get()
    peso = self.entry_veiculo.get()
    dia = self.entry_dia.get()
    mes = self.entry_mes.get()
    ano = self.entry_ano.get()

    # Validar se todos os campos foram preenchidos
    if not nome or not email or not cpf_cnpjoto:
        messagebox.showwarning("Aviso", "Preencha todos os campos!!")
        return

    # Nome do arquivo PDF
    nome_arquivo = f"{nome}_dados_formulario.pdf"

    # Criar PDF
    pdf = canvas.Canvas(nome_arquivo)

    # Adicionar  elementos ao PDF
    pdf.drawImage('G:\\pythonProject1\\logopdf.png', 100, 780, width=420, height=100)
    pdf.drawString(100, 700, f"Nome: {nome}")
    pdf.drawString(100, 680, f"Email: {email}")
    pdf.drawString(100, 660, f"CPF/CNPJ: {cpf_cnpjoto}")
    pdf.drawString(100, 640, f"email: {email}")
    pdf.drawString(100, 620, f"Tipo do adubo: {adubo}")
    pdf.drawString(100, 600, f"Quantidade do Produto(toneladas): {quantidade}")
    pdf.drawString(100, 580, f"Valor total(R$): {valor}")
    pdf.drawString(100, 560, f"Status do Pedido: {status}")
    pdf.drawString(100, 540, f"Responsável pela emissão: {emissão}")
    pdf.drawString(100, 520, f"Número da NF: {nf}")
    pdf.drawString(100, 500, f"Peso total do veículo(Toneladas) : {peso}")
    pdf.drawString(100, 480, f"{dia} de {mes} de {ano}")
    pdf.save()
    messagebox.showinfo("Concluído", f"Os dados foram salvos em {nome_arquivo}")

def limpar_formulario(self):
    self.entry_name.delete(0, tk.END)
    self.entry_cpfcnpj.delete(0, tk.END)
    self.entry_email.delete(0, tk.END)
    self.entry_adubo.delete(0, tk.END)
    self.entry_quantidade.delete(0, tk.END)
    self.entry_valor.delete(0, tk.END)
    self.entry_status.delete(0, tk.END)
    self.entry_emissao.delete(0, tk.END)
    self.entry_nf.delete(0, tk.END)
    self.entry_veiculo.delete(0, tk.END)
    self.entry_dia.delete(0, tk.END)
    self.entry_mes.delete(0, tk.END)
    self.entry_ano.delete(0, tk.END)

class Toplevel1:
    def __init__(self, top=None):
        top = tk.Tk()
        top.geometry('600x450+498+229')
        top.iconbitmap("G:\\pythonProject1\\adubologo.png")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(False, False)
        top.title("Formulário de Controle de Saída")
        top.configure(background="#000000")


        self= tk.StringVar()
        self.top=top

        self.combobox = tk.StringVar()
        self.combobox2 = tk.StringVar()
        self.combobox3 = tk.StringVar()
        self.combobox4 = tk.StringVar()
        self.combobox5 = tk.StringVar()

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.3, rely=0.044, height=20, width=400)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Times New Roman} -size 19 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Controle de Saída''')

        '''***************************************Nome Cliente*******************************************'''
        self.nome_cliente = tk.Label(self.top)
        self.nome_cliente.place(relx=0.017, rely=0.2, height=21, width=124)
        self.nome_cliente.configure(anchor='w')
        self.nome_cliente.configure(background="#000000")
        self.nome_cliente.configure(compound='left')
        self.nome_cliente.configure(cursor="fleur")
        self.nome_cliente.configure(disabledforeground="#a3a3a3")
        self.nome_cliente.configure(font="-family {Times New Roman} -size 12")
        self.nome_cliente.configure(foreground="#ffffff")
        self.nome_cliente.configure(text='''Nome Cliente:''')
        self.entry_name = tk.Entry(self.top)
        self.entry_name.place(relx=0.167, rely=0.2, height=20, relwidth=0.373)
        self.entry_name.configure(background="white")
        self.entry_name.configure(disabledforeground="#a3a3a3")
        self.entry_name.configure(font="TkFixedFont")
        self.entry_name.configure(foreground="#000000")
        self.entry_name.configure(insertbackground="black")

        '''***********************************************CPF/CNPJ*******************************************'''
        self.cff_cnpj = tk.Label(self.top)
        self.cff_cnpj.place(relx=0.567, rely=0.2, height=21, width=124)
        self.cff_cnpj.configure(activebackground="#f9f9f9")
        self.cff_cnpj.configure(anchor='w')
        self.cff_cnpj.configure(background="#000000")
        self.cff_cnpj.configure(compound='left')
        self.cff_cnpj.configure(disabledforeground="#a3a3a3")
        self.cff_cnpj.configure(font="-family {Times New Roman} -size 12")
        self.cff_cnpj.configure(foreground="#ffffff")
        self.cff_cnpj.configure(highlightbackground="#d9d9d9")
        self.cff_cnpj.configure(highlightcolor="black")
        self.cff_cnpj.configure(text='''CNPJ/CPF:''')
        self.entry_cpfcnpj = tk.Entry(self.top)
        self.entry_cpfcnpj.place(relx=0.717, rely=0.2, height=20, relwidth=0.257)
        self.entry_cpfcnpj.configure(background="white")
        self.entry_cpfcnpj.configure(disabledforeground="#a3a3a3")
        self.entry_cpfcnpj.configure(font="TkFixedFont")
        self.entry_cpfcnpj.configure(foreground="#000000")
        self.entry_cpfcnpj.configure(highlightbackground="#d9d9d9")
        self.entry_cpfcnpj.configure(highlightcolor="black")
        self.entry_cpfcnpj.configure(insertbackground="black")
        self.entry_cpfcnpj.configure(selectbackground="#c4c4c4")
        self.entry_cpfcnpj.configure(selectforeground="black")

        '''*********************************************Endereço*******************************************'''
        self.email = tk.Label(self.top)
        self.email.place(relx=0.017, rely=0.289, height=21, width=124)
        self.email.configure(activebackground="#f9f9f9")
        self.email.configure(anchor='w')
        self.email.configure(background="#000000")
        self.email.configure(compound='left')
        self.email.configure(disabledforeground="#a3a3a3")
        self.email.configure(font="-family {Times New Roman} -size 12")
        self.email.configure(foreground="#ffffff")
        self.email.configure(highlightbackground="#d9d9d9")
        self.email.configure(highlightcolor="black")
        self.email.configure(text='''Email:''')
        self.entry_email = tk.Entry(self.top)
        self.entry_email.place(relx=0.133, rely=0.289, height=20
                                  , relwidth=0.407)
        self.entry_email.configure(background="white")
        self.entry_email.configure(disabledforeground="#a3a3a3")
        self.entry_email.configure(font="TkFixedFont")
        self.entry_email.configure(foreground="#000000")
        self.entry_email.configure(highlightbackground="#d9d9d9")
        self.entry_email.configure(highlightcolor="black")
        self.entry_email.configure(insertbackground="black")
        self.entry_email.configure(selectbackground="#c4c4c4")
        self.entry_email.configure(selectforeground="black")

        '''***********************************************Tipos de Adubos*******************************************'''
        self.tipo_adubo = tk.Label(self.top)
        self.tipo_adubo.place(relx=0.55, rely=0.289, height=21, width=114)
        self.tipo_adubo.configure(activebackground="#f9f9f9")
        self.tipo_adubo.configure(anchor='w')
        self.tipo_adubo.configure(background="#000000")
        self.tipo_adubo.configure(compound='left')
        self.tipo_adubo.configure(disabledforeground="#a3a3a3")
        self.tipo_adubo.configure(font="-family {Times New Roman} -size 12")
        self.tipo_adubo.configure(foreground="#ffffff")
        self.tipo_adubo.configure(highlightbackground="#d9d9d9")
        self.tipo_adubo.configure(highlightcolor="black")
        self.tipo_adubo.configure(text='''Tipo de adubo:''')
        _style_code()
        self.entry_adubo = ttk.Combobox(self.top)
        self.entry_adubo.place(relx=0.733, rely=0.289, relheight=0.047
                               , relwidth=0.238)
        self.entry_adubo.configure(textvariable=self.combobox, values="00.18.18 00.20.10 00.20.15 00.20.18 00.20.20 "
                                                                      "0.20.30 00.25.25 00.28.20 00.30.10 00.30.10"
                                                                      " 00.30.20 02.16.08")
        self.entry_adubo.configure(takefocus="")
        self.entry_adubo.configure(cursor="fleur")

        '''*********************************************Quantidade*******************************************'''
        self.quantidade = tk.Label(self.top)
        self.quantidade.place(relx=0.017, rely=0.378, height=21, width=144)
        self.quantidade.configure(activebackground="#f9f9f9")
        self.quantidade.configure(anchor='w')
        self.quantidade.configure(background="#000000")
        self.quantidade.configure(compound='left')
        self.quantidade.configure(disabledforeground="#a3a3a3")
        self.quantidade.configure(font="-family {Times New Roman} -size 12")
        self.quantidade.configure(foreground="#ffffff")
        self.quantidade.configure(highlightbackground="#d9d9d9")
        self.quantidade.configure(highlightcolor="black")
        self.quantidade.configure(text='''Quntidade(toneladas):''')
        self.entry_quantidade = tk.Entry(self.top)
        self.entry_quantidade.place(relx=0.25, rely=0.378, height=20
                                    , relwidth=0.257)
        self.entry_quantidade.configure(background="white")
        self.entry_quantidade.configure(disabledforeground="#a3a3a3")
        self.entry_quantidade.configure(font="TkFixedFont")
        self.entry_quantidade.configure(foreground="#000000")
        self.entry_quantidade.configure(highlightbackground="#d9d9d9")
        self.entry_quantidade.configure(highlightcolor="black")
        self.entry_quantidade.configure(insertbackground="black")
        self.entry_quantidade.configure(selectbackground="#c4c4c4")
        self.entry_quantidade.configure(selectforeground="black")

        '''**********************************************VALOR R$******************************************'''
        self.valor = tk.Label(self.top)
        self.valor.place(relx=0.517, rely=0.378, height=21, width=144)
        self.valor.configure(activebackground="#f9f9f9")
        self.valor.configure(anchor='w')
        self.valor.configure(background="#000000")
        self.valor.configure(compound='left')
        self.valor.configure(disabledforeground="#a3a3a3")
        self.valor.configure(font="-family {Times New Roman} -size 12")
        self.valor.configure(foreground="#ffffff")
        self.valor.configure(highlightbackground="#d9d9d9")
        self.valor.configure(highlightcolor="black")
        self.valor.configure(text='''Valor Total (R$):''')
        self.entry_valor = tk.Entry(self.top)
        self.entry_valor.place(relx=0.717, rely=0.378, height=20, relwidth=0.257)
        self.entry_valor.configure(background="white")
        self.entry_valor.configure(disabledforeground="#a3a3a3")
        self.entry_valor.configure(font="TkFixedFont")
        self.entry_valor.configure(foreground="#000000")
        self.entry_valor.configure(highlightbackground="#d9d9d9")
        self.entry_valor.configure(highlightcolor="black")
        self.entry_valor.configure(insertbackground="black")
        self.entry_valor.configure(selectbackground="#c4c4c4")
        self.entry_valor.configure(selectforeground="black")
        self.entry_valor.configure(textvariable=self)

        '''*****************************************************Status pedido*******************************************'''
        self.status = tk.Label(self.top)
        self.status.place(relx=0.017, rely=0.467, height=21, width=144)
        self.status.configure(activebackground="#f9f9f9")
        self.status.configure(anchor='w')
        self.status.configure(background="#000000")
        self.status.configure(compound='left')
        self.status.configure(cursor="fleur")
        self.status.configure(disabledforeground="#a3a3a3")
        self.status.configure(font="-family {Times New Roman} -size 12")
        self.status.configure(foreground="#ffffff")
        self.status.configure(highlightbackground="#d9d9d9")
        self.status.configure(highlightcolor="black")
        self.status.configure(text='''Status do pedido:''')
        self.entry_status = ttk.Combobox(self.top)
        self.entry_status.place(relx=0.217, rely=0.467, relheight=0.047
                                , relwidth=0.238)
        self.entry_status.configure(textvariable=self.combobox2, values=('Concluído Processando Inicado'))
        self.entry_status.configure(takefocus="")
        self.entry_status.configure(cursor="fleur")

        '''*****************************************Responsável Emissão*******************************************'''
        self.emissao = tk.Label(self.top)
        self.emissao.place(relx=0.45, rely=0.467, height=21, width=184)
        self.emissao.configure(activebackground="#f9f9f9")
        self.emissao.configure(anchor='w')
        self.emissao.configure(background="#000000")
        self.emissao.configure(compound='left')
        self.emissao.configure(disabledforeground="#a3a3a3")
        self.emissao.configure(font="-family {Times New Roman} -size 12")
        self.emissao.configure(foreground="#ffffff")
        self.emissao.configure(highlightbackground="#d9d9d9")
        self.emissao.configure(highlightcolor="black")
        self.emissao.configure(text='''Responsável pela emissão:''')
        self.entry_emissao = tk.Entry(self.top)
        self.entry_emissao.place(relx=0.733, rely=0.467, height=20
                                 , relwidth=0.257)
        self.entry_emissao.configure(background="white")
        self.entry_emissao.configure(cursor="fleur")
        self.entry_emissao.configure(disabledforeground="#a3a3a3")
        self.entry_emissao.configure(font="TkFixedFont")
        self.entry_emissao.configure(foreground="#000000")
        self.entry_emissao.configure(highlightbackground="#d9d9d9")
        self.entry_emissao.configure(highlightcolor="black")
        self.entry_emissao.configure(insertbackground="black")
        self.entry_emissao.configure(selectbackground="#c4c4c4")
        self.entry_emissao.configure(selectforeground="black")

        '''*****************************************************NF*******************************************'''
        self.NF = tk.Label(self.top)
        self.NF.place(relx=0.017, rely=0.556, height=21, width=94)
        self.NF.configure(activebackground="#f9f9f9")
        self.NF.configure(anchor='w')
        self.NF.configure(background="#000000")
        self.NF.configure(compound='left')
        self.NF.configure(cursor="fleur")
        self.NF.configure(disabledforeground="#a3a3a3")
        self.NF.configure(font="-family {Times New Roman} -size 12")
        self.NF.configure(foreground="#ffffff")
        self.NF.configure(highlightbackground="#d9d9d9")
        self.NF.configure(highlightcolor="black")
        self.NF.configure(text='''Número NF:''')
        self.entry_nf = tk.Entry(self.top)
        self.entry_nf.place(relx=0.183, rely=0.556, height=20, relwidth=0.257)
        self.entry_nf.configure(background="white")
        self.entry_nf.configure(cursor="fleur")
        self.entry_nf.configure(disabledforeground="#a3a3a3")
        self.entry_nf.configure(font="TkFixedFont")
        self.entry_nf.configure(foreground="#000000")
        self.entry_nf.configure(highlightbackground="#d9d9d9")
        self.entry_nf.configure(highlightcolor="black")
        self.entry_nf.configure(insertbackground="black")
        self.entry_nf.configure(selectbackground="#c4c4c4")
        self.entry_nf.configure(selectforeground="black")

        '''*****************************************************Veículo*******************************************'''
        self.peso_veiculo = tk.Label(self.top)
        self.peso_veiculo.place(relx=0.45, rely=0.556, height=21, width=174)
        self.peso_veiculo.configure(activebackground="#f9f9f9")
        self.peso_veiculo.configure(anchor='w')
        self.peso_veiculo.configure(background="#000000")
        self.peso_veiculo.configure(compound='left')
        self.peso_veiculo.configure(disabledforeground="#a3a3a3")
        self.peso_veiculo.configure(font="-family {Times New Roman} -size 12")
        self.peso_veiculo.configure(foreground="#ffffff")
        self.peso_veiculo.configure(highlightbackground="#d9d9d9")
        self.peso_veiculo.configure(highlightcolor="black")
        self.peso_veiculo.configure(text='''Peso Total do Veículo(T):''')
        self.entry_veiculo = tk.Entry(self.top)
        self.entry_veiculo.place(relx=0.733, rely=0.556, height=20, relwidth=0.257)
        self.entry_veiculo.configure(background="white")
        self.entry_veiculo.configure(disabledforeground="#a3a3a3")
        self.entry_veiculo.configure(font="TkFixedFont")
        self.entry_veiculo.configure(foreground="#000000")
        self.entry_veiculo.configure(highlightbackground="#d9d9d9")
        self.entry_veiculo.configure(highlightcolor="black")
        self.entry_veiculo.configure(insertbackground="black")
        self.entry_veiculo.configure(selectbackground="#c4c4c4")
        self.entry_veiculo.configure(selectforeground="black")

        '''*****************************************************Data*******************************************'''
        self.entry_dia = ttk.Combobox(self.top)
        self.entry_dia.place(relx=0.083, rely=0.667, relheight=0.047, relwidth=0.172)
        self.entry_dia.configure(textvariable=self.combobox3, values=[str(i).zfill(2) for i in range(1, 32)])
        self.entry_dia.configure(takefocus="")
        self.de_data = tk.Label(self.top)
        self.de_data.place(relx=0.267, rely=0.667, height=21, width=44)
        self.de_data.configure(activebackground="#f9f9f9")
        self.de_data.configure(anchor='w')
        self.de_data.configure(background="#000000")
        self.de_data.configure(compound='left')
        self.de_data.configure(cursor="fleur")
        self.de_data.configure(disabledforeground="#a3a3a3")
        self.de_data.configure(font="-family {Times New Roman} -size 12")
        self.de_data.configure(foreground="#ffffff")
        self.de_data.configure(highlightbackground="#d9d9d9")
        self.de_data.configure(highlightcolor="black")
        self.de_data.configure(text='''De''')

        self.entry_mes = ttk.Combobox(self.top)
        self.entry_mes.place(relx=0.367, rely=0.667, relheight=0.047, relwidth=0.172)
        month_names = list(month_name[1:])
        options = [f" {month}" for month in month_names]
        self.entry_mes.configure(textvariable=self.combobox4, values=options)
        self.entry_mes.configure(takefocus="")

        self.de = tk.Label(self.top)
        self.de.place(relx=0.55, rely=0.667, height=21, width=44)
        self.de.configure(activebackground="#f9f9f9")
        self.de.configure(anchor='w')
        self.de.configure(background="#000000")
        self.de.configure(compound='left')
        self.de.configure(disabledforeground="#a3a3a3")
        self.de.configure(font="-family {Times New Roman} -size 12")
        self.de.configure(foreground="#ffffff")
        self.de.configure(highlightbackground="#d9d9d9")
        self.de.configure(highlightcolor="black")
        self.de.configure(text='''De''')

        self.entry_ano = ttk.Combobox(self.top)
        self.entry_ano.place(relx=0.65, rely=0.667, relheight=0.047, relwidth=0.172)
        years = [str(year) for year in range(2023, 2101)]
        option_yers = [f"{year}"  for year in years]
        self.entry_ano.configure(textvariable=self.combobox5, values=option_yers)
        self.entry_ano.configure(takefocus="")

        '''*************************************************Botões*******************************************'''

        self.Button1 = tk.Button(self.top, command=lambda :salvar_pdf(self))
        self.Button1.place(relx=0.267, rely=0.822, height=24, width=97)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#008000")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Times New Roman} -size 13 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Gerar''')


        self.Button1_1 = tk.Button(self.top, command=lambda :limpar_formulario(self))
        self.Button1_1.place(relx=0.5, rely=0.822, height=24, width=97)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(activeforeground="black")
        self.Button1_1.configure(background="#ff0000")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Times New Roman} -size 13 -weight bold")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Limpar''')


        self.top.mainloop()
if __name__ == "__main__":
     Toplevel1()

