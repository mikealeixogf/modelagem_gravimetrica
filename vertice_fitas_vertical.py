import numpy as np
import matplotlib.pyplot as plt

p=2 #espessura do prisma
dj= 0.5 #profundidade do prisma
dx= 3 #extensão do prisma
xj=[15]
n=70 #numero de fitas
t1=p/n #espessura de cada fita
zca=t1/2+dj #profundidade do centro da primeira fita
a1=[]
b1=[]

for j in (xj):
    x1 = j - (dx / 2)  # Coordenada do primeiro vertice; em função de x
    x2 = j + (dx / 2)
    a=[x1,x2,x2,x1,x1]


for i in  range (0,n):
    zc= zca+i*t1 #profundidade do centro da profundidade de cada fita.
    # Cooedenada do segundo vertice; em função de x
    z1 = zc - t1 / 2  # Profundidade de um dos vertices da fita em fumcao de x
    z2 = z1
    z3 = zc + t1 / 2
    z4 = z3
    b=[z1,z2,z3,z4,z1]
    a1.extend(a)
    b1.extend(b)
    # print(f'O prirsma {zc} é: ')
    # print(f'O par ordenado de A é x1 = {xz1} e z1 = {z1}')
    # print(f'O par ordenado de B é x2 = {xz2} e z2 = {z2}')
    # print(f'O par ordenado de C é x2 = {xz3} e z3 = {z3}')
    # print(f'O par ordenado de D é x1 = {xz4} e z4 = {z4}')
    # print(f'O par ordenado que fecha o prisma é {xz0} e {z0}')


plt.plot(a1,b1)
plt.ylabel('Profundidade (km)')
plt.xlabel('Extensão horizontal (km)')
plt.title('Fitas Dispostas na vertical')
plt.xlim(10, 20)
plt.ylim(0.4, 4)
plt.legend(['Fitas'])
plt.gca().invert_yaxis()  # comando que invert os eixos.
plt.show()