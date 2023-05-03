import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from numpy import diff
plt.style.use('bmh')

#Fermion System - Electrons
#Boson System - W Bosons
K = 8.617e-5
g = 1
h = 6.626e-34
c = 3e8
m_e = 9.1e-31
m_w = 134.268e-27
V = 1

def NonRelativisticParticle(eps, beta, k, mu):

    if k == 1:
        C = ((2*np.pi*(2*m_e)**(3/2))/(h**3))*g
    else:
        C = ((2*np.pi*(2*m_w)**(3/2))/(h**3))*g

    
    return C*V*(eps**(1/2))/(np.exp(beta*(eps-mu))+k)

def RelativisticParticle(eps, beta, k, mu):
    
    C = (4*np.pi*V*g)/((h*c)**3)
    
    return C*(eps**2)/(np.exp(beta*(eps-mu))+k)

    
def graphing(x_vals, func, title, xlabel, ylabel):
    plt.plot(x_vals, func)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

e_range = np.linspace(0,10,500)

graphing(e_range, NonRelativisticParticle(e_range, 1/(K*100), 1, 5), 'Non Relativistic Fermi Dirac Gas at Low Temps', 'E(eV)', 'dN/dE')
graphing(e_range, NonRelativisticParticle(e_range, 1/(K*10000), 1, 5), 'Non Relativistic Fermi Dirac Gas at High Temps', 'E(eV)', 'dN/dE')
graphing(e_range, NonRelativisticParticle(e_range, 1/(K*1000), -1, -5), 'Non Relativistic Bose Einstein Gas at Low Temps', 'E(eV)', 'dN/dE')
graphing(e_range, NonRelativisticParticle(e_range, 1/(K*10000), -1, -5), 'Non Relativistic Bose Einstein Gas at High Temps', 'E(eV)', 'dN/dE')


graphing(e_range, RelativisticParticle(e_range, 1/(K*100), 1, 5), 'Relativistic Fermi Dirac Gas at Low Temps', 'E(eV)', 'dN/dE')
graphing(e_range, RelativisticParticle(e_range, 1/(K*10000), 1, 5), 'Relativistic Fermi Dirac Gas at High Temps', 'E(eV)', 'dN/dE')
graphing(e_range, RelativisticParticle(e_range, 1/(K*1000), -1, -5), 'Relativistic Bose Einstein Gas at Low Temps', 'E(eV)', 'dN/dE')
graphing(e_range, RelativisticParticle(e_range, 1/(K*10000), -1, -5), 'Relativistic Bose Einstein Gas at High Temps', 'E(eV)', 'dN/dE')


def NonRelEnergy(eps, beta, k, mu):

    if k == 1:
        C = ((2*np.pi*(2*m_e)**(3/2))/(h**3))*g
    else:
        C = ((2*np.pi*(2*m_w)**(3/2))/(h**3))*g

    return C*V*(eps**(3/2))/(np.exp(beta*(eps-mu))+k)

def RelEnergy(eps, beta, k, mu):

    C = (4*np.pi*V*g)/((h*c)**3)

    return C*(eps**3)/(np.exp(beta*(eps-mu))+k)

def InternalEnergy(func, T_vals, k, mu):
    U_non_rel_fermi = []
    for i in T_vals:
        U = quad(func, 0, np.inf, args=(1/(K*i), k, mu))[0]
        U_non_rel_fermi.append(U)

    return U_non_rel_fermi

T_range = np.linspace(10, 1e5, 500)

graphing(T_range, InternalEnergy(NonRelEnergy, T_range, 1, 5), 'Internal Energy for Non Relativistic Fermi Dirac Gas', 'T(K)', 'U')
graphing(T_range, InternalEnergy(NonRelEnergy, T_range, -1, -5), 'Internal Energy for Non Relativistic Bose Einstein Gas', 'T(K)', 'U')

graphing(T_range, InternalEnergy(RelEnergy, T_range, 1, 5), 'Internal Energy for Relativistic Fermi Dirac Gas', 'T(K)', 'U')
graphing(T_range, InternalEnergy(RelEnergy, T_range, -1, -5), 'Internal Energy for Relativistic Bose Einstein Gas', 'T(K)', 'U')


def C_v(U_vals, T_vals):

    return diff(U_vals)/diff(T_vals)

graphing(T_range[:-1], C_v(InternalEnergy(NonRelEnergy, T_range, 1, 5), T_range), 'C_v for Non Relativistic Fermi Dirac Gas', 'T(K)', 'C_v')
graphing(T_range[:-1], C_v(InternalEnergy(NonRelEnergy, T_range, -1, -5), T_range), 'C_v for Non Relativistic Bose Einstein Gas', 'T(K)', 'C_v')


graphing(T_range[:-1], C_v(InternalEnergy(RelEnergy, T_range, 1, 5), T_range), 'C_v for Relativistic Fermi Dirac Gas', 'T(K)', 'C_v')
graphing(T_range[:-1], C_v(InternalEnergy(RelEnergy, T_range, -1, -5), T_range), 'C_v for Relativistic Bose Einstein Gas', 'T(K)', 'C_v')
