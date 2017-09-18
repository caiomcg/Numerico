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

Copyright (c) 2016 Caio Marcelo Campoy Guedes, Diego Filipe Souza de Lima, 
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

class Lista3(Grupo5_ListaX.ListaX):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def __init__(self):
        Grupo5_ListaX.ListaX.__init__(self, "Lista3")

    def questao01_a(self, matriz_A, vetor_b):
        
        """
        documentar
        Método de Eliminação de Gauss ( http://www.dcc.ufrj.br/~rincon/Disciplinas/Algebra%20Linear/Aula_013.pdf )

        matriz_A : matriz de coeficientes

        vetor_b : "matriz" de veriaveis livres.

        retorno: solução do sistema

    
        """
        if len(matriz_A) != len(vetor_b):
            return None
        matrizExtendida = matriz_A[:]
        for i in range(len(matrizExtendida)):
            matrizExtendida[i].append(vetor_b[i])

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
        """
        pass
        """
    def questao01_b(self):
        """
        documentar
        """
        pass

    def questao01_c(self):
        """
        documentar
        """
        pass

    def questao01_d(self):
        """
        documentar
        """
        pass

    def questao01_e(self):
        """
        documentar
        """
        pass

    def questao01_f(self):
        """
        documentar
        """
        pass

    def questao01_g(self):
        """
        documentar
        """
        pass

    def questao01_h(self):
        """
        documentar
        """
        pass

    def test(self):
        """
        Define todos os testes da lista
        """

        print("Eliminação de Gauss simples:\n")
        print("Para:\n")
        print("[1 -1 2 2]")
        print("[2 1 -1 1]")
        print("[-2 -5 3 3]")
        matriz = []
        linha = [1, -1, 2]
        matriz.append(linha)
        linha = [2, 1, -1]
        matriz.append(linha)
        linha = [-2, -5, 3]
        matriz.append(linha)
        vetor=[2, 1, 3]
        
        result = self.questao01_a(matriz, vetor)
        if result == None:
            print("O método falhou")
        else:
            print("solucao:")
            print(result)


        #------------------------------------------------------------------
