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
        if self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == self.jogador:
            return self.jogador           
        elif self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == self.jogador:
            return self.jogador
        elif self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == self.jogador:
            return self.jogador
        elif self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == self.jogador:
            return self.jogador
        elif self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == self.jogador:
            return self.jogador
        elif self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == self.jogador:
            return self.jogador
        elif self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == self.jogador:
            return self.jogador
        elif self.matriz[2][0] == self.matriz[1][1] == self.matriz[0][2] == self.jogador:
            return self.jogador
        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.matriz[i][j] != 0:            
                        valor = 0
                    else:
                        valor = -1
            return valor
            
    def limpa_jogadas(self):
        self.matriz = np.zeros([3,3])

        
        
        