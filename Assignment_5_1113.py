import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import linregress

h = 6.626e-34
c = 3e8
k =1.38e-23
T = 5800

#Wiens Displacement Law

def F_p(x):
    return (x**3)/(np.exp(x)-1)

x_range = np.linspace(1e-10,20,10000)

plt.plot(x_range, F_p(x_range))
plt.xlabel('x')
plt.ylabel('F_p(x)')
plt.title('Wiens Displacement Law')
plt.grid()
plt.show()

max_val = max(F_p(x_range))

for i in range(len(x_range)):
    values = F_p(x_range[i])
    if values == max_val:
        x_max = x_range[i]
        print('x_mean',x_range[i])

    else:
        pass

print('Wiens Constant =', (h*c)/(k*x_max))
print('Wavelength = ', (h*c)/(x_max*k*T))

for i in range(len(x_range)):

    integral_1 = quad(F_p, x_range[0], x_range[10+i])
    integral_2 = quad(F_p, x_range[10+i], x_range[-1])

    if integral_1 >= integral_2:
        actual_x = (x_range[10+i])
        print('x_median',actual_x)
        break

    else:
        pass

print('Wiens Constant =', (h*c)/(k*actual_x))
print('Wavelength = ', (h*c)/(actual_x*k*T))

#Stefans Boltzmann Law
I_p = quad(F_p, 1e-10, 50)[0]
print('Values of I_p = ',I_p)

def C(T):
    return (8*np.pi*k**4*T**4)/(h**3*c**3)

T_range = np.arange(100,10000,500, dtype = float)

print(T_range)

U_range = C(T_range)*I_p

F_range = (c/4)*U_range

plt.plot(T_range, F_range)
plt.xlabel('T')
plt.ylabel('F(T)')
plt.title('F vs T')
plt.grid()
plt.show()

plt.plot(np.log(T_range), np.log(F_range))
plt.xlabel('lnT')
plt.ylabel('lnF(T)')
plt.title('lnF vs lnT')
plt.grid()
plt.show()

result = linregress(np.log(T_range), np.log(F_range))
print(result)
print('Stefans Constant = ', np.exp(result)[1])