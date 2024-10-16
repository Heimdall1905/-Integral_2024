import numpy as np

L = 2
m_square = 2
m_trapezoid = 2
m_simpson = 4
m_newton = 3  #АСТ не менее, чем n-1(n=3), так что m не менее n
m_gauss = 1

def foo_1(s1, s2):
    a = s2 - s1
    b = 1 - pow(L, -1*m_square)
    c = pow(L, m_square) - 1
    R1 = a/b
    R2 = a/c
    return [R1, R2]

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

def foo_4(s1, s2):
    a = s2 - s1
    b = 1 - pow(L, -1*m_newton)
    c = pow(L, m_newton) - 1
    R1 = a/b
    R2 = a/c
    return [R1, R2]

def foo_5(s1, s2):
    a = s2 - s1
    b = 1 - pow(L, -1*m_gauss)
    c = pow(L, m_gauss) - 1
    R1 = a/b
    R2 = a/c
    return [R1, R2]

def eitken(s1, s2, s3):
    j = (s3-s2)/(s2-s1)
    a = -1 * np.log(float(abs(j)))
    b = np.log(L)
    return a / b



