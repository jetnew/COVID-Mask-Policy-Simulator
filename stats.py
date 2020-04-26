import pandas as pd


class Stats:
    def __init__(self,
                 num_hawks,
                 num_doves,
                 num_hawks_infected_initial,
                 num_doves_infected_initial,
                 infection_rate,
                 mask_effectiveness,
                 percent_stationary,
                 improper_mask_usage_severity,
                 percent_improper_mask_usage,
                 probability_quarantined):
        self.num_hawks = num_hawks
        self.num_doves = num_doves
        self.total = num_hawks + num_doves
        self.num_hawks_infected_initial = num_hawks_infected_initial
        self.num_doves_infected_initial = num_doves_infected_initial
        self.curr_infected = num_doves_infected_initial + num_hawks_infected_initial
        self.infection_rate = infection_rate
        self.mask_effectiveness = mask_effectiveness
        self.percent_stationary = percent_stationary
        self.improper_mask_usage_severity = improper_mask_usage_severity
        self.percent_improper_mask_usage = percent_improper_mask_usage
        self.probability_quarantined = probability_quarantined
        self.infected_hawks = 0
        self.infected_doves = 0
        self.infected_hawk_hist = []
        self.infected_dove_hist = []
        self.total_infected_hist = []
        self.time_taken_25 = None
        self.time_taken_50 = None
        self.time_taken_75 = None
        self.time_taken_100 = None
        self.t = 0

    def update(self, t):
        self.t = t
        self.total_infected = self.infected_hawks + self.infected_doves
        # self.infected_hawk_hist.append(self.infected_hawks)
        # self.infected_dove_hist.append(self.infected_doves)
        # self.total_infected_hist.append(self.total_infected)
        if self.total_infected >= 0.25 * self.total and self.time_taken_25 is None:
            self.time_taken_25 = t
        if self.total_infected >= 0.50 * self.total and self.time_taken_50 is None:
            self.time_taken_50 = t
        if self.total_infected >= 0.75 * self.total and self.time_taken_75 is None:
            self.time_taken_75 = t
        if self.total_infected >= 1 * self.total and self.time_taken_100 is None:
            self.time_taken_100 = t

    def get_trajectory_stats(self):
        n = len(self.total_infected_hist)
        self.infected_hawk_hist += [100 for _ in range(20000 - n)]
        self.infected_dove_hist += [100 for _ in range(20000 - n)]
        self.total_infected_hist += [200 for _ in range(20000 - n)]
        return {
            'infected_hawks': self.infected_hawk_hist,
            'infected_doves': self.infected_dove_hist,
            'total_infected': self.total_infected_hist,
        }

    def get_experiment_stats(self):
        return {
            'num_hawks': self.num_hawks,
            'num_doves': self.num_doves,
            'num_hawks_infected': self.num_hawks_infected_initial,
            'num_doves_infected': self.num_doves_infected_initial,
            'infection_rate': self.infection_rate,
            'mask_effectiveness': self.mask_effectiveness,
            'improper_mask_usage_severity': self.improper_mask_usage_severity,
            'percent_improper_mask_usage': self.percent_improper_mask_usage,
            'percent_stationary': self.percent_stationary,
            'probability_quarantined': self.probability_quarantined,
            'time_25': self.time_taken_25,
            'time_50': self.time_taken_50,
            'time_75': self.time_taken_75,
            'time_100': self.time_taken_100,
            'total_infected': self.total_infected,
            'total_time': self.t,
        }

    def __repr__(self):
        return f"t: {self.t}, Total infected: {self.total_infected}"
