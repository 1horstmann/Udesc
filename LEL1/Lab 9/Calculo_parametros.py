import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Dando entrada nos dados
V = np.arange(0, 5.01, 0.25)
idn = np.array([0, 510e-15, 1.01e-12, 1.51e-12, 2.01e-12, 2.51e-12, 3.02e-6, 37.07e-6, 109.09e-6, 209.22e-6, 367.59e-6, 504.37e-6, 779.70e-6, 1.04e-3, 1.35e-3, 1.69e-3, 2.07e-3, 2.49e-3, 2.95e-3, 3.45e-3, 3.98e-3])
idp = np.array([0, 250e-15, 500e-15, 225e-15, 1e-12, 18.99e-6, 76.14e-6, 171.76e-6, 306.12e-6, 479.54e-6, 692.31e-6, 944.73e-6, 1.24e-3, 1.57e-3, 1.94e-3, 2.36e-3, 2.81e-3, 3.31e-3, 3.85e-3, 4.43e-3, 5.05e-3])


# Calculando Ro e Y 
ron = (10-4.9672)/(1.0332e-3-1.0066e-3)
yn = 1/(1.0066e-3*ron-4.9672)

rop = (10-4.9986)/(1.0559e-3-1.0003e-3)
yp = 1/(1.0003e-3*rop-4.9986)


# Calculando os polinómios de 3° ordem
x1 = np.arange(1.50, 5.01, 0.01)
pn = np.polyfit(V[6:], idn[6:], 3)
sn = np.polyval(pn, x1)

x2 = np.arange(1.25, 5.01, 0.01)
pp = np.polyfit(V[5:], idp[5:], 3)
sp = np.polyval(pp, x2)

# Printando os polinômios encontrados
print(f'Polinômio do nMOSFET -> {pn}')
print(f'Polinômio do pMOSFET -> {pp}')


# Encontrando valores de k e Vt
kn = 2*pn[0]/yn
vtn = np.sqrt(pn[-1]*2/np.abs(kn))

kp = 2*pp[0]/yn
vtp = np.sqrt(pp[-1]*2/kp)


# Plotando os valores de K e de Vt
print(f'kn={kn:.4e},vtn={vtn:.4e}, kp={kp:.4e}, vtp={vtp:.4e}')


#Plotando os gráficos
plt.figure(1)
plt.plot(V, idn, 'ko', label='Experimental')
plt.plot(x1, sn,'b', label='Aproximação Polinômial')
plt.title('nMOSFET')
plt.xlabel('Variação da fonte de tensão')
plt.ylabel('Variação da corrente no dreno')
plt.legend()
plt.grid(True)

plt.figure(2)
plt.plot(V, idp, 'ko', label='Experimental')
plt.plot(x2, sp,'b', label='Aproximação Polinômial')
plt.title('pMOSFET')
plt.xlabel('Variação da fonte de tensão')
plt.ylabel('Variação da corrente no dreno')
plt.legend()
plt.grid(True)

plt.show()

#teste teste