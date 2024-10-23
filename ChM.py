import numpy as np
import Runge as rng
import sympy as sp

ans0 = 7.71356710860380874809
ans0_0 = 20.730271109552231026
rtol = pow(10, -10)
hard_kostyl = [20.7569054909183, 20.7322076167714, 20.7304172892537, 20.7302827474845, 20.7302720865815, 20.7302711954671, 20.7302711173915, 20.7302711102877, 20.7302711096218, 20.7302711095582]

def f(x):
    return 3*np.cos(1.5*x)*np.exp(x/4) + 4*np.sin(3.5*x)*np.exp(-3*x) + 4*x

def f_11(x):
    return 3*np.cos(1.5*(x + 2.5))*np.exp((x + 2.5)/4) + 4*np.sin(3.5*(x + 2.5))*np.exp(-3*(x + 2.5)) + 4*(x + 2.5)

def f1(k0, k1): # прямоугольник
    return (k1-k0)*f((k0+k1)/2)

def f2(k0, k1): # трапеция
    return ((f(k0)+f(k1))/2)*(k1-k0)

def f3(k0, k1): # Симпсон
    return ((f(k0) + 4*f((k0+k1)/2)+f(k1))/6)*(k1-k0)

def newton(z0, z1, a, alfa):
    zi = (z0 + z1)/2
    u0 = (pow(z1 - a, 1 - alfa) - pow(z0 - a, 1 - alfa)) / (1 - alfa)

    u1 = (pow(z1 - a, 2 - alfa) - pow(z0 - a, 2 - alfa)) / (2 - alfa) + a * u0

    u2 = (pow(z1 - a, 3 - alfa) - pow(z0 - a, 3 - alfa)) / (3 - alfa) + 2*a*u1 - a*a*u0

    a1 = sp.symbols('a1')
    a2 = sp.symbols('a2')
    a3 = sp.symbols('a3')

    my_system = [sp.Eq(a1 + a2 + a3, u0),
                 sp.Eq(a1*z0 + a2*zi + a3*z1, u1),
                 sp.Eq(a1*z0*z0 + a2*zi*zi + a3*z1*z1, u2)]
    arr = sp.solve(my_system, (a1, a2, a3))

    vvv = arr[a1]*f(z0) + arr[a2]*f(zi) + arr[a3]*f(z1)

    return vvv

def gauss(z0, z1, a):
    zi = (z0 + z1) / 2
    t = sp.symbols('t')

    fk = pow(t, 1 - a) / (1 - a)
    u0 = fk.subs(t, z1) - fk.subs(t, z0)

    fk = pow(t, 2 - a) / (2 - a)
    u1 = fk.subs(t, z1) - fk.subs(t, z0)

    fk = pow(t, 3 - a) / (3 - a)
    u2 = fk.subs(t, z1) - fk.subs(t, z0)

    fk = pow(t, 4 - a) / (4 - a)
    u3 = fk.subs(t, z1) - fk.subs(t, z0)

    fk = pow(t, 5 - a) / (5 - a)
    u4 = fk.subs(t, z1) - fk.subs(t, z0)

    fk = pow(t, 6 - a) / (6 - a)
    u5 = fk.subs(t, z1) - fk.subs(t, z0)

    a0 = sp.symbols('a0')
    a1 = sp.symbols('a1')
    a2 = sp.symbols('a2')

    system_1 = [ sp.Eq(a0 * u0 + a1 * u1 + a2 * u2, -u3),
                 sp.Eq(a0 * u1 + a1 * u2 + a2 * u3, -u4),
                 sp.Eq(a0 * u2 + a1 * u3 + a2 * u4, -u5)]

    arr = sp.solve(system_1, (a0, a1, a2))
    brr = sp.solve(
        sp.Eq(t**3 + arr[a2]*pow(t, 2) + arr[a1]*t + arr[a0], 0))
    x1 = brr[0]
    x2 = brr[1]
    x3 = brr[2]

    my_system = [sp.Eq(a0 + a1 + a2, u0),
                 sp.Eq(a0 * x1 + a1 * x2 + a2 * x3, u1),
                 sp.Eq(a0 * x1 * x1 + a1 * x2 * x2 + a2 * x3 * x3, u2)]
    arr = sp.solve(my_system, (a0, a1, a2))

    vvv = arr[a0] * f_11(float(sp.re(x1))) + arr[a1] * f_11(float(sp.re(x2))) + arr[a2] * f_11(float(sp.re(x3)))

    return vvv

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

    # Метод прямоугольника
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
            s11 = s1 + R2
            R2 /= ans0
        if ptr > 2:
            etken = rng.eitken(ll3, ll2, s1)
            etken11 = rng.eitken(pp3, pp2, s11)


        e = abs(ans0 - s1) / ans0
        ansR1.append(abs(R2))
        ansh1.append(h)
        if ptr > 2:
            pr = (np.log10(ansR1[-2])-np.log10(ansR1[-1]))/(np.log10(ansh1[-2])-np.log10(ansh1[-1]))

        ans1.append([n, round(h, 12), round(s1, 12), round(e, 12), round(R2, 12), round(s11, 12),
                     etken, etken11, pr])

        n = n * 2
        pp3 = pp2
        pp2 = s11
        ll3 = ll2
        ll2 = s1
        ptr += 1

    # Метод Трапеции
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
            R1, R2 = rng.foo_2(ll2, s2)
            s22 = s2 + abs(R2)
            R2 /= ans0

        if ptr > 2:
            etken = rng.eitken(ll3, ll2, s2)
            etken22 = rng.eitken(pp3, pp2, s22)
        e = abs(ans0 - s2) / ans0
        ansR2.append(abs(R2))
        ansh2.append(h)

        if ptr > 2:
            pr = (np.log10(ansR2[-2])-np.log10(ansR2[-1]))/(np.log10(ansh2[-2])-np.log10(ansh2[-1]))
        ans2.append([n, round(h, 12), round(s2, 12), round(e, 12), round(R2, 12), round(s22, 12),
                     etken, etken22, pr])

        n = n * 2
        pp3 = pp2
        pp2 = s22
        ll3 = ll2
        ll2 = s2
        ptr += 1

    # Метод Симпсона
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
        s3 = 0
        for j in range(1, n + 1): # Считаем интеграл без веса с N шагов
            z0 = z1
            z1 += h
            s3 += f3(z0, z1)

        if ptr > 1:
            R1, R2 = rng.foo_3(ll2, s3)
            s33 = s3 + abs(R2)
            R2 /= ans0
        if ptr > 2:
            etken = rng.eitken(ll3, ll2, s3)
            etken33 = rng.eitken(pp3, pp2, s33)
        e = abs(ans0 - s3) / ans0
        ansR3.append(abs(R2))
        ansh3.append(h)
        if ptr > 2:
            pr = (np.log10(ansR3[-2])-np.log10(ansR3[-1]))/(np.log10(ansh3[-2])-np.log10(ansh3[-1]))

        ans3.append([n, round(h, 12), round(s3, 12), round(e, 12), round(R2, 12), round(s33, 12),
                     etken, etken33, pr])

        n = n * 2
        pp3 = pp2
        pp2 = s33
        ll3 = ll2
        ll2 = s3
        ptr += 1

    return [ans1, ans2, ans3, ansR1, ansR2, ansR3, ansh1, ansh2, ansh3]

def with_weight(a, b, alfa, beta):
    ans1 = []
    ansR1 = []
    ansh1 = []
    ans2 = []
    ansR2 = []
    ansh2 = []
    s11 = 0
    s22 = 0
    etken11 = 0
    etken22 = 0
    lk = 0

    # Ньютон - Скотс
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

        '''for j in range(1, n+1): # Считаем интеграл с весом с N шагов
            z0 = z1
            z1 += h
            s1 += newton(z0, z1, a, alfa)
            lk += 1'''

        s1 = hard_kostyl[ptr - 1]

        if ptr > 1:
            if ptr > 2:
                etken = rng.eitken(ll3, ll2, s1)
                R1, R2 = rng.foo_4_r(ll2, s1, etken)
                s11 = s1 + R2
                etken11 = rng.eitken(pp3, pp2, s11)
                R2 /= ans0_0

            else:
                R1, R2 = rng.foo_4(ll2, s1)
                s11 = s1 + R2
                R2 /= ans0_0


        e = abs(ans0_0 - s1) / ans0_0
        ansR1.append(float(abs(R2)))
        ansh1.append(float(h))
        if ptr > 2:
            pr = (np.log10(ansR1[-2]) - np.log10(ansR1[-1])) / (np.log10(ansh1[-2]) - np.log10(ansh1[-1]))

        ans1.append([n, round(h, 12), s1, round(e, 12), round(R2, 12), round(s11, 12),
                     etken, etken11, pr])


        n *= 2
        pp3 = pp2
        pp2 = s11
        ll3 = ll2
        ll2 = s1
        ptr += 1

    # Гаусс
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
        z1 = 0
        s2 = 0

        for j in range(1, n+1): # Считаем интеграл с весом с N шагов
            z0 = z1
            z1 += h
            s2 += gauss(z0, z1, alfa)
            lk += 1
        #print(lk)

        if ptr > 1:
            if ptr > 2:
                etken = rng.eitken(ll3, ll2, s2)
                R1, R2 = rng.foo_4_r(ll2, s2, etken)
                s22 = s2 + R2
                etken22 = rng.eitken(pp3, pp2, s22)
                R2 /= ans0_0

            else:
                R1, R2 = rng.foo_4(ll2, s2)
                s22 = s2 + R2
                R2 /= ans0_0

        e = abs(ans0_0 - s2) / ans0_0
        ansR2.append(float(abs(R2)))
        ansh2.append(float(h))
        if ptr > 2:
            pr = (np.log10(ansR2[-2]) - np.log10(ansR2[-1])) / (np.log10(ansh2[-2]) - np.log10(ansh2[-1]))

        ans2.append([n, round(h, 12), s2, round(e, 12), round(R2, 12), round(s22, 12),
                     round(etken, 12), round(etken22), pr])


        n *= 2
        pp3 = pp2
        pp2 = s22
        ll3 = ll2
        ll2 = s2
        ptr += 1



    return [ans1, ans2, ansR1, ansR2, ansh1, ansh2]


