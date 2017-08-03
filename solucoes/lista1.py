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

import math

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
        if initial <= final:
            return round((initial * (initial + 1)) / 2.0, 4) + self.questao15(initial + 1, final)
        return 0

    def questao16(self, value, counter=1):
        """
		Resolução da questão 16
		----------
		initial : float
			O valor a ser utilizado na função
		Returns
		-------
		float
			O resultado do somatório
    	"""
        if counter <= 2:
            return round(1 if counter == 1 else value, 4) + self.questao16(value, counter + 1)
        elif counter <= 25:
            return round(value ** (counter - 1) / math.factorial(counter-1), 4) + self.questao16(value, counter + 1)
        return 0

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
        if initial <= final:
            return round(math.cos((3 * math.pi * initial) / 4)* (2 / initial ** 2), 4) + self.questao17(initial + 1, final)
        return 0

    def questao18(self, radius, scale):
        """
		Resolução da questão 18
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
        volume = self.__volume(radius)
        return self.__radius(volume * scale)



    def questao19(self, initial, final, increase=True):
        """
		Resolução da questão 18
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
        if increase:
            if initial <= final:
                return round(1.0 / initial ** 4, 4) + self.questao19(initial + 1, final)
            else:
                return 0
        else:
            if final >= initial:
                return round(1.0 / final ** 4, 4) + self.questao19(initial, final-1, False)
            else: 
                return 0

    def __volume(self, radius):
        return (4/3.0) * math.pi * (radius ** 3)

    def __radius(self, volume):
        return ((3 * volume)  / (4 * math.pi)) ** (1/3.0)