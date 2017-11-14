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

import math

class Lista6(Grupo5_ListaX.ListaX):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def __init__(self):
        Grupo5_ListaX.ListaX.__init__(self, "Lista6")

    def __getDx(self, a, b):
        return (b - a) / 2.0

    def __gaussianQuadractureTwoPoints(self, equation, a=0.0, b=1.0,):
        X1 = math.sqrt(3)/3.0
        X2 = -X1

        if a != -1 and b != 1:
            dx = self.__getDx(a,b)
            x = lambda a, b, t : (a + b + t * a - t * b) / 2.0
            return (dx * equation(x(a, b, X1)) + equation(x(a, b, X2)))
        else:
            return (equation(X1) + equation(X2))

        return None

    def __gaussianQuadractureThreePoints(self, equation, a=0.0, b=1.0,):
        X1 = math.sqrt(3/5.0)
        X2 = -X1
        X3 = 0

        A1 = A2 = 5 / 9.0
        A3 = 8 / 9.0

        if a != -1 and b != 1:
            dx = self.__getDx(a,b)
            x = lambda a, b, t : (a + b + t * a - t * b) / 2.0
            return (dx * (A1 * equation(x(a, b, X1)) + A3 * equation(x(a, b, X3)) + A2 * equation(x(a, b, X2))))
        else:
            return (A1 * equation(X1) + A3 * equation(X2) + A2 * equation(X3))

        return None           

    def questao01(a, b, n, lambda_func):
        h = (b-a)/n
        soma = lambda_func(a)
        for i in range(1, n):
           soma = soma + 2*lambda_func(h*i)
        soma = soma + lambda_func(b)
        ITR = (h/2)*soma
        return ITR

    def questao02(a, b, n, lambda_func):
        h = (b-a)/n
        soma = lambda_func(a)
        #i impar
        for i in range(1, n, 2):
            soma = soma + 4*lambda_func(h*i)
        #i par
        for i in range(2, n, 2):
            soma = soma + 2*lambda_func(h*i)
        soma = soma + lambda_func(b)
        ISR = (h/3)*soma
        return ISR

    def questao3(self, equation, a=0.0, b=1.0, n=1):
        if n == 2:
            return self.__gaussianQuadractureTwoPoints(equation, a, b)
        elif n == 3:
            return self.__gaussianQuadractureThreePoints(equation, a, b)

    def test(self):
        """
        Define todos os testes da lista
        """

        print("\n\nQuestão 1\n")
        
        #print(self.questao01(0, 1, 10, lambda x : math.exp(x)))
        #print(self.questao01(0, 1, 10, lambda x : x**2))

        print("\n\nQuestão 2\n")
        
        #print(questao02(0, 1, 10, lambda x : math.exp(x)))
        #print(questao02(0, 1, 10, lambda x : x**2))

        print("\n\nQuestão 3\n")

        print("Para 2 pontos:\n\n")

        print("Integral de -1 a 1 e equação: sqrt(2 - x**2)")
        print("Resposta: {}\n".format(self.questao3(lambda x: math.sqrt(2 - x**2), -1, 1, 2)))
        print("Integral de 0 a 10 e equação: e**(-x))")
        print("Resposta: {}\n".format(self.questao3(lambda x: math.e**(-x), 0, 10, 2)))

        print("\n\nQuestão 4\n")

        print("Para 3 pontos:\n\n")

        print("Integral de 2 a 3 e equação: x / (1 + x ** 4)")
        print("Resposta: {}\n".format(self.questao3(lambda x: x / (1 + x ** 4), 2, 3, 3)))
