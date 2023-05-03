import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def DulongPetit(x):
    return x/x

def Einstein(x):
    return (1/x**2)*(np.exp(1/x))/((np.exp(1/x)-1)**2)

def integral(x):
    return (x**3)/(np.exp(x)-1)

def Debye(x):
    values = []
    for i in range(len(x)):
        temp = ((-3*x[i])/(np.exp(x[i])-1))+((12)/(x[i]**3))*quad(integral, 0, x[i])[0]
        values.append(temp)
    return values

x_range = np.linspace(0, 2, 100)

plt.plot(x_range, DulongPetit(x_range))
plt.scatter(x_range, DulongPetit(x_range), s = 10, label = 'Dulong and Petit')

#Copper
#theta_e = 230
#theta_d = 343
#x_range * theta_e/theta_d
plt.plot(x_range, Einstein(x_range*230/343))
plt.scatter(x_range, Einstein(x_range*230/343), s = 10, label = 'Einstein')

plt.plot(x_range, Debye(1/x_range))
plt.scatter(x_range, Debye(1/x_range), s = 10, label = 'Debye')

plt.xlabel('x(T)')
plt.ylabel('Cv/3R')
plt.title('Specific Heat as a function of Temperature(Copper)')
plt.grid()
plt.legend()
plt.show()

V_E = np.linspace(0, 2, 101)
DOS_e = []

for i in V_E:
    if i != 1:
        DOS_e.append(0)

    else:
        DOS_e.append(1)

plt.plot(V_E, DOS_e)
plt.xlabel('V/V_e')
plt.ylabel('Density of States')
plt.title('Density of States for Einstein Model')
plt.grid()
plt.show()

def DOS_d(v):
    return v**2

V_range = np.linspace(0,1,100)

plt.plot(V_range, DOS_d(V_range))
plt.xlabel('V/V_d')
plt.ylabel('Density of States')
plt.title('Density of States for Debye Model')
plt.grid()
plt.show()