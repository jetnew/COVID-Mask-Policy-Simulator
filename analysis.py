import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')


# visualise("data/control_1/experimental_control_1_combined.csv")
# visualise("data/control_1/experimental_control_1_0.csv")

# df = pd.read_csv("data/control_1/experimental_control_1_combined.csv")
# ax = plt.axes()
# ax.set_xlabel("Time Taken")
# ax.set_ylabel("No. of Infections")
# plt.plot(df['total_infected'], label='Total Infected People')
# plt.plot(df['infected_doves'], label='Infected Mask Wearers')
# plt.plot(df['infected_hawks'], label='Infected Non-mask Wearers')
# plt.title("Experimental Control, Objective 1, Averaged (n=30)")
# plt.legend(loc="upper left")
# plt.show()

def plot(x, y, z, title, x_label, y_label, z_label):
  X, Y = np.meshgrid(x, y)
  Z = z.reshape((len(y), len(x)))
  x = X.flatten()
  y = Y.flatten()
  ax = plt.axes(projection='3d')
  plt.title(title)
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_zlabel(z_label)
  ax.scatter(x, y, z, c=z, cmap='plasma', linewidth=0.5)
  plt.show()


# # MASK EFFECTIVENESS DIFFERENCE PLOT
# df = pd.read_csv("data/mask_effectiveness/mask_effectiveness_condition_combined.csv")
# x = np.arange(0.05, 1, 0.05)
# y = np.arange(1, 6, 1)
# for t in ['time_25', 'time_50', 'time_75', 'time_100']:
#   plot(x, y, df[t].values, f"Mask Effectiveness Condition ({t}), Averaged (n=30)", "n_M/n_T", "e_m", t)

# df = pd.read_csv("data/mask_effectiveness/diff.csv")
# ax = plt.axes()
# ax.set_xlabel("e_m")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across e_m")
# plt.plot(df['m_e'], df['d_mu'])
# plt.plot(df['m_e'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper left')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['m_e'], df['d_mu'])[0])


# # IMPROPER MASK HANDLING DIFFERENCE PLOT
# df = pd.read_csv("data/improper_mask_usage/improper_mask_usage_condition_combined.csv")
# x = np.arange(0.05, 1, 0.05)
# y = np.arange(0, 2, 0.4)
# for t in ['time_25', 'time_50', 'time_75', 'time_100']:
#   plot(x, y, df[t].values, f"Improper Mask Handling Condition ({t}), Averaged (n=30)", "n_M/n_T", "s_u", t)

# df = pd.read_csv("data/improper_mask_usage/diff.csv")
# ax = plt.axes()
# ax.set_xlabel("s_u")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across s_u")
# plt.plot(df['s_u'], df['d_mu'])
# plt.plot(df['s_u'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper right')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['s_u'], df['d_mu'])[0])


# Social distancing analysis
# df = pd.read_csv("data/social_distancing/social_distancing_policy_combined.csv")
# x = np.arange(0.05, 1, 0.05)
# y = np.arange(0, 1, 0.2)
# for t in ['time_25', 'time_50', 'time_75', 'time_100']:
#   plot(x, y, df[t].values, f"Lockdown Policy ({t}), Averaged (n=30)", "n_M/n_T", "p_s", t)

# df = pd.read_csv("data/social_distancing/social_distancing_policy_diff.csv")
# ax = plt.axes()
# ax.set_xlabel("p_s")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across p_s")
# plt.plot(df['p_s'], df['d_mu'])
# plt.plot(df['p_s'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper left')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['p_s'], df['d_mu'])[0])
#
# ax = plt.axes()
# ax.set_xlabel("p_s^2")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across p_s^2")
# plt.plot(df['p_s^2'], df['d_mu'])
# plt.plot(df['p_s^2'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper left')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['p_s^2'], df['d_mu'])[0])
#
# ax = plt.axes()
# ax.set_xlabel("p_s^4")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across p_s^4")
# plt.plot(df['p_s^4'], df['d_mu'])
# plt.plot(df['p_s^4'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper left')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['p_s^4'], df['d_mu'])[0])


# # Improved Hygiene policy analysis
# df = pd.read_csv("data/improved_hygiene/improved_hygiene_policy_combined.csv")
# x = np.arange(0.05, 1, 0.05)
# y = np.arange(0.04, 0.24, 0.04)
# for t in ['time_25', 'time_50', 'time_75', 'time_100']:
#   plot(x, y, df[t].values, f"Improved Hygiene Policy ({t}), Averaged (n=30)", "n_M/n_T", "r_i", t)

# df = pd.read_csv("data/improved_hygiene/improved_hygiene_policy_diff.csv")
# ax = plt.axes()
# ax.set_xlabel("r_i")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across r_i")
# plt.plot(df['r_i'], df['d_mu'])
# plt.plot(df['r_i'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper right')
# plt.show()
#
# ax = plt.axes()
# ax.set_xlabel("r_i^2")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across r_i^2")
# plt.plot(df['r_i^2'], df['d_mu'])
# plt.plot(df['r_i^2'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper right')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['r_i^2'], df['d_mu'])[0])
#
# ax = plt.axes()
# ax.set_xlabel("r_i^4")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across r_i^4")
# plt.plot(df['r_i^4'], df['d_mu'])
# plt.plot(df['r_i^4'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper right')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['r_i^4'], df['d_mu'])[0])


# df = pd.read_excel("data/control_2/std_dev_2.xlsx", sheet_name="Sheet2")
# ax = plt.axes()
# ax.set_xlabel("n_M/n_T")
# ax.set_ylabel("std_dev at t_50")
# plt.title("Standard Deviation at t_50 against n_M/n_T")
# plt.plot(df['ratio'], df['std dev'], label="std_dev")
# plt.legend(loc='upper left')
# plt.show()


# Widespread Testing policy analysis
# df = pd.read_csv("data/widespread_testing/widespread_testing_policy_combined.csv")
# x = np.arange(0.05, 1, 0.05)
# y = np.arange(0, 0.02, 0.004)
# for t in ['time_25', 'time_50', 'time_75', 'time_100']:
#   plot(x, y, df[t].values, f"Aggressive Testing Policy ({t}), Averaged (n=30)", "n_M/n_T", "p_q", t)

# df = pd.read_csv("data/widespread_testing/widespread_testing_policy_diff.csv")
# ax = plt.axes()
# ax.set_xlabel("p_q")
# ax.set_ylabel("d_mu")
# plt.title("Difference in t_50 between n_M/n_T=0.3 and =0.7 across p_q")
# plt.plot(df['p_q'], df['d_mu'])
# plt.plot(df['p_q'], df['d_mu'], '.', c='r', label='d_mu')
# plt.legend(loc='upper left')
# plt.show()
# from scipy.stats import pearsonr
# print(pearsonr(df['p_q'], df['d_mu'])[0])

df = pd.read_csv("data/widespread_testing/widespread_testing_policy_combined.csv")
x = np.arange(0.05, 1, 0.05)
y = np.arange(0, 0.02, 0.004)
plot(x, y, df['total_infected'].values, f"Aggressive Testing Policy, Averaged (n=30)", "n_M/n_T", "p_q", "total infected")