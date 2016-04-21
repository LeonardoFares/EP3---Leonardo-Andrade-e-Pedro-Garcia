# -*- coding: utf-8 -*-
import numpy as np
class Jogo:
    def __init__(self):
        self.jogador = 1
        self.matriz = np.zeros([3,3])                
        
        
    def recebe_jogada(self,linha,coluna):
        self.matriz[linha][coluna]=self.jogador     
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
                
    def verifica_ganhador(self):
        if self.matriz[0][0] == 1 and self.matriz[0][1] == 1 and self.matriz[0][2] == 1:
            return 1            
        elif self.matriz[0][0] == 1 and self.matriz[1][0] == 1 and self.matriz[2][0] == 1:
            return 1
        elif self.matriz[1][0] == 1 and self.matriz[1][1] == 1 and self.matriz[1][2] == 1:
            return 1
        elif self.matriz[2][0] == 1 and self.matriz[2][1] == 1 and self.matriz[2][2] == 1:
            return 1
        elif self.matriz[0][0] == 1 and self.matriz[1][1] == 1 and self.matriz[2][2] == 1:
            return 1
        elif self.matriz[0][1] == 1 and self.matriz[1][1] == 1 and self.matriz[2][1] == 1:
            return 1
        elif self.matriz[0][2] == 1 and self.matriz[1][2] == 1 and self.matriz[2][2] == 1:
            return 1
        elif self.matriz[2][0] == 1 and self.matriz[1][1] == 1 and self.matriz[0][2] == 1:
            return 1
        elif self.matriz[0][0] == 2 and self.matriz[0][1] == 2 and self.matriz[0][2] == 2:
            return 2            
        elif self.matriz[0][0] == 2 and self.matriz[1][0] == 2 and self.matriz[2][0] == 2:
            return 2
        elif self.matriz[1][0] == 2 and self.matriz[1][1] == 2 and self.matriz[1][2] == 2:
            return 2
        elif self.matriz[2][0] == 2 and self.matriz[2][1] == 2 and self.matriz[2][2] == 2:
            return 2
        elif self.matriz[0][0] == 2 and self.matriz[1][1] == 2 and self.matriz[2][2] == 2:
            return 2
        elif self.matriz[0][1] == 2 and self.matriz[1][1] == 2 and self.matriz[2][1] == 2:
            return 2
        elif self.matriz[0][2] == 2 and self.matriz[1][2] == 2 and self.matriz[2][2] == 2:
            return 2
        elif self.matriz[2][0] == 2 and self.matriz[1][1] == 2 and self.matriz[0][2] == 2:
            return 2  
        elif self.matriz 
            return 0
            
    def limpa_jogadas(self):
        self.matriz = np.zeros([3,3])

        
        
        