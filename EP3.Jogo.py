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
                
    def verifica_ganhador():
        if matriz[0][0] and matriz[0][1] and matriz[0][2] == 1:
            print ("jogador 1 ganhou")
            return             
        elif matriz[0][0] and matriz[1][0] and matriz[2][0] == 1:
            print ("jogador 1 ganhou")
            return
        elif matriz[1][0] and matriz[1][1] and matriz[1][2] == 1:
            print("jogador 1 ganhou")
            return
        elif matriz[2][0] and matriz[2][1] and matriz[2][2] == 1:
            print("jogador 1 ganhou")
            return
        elif matriz[0][0] and matriz[1][1] and matriz[2][2] == 1:
            print("jogador 1 ganhou")
            return
        elif matriz[0][1] and matriz[1][1] and matriz[2][1] == 1:
            print("jogador 1 ganhou")
            return
        elif matriz[0][2] and matriz[1][2] and matriz[2][2] == 1:
            print("jogador 1 ganhou")
            return
        elif matriz[2][0] and matriz[1][1] and matriz[0][2] == 1:
            print("jogador 1 ganhou")
            return    
    def limpa_jogadas():
        
        
        