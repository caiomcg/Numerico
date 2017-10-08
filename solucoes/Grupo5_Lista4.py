#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Caio Marcelo Campoy Guedes
E-Mail: caiomcg@gmail.com

Author: Diego Filipe Souza de Lima 
E-Mail: diegooo_felipe@hotmail.com

Author: Germano Martins de Souza
E-Mail: germano_nino@hotmail.com

Author: Kevin Vieira Lucena Veloso
E-Mail: kevinveloso@gmail.com

Author: Richelieu Ramos de Andrade Costa
E-Mail: richelieu.costa@eng.ci.ufpb.br

Author: Thiago Luiz Pereira Nunes
E-Mail: thiago.luiz@lavid.ufpb.br

License:
MIT License

Copyright (c) 2017 Caio Marcelo Campoy Guedes, Diego Filipe Souza de Lima, 
                   Germano Martins de Souza, Kevin Vieira Lucena Veloso,
                   Richelieu Ramos de Andrade Costa, Thiago Luiz Pereira Nunes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from solucoes import Grupo5_ListaX

import math

class Lista4(Grupo5_ListaX.ListaX):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def __init__(self):
        Grupo5_ListaX.ListaX.__init__(self, "Lista4")

    def questao01(self, matriz_A, vetor_x_k, vetor_b):

        for i in range(len(matriz_A)):
            if matriz_A[i][i]== 0:
                print("coeficiente nulo na diagonal principal")
                return None
        alfa=vetor_x_k[:]
        for i in range(len(matriz_A)):
            alfa[i]=0
            for j in range(0,i,1):
                #print(matriz_A[i][j])
                alfa[i]+=abs(matriz_A[i][j])
            for j in range(i+1,len(matriz_A),1):
                #print(matriz_A[i][j])
                alfa[i]+=abs(matriz_A[i][j])
            alfa[i]/=abs(matriz_A[i][i])
            if alfa[i] >= 1 :
                print("alfa: ",alfa[i])
                return "não se pode afirmar a convergencia"
            return "ok"
        """
        pass
        """
    def questao02(self, matriz_A, vetor_x_k, vetor_b):
        if self.questao01(matriz_A, vetor_x_k, vetor_b) == None:
            print("coeficiente nulo na diagonal principal")
            return None
        vetor_x_k1=vetor_x_k[:]
        for iterecoes in range(0,20, 1): # A questão não expecificou nenhum parametro sobre quando parar
            vetor_x_k=vetor_x_k1[:]
            for i in range(len(matriz_A)):
                vetor_x_k1[i]=0
                
                for j in range(0,i,1):
                    #print(matriz_A[i][j]," * ", vetor_x_k[j])
                    vetor_x_k1[i]-=matriz_A[i][j]*vetor_x_k[j]
                    
                for j in range(i+1,len(matriz_A),1):
                    #print(matriz_A[i][j]," * ", vetor_x_k[j])
                    vetor_x_k1[i]-=matriz_A[i][j]*vetor_x_k[j]

                vetor_x_k1[i]+=vetor_b[i]
                vetor_x_k1[i]/=matriz_A[i][i]

        return vetor_x_k1
    
    def questao03(self, matriz_A, vetor_x_k, vetor_b):
        """
        documentar
        """
        # a letra i que varre o beta tem o range da dimenssão N da matriz
        beta=vetor_x_k[:]
        for i in range(len(matriz_A)):
            beta[i]=0
            for j in range(0,i,1):
                #print(matriz_A[i][j])
                beta[i]+=abs(matriz_A[i][j])*beta[i]
            for j in range(i+1,len(matriz_A),1):
                #print(matriz_A[i][j])
                beta[i]+=abs(matriz_A[i][j])
            beta[i]/=abs(matriz_A[i][i])
            if beta[i] >= 1 :
                print("beta: ",beta[i])
                return "não se pode afirmar a convergencia"
        return "ok"
        """
        size = len(matrix)
        L = [[1 if x == y else 0 for y in range(size)] for x in range(size)]

        for i in range(size):
            for j in range(i+1, size):
                if matrix[i][i] != 0:
                    c = matrix[j][i]/matrix[i][i]
                    L[j][i] = c
                    matrix[j][i] = 0
                    if c != 0:
                        for k in range(i+1, size):
                            matrix[j][k]-=c*matrix[i][k]
        """
       

    def questao04(self, matriz_A, vetor_x_k, vetor_b):
        """
        documentar
        """
        if self.questao01(matriz_A, vetor_x_k, vetor_b) == None:
            print("Não passou no Critério das linhas")
            if self.questao03(matriz_A, vetor_x_k, vetor_b) == None:
                print("Não passou no Critério de Sassenfeld")
                return None
        vetor_x_k1=vetor_x_k[:]
        for iterecoes in range(0,20, 1): # A questão não expecificou nenhum parametro sobre quando parar
            vetor_x_k=vetor_x_k1[:]
            for i in range(len(matriz_A)):
                vetor_x_k1[i]=0
                
                for j in range(0,i,1):
                    #print(matriz_A[i][j]," * ", vetor_x_k1[j])
                    vetor_x_k1[i]-=matriz_A[i][j]*vetor_x_k1[j]
                    
                for j in range(i+1,len(matriz_A),1):
                    #print(matriz_A[i][j]," * ", vetor_x_k[j])
                    vetor_x_k1[i]-=matriz_A[i][j]*vetor_x_k[j]

                vetor_x_k1[i]+=vetor_b[i]
                vetor_x_k1[i]/=matriz_A[i][i]

        return vetor_x_k1
    
    def questao05(self, matrix, vector):
        """
        documentar
        """
        """
        size = len(matrix)
        L = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
        U = matrix

        x = [0, 0, 0]
        y = [0, 0, 0]

        mult = 0.0

        for i in range(1, size):
            for j in range(i):
                mult = U[i][j]/U[j][j]
                L[i][j] = mult
                for k in range(size):
                    U[i][k] -= mult * U[j][k]

        for i in range(size):
            y[i] = vector[i]
            for j in range(i):
                y[i] -= L[i][j]*y[j]

        for i in range(size-1, -1, -1):
            x[i] = vector[i]
            for j in range(i, size, -1):
                x[i] -= L[i][j]*x[j]
        """
        pass
        return None

    def questao06(self, matrix, vector):
        """
        documentar
        """
        """
        size = len(matrix)
        L = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
        U = matrix

        x = [0, 0, 0]
        y = [0, 0, 0]

        mult = 0.0

        for i in range(1, size):
            for j in range(i):
                mult = U[i][j]/U[j][j]
                L[i][j] = mult
                for k in range(size):
                    U[i][k] -= mult * U[j][k]

        for i in range(size):
            y[i] = vector[i]
            for j in range(i):
                y[i] -= L[i][j]*y[j]

        for i in range(size-1, -1, -1):
            x[i] = vector[i]
            for j in range(i, size, -1):
                x[i] -= L[i][j]*x[j]
        """
        pass
        return None

    def questao07(self, matrix, vector):
        """
        documentar
        """
        """
        size = len(matrix)
        L = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
        U = matrix

        x = [0, 0, 0]
        y = [0, 0, 0]

        mult = 0.0

        for i in range(1, size):
            for j in range(i):
                mult = U[i][j]/U[j][j]
                L[i][j] = mult
                for k in range(size):
                    U[i][k] -= mult * U[j][k]

        for i in range(size):
            y[i] = vector[i]
            for j in range(i):
                y[i] -= L[i][j]*y[j]

        for i in range(size-1, -1, -1):
            x[i] = vector[i]
            for j in range(i, size, -1):
                x[i] -= L[i][j]*x[j]
        """
        pass
        return None

    def questao08(self, matrix, vector):
        """
        documentar
        """
        """
        size = len(matrix)
        L = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
        U = matrix

        x = [0, 0, 0]
        y = [0, 0, 0]

        mult = 0.0

        for i in range(1, size):
            for j in range(i):
                mult = U[i][j]/U[j][j]
                L[i][j] = mult
                for k in range(size):
                    U[i][k] -= mult * U[j][k]

        for i in range(size):
            y[i] = vector[i]
            for j in range(i):
                y[i] -= L[i][j]*y[j]

        for i in range(size-1, -1, -1):
            x[i] = vector[i]
            for j in range(i, size, -1):
                x[i] -= L[i][j]*x[j]
        return L, U, x, y
        """
        return None

    def test(self):
        """
        Define todos os testes da lista
        """
        matriz_A= [[1, 1], [1, -3]]
        vetor_x_k=[0.7, -1.6]
        vetor_b=[3, -3]
        print(matriz_A)
        print(vetor_x_k)
        print(vetor_b)
        result = self.questao01(matriz_A, vetor_x_k, vetor_b)
        if result == None:
            print("O método falhou")
        else:
            print("solucao q_01:")
            print(result)
        matriz_A= [[10, 2, 1], [1, 5, 1], [2, 3, 10]]
        vetor_x_k=[0.7, -1.6, 0.6]
        vetor_b=[7, -8, 6]
        print(matriz_A)
        print(vetor_x_k)
        print(vetor_b)
        result = self.questao02(matriz_A, vetor_x_k, vetor_b)
        if result == None:
            print("O método falhou")
        else:
            print("solucao q_02:")
            print(result)

        matriz_A= [[1, 0.5, -0.1, 0.1], [0.2, 1, -0.2, -0.1],[-0.1, -0.2, 1, 0.2],[0.1, 0.3, 0.2, 1]]
        vetor_x_k=[0.7, 1, 1, -1.6]
        vetor_b=[0.2, -2.6, 1, -2.5]
        print(matriz_A)
        print(vetor_x_k)
        print(vetor_b)
        result = self.questao03(matriz_A, vetor_x_k, vetor_b)
        if result == None:
            print("O método falhou")
        else:
            print("solucao q_03:")
            print(result)

        matriz_A= [[2, 1, 3], [0, -1, 1], [1, 0, 3]]
        vetor_x_k=[0.7, -1.6, 0.6]
        vetor_b=[9, 1, 3]
        print(matriz_A)
        print(vetor_x_k)
        print(vetor_b)
        result = self.questao03(matriz_A, vetor_x_k, vetor_b)
        if result == None:
            print("O método falhou")
        else:
            print("solucao q_03:")
            print(result)

        matriz_A= [[10, 2, 1], [1, 5, 1], [2, 3, 10]]
        vetor_x_k=[0.7, -1.6, 0.6]
        vetor_b=[7, -8, 6]
        print(matriz_A)
        print(vetor_x_k)
        print(vetor_b)
        result = self.questao04(matriz_A, vetor_x_k, vetor_b)
        if result == None:
            print("O método falhou")
        else:
            print("solucao q_04:")
            print(result)

