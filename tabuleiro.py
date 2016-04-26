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
        self.janela.rowconfigure(3, minsize = 50)
        self.janela.columnconfigure(0, minsize = 100)
        self.janela.columnconfigure(1, minsize = 100)
        self.janela.columnconfigure(2, minsize = 100)
        self.janela.columnconfigure(3, minsize = 100)
        
        self.label = tk.Label(self.janela)
        self.label.configure(text="Proximo jogador:1")
        self.label.grid(row=3, column=0, columnspan=3, sticky="nsew")         
        
        self.botao = [[1,2,3],
                       [4,5,6],
                       [7,8,9]]
        
        
        self.botao[0][0] = tk.Button(self.janela)
        self.botao[0][0].grid(row=0,column=0,sticky="nsew")
        self.botao[0][0].configure(command=self.clicar_botao00)
        
        self.botao[0][1] = tk.Button(self.janela)
        self.botao[0][1].grid(row=0,column=1,sticky="nsew")
        self.botao[0][1].configure(command=self.clicar_botao01)
        
        self.botao[0][2]= tk.Button(self.janela)
        self.botao[0][2].grid(row=0,column=2,sticky="nsew")
        self.botao[0][2].configure(command=self.clicar_botao02)
        
        self.botao[1][0]= tk.Button(self.janela)
        self.botao[1][0].grid(row=1,column=0,sticky="nsew")
        self.botao[1][0].configure(command=self.clicar_botao10)
        
        self.botao[2][0]= tk.Button(self.janela)
        self.botao[2][0].grid(row=2,column=0,sticky="nsew")
        self.botao[2][0].configure(command=self.clicar_botao20)
        
        self.botao[1][1] = tk.Button(self.janela)
        self.botao[1][1].grid(row=1,column=1,sticky="nsew")
        self.botao[1][1].configure(command=self.clicar_botao11)
        
        self.botao[1][2] = tk.Button(self.janela)
        self.botao[1][2].grid(row=1,column=2,sticky="nsew")
        self.botao[1][2].configure(command=self.clicar_botao12)
        
        self.botao[2][1]= tk.Button(self.janela)
        self.botao[2][1].grid(row=2,column=1,sticky="nsew")
        self.botao[2][1].configure(command=self.clicar_botao21)
        
        self.botao[2][2] = tk.Button(self.janela)
        self.botao[2][2].grid(row=2,column=2,sticky="nsew")
        self.botao[2][2].configure(command=self.clicar_botao22)
    
    
    def reiniciar(self):
        self.Comandos.limpa_jogadas()
        self.botao[0][0].config(text="")        
        self.botao[0][0].config(state="normal")
        self.botao[0][1].config(text="")        
        self.botao[0][1].config(state="normal")
        self.botao[0][2].config(text="")        
        self.botao[0][2].config(state="normal")
        self.botao[1][0].config(text="")        
        self.botao[1][0].config(state="normal")
        self.botao[2][0].config(text="")        
        self.botao[2][0].config(state="normal")
        self.botao[1][1].config(text="")        
        self.botao[1][1].config(state="normal")
        self.botao[2][1].config(text="")        
        self.botao[2][1].config(state="normal")
        self.botao[1][2].config(text="")        
        self.botao[1][2].config(state="normal")
        self.botao[2][2].config(text="")        
        self.botao[2][2].config(state="normal")        
        
        
 
    def botao_reinicio(self):
         self.reinicio = tk.Button(self.janela)
         self.reinicio.grid(row=3,column=2,sticky="nsew")
         self.reinicio.configure(text="reiniciar")
         self.reinicio.configure(command=self.reiniciar())       
         
       
    def vitoria(self):
        resultado = self.Comandos.verifica_ganhador()
        print (resultado)
        if resultado == 1:
            self.label.configure(text="Jogador 1 ganhou!")
            self.botao_reinicio()
        elif resultado == 2:
            self.label.configure(text="Jogador 2 ganhou")
            self.botao_reinicio()
        elif resultado == 0:
            self.label.configure(text="Empate!")
            self.botao_reinicio()
        else:
            self.label.configure(text="Proximo jogador: {0}".format(self.Comandos.jogador))
        
        
    def clicar_botao00(self):
        if self.Comandos.jogador == 1:
            self.botao[0][0].config(text="x")
        else:
            self.botao[0][0].config(text="o")
        self.Comandos.recebe_jogada(0,0)
        self.vitoria()
        self.botao[0][0].config(state="disable")
    def clicar_botao01(self):        
        if self.Comandos.jogador == 1:
            self.botao[0][1].config(text="x")
        else:
            self.botao[0][1].config(text="o")
        self.Comandos.recebe_jogada(0,1)    
        self.botao[0][1].config(state="disable")
        self.vitoria()
    def clicar_botao02(self):
        if self.Comandos.jogador == 1:
            self.botao[0][2].config(text="x")
        else:
            self.botao[0][2].config(text="o")    
        self.Comandos.recebe_jogada(0,2)
        self.vitoria()
        self.botao[0][2].config(state="disable")
    def clicar_botao10(self):
        if self.Comandos.jogador == 1:
            self.botao[1][0].config(text="x")
        else:
            self.botao[1][0].config(text="o")    
        self.Comandos.recebe_jogada(1,0)
        self.vitoria()
        self.botao[1][0].config(state="disable")
    def clicar_botao20(self):
        if self.Comandos.jogador == 1:
            self.botao[2][0].config(text="x")
        else:
            self.botao[2][0].config(text="o")    
        self.Comandos.recebe_jogada(2,0)
        self.vitoria()
        self.botao[2][0].config(state="disable")
    def clicar_botao11(self):
        if self.Comandos.jogador == 1:
            self.botao[1][1].config(text="x")
        else:
            self.botao[1][1].config(text="o")    
        self.Comandos.recebe_jogada(1,1)
        self.vitoria() 
        self.botao[1][1].config(state="disable")
    def clicar_botao12(self):
        if self.Comandos.jogador == 1:
            self.botao[1][2].config(text="x")
        else:
            self.botao[1][2].config(text="o")    
        self.Comandos.recebe_jogada(1,2)
        self.vitoria() 
        self.botao[1][2].config(state="disable")
    def clicar_botao21(self):
        if self.Comandos.jogador == 1:
            self.botao[2][1].config(text="x")
        else:
            self.botao[2][1].config(text="o")    
        self.Comandos.recebe_jogada(2,1)
        self.vitoria() 
        self.botao[2][1].config(state="disable")
    def clicar_botao22(self):
        if self.Comandos.jogador == 1:
            self.botao[2][2].config(text="x")
        else:
            self.botao[2][2].config(text="o")    
        self.Comandos.recebe_jogada(2,2)
        self.vitoria()             
        self.botao[2][2].config(state="disable")
     
        
     
     
    def iniciar(self):
        self.janela.mainloop()
    
    
        
    
        
app = Tabuleiro()
app.iniciar()




