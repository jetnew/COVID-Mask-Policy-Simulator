import numpy as np
import pandas as pd
import scipy


# # Experiment control 1
# data = pd.read_csv("data/control_1/experimental_control_1_0.csv")
# for i in range(1, 30):
#     data += pd.read_csv(f"data/control_1/experimental_control_1_{i}.csv")
# data /= 30
# data.to_csv("data/control_1/experimental_control_1_combined.csv", index=None)


# # Improper mask usage
# df = pd.read_csv("data/improper_mask_usage/improper_mask_usage_condition.csv")
# data = df.loc[:94]
# for i in range(1, 30):
#   data += df.loc[i*95:(i+1)*95-1].reset_index()
# data /= 30
# data.to_csv("data/improper_mask_usage   /improper_mask_usage_condition_combined.csv", index=None)


# # Mask effectiveness
# df = pd.read_csv("data/mask_effectiveness/mask_effectiveness_condition_29.csv")
# data = df.loc[:94]
# for i in range(1, 30):
#   data += df.loc[i*95:(i+1)*95-1].reset_index()
# data /= 30
# data.to_csv("data/mask_effectiveness/mask_effectiveness_condition_combined.csv", index=None)

# # Mask Effectiveness Difference Analysis
# df = pd.read_csv("data/mask_effectiveness/mask_effectiveness_condition_combined.csv")
# diff = []
# t1s = []
# t2s = []
# for i in range(1, 6):
#     t1 = df.loc[df['num_doves'] == 60].loc[df['mask_effectiveness'] == i]['time_50'].values[0]
#     t2 = df.loc[df['num_doves'] == 140].loc[df['mask_effectiveness'] == i]['time_50'].values[0]
#     t1s.append(t1)
#     t2s.append(t2)
#     diff.append(t2 - t1)
#
# pd.DataFrame({
#     'm_e': [1,2,3,4,5],
#     '60': t1s,
#     '140': t2s,
#     'd_mu': diff,
# }).to_csv("data/mask_effectiveness/diff.csv", index=False)
# print(t1s)
# print(t2s)
# print(diff)


# # Improper Mask Handling Difference Analysis
# df = pd.read_csv("data/improper_mask_usage/improper_mask_usage_condition_combined.csv")
# # print(df.loc[df['num_doves'] == 60].loc[df['improper_mask_usage_severity'] == 1.6]['time_50'])
# diff = []
# t1s = []
# t2s = []
# for i in range(5):
#     t1 = df.loc[df['num_doves'] == 60].loc[df['improper_mask_usage_severity'] == round(i*0.4,1)]['time_50'].values[0]
#     t2 = df.loc[df['num_doves'] == 140].loc[df['improper_mask_usage_severity'] == round(i*0.4,1)]['time_50'].values[0]
#     t1s.append(t1)
#     t2s.append(t2)
#     diff.append(t2 - t1)
#
# pd.DataFrame({
#     's_u': [i*0.4 for i in range(5)],
#     '60': t1s,
#     '140': t2s,
#     'd_mu': diff,
# }).to_csv("data/improper_mask_usage/diff.csv", index=False)
# print(t1s)
# print(t2s)
# print(diff)


# # Social Distancing ocmbined
# df = pd.read_csv("data/social_distancing/social_distancing_policy.csv")
# data = df.loc[:94]
# for i in range(1, 30):
#   data += df.loc[i*95:(i+1)*95-1].reset_index()
# data /= 30
# data.to_csv("data/social_distancing/social_distancing_combined.csv", index=None)

# # Social distancing Difference Analysis
df = pd.read_csv("data/social_distancing/social_distancing_policy_combined.csv")
# print(df.loc[df['num_doves'] == 60].loc[round(df['percent_stationary'],1) == 0.2])
# print(df.loc[df['num_doves'] == 60]['percent_stationary'][81])
# diff = []
# t1s = []
# t2s = []
#
#
# for i in np.arange(0, 1, 0.2):
#     t1 = df.loc[df['num_doves'] == 60].loc[round(df['percent_stationary'],1) == round(i,1)]['time_50'].values[0]
#     t2 = df.loc[df['num_doves'] == 140].loc[round(df['percent_stationary'],1) == round(i,1)]['time_50'].values[0]
#     t1s.append(t1)
#     t2s.append(t2)
#     diff.append(t2 - t1)
# pd.DataFrame({
#     'p_s': [0,0.2,0.4,0.6,0.8],
#     '60': t1s,
#     '140': t2s,
#     'd_mu': diff,
# }).to_csv("data/social_distancing/social_distancing_policy_diff.csv", index=False)
# print(t1s)
# print(t2s)
# print(diff)


# Improved Hygiene
# df = pd.read_csv("data/improved_hygiene/improved_hygiene_policy.csv")
# for i in range(11, 30):
#     _df = pd.read_csv(f"data/improved_hygiene/improved_hygiene_policy_{i}.csv")
#     df = df.append(_df, ignore_index=True)
# df.to_csv("data/improved_hygiene/improved_hygiene_policy_all.csv", index=False)


# # Improved Hygiene Difference Analysis
# df = pd.read_csv("data/improved_hygiene/improved_hygiene_policy_all.csv")
# print(df)
# data = df.loc[:94]
# for i in range(1, 30):
#   data += df.loc[i*95:(i+1)*95-1].reset_index()
# data /= 30
# data.to_csv("data/improved_hygiene/improved_hygiene_policy_combined.csv", index=None)


# Improved Hygiene Policy
# df = pd.read_csv("data/improved_hygiene/improved_hygiene_policy_combined.csv")
# # print(df.loc[df['num_doves'] == 60].loc[round(df['infection_rate'],2) == round(0.2,2)]['time_50'].values[0])
# diff = []
# t1s = []
# t2s = []
#
# for i in np.arange(0.2, 0, -0.04):
#     t1 = df.loc[df['num_doves'] == 60].loc[round(df['infection_rate'],2) == round(i,2)]['time_50'].values[0]
#     t2 = df.loc[df['num_doves'] == 140].loc[round(df['infection_rate'],2) == round(i,2)]['time_50'].values[0]
#     t1s.append(t1)
#     t2s.append(t2)
#     diff.append(t2 - t1)
# pd.DataFrame({
#     'r_i': [0.04,0.08,0.12,0.16,0.20],
#     '60': t1s,
#     '140': t2s,
#     'd_mu': diff,
# }).to_csv("data/improved_hygiene/improved_hygiene_policy_diff.csv", index=False)
# print(t1s)
# print(t2s)
# print(diff)


# Aggressive Testing Policy
# df1 = pd.read_csv("data/widespread_testing/widespread_testing_policy_1_18.csv")
# df2 = pd.read_csv("data/widespread_testing/widespread_testing_policy_19_22.csv")
# df3 = pd.read_csv("data/widespread_testing/widespread_testing_policy_23_27.csv")
# df4 = pd.read_csv("data/widespread_testing/widespread_testing_policy_28_30.csv")
# df = df1.append(df2, ignore_index=True).append(df3, ignore_index=True).append(df4, ignore_index=True)
# df.to_csv("data/widespread_testing/widespread_testing_policy_all.csv", index=False)

# df = pd.read_csv("data/widespread_testing/widespread_testing_policy_all.csv")
# data = df.loc[:94]
# for i in range(1, 30):
#   data += df.loc[i*95:(i+1)*95-1].reset_index()
# data /= 30
# data.to_csv("data/widespread_testing/widespread_testing_policy_combined.csv", index=None)

df = pd.read_csv("data/widespread_testing/widespread_testing_policy_combined.csv")
diff = []
t1s = []
t2s = []

for i in np.arange(0, 0.02, 0.004):
    t1 = df.loc[df['num_doves'] == 60].loc[round(df['probability_quarantined'],2) == round(i,2)]['time_50'].values[0]
    t2 = df.loc[df['num_doves'] == 140].loc[round(df['probability_quarantined'],2) == round(i,2)]['time_50'].values[0]
    t1s.append(t1)
    t2s.append(t2)
    diff.append(t2 - t1)
pd.DataFrame({
    'p_q': [0.004,0.008,0.012,0.016,0.020],
    '60': t1s,
    '140': t2s,
    'd_mu': diff,
}).to_csv("data/widespread_testing/widespread_testing_policy_diff.csv", index=False)
print(t1s)
print(t2s)
print(diff)