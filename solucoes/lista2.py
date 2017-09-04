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

import math # Operações matemáticas

class Lista2(object):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def bissecao(self, func, a, b, tol, n):
        """
		Resolução parcial da questão 1 da lista 2
		----------
		func : function
			Função a ser utilizada nos cálculos
		a : int
			O limite a esquerda
        b : int
			O limite a direita.
        tol : int
			A tolerância do cálculo.
        n : int
			Numero máximo de iterações.
		Returns
		-------
		float
			A raiz procurada
    	"""
        k = 0

        while k <= n:
            c = (a + b) / 2
            if func(c) == 0 or (b - a) / 2 < tol:
                return round(c, 4)
            if func(c) < 0 and func(a) < 0 or func(c) > 0 and func(a) > 0:
                a = c
            else:
                b = c
            k += 1
        return None

    def posicaoFalsa(self, func, a, b, tol, n):
        """
		Resolução parcial da questão 1 da lista 2
		----------
		func : function
			Função a ser utilizada nos cálculos
		a : int
			O limite a esquerda
        b : int
			O limite a direita.
        tol : int
			A tolerância do cálculo.
        n : int
			Numero máximo de iterações.
		Returns
		-------
		float
			A raiz procurada
    	"""
        if func(a) * func(b) < 0:
            k = 0
            c = (a * func(b) - b * func(a)) / (func(b) - func(a))
            while k <= n:
                if abs(func(c)) >= tol:
                    if func(a) * func(b) < 0:
                        b = c
                    else:
                        a = c  
                else:
                    return round(c, 4)
                c = (a * func(b) - b * func(a)) / (func(b) - func(a))
                k += 1
        return None

    def newtonRaphson(self, func, derivative, a, b, tol, n):
        """
		Resolução parcial da questão 1 da lista 2
		----------
		func : function
			Função a ser utilizada nos cálculos
        derivative : function
            Derivad de func
		a : int
			O limite a esquerda
        b : int
			O limite a direita.
        tol : int
			A tolerância do cálculo.
        n : int
			Numero máximo de iterações.
		Returns
		-------
		float
			A raiz procurada
    	"""
        k = 0
        c = a

        while k <= n:
            if abs(func(a)) < tol:
                return round(a, 4)
            b = a - func(a) / derivative(a)
            if abs(func(b)) < tol and abs(b - a) < tol:
                return round(b, 4)
            a = b
            k += 1
    
    def secante(self, func, a, b, tol, n):
        """
		Resolução parcial da questão 1 da lista 2
		----------
		func : function
			Função a ser utilizada nos cálculos
		a : int
			O limite a esquerda
        b : int
			O limite a direita.
        tol : int
			A tolerância do cálculo.
        n : int
			Numero máximo de iterações.
		Returns
		-------
		float
			A raiz procurada
    	"""
        k = 0
        c = 0

        while k <= n:
            if abs(func(a)) > tol or abs(b - a) > tol:
                c = b - (b -a) * (func(b) / (func(b) - func(a)))
                a = b
                b = c
            k += 1
        
        return round(c, 4)