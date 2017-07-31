#!/usr/bin/env python

"""
sadasdas
"""
import math

class Lista1(object):
    """
    bla bola
    """
    def __init__(self):
        """
        bla
        """
        pass
    def questao15(self, initial=0.0, final=0.0):
        """ 
        bla
        """
        if initial <= final:
            amount = (initial*(initial+1))/2.0
            return amount + self.questao15(initial + 1, final)
        else:
            return 0

    def questao16(self, value, counter=1):
        """
        bla
        """
        if counter <= 2:
            return (1 if counter == 1 else value) + self.questao16(value, counter + 1)
        elif counter <= 25:
            return (value ** (counter - 1) / math.factorial(counter-1)) + self.questao16(value, counter + 1)
        else:
            return 0

    def questao17(self, initial, final):
        """
        bla
        """
        return "Doing"