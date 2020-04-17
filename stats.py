import pandas as pd


class Stats:
    def __init__(self):
        self.infected_hawks = 0
        self.infected_doves = 0
        self.total_infected = 0
        self.infected_hawk_hist = []
        self.infected_dove_hist = []
        self.total_infected_hist = []
    def update(self):
        self.total_infected = self.infected_hawks + self.infected_doves
        self.infected_hawk_hist.append(self.infected_hawks)
        self.infected_dove_hist.append(self.infected_doves)
        self.total_infected_hist.append(self.total_infected)
    def to_csv(self, file):
        df = pd.DataFrame({
            'infected_hawks': self.infected_hawk_hist,
            'infected_doves': self.infected_dove_hist,
            'total_infected': self.total_infected_hist,
        })
        df.to_csv(file)