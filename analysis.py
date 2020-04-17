import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


def visualise(filename):
    df = pd.read_csv(filename, index_col=0)
    df.plot()
    plt.show()