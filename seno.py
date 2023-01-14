import math


def seno(x):
    x = math.modf(x / math.pi)[0] * math.pi
    x2 = x*x
    fator = float('inf')
    termo = x
    total = x
    cont = 1
    while abs(fator) > 1e-6:
        cont2 = cont << 1
        fator = -(x2 / ((cont2 + 1) * cont2))
        termo *= fator
        total += termo
        cont += 1
    return total
    

if __name__ == '__main__':
    for i in range(-100, 101):
        x = i / 100.0 * 2 * math.pi
        print(i/100.0, x, math.sin(x), seno(x))

