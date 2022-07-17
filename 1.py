# 1. Вычислить число пи c заданной точностью d. 10^(-1) ≤ d ≤10^(-10).

import math

def get_pi (d):
    pi = round(math.pi, d)
    return pi

d = len(input('Введите точность числа в формате 0.х: ')) - 2
if d > 0 and d < 11:
    print(f'Число Pi с заданной точностью: {get_pi(d)}')
else: print('Неподдерживаемая точность.')
