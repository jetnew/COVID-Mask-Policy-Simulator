from agents import *
from env import *
from animate import *
from stats import *
import random
import pandas as pd
import tqdm


def initialise_param():
    return {
        'num_hawks': 100,
        'num_doves': 100,
        'num_hawks_infected': 10,  # Initial no. of unmasked infected
        'num_doves_infected': 10,  # Initial no. of masked infected
        'infection_rate': 0.20,  # Rate from unmasked to unmasked
        'mask_effectiveness': 5,  # [1, inf], Rate / Effectiveness = Rate from unmasked to masked
        'improper_mask_usage_severity': 0,  # [0, 1], Percentage increase of rate
        'percent_improper_mask_usage': 0,  # Percent of doves that improperly use masks
        'percent_stationary': 0,  # Percent of people that abide by social distancing
        'probability_quarantined': 0  # Probability of being tested and diagnosed
    }


def experiment(param):
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

    env.play()
    return stats.get_trajectory_stats(), stats.get_experiment_stats()

def initialise_data():
    return {
        'num_hawks': [],
        'num_doves': [],
        'num_hawks_infected': [],
        'num_doves_infected': [],
        'infection_rate': [],
        'mask_effectiveness': [],
        'improper_mask_usage_severity': [],
        'percent_improper_mask_usage': [],
        'percent_stationary': [],
        'probability_quarantined': [],
        'time_25': [],
        'time_50': [],
        'time_75': [],
        'time_100': [],
        'total_infected': [],
        'total_time': [],
    }

# # Experimental control 1: Visualise trajectory of hawk-dove infections
# print("Experimental control 1")
# param = initialise_param()
# experiment_data = initialise_data()
# for i in tqdm.tqdm(range(30)):
#     data1, data2 = experiment(param)
#     pd.DataFrame(data1).to_csv(f"data/control_1/experimental_control_1_{i}.csv", index=False)
#     for d in data2:
#         experiment_data[d].append(data2[d])
# pd.DataFrame(experiment_data).to_csv("data/control_1/experimental_control_1_t.csv", index=False)
# # Combine average
# data = pd.read_csv("data/control_1/experimental_control_1_0.csv")
# for i in range(1, 30):
#     data += pd.read_csv(f"data/control_1/experimental_control_1_{i}.csv")
# data /= 30
# data.to_csv("data/control_1/experimental_control_1_combined.csv", index=None)


# # Experimental control 2: Only tweak hawk-dove ratio
# print("Experimental control 2")
# param = initialise_param()
# experiment_data = initialise_data()
# for j in range(30):
#     print("j:", j)
#     for i in tqdm.tqdm(range(10, 200, 10)):
#         param['num_hawks'] = 200 - i
#         param['num_doves'] = i
#         _, data = experiment(param)
#         for d in data:
#             experiment_data[d].append(data[d])
#     pd.DataFrame(experiment_data).to_csv(f"data/control_2/experimental_control_{j}.csv", index=False)
# Combined Averages
# df = pd.read_csv("data/control_2/experimental_control_29.csv")
# data = df.loc[:18]
# for i in range(1, 30):
#   data += df.loc[i*19:(i+1)*19-1].reset_index()
#   data /= 30
# data.to_csv("data/control_2/experimental_control_2_combined.csv", index=None)


# # Mask Effectiveness Condition: Only tweak difference in transmission rate between masked and unmasked
# print("Mask Effectiveness Condition")
# param = initialise_param()
# experiment_data = initialise_data()
# for k in tqdm.tqdm(range(30)):
#     for j in range(1, 6):
#         param['mask_effectiveness'] = j
#         for i in range(10, 200, 10):
#             param['num_hawks'] = 200 - i
#             param['num_doves'] = i
#             _, data = experiment(param)
#             for d in data:
#                 experiment_data[d].append(data[d])
#     pd.DataFrame(experiment_data).to_csv(f"data/mask_effectiveness/mask_effectiveness_condition_{k}.csv", index=False)
# # Combined Averages
# df = pd.read_csv("data/mask_effectiveness/mask_effectiveness_condition_29.csv")
# data = df.loc[:18]
# for i in range(1, 30):
#   data += df.loc[i*19:(i+1)*19-1].reset_index()
# data /= 30
# data.to_csv("data/mask_effectiveness/mask_effectiveness_condition_combined.csv", index=None)


# # Improper Mask Usage Condition: Only tweak infection rate to masked than to unmasked
# print("Improper Mask Usage Condition")
# param = initialise_param()
# experiment_data = initialise_data()
# param['percent_improper_mask_usage'] = 0.5
# for k in tqdm.tqdm(range(30)):
#     for j in np.arange(0, 2, 0.4):
#         param['improper_mask_usage_severity'] = j
#         for i in range(10, 200, 10):
#             param['num_hawks'] = 200 - i
#             param['num_doves'] = i
#             _, data = experiment(param)
#             for d in data:
#                 experiment_data[d].append(data[d])
# pd.DataFrame(experiment_data).to_csv("data/improper_mask_usage/improper_mask_usage_condition.csv", index=False)
# # Combined Averages
# df = pd.read_csv("data/improper_mask_usage/improper_mask_usage_condition.csv")
# data = df.loc[:18]
# for i in range(1, 30):
#   data += df.loc[i*19:(i+1)*19-1].reset_index()
# data /= 30
# data.to_csv("data/improper_mask_usage/improper_mask_usage_condition_combined.csv", index=None)


# # Improved Hygiene Policy: Only tweak infection rate
# print("Improved Hygiene Policy")
# param = initialise_param()
# experiment_data = initialise_data()
# for k in tqdm.tqdm(range(22)):
#     for j in np.arange(0.20, 0, -0.04):
#         print(j)
#         param['infection_rate'] = j
#         for i in range(10, 200, 10):
#             param['num_hawks'] = 200 - i
#             param['num_doves'] = i
#             _, data = experiment(param)
#             for d in data:
#                 experiment_data[d].append(data[d])
#     pd.DataFrame(experiment_data).to_csv("data/improved_hygiene/improved_hygiene_policy.csv", index=False)


# # Social Distancing Policy: Only tweak percent stationary
# print("Social Distancing Policy")
# param = initialise_param()
# experiment_data = initialise_data()
# for k in tqdm.tqdm(range(30)):
#     for j in np.arange(0, 1, 0.2):
#         print("j:", j)
#         param['percent_stationary'] = j
#         for i in range(10, 200, 10):
#             param['num_hawks'] = 200 - i
#             param['num_doves'] = i
#             _, data = experiment(param)
#             for d in data:
#                 experiment_data[d].append(data[d])
#     pd.DataFrame(experiment_data).to_csv("data/social_distancing/social_distancing_policy.csv", index=False)
# # Combined Averages
# df = pd.read_csv("data/social_distancing/social_distancing_policy.csv")
# data = df.loc[:94]
# for i in range(1, 30):
#   data += df.loc[i*95:(i+1)*95-1].reset_index()
# data /= 30
# data.to_csv("data/social_distancing/social_distancing_policy_combined.csv", index=None)


# Widespread Testing Policy: Only tweak percent probability quarantined
print("Widespread Testing Policy")
param = initialise_param()
experiment_data = initialise_data()
for k in tqdm.tqdm(range(7)):
    for j in np.arange(0, 0.02, 0.004):
        print(j)
        param['probability_quarantined'] = j
        for i in range(10, 200, 10):
            param['num_hawks'] = 200 - i
            param['num_doves'] = i
            _, data = experiment(param)
            for d in data:
                experiment_data[d].append(data[d])
    pd.DataFrame(experiment_data).to_csv("data/widespread_testing/widespread_testing_policy.csv", index=False)
# # Combined Averages
# df = pd.read_csv("data/widespread_testing/widespread_testing_policy.csv")
# data = df.loc[:18]
# for i in range(1, 30):
#   data += df.loc[i*19:(i+1)*19-1].reset_index()
# data /= 30
# data.to_csv("data/widespread_testing/widespread_testing_policy_combined.csv", index=None)