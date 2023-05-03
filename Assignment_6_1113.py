import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

K = 8.617*10**-5
N_par= 1

def Partition(n, g, e, T):
    z = 0

    for i in range(n):
        z += g[i]*np.exp(-e[i]/(K*T))

    return z

low_temp = np.linspace(0.01, 5000, 100)
high_temp = np.linspace(5000, 10**5, 100)

def plot(x, func, xlabel, ylabel, title):
        
    plt.plot(x, func)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    


Z_low = Partition(2, [1,1], [0,1], low_temp)
Z_high = Partition(2, [1,1], [0,1], high_temp)

plot(low_temp, Z_low, 'T', 'Z', 'Partition Function(Low Temp)')
plt.show()
plot(high_temp, Z_high, 'T', 'Z', 'Partition Function(High Temp)')
plt.show()

def frac_pop(n, g, e, T, Z_val):
    N = []
    
    for i in range(n):
        value = (g[i]*np.exp(-e[i]/(K*T)))/(N_par*Z_val)
        N.append(value)

    return N

Population_low = frac_pop(2, [1,1], [0,1], low_temp, Z_low)
Population_high = frac_pop(2, [1,1], [0,1], high_temp, Z_high)

plot(low_temp, Population_low[0], 'T', 'Ni/N', 'Fractional Population(Low Temp)')
plot(low_temp, Population_low[1], 'T', 'Ni/N', 'Fractional Population(Low Temp)')
plt.show()
plot(high_temp, Population_high[0], 'T', 'Ni/N', 'Fractional Population(High Temp)')
plot(high_temp, Population_high[1], 'T', 'Ni/N', 'Fractional Population(High Temp)')
plt.show()

#Internal Energy
U_low = Population_low[0]*0 + Population_low[1]*1
U_high = Population_high[0]*0 + Population_high[1]*1

plot(low_temp, U_low, 'T', 'U', 'Internal Energy(Low Temp)')
plt.show()
plot(high_temp, U_high, 'T', 'U', 'Internal Energy(High Temp)')
plt.show()

#Entropy
S_low = []
for i in range(len(low_temp)):

    val = K*np.log(Z_low[i]/N_par) + U_low[i]/low_temp[i] + K
    S_low.append(val)

S_high = []
for i in range(len(high_temp)):

    val = K*np.log(Z_high[i]/N_par) + U_high[i]/high_temp[i] + K
    S_high.append(val)


plot(low_temp, S_low, 'T', 'S', 'Entropy(Low Temp)')
plt.show()
plot(high_temp, S_high, 'T', 'S', 'Entropy(High Temp)')
plt.show()

#Helmholtz Free Energy
F_low = []
for i in range(len(low_temp)):
    
    val = -K*low_temp[i]*np.log(Z_low[i])
    F_low.append(val)

F_high = []
for i in range(len(high_temp)):
    
    val = -K*high_temp[i]*np.log(Z_high[i])
    F_high.append(val)


plot(low_temp, F_low, 'T', 'F', 'Helmholtz Free Energy(Low Temp)')
plt.show()
plot(high_temp, F_high, 'T', 'F', 'Helmholtz Free Energy(High Temp)')
plt.show()