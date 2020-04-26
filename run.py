from agents import *
from env import *
from animate import *
from stats import *
# from analysis import *
import random


param = {
    'num_hawks': 100,
    'num_doves': 100,
    'num_hawks_infected': 10,  # Initial no. of unmasked infected
    'num_doves_infected': 10,  # Initial no. of masked infected
    'infection_rate': 0.20,  # Rate from unmasked to unmasked
    'mask_effectiveness': 1,  # [1, inf], Rate / Effectiveness = Rate from unmasked to masked
    'improper_mask_usage_severity': 0,  # [0, 1], Percentage increase of rate
    'percent_improper_mask_usage': 0,  # Percent of doves that improperly use masks
    'percent_stationary': 0,  # Percent of people that abide by social distancing
    'probability_quarantined': 0.1  # Probability of being tested and diagnosed
}

stats = Stats(num_hawks=param['num_hawks'],
              num_doves=param['num_doves'],
              num_hawks_infected_initial=param['num_hawks_infected'],
              num_doves_infected_initial=param['num_doves_infected'],
              infection_rate=param['infection_rate'],
              mask_effectiveness=param['mask_effectiveness'],
              percent_stationary=param['percent_stationary'],
              improper_mask_usage_severity=param['improper_mask_usage_severity'],
              percent_improper_mask_usage=param['percent_improper_mask_usage'],
              probability_quarantined=param['probability_quarantined'])

env = Env(num_hawks=param['num_hawks'],
          num_doves=param['num_doves'],
          num_hawks_infected=param['num_hawks_infected'],
          num_doves_infected=param['num_doves_infected'],
          infection_rate=param['infection_rate'],
          mask_effectiveness=param['mask_effectiveness'],
          percent_stationary=param['percent_stationary'],
          improper_mask_usage_severity=param['improper_mask_usage_severity'],
          percent_improper_mask_usage=param['percent_improper_mask_usage'],
          probability_quarantined=param['probability_quarantined'],
          size=(100, 100),
          stats=stats)

# env.play()
ani = Animation(env, speed=1, dim=(600, 600))
ani.play()

print(stats.get_experiment_stats())
# stats.to_csv_trajectory("traj.csv")
# visualise("traj.csv")