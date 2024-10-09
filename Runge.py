import numpy as np
from decimal import Decimal
import math as mt

L = 2
m_square = 1
m_trapezoid = 1
m_simpson = 3

def foo_1(s1, s2):
    a = s2 - s1
    b = 1 - pow(L, -1*m_square)
    c = pow(L, m_square) - 1
    R1 = a/b
    R2 = a/c
    return R1, R2

def foo_2(s1, s2):
    a = s2 - s1
    b = 1 - pow(L, -1*m_trapezoid)
    c = pow(L, m_trapezoid) - 1
    R1 = a/b
    R2 = a/c
    return [R1, R2]

def foo_3(s1, s2):
    a = s2 - s1
    b = 1 - pow(L, -1*m_simpson)
    c = pow(L, m_simpson) - 1
    R1 = a/b
    R2 = a/c
    return [R1, R2]

def eitken(s1, s2, s3):
    a = -1 * np.log(abs((s3-s2)/(s2-s1)))
    b = np.log(L)
    return a / b




