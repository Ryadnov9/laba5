"""3. Описати функцію Mediana(A, B, C) дійсного типу,
яка знаходить медіану трикутника. Скласти програму пошуку
всіх медіан трикутника, заданого сторонами a, b, c (a, b, c -
дійсні числа)."""

import math


def med(a, b, c):
    med = math.sqrt(2 * (b * b + c * c) - a * a) / 2
    return med


print("Введіть сторони трикутника:")
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
if abs(a - b) >= c | a + b <= c:
    print("не є трикутником ")
print("Медіани трикутника :")
ma = med(a, b, c)
mb = med(b, a, c)
mc = med(c, a, b)
print("перша медіана", ma, "\tдруга медіана", mb, "\tтретя медіана", mc)
print("Шукані  медіаны:")
mma = med(ma, mb, mc)
mmb = med(mb, ma, mc)
mmc = med(mc, ma, mb)
print("перша медіана", mma, "\tдруга медіана", mmb, "\tтретя медіана", mmc)
