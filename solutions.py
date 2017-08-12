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
from solucoes import lista1 # Importa as soluções

if __name__ == "__main__":
    sys.setrecursionlimit(100000) # A recursão limite do python precisa ser sobreescrita

    LISTA1 = lista1.Lista1() # Instancia as solucoes da lista 1
    print("Questão 15")
    print("Solução: " + str(LISTA1.questao15(1, 1000)))

    print("\nQuestão 16")
    print("Solução: " + str(LISTA1.questao16(-0.15)))
    print("Solução: " + str(round(1.0 / LISTA1.questao16(0.15), 4)))

    print("\nQuestão 17")
    ANS = LISTA1.questao17(1, 10)
    print("Solução: ")
    for key, values in ANS.items():
        print("\t[" + str(key) + "] - " + str(values))

    print("\nQuestão 18")
    print("Solução: " + str(LISTA1.questao18(4, 0.4)))
 
    print("\nQuestão 20")
    print("Solução(Crescente):   " + str(LISTA1.questao20(1, 10000)))
    print("Solução(Decrescente): " + str(LISTA1.questao20(1, 10000, False)))
