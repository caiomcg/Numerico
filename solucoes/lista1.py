#!/usr/bin/env python
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

import math # Operações matemáticas

class Lista1(object):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def questao15(self, initial=0, final=0):
        """
		Resolução da questão 15
		----------
		initial : int
			O limite inferiro do somatório.
		final : int
			O limite superior do somatório.
		Returns
		-------
		float
			O resultado do somatório
    	"""
        if initial <= final: # Realiza o calculo até que a condição de parada seja atingida
            return round((initial * (initial + 1)) / 2.0, 4) + self.questao15(initial + 1, final) # Efetua o calculo: 
			# i(i + 1) / 2 e chama a função recursivamente até que a condição de parada seja atingida
        return 0 # Para a recursão

    def questao16(self, value, counter=1):
        """
		Resolução da questão 16 e 19
		----------
		value : float
			O valor a ser utilizado na função
		Returns
		-------
		float
			O resultado da função exponencial elevada a x
    	"""
        if counter <= 2: # Se a iteração estiver em seu 1º ou 2º loop tratamos os casos especiais
            return round(1 if counter == 1 else value, 4) + self.questao16(value, counter + 1) # Tratamos e chamamos recursivamente
        elif counter <= 25: # Realiza o calculo até que a condição de parada seja atingida
            return round(value ** (counter - 1) / math.factorial(counter-1), 4) + self.questao16(value, counter + 1) # Efetua o calculo:
			# 1 + x + + (x^2)/2! + (x^n)/n! + ... e chama a função recursivamente até que a condição de parada seja atingida
        return 0 # Para a recursão

    def questao17(self, initial, final):
        """
		Resolução da questão 17
		----------
		initial : int
			O limite inferiro do somatório.
		final : int
			O limite superior do somatório.
		Returns
		-------
		float
			O resultado do somatório
    	"""
        calculate = lambda x: round(math.cos((3 * math.pi * x) / 4) * (2.0 / x ** 2), 4) # Definimos a função que retorna o valor da equação
        results = {} # Dictionary onde os resultados serão mantidos

        for x in range(initial, final+1): # Iteramos sobre os limites do somatório
            if x == 1: # No primeiro elemento simplesmente calculamos e inserimos no dictionary
                results[x] = calculate(x) # Calcula, arredonda e insere
            else: # Para os demais
                results[x] = (results[x-1] + calculate(x)) # Calculamos o novo e somamos aos elementos anteriores

        return results # Retornamos os resultados

    def questao18(self, radius, scale):
        """
		Resolução da questão 18
		----------
		radius : int
			O raio da esfera.
		scale : int
			O valor a escalar a esfera.
		Returns
		-------
		float
			O raio de uma esfera com volume x% maior
    	"""
        volume = self.__volume(radius) # Calculamos o volume da esfera de raio x
        return round(self.__radius(volume + volume * scale), 4) # Calculamos o raio para a nova esfera 



    def questao20(self, initial, final, increase=True):
        """
		Resolução da questão 20
		----------
		initial : int
			O limite inferiro do somatório.
		final : int
			O limite superior do somatório.
		Returns
		-------
		float
			O resultado do somatório
    	"""
        if increase: # Mudar para um somatorio negativo se for falso
            if initial <= final: # Realiza o calculo até que a condição de parada seja atingida
                return round(1.0 / initial ** 4, 4) + self.questao20(initial + 1, final) # Calculamos recursivamente
            else: # Se o limite superior for ultrapassado
                return 0 # Para a recursão
        else:
            if final >= initial: # Realiza o calculo até que a condição de parada seja atingida
                return round(1.0 / final ** 4, 4) + self.questao20(initial, final-1, False) # Calculamos recursivamente
            else: # Se o limite superior for ultrapassado
                return 0 # Para a recursão

    def __volume(self, radius):
        """
		Calcula o volume de uma esfera
		----------
		radius : float
			O raio da esfera
		Returns
		-------
		float
			O volume da esfera
    	"""
        return (4/3.0) * math.pi * (radius ** 3) # Calculo do volume de uma esfera

    def __radius(self, volume):
        """
		Calcula o raio de uma esfera
		----------
		volume : float
			O volume da esfera
		Returns
		-------
		float
			O raio da esfera
    	"""
        return ((3 * volume)  / (4 * math.pi)) ** (1/3.0) # Calculo do raio de uma esfera