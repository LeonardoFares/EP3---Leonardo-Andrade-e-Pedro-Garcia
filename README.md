# EP3---Leonardo-Andrade-e-Pedro-Garcia
Exercício Programa 3 - Design de Software - Leonardo Andrade e Pedro Garcia

import tkinter as tk
import numpy as np

class Tabuleiro:
    "Classe do tabuleiro do jogo da velha"
    def __init__(self):
        self.janela = tk.Tk()  
        self.janela.title("Jogo da Velha")
        
        
        matriz_botoes = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range (0,3):
            for j in range(0,3):
                matriz_botoes[i][j] = tk.Button(self.janela)

        
    def iniciar(self):
        self.janela.mainloop()
        
        
app = Tabuleiro()
app.iniciar()
