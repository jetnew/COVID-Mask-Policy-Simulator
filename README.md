# COVID Mask Policy Simulator

<img src="https://user-images.githubusercontent.com/27071473/80305146-b57ba680-87ed-11ea-9324-2ff88b57cd55.png" width="50%">

COVID Mask Policy Simulator is an Agent-Based Model built to simulate the spread of infectious diseases in order to investigate the extent to which mask-wearing is beneficial in the context of different policy interventions. 

6 different experiments are performed in the simulation: An experimental control, a mask effectiveness condition, an improper mask handling condition, an improved hygiene policy, a lockdown policy and an aggressive testing policy.

The results show that the practice of mask-wearing allows mask wearers to benefit from a range of policy interventions to a greater extent than non-mask wearers.

# Research Questions

1. If masks are less effective, how much safer are mask-wearers than non mask-wearers?
2. If masks are improperly handled, how much safer/dangerous are mask-wearers?
3. How does improved hygiene policy affect the effectiveness of mask wearing?
4. How does the effectiveness of lockdown policies affect the effectiveness of mask-wearing?
5. How does the effectiveness of aggressive testing policies affect the effectiveness of mask-wearing?

![image](https://user-images.githubusercontent.com/27071473/80305162-cb896700-87ed-11ea-98e5-6e43d5e01e91.png)

# Experiment 1: Experimental Control
The objectives of the experimental control are: 1. to compare the transmission rate between mask wearers and non-mask wearers; and 2. to analyse how the percentage of mask wearers (tM/tT) in the population affects transmission rate.

![image](https://user-images.githubusercontent.com/27071473/80305424-1bb4f900-87ef-11ea-90a4-320cc2ed5113.png)

No. of transmissions over time. Left: Sample 1, Right: Averaged (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305215-11462f80-87ee-11ea-8711-8d34a92c613e.png)

Time taken to infect T% of the population against nM)/nT Left: Sample 1, Right: Averaged (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305241-2e7afe00-87ee-11ea-9525-fca8023c404d.png)

Exponential regression of time taken against nM)/nT

![image](https://user-images.githubusercontent.com/27071473/80305247-405ca100-87ee-11ea-95ff-409c6818c82c.png)

# Experiment 2: Mask Effectiveness Condition
The objective of the mask effectiveness condition is to analyse how the effectiveness of mask (em) affects the difference in transmission rate between mask wearers and non-mask wearers (dmu). The effectiveness of masks is inversely proportional to the rate of infection.

![image](https://user-images.githubusercontent.com/27071473/80305258-5702f800-87ee-11ea-9d2f-dcd7806d0a1f.png)

Time taken to infect T% of the population, against em and nM/nT, averaged over 30 samples (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305264-5ff3c980-87ee-11ea-859e-db987c529b7e.png)

Difference in t50 between nM/nT = 0.3 and 0.7 against em, averaged (n=30)

# Experiment 3: Improper Mask Handling Condition
The objective of the improper mask handling condition is to analyse how the severity of improper mask handling (su) affects the difference in transmission rate between mask wearers and non-mask wearers (dmu). An assumption made to reduce simulation complexity is that 50% of mask wearers handle masks improperly. As the study investigates relative values, the severity of improper mask handling sufficiently captures the consequence of the improper mask handling situation.

![image](https://user-images.githubusercontent.com/27071473/80305274-70a43f80-87ee-11ea-8fa0-b1e61ddd2a7c.png)

Time taken to infect T% of the population, against su and nM/nT, averaged (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305281-79951100-87ee-11ea-83fd-288ceeb8ec9f.png)

Difference in t50 against su, averaged (n=30)

# Experiment 4: Improved Hygiene Policy
The objective of the improved hygiene policy is to analyse how reduced transmission rate from improved hygiene (ri) affects the difference in transmission rate between mask wearers and non-mask wearers (dmu). The effectiveness of the hygiene policy is inversely proportional to the infection rate (ri). The rate of infection (ri) between non-mask wearers is thus modified to indicate the effectiveness of the hygiene policy.

![image](https://user-images.githubusercontent.com/27071473/80305284-83b70f80-87ee-11ea-961a-7ec3eb4bd4ac.png)

Time taken to infect T% of the population, against ri and nM/nT, averaged (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305295-929dc200-87ee-11ea-9843-240d7e61e449.png)

Difference in t50 against ri vs ri^4, averaged (n=30)

# Experiment 5: Lockdown Policy
The objective of the lockdown policy is to analyse how percentage of people abiding by a lockdown (ps) affects the difference in transmission rate between mask wearers and non-mask wearers (dmu). Agents that abide by the lockdown policy will remain stationary, while agents that do not will continue movement.

![image](https://user-images.githubusercontent.com/27071473/80305311-a1847480-87ee-11ea-92d3-399a6a9fcd0b.png)

Time taken to infect T% of the population, against su and nM/nT, averaged (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305321-aba67300-87ee-11ea-9ce8-846a15cbb274.png)

Difference in t50 against ps vs ps^4, averaged (n=30)

# Experiment 6: Aggressive Testing Policy
The objective of the aggressive testing policy is to analyse how aggressiveness of testing (and quarantine) (pq) affects the difference in transmission rate between mask wearers and non-mask wearers (dmu). At every timestamp, every infected agent has a probability of being tested and quarantined at pq, and removed from the environment, preventing further spread from the diagnosed agent. An assumption made to enable inter-experimental comparison is that the probability pq is restricted to a low value to enable 100% of the population to be infected at the end of the simulation.

![image](https://user-images.githubusercontent.com/27071473/80305344-caa50500-87ee-11ea-8ab6-6add3799d9bb.png)

Time taken to infect T% of the population, against su and nM/nT, averaged (n=30)

![image](https://user-images.githubusercontent.com/27071473/80305353-d5f83080-87ee-11ea-8bf5-d51e946c8bf7.png)

Left: Difference in t50 against pq, averaged (n=30), Right: Total Infected at the end of the experiment, averaged (n=30)

# Results and Discussion
Mask wearers are safer than non-mask wearers for the baseline experiment with all other variables held constant. A strong positive linear relationship was found between effectiveness of masks and difference in transmission rate between mask wearers and non-mask wearers. There was also a strong negative linear relationship between severity of improper mask handling and difference in transmission rate between mask wearers and non-mask wearers. For mask wearers to maximise the benefits of mask-wearing, they have to ensure that the better masks are used and masks are properly handled.
 
While many policies are generally effective in reducing transmission rates, mask wearers and non-mask wearers reap the benefits differently. When implemented in tandem with policies driving improved hygiene, aggressive testing and lockdown measures, the difference in transmission rate between mask wearers and non-mask wearers increases as the extent of policy intervention increases. For simulations conducted for improved hygiene policy and lockdown policy, a quartic relationship was observed between policy intervention, represented by rate of transmission between non-mask wearers and difference in transmission rate between mask wearers and non-mask wearers. For simulations conducted for aggressive testing policy, the higher the effectiveness of the aggressive testing policy, the larger the difference in transmission rate between mask wearers and non-mask wearers.  This shows that as policies are implemented widely, their effectiveness will also be boosted when more people wear masks, thus benefiting the population at large with longer transmission times. 

In our formulation of the best case scenarios (i.e. high number of mask-wearers and high policy intervention), results showed higher variability in the time taken for a certain population to be infected. However, it is important to note that higher variability with lower transmission rate is a significantly better situation than a lower variability with higher transmission rate.

# Limitations and Future Directions
A limitation of our study that future studies can build on is the simplified representation of reality in our simulation. We chose to reduce the environment’s complexity due to our research’s focus on the relative consequences of mask wearers and non-mask wearers with respect to circumstances and policy interventions, rather than the realism of the empirical results. As a result, the following assumptions are made. Firstly, the spread of the disease was modeled with only 2 states (infected and uninfected) and 2 homogenous categories of agents (masked and unmasked). Secondly, the agents modelled in our simulation display stationarity of behaviour, as mask wearers remain as mask wearers and vice versa throughout the duration of the simulation. This assumption might not hold true as behaviors might be altered by policy interventions or increase in infection rates. Thirdly, the country is modelled as a closed environment of low complexity (2D grid world), with agent movement modelled as random walks. An improvement would be to add details, at the cost of higher complexity, to better represent the underlying situation of the spread of COVID-19. For example, an application could model travel patterns and areas of travel such as work and home more realistically.

To build upon our findings, other studies could utilize agent-based modeling using the COVID Mask Simulator to represent the spread of COVID-19 in other situations, such as within hospitals or workplaces, or to even model the effects of policy interventions in order to guide government decision-making. (e.g. time required for a lockdown to curb the spread of the disease).

# Conclusion
In conclusion, the results of our agent-based modeling study strongly support correctly wearing quality masks to curb the spread of COVID-19. Our results from simulating policy interventions on the COVID Mask Policy Simulator show that the practice of mask-wearing allows mask wearers to benefit from a range of policy interventions to a greater extent than non-mask wearers. Mask-wearing produces a positive reinforcing effect on policy interventions and ultimately produces better outcomes for the entire population in terms of curbing the spread of disease.
