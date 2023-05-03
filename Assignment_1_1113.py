import numpy as np
import matplotlib.pyplot as plt
import random

#Heads = 0
#Tails = 1

def toss(N_c):

    outcomes = []
    for i in range(0, N_c):

        result = random.randint(0,1)
        outcomes.append(result)
    return outcomes


def macrostates(N_c, N_t):

    counts = np.zeros(N_c+1)
    ensemble = []
    no_of_heads = []

    for i in range(0, N_t):
        temp = toss(N_c)

        heads = temp.count(0)
        no_of_heads.append(heads)
        
        for i in range(0, N_c+1):

            if sum(temp) == i:
    
                counts[i] = counts[i] + 1
            

        ensemble.append(temp)

    return counts, no_of_heads

N_T=[]

for i in range(1,6):
    temps = 10**i
    N_T.append(temps)

def frequency(N_c, N_t):

    freq = []

    counts = macrostates(N_c, N_t)[0]
    for i in range(0, N_c+1):
        freq.append(counts[i]/sum(counts))

    return freq
        

def plot1(N_c, N_t):
    heads = np.arange(0,N_c + 1)
    
    for i in range(len(N_t)):
        plt.plot(heads, frequency(N_c, N_t[i]), label = f'N_t = {N_t[i]}')

    plt.xlabel('No of Heads')
    plt.ylabel('Probability')
    plt.title('Probability Vs No of Heads')
    plt.grid()
    plt.legend()
    plt.show()

plot1(5, N_T)


N_C=[]

for i in range(2,11):
    temps = i
    N_C.append(temps)

def plot2(N_c, N_t):
    
    for i in range(len(N_c)):
        heads = np.arange(0,N_c[i] + 1)

        plt.plot(heads, frequency(N_c[i], N_t), label = f'N_c = {N_c[i]}')

    plt.xlabel('No of Heads')
    plt.ylabel('Probability')
    plt.title('Probability Vs No of Heads')
    plt.grid()
    plt.legend()
    plt.show()

plot2(N_C, 1000)


def plot3(N_c, N_t):

    head_list = macrostates(N_c, N_t)[1]
    p = []
    q = []

    for i in range(len(head_list)):

        prob1 = (np.sum(head_list[:i]))/(N_c*(i+1))
        prob2 = 1 - prob1
        p.append(prob1)
        q.append(prob2)
    
    x_range = np.linspace(0, N_t, N_t)
    plt.plot(x_range, p, label = 'p(heads)')
    plt.plot(x_range, q, label = 'q(tails)')
    plt.xlabel('No of Tosses')
    plt.ylabel('p and q')
    plt.title('p and q Vs No of Tosses')
    plt.grid()
    plt.legend()
    plt.show()

plot3(3, 500)