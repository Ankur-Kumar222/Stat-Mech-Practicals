import numpy as np
import matplotlib.pyplot as plt


bolt_const = 8.617*(10**-5)
x_range = np.linspace(-4, 4, 50)


def Maxwell_boltzmann(A, x):

    return A*np.exp(-x)


def BoseEinstein(alpha, x):

    return 1/(np.exp(x+alpha) - 1)


def FermiDirac(alpha, x):

    return 1/(np.exp(x+alpha) + 1)


def plotting(x, func, constant, temp, title, key = 0):

    if key == 0:
        plt.plot(x, func(constant, x), label = f'T = {temp}')
        plt.scatter(x, func(constant, x))
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.title(title + " (Alpha) = " + str(constant))
        plt.grid()
        plt.show()

    else:
        scale = temp * bolt_const

        plt.plot(x*scale, func(constant, x), label = f'T = {temp}')
        plt.scatter(x*scale, func(constant, x))
    plt.xlabel('e')
    plt.ylabel('f(e)')
    plt.title(title + " (Alpha) = " + str(constant))
    plt.legend()
    plt.grid()
    

Temp_list = [100, 200, 500, 1000]

plotting(x_range, Maxwell_boltzmann, 1, 1000, 'Maxwell Boltzmann Distribution', key = 0)

for i in Temp_list:
    plotting(x_range, Maxwell_boltzmann, 1, i, 'Maxwell Boltzmann (Temperature Variation)', key = 1)
plt.show()



plotting(x_range, BoseEinstein, 0, 1000, 'BoseEinstein Distribution', key = 0)

for i in Temp_list:
    plotting(x_range, BoseEinstein, 0, i, 'BoseEinstein (Temperature Variation)', key = 1)
plt.show()



plotting(x_range, FermiDirac, 0, 1000, 'FermiDirac Distribution', key = 0)

for i in Temp_list:
    plotting(x_range, FermiDirac, 0, i, 'FermiDirac (Temperature Variation)', key = 1)
plt.show()