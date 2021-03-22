import numpy as np               #Para trabalhar numericamente
import matplotlib.pyplot as plt  #Para plotar
import sympy as sp               #Para trabalhar com símbolos

#Constantes
A=2
k1=1.5
k2=0.8
u2=1
hb=1.9775

#Gráfico 01
u1=np.arange(0,1,0.001)
u1b_1=0.75*np.ones(len(u1))
du1_1=u1-u1b_1

hl_1=2*du1_1*u1b_1*(k1/(k2*u2))**2+hb
hnl=(k1*u1/(k2*u2))**2
#Cálculo do erro
erro_1=100*np.abs((hnl-hl_1)/(hnl+hb))

#Construindo o gráfico
plt.figure(1)
plt.subplot(2,1,1)
plt.title('Exercício 07')
plt.plot(u1,hnl,color='b',label='$h_{Não-Linear}$')
plt.plot(u1,hl_1,color='k',label='$h_{Linearizado}$')
plt.grid(True)
plt.legend()
plt.xlabel('Abertura da Válvula de Entrada')
plt.ylabel('Nível do Sistema')
plt.axis([0,1,-2,3.6])
plt.subplot(2,1,2)
plt.plot(u1,erro_1,color='r',label='Erro%')
plt.grid(True)
plt.xlabel('Abertura da Válvula de Entrada')
plt.ylabel('Erro [%]')
plt.axis([0,1,0,100])
plt.legend()

#Gráfico 02
u1=np.arange(0,1,0.001)
u1b_2=0.4*np.ones(len(u1))
du1_2=u1-u1b_2
hnl=(k1*u1/(k2*u2))**2
hl_2=(2*du1_2*u1b_2*(k1/(k2*u2))**2+hb)
#Cálculo do erro
erro_2=100*abs((hnl-hl_2)/(hnl+hb))

#Construindo o gráfico
plt.figure(2)
plt.subplot(2,1,1)
plt.title('Exercício 07')
plt.plot(u1,hnl,color='b',label='$h_{Não-Linear}$')
plt.plot(u1,hl_2,color='k',label='$h_{Linearizado}$')
plt.axis([0,1,0,3.7])
plt.legend()
plt.grid(True)
plt.xlabel('Abertura da Válvula de Entrada')
plt.ylabel('Nível do Sistema')
plt.subplot(2,1,2)
plt.plot(u1,erro_2,color='r',label='Erro%')
plt.grid(True)
plt.xlabel('Abertura da Válvula de Entrada')
plt.ylabel('Erro [%]')
plt.axis([0,1,0,62])
plt.legend()
plt.show()
