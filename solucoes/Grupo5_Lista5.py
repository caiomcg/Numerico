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

from matplotlib import pyplot as plt
from matplotlib import style
from numpy.linalg import inv
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import FormatStrFormatter
import tkinter as tk
from tkinter import Label, LabelFrame, Entry, Text, Button, Listbox

import numpy as np


"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Questão 2º(SEGUNDA) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
class Lista5(Grupo5_ListaX.ListaX):
    """
    As questões implementadas consistem em metodos desta classe.
    """
    def __init__(self):
        Grupo5_ListaX.ListaX.__init__(self, "Lista5")
        # Assign matplotlib backend to TK
        matplotlib.use("TkAgg")
        # Create top level window object and variables
        self.window = tk.Tk()

    def drawgraph(self, xtabela, functabela, xtheta, functheta): 
        # functabela: valores da função
        # xtabela: valores de x
        # funtheta: Valores da função com os coeficientes   
        # Inicia o gráfico
        figgraph = Figure(figsize=(10, 10), dpi=60)
        # Gráfico 2D: 1 Loluna, 1 Linha, 1 Plotagem
        axes = figgraph.add_subplot(111)
        # Exite 4 casas decimais no gráfico
        axes.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
        # Plota o Gráfico
        axes.plot(xtabela, functabela, 'ro') # Plota os pontos
        axes.plot(xtheta, functheta) # Plota o polinômio ajuste
        # Canvas placed in main frame, controlled by figgraph
        self.window.canvas = FigureCanvasTkAgg(figgraph, master=self.window.mainframe)
        self.window.canvas.get_tk_widget().place(relx=0.26, rely=0.01, relheight=0.46, relwidth=0.74)
        self.window.canvas.draw()    


    def calculaphi(self, n, x):
        # Calcula o valor de uma linha de phi
        componentes = n+1 #Um polinômio de grau n possui n + 1 componentes
        arr = np.zeros(componentes) # Cria o array das componentes de x
        for i in range(0, componentes):
            arr[i] = x**n #Cada valor de x é elevado a uma potência, exemplo, em uma função linear t~em f(x) = ax + b, o valor de a é multiplicado por x^1 e b por x^0 
            n = n - 1 #A próxima componente tem um grau menor
        phi = np.array(arr) 
        return phi

    def calculate(self, p, n, pontos, funcpontos):
        phi = np.empty(shape=[p, n+1])
        # Itera cada linha para preencher a matriz phi
        for i in range(0, p):        
            phi[i] = self.calculaphi(n, pontos[i])
            
        phitransposta = np.transpose(phi)    

        #Fórmula: theta = inv(phitransposta*phi)*phitransposta*g
        tmp1 = phitransposta.dot(phi)
        invtmp1 = inv(tmp1)
        tmp2 = invtmp1.dot(phitransposta)
        theta = tmp2.dot(funcpontos)    
        np.set_printoptions(precision=4) #Seta a precisão para 4 casas decimais
        np.set_printoptions(suppress=True) #Suprime a notação científica
        print(theta)
        
        #calcula os valores de theta para cada x    
        maxponto = int(abs(max(pontos.min(), pontos.max(), key=abs)*2))
        qtdpontos = 100 # Quantidade de pontos para exibir o polinômio ajuste
        pontostheta = np.linspace(-maxponto, maxponto, qtdpontos) # Valores da função theta em pontos no invervalo do máximo valor absoluto*10
        functheta = [float for i in range(0, len(pontostheta))] #Valores da função theta nos pontos
        for i in range(0, len(pontostheta)):        
            functheta[i] = 0
            grau = n
            for j in range(0, n+1):
                functheta[i] = functheta[i] + (theta[j]*(pontostheta[i]**grau)) #Soma as componentes do polinômio
                grau = grau - 1            

        self.drawgraph(pontos, funcpontos, pontostheta, functheta)

    def gauss_elimination(self, a, b):

        # number of lines
        n = len(b)

        # limination progressive

        # k: Coluna atual
        for k in range(0, n - 1):
            # i: current line
            # from de second line (k + 1)
            for i in range(k + 1, n):
                # don't execute i line if Aik be 0
                if a[i, k] != 0.0:
                    fator = a[i, k] / a[k, k]
                    # the k column from current line will be replaced to 0
                    # the k column is ignored, because your values are irrelevant
                    # Then, initialize it by column 2 (k+1)
                    a[i, k + 1: n] = a[i, k + 1: n] - fator * a[k, k + 1: n]
                    b[i] = b[i] - fator * b[k]

        # Regressive replacement like the definition
        # Finds the value from each coefficient
        for k in range(n - 1, -1, -1):
            b[k] = (b[k] - np.dot(a[k, k + 1: n], b[k + 1: n])) / a[k, k]
        return b

    """ 
    <<<<<<<<<<<<<<<<<<<< Functions to be used >>>>>>>>>>>>>>>>>>>>>
    """
    def show_polynomial(self, coeff_poly):

        print('{0:.4f}'.format(coeff_poly[0]), end='  ')
        # Each index means one coefficient and a polynomial degree
        for i in range(1, len(coeff_poly)):
            # Negative coefficient
            if coeff_poly[i] < 0:
                print(' -', end=' ')
            # Positive coefficient
            else:
                print(' +', end=' ')

            print('{0:.4f}'.format(coeff_poly[i]), end=' (x^')
            print(i, end=')')
        print(end='\n\n')


    def plot_polynomial2(self, points_x, points_y, coeff):
        """
            Show function of the a polynomial with soft curves
        """

        # coeff

        m = len(coeff)
        x1 = min(points_x)
        x2 = max(points_x)
        dx = (x2 - x1) / 20.0

        x = np.arange(x1, x2 + dx / 10.0, dx)
        y = np.zeros((len(x))) * 1.0

        for i in range(m):
            y = y + coeff[i] * x ** i

        # show

        plt.plot(points_x, points_y, x, y, '-')
        plt.xlabel('Axis x')
        plt.ylabel('Axis y')
        plt.grid(True)
    plt.show()


    """
        Continuous case
    """

    def f_(self, x):
        return 4 * (x ** 3)


    def a11(self, x):
        return x


    def a12(self, x):
        return (x ** 2) / 2


    def a22(self, x):
        return (x ** 3) / 3


    def b1(self, x):
        return x ** 4


    def b2(self, x):
        return 4 * (x ** 5) / 5


    def continuous_minimum_square(self, grau, a, b):

        # Matrix size according with the polynomial degree wanted
        m = np.empty([grau + 1, grau + 1])

        print('Polynomial degree: ' + str(grau))
        print('Interval: ', end='')
        print('(a, b) = (', end='')
        print(a, end=', ')
        print(b, end=')\n\n')

        # Fills the matrix with an integral from g(x) product
        # g(x)*g(x)

        # a11
        gg = self.a11(b) - self.a11(a)
        m[0][0] = gg

        # a12 = a21
        gg = self.a12(b) - self.a12(a)
        # Fills symmetrically
        m[0][1] = gg
        m[1][0] = gg

        # a22
        gg = self.a22(b) - self.a22(a)
        m[1][1] = gg

        # The independent vector v from Mx = v
        v = np.empty([grau + 1])

        v[0] = self.b1(b) - self.b1(a)
        v[1] = self.b2(b) - self.b1(a)

        print('Symmetrical matrix', end='\n\n')
        print(m)
        print()
        print('Independent vector', end='\n\n')
        print(v)
        print()

        # We have a system Mx = v
        # Resolving with Gauss Elimination

        # Finds the values of the coefficients from polynomial
        return self.gauss_elimination(m, v)


    # ------------------ running ------------------

    def test(self):
        """
        Define todos os testes da lista
        """

        # Decimal precision from Numpy package
        np.set_printoptions(precision=4)

        print('------- Problem 2 -------', end='\n\n')

        # 4x^3
        coeff_real = np.array([0, 0, 0, 4])
        print('Polynomial real')
        self.show_polynomial(coeff_real)
        print()

        coeff_ajuste = self.continuous_minimum_square(1, 0, 1)
        print('Adjust polynomial')
        self.show_polynomial(coeff_ajuste)
        print()

        print('------- Problem 1 -------', end='\n\n')

        k_points = 2
        # Start array with k intevals
        # linspace(begin, end, inteval)
        x = np.linspace(0, 0.4, num=k_points)
        y = np.linspace(0, 0.4, num=k_points)

        self.plot_polynomial2(x, y, coeff_real)

        # a matplotlib graph will be thrown in here on getMarketHistory
        self.window.mainframe = LabelFrame(self.window, text="Main")
        self.window.mainframe.place(relx=0.01, rely=0.08, relheight=0.77, relwidth=0.99)

        #points = np.array([-1.0, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5,   0.7,    1]) # Tabela de pontos
        #g =      np.array([2.05, 1.153, 0.45,  0.4,  0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]) # Valores da função nos pontos
        #n = 2 # Grau n do polinômio ajuste
        #points = np.array([  -20,    10,    70])
        #g =      np.array([0.128, 0.134, 0.144])
        #n = 1
        points = np.array([-1, -0.5,   0, 0.5,   1])
        g =      np.array([ 2,    1, 0.5,   2, 1.5])
        n = 2

        p = len(points) # Quantidade de pontos da tabela

        # Calcula theta e exibe o gráfico
        self.calculate(p, n, points, g)

        self.window.mainloop()
