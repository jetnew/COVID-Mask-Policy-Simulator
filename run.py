from agents import *
from env import *
from animate import *
from stats import *
from analysis import *
import random


stats = Stats()
env = Env(num_hawks=0,
          num_doves=200,
          num_hawks_infected=0,
          num_doves_infected=20,
          size=(100, 100),
          stats=stats)

env.play()
# ani = Animation(env, speed=1, dim=(600, 600))
# ani.play()
stats.to_csv("df.csv")
visualise("df.csv")