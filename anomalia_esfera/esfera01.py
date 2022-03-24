import numpy as np
import matplotlib.pyplot as plt
x1=np.arange(-80,80)
constante_g= 6.67*10e-11
rho=0.4
z1=[20,40]
r1=[5]
r2=[10]
g=(4*constante_g*rho*(r**2)*np.pi*z)/(3*(x1**2+z**2)**(3/2))
plt.plot(x1,g,label=f'z={z} e r{r}')
plt.plo