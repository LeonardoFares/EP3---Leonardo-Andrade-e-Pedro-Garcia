# -*- coding: utf-8 -*-
import numpy as np


def matriz0():
    return [[0,0,0],
            [0,0,0],
            [0,0,0]]

class Jogo:
    def __init__(self):
        self.jogador = 1
        self.matriz = matriz0()   

                 
        
        
    def recebe_jogada(self,linha,coluna):
        self.matriz[linha][coluna]=self.jogador     
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
                
    def verifica_ganhador(self):
        for i in range(3):
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] and self.matriz[i][0] != 0:
                return self.matriz[i][0]           
            elif self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] and self.matriz[0][i] != 0:
                return self.matriz[0][i]
        if self.matriz[0][0]==self.matriz[1][1]==self.matriz[2][2] and self.matriz[0][0] != 0:
            return self.matriz[0][0]
        if self.matriz[2][0]==self.matriz[1][1]==self.matriz[0][2] and self.matriz[2][0] != 0:
            return self.matriz[2][0]
        
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == 0:            
                    return -1                    
        return 0
            
    def limpa_jogadas(self):
        self.matriz = matriz0()
        

        
        
        