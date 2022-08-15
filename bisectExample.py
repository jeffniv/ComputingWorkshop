#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jeff Nivitanont, U. Wyoming 2022

import numpy as np

def bisect(f, a, b, delta=1e-3, i_lim=1e3):
    if f(a)*f(b) > 0:
        print('Invalid interval.')
        return np.nan
    i = 0
    while ((np.abs(a-b) > delta) and (i < i_lim)):
        c = (a+b)/2
        if f(a)*f(c) > 0:
            a = c
        else:
            b = c
        i = i+1
    print(i, 'iterations.')
    print('delta =', a-b, '.')
    return a
