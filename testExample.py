#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jeff Nivitanont, U. Wyoming 2022

from bisectExample import bisect
from classExample import Bisector
import numpy as np

f = lambda x: x**2
g = lambda x: f(x)-2
soln = bisect(g, 0, 2)
print(f'Solution is {soln}')

testobj = Bisector()
testobj.setFxn(f)
testobj.setTarget(2)
testobj.setBounds(0, 10)
testobj.bisect()
