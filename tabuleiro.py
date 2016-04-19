# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:12:53 2016

@author: Leonardo Andrade
"""

import tkinter as tk
import numpy as np

class Tabuleiro:
    #Classe do tabuleiro do jogo da velha
    
    def __init__(self):
        self.janela = tk.Tk()  
        self.janela.title("Jogo da Velha")
        self.janela.geometry("400x400+100+100")
        self.janela.rowconfigure(0, minsize = 50)
        self.janela.rowconfigure(1, minsize = 50)
        self.janela.columnconfigure(0, minsize = 50)
        self.janela.columnconfigure(1, minsize = 50)
        
    def iniciar(self):
        self.janela.mainloop()
        
        
        
        self.matriz_botoes = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        for i in range (0,3):
            for j in range(0,3):
                self.matriz_botoes[i][j] = tk.Button(self.janela)
                self.matriz_botoes.grid(row = i, column = j, columnspan = 2, sticky = "nsew")
        
        
app = Tabuleiro()
app.iniciar()