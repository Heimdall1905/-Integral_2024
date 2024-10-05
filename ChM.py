import numpy as np

def f(x):
    return 3*np.cos(1.5*x)*np.exp(x/4) + 4*np.sin(3.5*x)*np.exp(-3*x) + 4*x

def f1(k0, k1): # прямоугольник
    return (k1-k0)*f((k0+k1)/2)

def f2(k0, k1): # трапеция
    return ((f(k0)+f(k1))/2)*(k1-k0)

def f3(k0, k1): # Симпсон
    return ((f(k0) + 4*f((k0+k1)/2)+f(k1))/6)*(k1-k0)

def not_weight(n, a, b):
    ans1 = []
    ans2 = []
    ans3 = []

    for k in range (11):
        h = (b - a) / n
        z1 = a
        s1 = 0
        s2 = 0
        s3 = 0
        for j in range(1, n + 1): # Считаем интеграл без веса с N шагов

            z0 = z1
            z1 += h

            s1 += f1(z0, z1)
            s2 += f2(z0, z1)
            s3 += f3(z0, z1)
        ans1.append([n, h, s1, 0, 0, 0, 0, 0, 0])
        ans2.append([n, h, s2, 0, 0, 0, 0, 0, 0])
        ans3.append([n, h, s3, 0, 0, 0, 0, 0, 0])

        n = n * 2
    return [ans1, ans2, ans3]

def with_weight(n, a, b):
    pass







