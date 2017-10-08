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

    def questao01(self, matriz_A, vetor_b):
        
        """
        documentar
      
    
        """
        """
       ###### Trecho para obtenção da matriz extendida
        
        if len(matriz_A) != len(vetor_b):
            return None
        matrizExtendida = matriz_A[:]
        for i in range(len(matrizExtendida)):
            matrizExtendida[i].append(vetor_b[i])
        ######

            
        for i in range(len(matrizExtendida)):
           # print(i)
           # print("pivo:", matrizExtendida[i][i])
            #print((len(matrizExtendida)-i))
            for j in range((i+1),(len(matrizExtendida)), 1):
              #  print(j)
                if matrizExtendida[i][i] != 0:
                    c = matrizExtendida[j][i]/matrizExtendida[i][i]
                    #print(c)
                    if c != 0:
                        for k in range(len(matrizExtendida[i])):
                            matrizExtendida[j][k]-=c*matrizExtendida[i][k]
                else:
                    return None
        #return matrizExtendida
        solucoes=[]
        solucoes.append(matrizExtendida[len(matrizExtendida)-1][len(matrizExtendida)]/matrizExtendida[len(matrizExtendida)-1][len(matrizExtendida)-1])
        #for i in matrizExtendida: # matriz triangular
        #        print(i)
        for i in range(len(matrizExtendida)-2,-1,-1):
            c=0
            for j in range(len(solucoes)):
                c+=solucoes[j]*matrizExtendida[i][len(matrizExtendida)-1-j]
            solucoes.append((matrizExtendida[i][len(matrizExtendida)]-c)/matrizExtendida[i][i])
        solucoes.reverse()
        return solucoes
        
        pass
        """
    def questao02(self, matriz_A, vetor_b):
             
        """
        documentar
        Método de Eliminação de Gauss ( http://www.dcc.ufrj.br/~rincon/Disciplinas/Algebra%20Linear/Aula_013.pdf )

        matriz_A : matriz de coeficientes

        vetor_b : "matriz" de veriaveis livres.

        retorno: solução do sistema

    
        """
        """

        ###### Trecho para obtenção da matriz extendida
        
        if len(matriz_A) != len(vetor_b):
            return None
        matrizExtendida = matriz_A[:]
        for i in range(len(matrizExtendida)):
            matrizExtendida[i].append(vetor_b[i])
        ######
            
        maiorEmModulo=0
        for i in range(len(matrizExtendida)):
            for i2 in range(i, len(matrizExtendida),1):
                if abs(matrizExtendida[i2][i])>matrizExtendida[maiorEmModulo][i]:
                    maiorEmModulo=i2
            matrizExtendida.insert(i,matrizExtendida.pop(maiorEmModulo))
         #   print(matrizExtendida[i])
            for j in range((i+1),(len(matrizExtendida)), 1):
              #  print(j)
                if matrizExtendida[i][i] != 0:
                    c = matrizExtendida[j][i]/matrizExtendida[i][i]
                    if c != 0:
                        for k in range(len(matrizExtendida[i])):
                            matrizExtendida[j][k]-=c*matrizExtendida[i][k]
                else:
                    return None
        
        solucoes=[]
        solucoes.append(matrizExtendida[len(matrizExtendida)-1][len(matrizExtendida)]/matrizExtendida[len(matrizExtendida)-1][len(matrizExtendida)-1])
      #  for i in matrizExtendida: # matriz triangular
      #         print(i)
        for i in range(len(matrizExtendida)-2,-1,-1):
            c=0
            for j in range(len(solucoes)):
                c+=solucoes[j]*matrizExtendida[i][len(matrizExtendida)-1-j]
            solucoes.append((matrizExtendida[i][len(matrizExtendida)]-c)/matrizExtendida[i][i])
        solucoes.reverse()
        return solucoes
    """
    def questao03(self, matrix):
        """
        documentar
        """
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
    
        return L, matrix
"""
    def questao04(self, matrix):
        """
        documentar
        """
"""
        size = len(matrix)
        L = [[1 if x == y else 0 for y in range(size)] for x in range(size)]

        maiorEmModulo=0

        for i in range(size):
            for i2 in range(i, size,1):
                if abs(matrix[i2][i])>matrix[maiorEmModulo][i]:
                    maiorEmModulo=i2
            matrix.insert(i,matrix.pop(maiorEmModulo))
            for j in range((i+1),(size), 1):
                if matrix[i][i] != 0:
                    c = matrix[j][i]/matrix[i][i]
                    L[j][i] = c
                    if c != 0:
                        for k in range(len(matrix[i])):
                            matrix[j][k]-=c*matrix[i][k]

        return L, matrix
"""
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
        return L, U, x, y
        """

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
        return L, U, x, y
        """
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
        return L, U, x, y
        """
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
    def test(self):
        """
        Define todos os testes da lista
        """
       
        result = self.questao01(matriz, vetor)
        if result == None:
            print("O método falhou")
        else:
            print("solucao:")
            print(result)

