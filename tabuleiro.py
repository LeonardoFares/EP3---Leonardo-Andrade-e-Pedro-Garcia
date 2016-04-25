# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:12:53 2016

@author: Leonardo Andrade
"""

import tkinter as tk
import Jogadas

class Tabuleiro:
    #Classe do tabuleiro do jogo da velha
    
    def __init__(self):
        self.Comandos = Jogadas.Jogo()
        self.janela = tk.Tk()  
        self.janela.title("Jogo da Velha")
        self.janela.geometry("300x350+100+100")
        self.janela.rowconfigure(0, minsize = 100)
        self.janela.rowconfigure(1, minsize = 100)
        self.janela.rowconfigure(2, minsize = 100)
        self.janela.rowconfigure(3, minsize = 100)
        self.janela.columnconfigure(0, minsize = 100)
        self.janela.columnconfigure(1, minsize = 100)
        self.janela.columnconfigure(2, minsize = 100)
        self.janela.columnconfigure(3, minsize = 100)
        
        self.botao_0_0 = tk.Button(self.janela)
        self.botao_0_0.grid(row=0,column=0,sticky="nsew")
        
        self.botao_0_1 = tk.Button(self.janela)
        self.botao_0_1.grid(row=0,column=1,sticky="nsew")
        
        self.botao_0_2 = tk.Button(self.janela)
        self.botao_0_2.grid(row=0,column=2,sticky="nsew")
        
        self.botao_1_0 = tk.Button(self.janela)
        self.botao_1_0.grid(row=1,column=0,sticky="nsew")
        
        self.botao_2_0 = tk.Button(self.janela)
        self.botao_2_0.grid(row=2,column=0,sticky="nsew")
        
        self.botao_1_1 = tk.Button(self.janela)
        self.botao_1_1.grid(row=1,column=1,sticky="nsew")
        
        self.botao_1_2 = tk.Button(self.janela)
        self.botao_1_2.grid(row=1,column=2,sticky="nsew")
        
        self.botao_2_1 = tk.Button(self.janela)
        self.botao_2_1.grid(row=2,column=1,sticky="nsew")
        
        self.botao_2_2 = tk.Button(self.janela)
        self.botao_2_2.grid(row=2,column=2,sticky="nsew")
        
        self.label = tk.Label(self.janela)
        self.label.grid(row=3,column=0,columnspan=3,sticky="nsew")
        
        
    def iniciar(self):
        self.janela.mainloop()
    
    def Clicar(self):
        receber_a_jogada = Comandos.recebe_jogadas(linha,coluna)
        self.verifica_ganhador
        self.limpa_jogadas
    
        
app = Tabuleiro()
app.iniciar()




