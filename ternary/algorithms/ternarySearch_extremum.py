# ТЕРНАРНЫЙ ПОИСК ЭКСТРЕМУМА ФУНКЦИИ ДЛЯ ВЕЩЕСТВЕННОГО АРГУМЕНТА
def ternarySearchExtrMin_real(f, l, r, eps):
    while r - l > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return f(r)


def ternarySearchExtrMax_real(f, l, r, eps):
    while r - l > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if f(m1) > f(m2):
            r = m2
        else:
            l = m1
    return f(r)


# ТЕРНАРНЫЙ ПОИСК ЭКСТРЕМУМА ФУНКЦИИ ДЛЯ ЦЕЛОЧИСЛЕННОГО АРГУМЕНТА
def ternarySearchExtrMax_int(f, l, r):
    while r - l > 2:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if f(m1) > f(m2):
            r = m2
        else:
            l = m1
    v1 = f(l)
    v2 = f(l + 1)
    v3 = f(r)
    return max(v1, v2, v3)


def ternarySearchExtrMin_int(f, l, r):
    while r - l > 2:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    v1 = f(l)
    v2 = f(l + 1)
    v3 = f(r)
    return min(v1, v2, v3)
