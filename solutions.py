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
"""
from solucoes import Grupo5_Lista1 # Importa as soluções da primeira lista
from solucoes import Grupo5_Lista2 # Importa as soluções da segunda lista
from solucoes import Grupo5_Lista3 # Importa as soluções da terceira lista
from solucoes import Grupo5_Lista4 # Importa as soluções da quarta lista
from solucoes import Grupo5_Lista5 # Importa as soluções da quinta lista
from solucoes import Grupo5_Lista6 # Importa as soluções da sexta lista
"""
from solucoes import Grupo5_Lista7 # Importa as soluções da setima lista

if __name__ == "__main__":
    sys.setrecursionlimit(100000) # A recursão limite do python precisa ser sobreescrita

    LISTAS = [] # Armazena todas as lista e as executa em sequência

    """
    LISTAS.append(Grupo5_Lista1.Lista1()) # Instancia as solucoes da lista 1
    LISTAS.append(Grupo5_Lista2.Lista2()) # Instancia as solucoes da lista 2
    LISTAS.append(Grupo5_Lista3.Lista3()) # Instancia as solucoes da lista 3
    LISTAS.append(Grupo5_Lista4.Lista4()) # Instancia as solucoes da lista 4
    LISTAS.append(Grupo5_Lista5.Lista5()) # Instancia as solucoes da lista 5
    LISTAS.append(Grupo5_Lista6.Lista6()) # Instancia as solucoes da lista 6
    """
    LISTAS.append(Grupo5_Lista7.Lista7()) # Instancia as solucoes da lista 7

    for lista in LISTAS:
        print("\n\n --- " + str(lista.getname()) + "---\n\n")
        try:
            lista.test()
        except:
            pass
        print("\n\n------------------------------------\n")
