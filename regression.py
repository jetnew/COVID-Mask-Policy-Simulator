"""https://stackoverflow.com/questions/4308168/sigmoidal-regression-with-scipy-numpy-python-etc"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


def sigmoid(p,x):
    x0,y0,c,k=p
    y = c / (1 + np.exp(-k*(x-x0))) + y0
    return y

def residuals(p,x,y):
    return y - sigmoid(p,x)

def resize(arr,lower=0.0,upper=1.0):
    arr=arr.copy()
    if lower>upper: lower,upper=upper,lower
    arr -= arr.min()
    arr *= (upper-lower)/arr.max()
    arr += lower
    return arr

def logistic_regression(x, y):
    p_guess=(np.median(x),np.median(y),1.0,1.0)
    p, cov, infodict, mesg, ier = scipy.optimize.leastsq(
        residuals,p_guess,args=(x,y),full_output=1)
    x0,y0,c,k=p
    print(f"x0={x0}\ny0={y0}\nc={c}\nk={k}\n")

    xp = np.linspace(0, 1.1, 1500)
    pxp=sigmoid(p,xp)
    return p, xp, pxp

# raw data
df = pd.read_csv("data/control_1/experimental_control_1_combined.csv")

T = df['total_infected']
D = df['infected_doves']
H = df['infected_hawks']

X = np.array(list(range(20000)))
p1, xp1, pxp1 = logistic_regression(X, H)
p2, xp2, pxp2 = logistic_regression(X, D)
p3, xp3, pxp3 = logistic_regression(X, T)


# Plot the results
plt.plot(X, H, '.', xp1, pxp1)
plt.plot(X, D, '.', xp2, pxp2)
plt.plot(X, T, '.', xp3, pxp3)
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal')
plt.grid(True)
plt.show()

