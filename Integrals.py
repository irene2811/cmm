#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:57:56 2023

@author: eiriniretsou
"""

#Compute integrals
import sympy as sym

# Define the symbol and function
x = sym.symbols('x')
f = x**2

# Compute the indefinite integral (antiderivative)
indefinite_integral = sym.integrate(f, x)
print("Indefinite Integral:", indefinite_integral)

# Compute the definite integral of f from 0 to 1
definite_integral = sym.integrate(f, (x, 0, 1))
print("Definite Integral:", definite_integral)
