﻿from math import *
import math #iport oli valesti tehtud
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) # int ei olinud
S=a**2
print("Ruudu pindala", round(S, 1))
P=4*a
print("Ruudu ümbermõõt", round(P, 1))
di=a*math.sqrt(2) # oli sqr on vaja sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print('Ristküliku pindala', round(S, 1))
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P, 1))
di=math.sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt", round(d, 1))
S=pi*r**2
print("Ringi pindala", round(S, 1))
C=2*pi*r
print("Ringjoone pikkus", round(C, 2))
