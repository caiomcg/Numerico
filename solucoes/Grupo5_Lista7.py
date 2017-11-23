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
import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
import numpy

class Lista7(Grupo5_ListaX.ListaX):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def __init__(self):
        Grupo5_ListaX.ListaX.__init__(self, "Lista7")

    def __taylor(self, x0, y0, w0, n, first_derivative, second_derivative):
        y = y0
        x = x0
        w = w0
        h = (y - x) / float(n)
        for i in range(0, n):
            w = w + h* ((first_derivative(x, w)) + ((h / 2.0) * (first_derivative(x, w) + second_derivative(x, w))))
            x += h
        return w

    def __previsor_corretor(self, xs, y0, h, func):
        ys = []
        ys.append(y0)

        for x in range(0, len(xs)):
            if x < 2:
                ys.append(ys[x] + h * func(xs[x], ys[x])) #EULER
            if x >= 1:
                ys.append(ys[x-1] + (h/12)*(-func(xs[x-2], ys[x-2]) + 8*func(xs[x-1], ys[x-1]) + 5*func(xs[x], ys[x])))
        return ys[-1]

    def questao01(self, letra, y0, x0, xn, h, lambda_func):
        y=0
        if letra == 'a':
            y=y0
            x_old=x0
            for i in range(0, int(xn/h)+1):
                y_old=y
                y=y_old+h*lambda_func(x_old,y_old)
                x_old=x_old+h
            return y
        elif letra == 'b':
            y=y0
            x_old=x0
            for i in range(0, int(xn/h)+1):
                y_old=y
                y=y_old+2*h*lambda_func(x_old,y_old)
                x_old=x_old+h
            return y
        elif letra == 'e':
            y=y0
            x_old=x0
            for i in range(0, int(xn/h)+1):
                y_old=y
                y=y_old+2*h*lambda_func(x_old+h,y_old+h*lambda_func(x_old,y_old))
                x_old=x_old+h
                #print("x_old= ",x_old)
                #print("y= ",y)
            return y
        elif letra == 'f':
            y=y0
            x_old=x0
            for i in range(0, int(xn/h)+1):
                y_old=y
                y=y_old+h*lambda_func(x_old+h/2,y_old+h*lambda_func(x_old,y_old)/2)
                x_old=x_old+h
            return y
        elif letra == 'g':
            y=y0
            x_old=x0
            for i in range(0, int(xn/h)+1):
                y_old=y
                k1=lambda_func(x_old,y_old)
                k2=lambda_func(x_old+h/2,y_old+k1/2)
                k3=lambda_func(x_old+(3*h)/4,y_old+(3*k2)/4)
                y=y_old+h*(2*k1/9 + 1*k2/3 + 4*k3/9)
                x_old=x_old+h
            return y
        elif letra == 'h':
            y=y0
            x_old=x0
            for i in range(0, int(xn/h)+1):
                y_old=y
                k1=lambda_func(x_old,y_old)
                k2=lambda_func(x_old+h/2,y_old+h*k1/2)
                k3=lambda_func(x_old+h/2,y_old+h*k2/2)
                k4=lambda_func(x_old+h,y_old+h*k3)
                y=y_old+h*(k1 + 2*k2 + 2*k3+k4)/6
                x_old=x_old+h
            return y

    def questao02(self, point_a, point_b, number):
        dx = 1/(number-1.0)
        delta = -1.0
        K = 1.0

        x = numpy.linspace(point_a,point_b,number)

        k = 0.5/100
        TFinal = 1
        NumOfTimeSteps = int(TFinal/k)

        c0 = numpy.transpose([numpy.ones(number)*1.0])

        F = numpy.transpose([numpy.zeros(number)])
        F[-1]=2.0*K*delta*(1.0/dx+1.0)

        A1=numpy.zeros([number])
        A2=numpy.zeros([number])
        A1[0]=0.0
        for i in range(1,number-1):
            array = numpy.zeros([number])
            array[i-1:i-1+3] = [1,-2,1]
            A1=numpy.vstack([A1,array])
            array = numpy.zeros([number])
            array[i-1:i-1+3] = [-1.0,0.0,1.0]
            A2=numpy.vstack([A2,array])
        array = numpy.zeros([number])
        array[-2:]=[2,-2]
        A1=numpy.vstack([A1,array])

        A1=A1*K/dx/dx
        A1=scipy.sparse.csr_matrix(A1)
        array = numpy.zeros([number])
        A2=numpy.vstack([A2,array])

        A2=A2*2.0*K/2.0/dx
        A2=scipy.sparse.csr_matrix(A2)

        data = []


        I = sparse.identity(number)


        for i in range(NumOfTimeSteps):
            A = (I - k/2.0*A1 - k/2.0*A2)
            b = (I + k/2.0*A1 + k/2.0*A2)*c0+k*F
            c0 = numpy.transpose(numpy.mat(sparse.linalg.spsolve(A, b)))

            data.append(c0)

        print("\n\nAproximações")
        print(c0[:,-1])
        
    def questao03(self, point_a, point_b, number):                
        h = (point_b - point_a)/(number-1)
        y = numpy.zeros(number)
        x = [float for i in range(0,number)]

        for i in range(0, number):
            x[i] = h*i

        y[0] = point_a
        y[number-1] = point_b                

        for i in range(0, number-1):
            y[i+1] = -y[i-1] + y[i]*(2+h**2*(numpy.sin(y[i]+i*h)))

        for i in range(0, number):
            print(y[i])    

    def test(self):
        """
        Define todos os testes da lista
        """

        print("\n\nQuestão 1\n")
        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("a) y= ",self.questao01('a', 2, 0, 0.3,0.1, lambda x,y : (-y+x+2)))

        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("b) y= ",self.questao01('b', 2, 0, 0.3,0.1, lambda x,y : (-y+x+2)))

        print("\nPVI")
        print("y'=y-x**2+1=f(x,y), xE[0,2]")
        print("y(0)=0,5, h=0.2")
        print("c) y= ",self.__taylor(0, 2, 0.5, 10, lambda x,y : (y-x**2+1), lambda x,y : (-2*x)))

        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("d) y= ", self.__previsor_corretor([0, 0.1, 0.2, 0.3], 2, 0.1,lambda x,y : (-y+x+2)))

        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("e) y= ",self.questao01('e', 2, 0, 0.3,0.1, lambda x,y : (-y+x+2)))

        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("f) y= ",self.questao01('f', 2, 0, 0.3,0.1, lambda x,y : (-y+x+2)))

        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("g) y= ",self.questao01('g', 2, 0, 0.3,0.1, lambda x,y : (-y+x+2)))

        print("\nPVI")
        print("y'=-y+x+2=f(x,y), xE[0,0.3]")
        print("y(0)=2, h=0.1")
        print("h) y= ",self.questao01('h', 2, 0, 0.3,0.1, lambda x,y : (-y+x+2)))


        print("\n\nQuestão 2\n")
        print("\nMetodo das diferenças Finitas para N = 10 e intervalo [0,1]")
        self.questao02(0, 1, 10)
        
        print("\n\nQuestão 3\n")
        print("\nMetodo das diferenças Finitas para N = 10 e intervalo [1,5]")
        self.questao03(1, 5, 10)     
        
