import numpy as np
import matplotlib.pyplot as plt

#input
gamma= 6.67
xi=np.arange(0,30,0.1)
xj= 15
dj= 0.5
dx= 0.2
t= 0.3
deltarho= -1.5
v=dx/2 # apenas para facilitar o calculo

#equação do prisma
x1=xj-v;
x2=xj+v;
A=xi-x1;
B=xi-x2;
C= dj;
D= dj+t;
gprisma = gamma*deltarho*(A*np.log((A**2+D**2)/(A**2+C**2)) - B*np.log((B**2+D**2)/ (B**2+C**2))-2*C*(np.arctan(A/C)-np.arctan(B/C))+ 2*D*(np.arctan(A/D)-np.arctan(B/D)))

print(gprisma)

#Dimensões do Prisma
x1=xj- (dx/2); # Coordenada do primeiro vertice; em função de x
x2=xj+ (dx/2); # Cooedenada do segundo vertice; em função de x
x3=xj+ (dx/2); # ""         do teceiro "           "
x4=xj- (dx/2); # "           do quarto "           "
x0=xj- (dx/2); # Corecao manual para completar a figura
z1=dj;         # Profundidade de um dos vertices da fita em fumcao de x
z2=dj;
z3=dj+t;
z4=z3;
z0=dj;

hozA=[x1, x2,x3,x4,x0];   #Preparação para plotagem
profB=[z1, z2, z3, z4, z0];

#Plot de figura
plt.figure(2)
plt.subplot(2,1,1)#duas linhas, uma coluna, posição 1
plt.plot(xi,gprisma,linestyle='-', color='r')


plt.ylabel('Anomalia (mGal)')
plt.xlabel('extensão horizontal (km)')
plt.legend(['f'])
plt.subplot(2,1,2)#duas linhas, uma coluna, posição 2
plt.plot(hozA,profB)

plt.gca().invert_yaxis() #comando que invert os eixos.
plt.ylabel('Profundidade (km)')
plt.xlabel('Extensão horizontal (km)')
#plt.title('Prisma vs Fita')
plt.legend(['Prisma Unitário'])

plt.show() #apresenta a imagem na tela
