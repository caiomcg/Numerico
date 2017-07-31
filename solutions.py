#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
asdasd
"""
import sys
from solucoes import lista1

sys.setrecursionlimit(10000) # A recursão limite do python precisa ser sobreescrita


LISTA1 = lista1.Lista1()

print("Questão 15")
print("Solução: " + str(LISTA1.questao15(1, 1000)))

print("\nQuestão 16")
print("Solução: " + str(LISTA1.questao16(-0.15)))

print("\nQuestão 17")
print("Solução: " + str(LISTA1.questao17(1, 2)))