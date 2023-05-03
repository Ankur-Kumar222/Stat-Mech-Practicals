import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def F_rj(x):
    return x**2

def F_p(x):
    return (x**3)/(np.exp(x)-1)

def plot(x, func, xlabel, ylabel, title, temperature):
    if temperature == None:
        plt.scatter(x, func)
    else:
        plt.scatter(x, func, label = f'T = {temperature}'+str('K'))
        plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()

    
k = 1.38*(10**-23)
h = 6.626*(10**-34)
c = 3*(10**8)
x_range = np.linspace(0,12,100)

plot(x_range, F_rj(x_range), 'x', 'F_rj(x)', 'Density of States(Rayleigh)', None)
plt.show()
plot(x_range, F_p(x_range), 'x', 'F_p(x)', 'Density of States(Planck)', None)
plt.show()

l = 1e-10
constant = 8*np.pi*((l/c)**3)
freq_range =10**(np.linspace(10, 30, 100))

plt.scatter(np.log(freq_range), np.log(F_rj(freq_range)*constant))
plt.xlabel('v')
plt.ylabel('G(v)')
plt.title('Rayleigh Jeans DOS(Log Plot)')
plt.grid()
plt.show()
print('slope = ', linregress(np.log(freq_range), np.log(F_rj(freq_range)*constant))[0])

def Rayleigh(x, T):
    temp = []
    function = F_rj(x)
    for i in range(len(x)):

        value = ((8*np.pi*(k**4)*(T**4))/((h**3)*(c**3)))*function[i]
        temp.append(value)
    return np.array(temp)

def Planck(x, T):
    temp = []
    function = F_p(x)
    for i in range(len(x)):

        value = ((8*np.pi*(k**4)*(T**4))/((h**3)*(c**3)))*function[i]
        temp.append(value)
    return np.array(temp)

T = [1000,1200,1500,1800]

for i in T:
    plot(x_range*(k*i)/(2*h), Rayleigh(x_range, i)*(2*h)/(k*i), 'x', 'U(v)', 'Rayleigh Jeans', i)
plt.grid()
plt.show()

for i in T:
    plot(x_range*(k*i)/(2*h), Planck(x_range, i)*(2*h)/(k*i), 'x', 'U(v)', 'Plancks', i)
plt.grid()
plt.show()


