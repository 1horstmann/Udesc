import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plotar(x, y, titulo, legenda, xlabel, ylabel, cor, mostrar=False):
    plt.figure()
    plt.plot(x, y, cor, label=legenda)
    plt.title(titulo)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if mostrar:
        plt.show()

idn = np.array([0, 510e-15, 1.01e-12, 1.51e-12, 2.01e-12, 2.51e-12, 3.02e-6, 37.07e-6, 109.09e-6, 209.22e-6, 367.59e-6, 504.37e-6, 779.70e-6, 1.04e-3, 1.35e-3, 1.69e-3, 2.07e-3, 2.49e-3, 2.95e-3, 3.45e-3, 3.98e-3])
idp = np.array([0, 250e-15, 500e-15, 225e-15, 1e-12, 18.99e-6, 76.14e-6, 171.76e-6, 306.12e-6, 479.54e-6, 692.31e-6, 944.73e-6, 1.24e-3, 1.57e-3, 1.94e-3, 2.36e-3, 2.81e-3, 3.31e-3, 3.85e-3, 4.43e-3, 5.05e-3])

ron = (10-4.9672)/(1.0332e-3-1.0066e-3)
rop = (10-4.9986)/(1.0559e-3-1.0003e-3)

yn = 1/(1.0066e-3*ron-4.9672)
yp = 1/(1.0003e-3*rop-4.9986)

V = np.arange(0, 5.25, 0.25)

x = np.arange(0, 5, 0.01)
pn = np.polyfit(V, idn, 3)
sn = np.polyval(pn, x)

kn = 2*pn[0]/yn
vtn = np.sqrt(pn[-1])

x = np.arange(0, 5, 0.01)
pp = np.polyfit(V, idp, 3)
sp = np.polyval(pp, x)

kp = 2*pp[0]/yn
vtp = np.sqrt(pp[-1])

print(f'kn={kn:.3e},vtn={vtn:.3e}, kp={kp:.3e}, vtp={vtp:.3e}')

plt.figure(1)
plt.plot(V, idn, 'ko', label='Pontos')
plt.plot(x, sn,'b',label=f'{pn}')
plt.title('n')
plt.legend()
plt.grid(True)
plt.figure(2)
plt.plot(V, idp, 'ko', label='Pontos')
plt.plot(x, sp,'b',label=f'{pp}')
plt.title('p')
plt.legend()
plt.grid(True)

# plotar(V, idn, 'titulo', 'legenda', 'xlabel', 'ylabel', 'r', True)

plt.show()
