#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jeff Nivitanont, U. Wyoming 2022
import types
import inspect
import numpy as np

class Bisector:
    def __init__(self):
        self.left = 0
        self.right = 1
        self.fxn = lambda x: x
        self.target = None
        self.soln = None
        self.delta = 1e-3
        self.i_lim = 1e3

    def __str__(self):
        code, __ = inspect.getsourcelines(self.fxn)
        funcprint = ''.join(code)
        return f'Start and End points are {self.left} and {self.right}\nFunction: {funcprint}\nTarget: {self.target}\nSolution: {self.soln}'

    def setFxn(self, fxn):
        if isinstance(fxn, types.FunctionType):
            self.fxn = fxn
        else:
            raise TypeError('Fxn must be type FunctionType.')

    def setTarget(self, tgt):
        self.target = tgt

    def setBounds(self, _l, _r):
        self.left = _l
        self.right = _r

    def bisect(self):
            a = self.left
            b = self.right
            _f = lambda x: self.fxn(x) - self.target
            if _f(a)*_f(b) > 0:
                print('Invalid interval.')
                return np.nan
            i = 0
            while ((np.abs(a-b) > self.delta) and (i < self.i_lim)):
                c = (a+b)/2
                if _f(a)*_f(c) > 0:
                    a = c
                else:
                    b = c
                i = i+1
            print(i, 'iterations.')
            print('delta =', a-b, '.')
            self.soln = a
            print(f'Solution is {self.soln}')
