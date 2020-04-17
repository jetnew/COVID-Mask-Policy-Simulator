import random


class Agent:
    def __init__(self, env, coord, masked, infected, stats):
        self.env = env
        self.coord = coord
        self.masked = masked
        self.infected = infected
        self.stats = stats

    def move(self):
        action = (random.choice([-1,0,1]), random.choice([-1,0,1]))
        x = min(self.env.x-1, max(0, self.coord[0] + action[0]))
        y = min(self.env.y-1, max(0, self.coord[1] + action[1]))
        self.coord = (x,y)

    def risk_infection(self, by_masked):
        """
        Probabilities:
        Masked to masked: 0.01
        Masked to unmasked: 0.05
        Unmasked to masked: 0.05
        Unmasked to unmaskled: 0.20
        """
        if not self.infected:
            if by_masked and self.masked:
                if random.random() < 0.01:
                    self.infected = True
                    self.stats.infected_doves += 1
            elif by_masked and not self.masked:
                if random.random() < 0.05:
                    self.infected = True
                    self.stats.infected_hawks += 1
            elif not by_masked and self.masked:
                if random.random() < 0.05:
                    self.infected = True
                    self.stats.infected_doves += 1
            else:
                if random.random() < 0.20:
                    self.infected = True
                    self.stats.infected_hawks += 1


