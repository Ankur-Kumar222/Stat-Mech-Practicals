import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from numpy import diff

h = 6.63*10**-34
m = 1.67*10**-27
k = 1.38*10**-23
N_a = 6.023*10**23

V_range = np.linspace(20*10**-3, 50*10**-2, 5)
T_range = np.linspace(150, 450, 5)

def Analytic(V, T):
    return V*(((2*np.pi*m*k)/h**2)**(3/2))*T**(3/2)

def Z_func(V,T):
    
    def Z_val(n_j):
        return n_j**2 * np.exp((-(h*n_j)**2)/(8*m*(V**(2/3))*k*T))
    
    return (np.pi/2)*quad(Z_val, 0, 10**11)[0] #n_j = [0, 10**14]


matrix = []

def matrixformation(T_vals, V_vals):

    for i in range(len(T_vals)):
        row = []
        for j in range(len(V_vals)):

            row.append(Z_func(V_range[j], T_range[i]))
        matrix.append(row)

    return matrix

matrixformation(T_range, V_range)

#ln Z vs ln T
for i in range(len(matrix)):
    plt.plot(np.log(np.array(T_range)), np.log(np.array(np.transpose(matrix)[i])), label =f'V = {V_range[i]}')
plt.title('ln Z vs ln T')
plt.xlabel('ln T')
plt.ylabel('ln Z')
plt.legend()
plt.grid()
plt.show()

#lnZ vs ln V

for i in range(len(matrix)):
    plt.plot(np.log(np.array(V_range)), np.log(np.array(matrix[i])), label =f'T = {T_range[i]}')
plt.title('lnZ vs ln V')
plt.xlabel('ln V')
plt.ylabel('lnZ')
plt.legend()
plt.grid()
plt.show()

#Pressure

for i in range(len(T_range)):
    dydx1 = diff(np.log(np.array(matrix[i])))/diff(np.array(V_range))
    Pressure = N_a*k*T_range[i]*dydx1

    plt.plot(np.array(V_range)[:-1], Pressure, label =f'T = {T_range[i]}')
plt.title('P vs V')
plt.xlabel('V')
plt.ylabel('P')
plt.legend()
plt.grid()
plt.show()

#Internal Energy ### <E> = U/N_a

for i in range(len(V_range)):

    dydx2 = diff(np.log(np.transpose(np.array(matrix))[i]))/diff(np.array(T_range))
    intenergy = N_a*k*np.array(T_range)[:-1]*np.array(dydx2)

    plt.plot(np.array(T_range)[:-1], intenergy, label =f'V = {V_range[i]}')

plt.title('U vs T')
plt.xlabel('T')
plt.ylabel('U')
plt.legend()
plt.grid()
plt.show()

#Entropy

S = (intenergy/np.array(T_range)[:-1]) + N_a*k*(np.log(np.transpose(np.array(matrix))[-1])[:-1]-np.log(N_a)+1)

plt.plot(np.array(T_range)[:-1], S)
plt.title('S vs T')
plt.xlabel('T')
plt.ylabel('S')
plt.grid()
plt.show()