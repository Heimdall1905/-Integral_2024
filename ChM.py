import numpy as np
import Runge as rng

ans0 = 7.71356710860380874809
rtol = pow(10, -10)

def f(x):
    return 3*np.cos(1.5*x)*np.exp(x/4) + 4*np.sin(3.5*x)*np.exp(-3*x) + 4*x

def f1(k0, k1): # прямоугольник
    return (k1-k0)*f((k0+k1)/2)

def f2(k0, k1): # трапеция
    return ((f(k0)+f(k1))/2)*(k1-k0)

def f3(k0, k1): # Симпсон
    return ((f(k0) + 4*f((k0+k1)/2)+f(k1))/6)*(k1-k0)

def not_weight(a, b):
    ans1 = []
    ansR1 = []
    ansh1 = []
    ans2 = []
    ansR2 = []
    ansh2 = []
    ans3 = []
    ansR3 = []
    ansh3 = []
    f = 1
    s11 = 0
    s22 = 0
    s33 = 0
    etken11 = 0
    etken22 = 0
    etken33 = 0

    n = 1
    ll2 = 0
    ll3 = 0
    pp2 = 0
    pp3 = 0
    ptr = 1
    R2 = 100
    etken = 0
    pr = 0
    while abs(R2) > rtol:
        h = (b - a) / n
        z1 = a
        s1 = 0

        for j in range(1, n + 1): # Считаем интеграл без веса с N шагов
            z0 = z1
            z1 += h
            s1 += f1(z0, z1)

        if ptr > 1:
            R1, R2 = rng.foo_1(ll2, s1)
            s11 = s1 + abs(R2)
        if ptr > 2:
            etken = rng.eitken(ll3, ll2, s1)
            etken11 = rng.eitken(pp3, pp2, s11)


        e = abs(ans0-s1)/ans0
        ansR1.append(abs(R2))
        ansh1.append(h)
        if ptr > 2:
            pr = (np.log10(ansR1[-1])-np.log10(ansR1[0]))/(np.log10(ansh1[-1])-np.log10(ansh1[0]))

        ans1.append([n, round(h, 12), round(s1, 12), round(e, 12), round(abs(R2), 12), round(s11, 12),
                     etken, etken11, pr])

        n = n * 2
        pp3 = pp2
        pp2 = s11
        ll3 = ll2
        ll2 = s1
        ptr += 1
    n = 1
    ll2 = 0
    ll3 = 0
    pp2 = 0
    pp3 = 0
    ptr = 1
    R2 = 100
    etken = 0
    pr = 0
    while abs(R2) > rtol:
        h = (b - a) / n
        z1 = a
        s2 = 0
        for j in range(1, n + 1): # Считаем интеграл без веса с N шагов

            z0 = z1
            z1 += h

            s2 += f2(z0, z1)

        if ptr > 1:
            R1, R2 = rng.foo_2(s2, ll2)
            s22 = s2 + abs(R2)

        if ptr > 2:
            etken = rng.eitken(ll3, ll2, s2)
            etken22 = rng.eitken(pp3, pp2, s22)
        e = abs(ans0 - s2) / ans0
        ansR2.append(abs(R2))
        ansh2.append(h)

        if ptr > 2:
            pr = (np.log10(ansR2[-1])-np.log10(ansR2[0]))/(np.log10(ansh2[-1])-np.log10(ansh2[0]))
        ans2.append([n, round(h, 12), round(s2, 12), round(e, 12), round(abs(R2), 12), round(s22, 12),
                     etken, etken22, pr])

        n = n * 2
        pp3 = pp2
        pp2 = s22
        ll3 = ll2
        ll2 = s2
        ptr += 1
    n = 1
    ll2 = 0
    ll3 = 0
    ptr = 1
    R2 = 100
    etken = 0
    pr = 0
    while abs(R2) > rtol:
        h = (b - a) / n
        z1 = a
        s3 = 0
        for j in range(1, n + 1): # Считаем интеграл без веса с N шагов

            z0 = z1
            z1 += h

            s3 += f3(z0, z1)

        if ptr > 1:
            R1, R2 = rng.foo_3(s3, ll2)
            s33 = s3 + abs(R2)
        if ptr > 2:
            etken = rng.eitken(ll3, ll2, s3)
            etken33 = rng.eitken(pp3, pp2, s33)
        e = abs(ans0 - s3) / ans0
        ansR3.append(abs(R2))
        ansh3.append(h)
        if ptr > 2:
            pr = (np.log10(ansR3[-1])-np.log10(ansR3[0]))/(np.log10(ansh3[-1])-np.log10(ansh3[0]))

        ans3.append([n, round(h, 12), round(s3, 12), round(e, 12), round(abs(R2), 12), round(s33, 12),
                     etken, etken33, pr])

        n = n * 2
        pp3 = pp2
        pp2 = s33
        ll3 = ll2
        ll2 = s3
        ptr += 1








    return [ans1, ans2, ans3, ansR1, ansR2, ansR3, ansh1, ansh2, ansh3]

def with_weight(a, b):
    pass










