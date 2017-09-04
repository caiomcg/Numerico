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

import sys # Opções do sistema
from solucoes import Grupo5_Lista1 # Importa as soluções
from solucoes import Grupo5_Lista2 # Importa as soluções da segunda lista

if __name__ == "__main__":
    sys.setrecursionlimit(100000) # A recursão limite do python precisa ser sobreescrita

    LISTA1 = Grupo5_Lista1.Lista1() # Instancia as solucoes da lista 1
    LISTA2 = Grupo5_Lista2.Lista2() # Instancia as solucoes da lista 2

    print("===Lista 1===\n\n")

    print("Questão 15")
    print("Solução: " + str(LISTA1.questao15(1, 1000)))

    print("\nQuestão 16")
    print("Solução: " + str(LISTA1.questao16(-0.15)))
    print("Solução: " + str(round(1.0 / LISTA1.questao16(0.15), 4)))

    print("\nQuestão 17")
    ANS = LISTA1.questao17(1, 10)
    
    print("Solução: ")
    for key, values in ANS.items():
        print("\t[" + str(key) + "] - " + str(round(values, 4)))

    print("\nQuestão 18")
    print("Solução: " + str(LISTA1.questao18(4, 0.4)))
 
    print("\nQuestão 20")
    NROUND      = 1.08232323371
    CRESCENTE   = LISTA1.questao20(1, 10000)
    DECRESCENTE = LISTA1.questao20(1, 10000, False)

    print("Solução(Crescente):   " + str(round(CRESCENTE, 4)))
    print("Solução(Crescente) - Error relativo percentual: " + str(round((((NROUND - CRESCENTE) / CRESCENTE) * 100), 4)) + "%")
    print("Solução(Decrescente): " + str(round(DECRESCENTE, 4)))
    print("Solução(Decrescente) - Error relativo percentual: " + str(round((((NROUND - DECRESCENTE) / DECRESCENTE) * 100), 4)) + "%")

    print("\n\n===Lista 2===\n\n")

    print("Método da bisseção:\n")
    print("Para: f(x) = x^3 - 9x + 3")

    a = lambda x : x**3 - 9*x + 3
    dadx = lambda x : 3*x**2 - 9

    print("\nNo Intervalo [-5, -3]")
    result = LISTA2.bissecao(a, -5, -3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [0, 1]")
    result = LISTA2.bissecao(a, 0, 1, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [2, 3]")
    result = LISTA2.bissecao(a, 2, 3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    #------------------------------------------------------------------

    print("\n\nMétodo da posição falsa:\n")
    print("Para: f(x) = x^3 - 9x + 3")

    print("\nNo Intervalo [-5, -3]")
    result = LISTA2.posicaoFalsa(a, -5, -3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [0, 1]")
    result = LISTA2.posicaoFalsa(a, 0, 1, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [2, 3]")
    result = LISTA2.posicaoFalsa(a, 2, 3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    #------------------------------------------------------------------

    print("\n\nMétodo de Newton-Raphson:\n")
    print("Para: f(x) = x^3 - 9x + 3")

    print("\nNo Intervalo [-5, -3]")
    result = LISTA2.newtonRaphson(a, dadx, -5, -3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [0, 1]")
    result = LISTA2.newtonRaphson(a, dadx, 0, 1, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [2, 3]")
    result = LISTA2.newtonRaphson(a, dadx, 2, 3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))


    #------------------------------------------------------------------

    print("\n\nMétodo da secante:\n")
    print("Para: f(x) = x^3 - 9x + 3")

    print("\nNo Intervalo [-5, -3]")
    result = LISTA2.secante(a, -5, -3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [0, 1]")
    result = LISTA2.secante(a, 0, 1, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))

    print("\nNo Intervalo [2, 3]")
    result = LISTA2.secante(a, 2, 3, 0.001, 11)
    if result == None:
        print("O método falhou")
    else:
        print("Resultado: " + str(result))