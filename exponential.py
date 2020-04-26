import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import pandas as pd
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(b * x) + c

# raw data
df = pd.read_csv("data/control_2/experimental_control_2_combined.csv")

T25 = df['time_25']
T50 = df['time_50']
T75 = df['time_75']
T100 = df['time_100']

X = df['num_doves'] / 200

popt, pcov = curve_fit(func, X, T25)
a, b, c = popt
print(f"a: {a}, b: {b}, c: {c}")

plt.plot(X, T25, 'o', label="t_25 = 19.580 * e ^ (5.130 * x) + 503.372")
plt.plot(X, func(X, *popt), '-', label="Fitted t_25")
plt.legend()

popt, pcov = curve_fit(func, X, T50)
a, b, c = popt
print(f"a: {a}, b: {b}, c: {c}")

plt.plot(X, T50, 'o', label="t_50 = 45.514 * e ^ (5.214 * x) + 951.922")
plt.plot(X, func(X, *popt), '-', label="Fitted t_50")

popt, pcov = curve_fit(func, X, T75)
a, b, c = popt
print(f"a: {a}, b: {b}, c: {c}")

plt.plot(X, T75, 'o', label="t_75 = 151.939 * e ^ (4.541 * x) + 1242.113")
plt.plot(X, func(X, *popt), '-', label="Fitted t_75")

popt, pcov = curve_fit(func, X, T100)
a, b, c = popt
print(f"a: {a}, b: {b}, c: {c}")

plt.title("Exponential Regression of t_25, t_50, t_75 and t_100")
plt.plot(X, T100, 'o', label="t_100 = 1808.685 * e ^ (3.055 * x) + 3438.740")
plt.plot(X, func(X, *popt), '-', label="Fitted t_100")
plt.legend()
ax = plt.axes()
ax.set_xlabel("n_M/n_T")
ax.set_ylabel("Time Taken")
plt.show()