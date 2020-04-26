import random


class Agent:
    def __init__(self,
                 env,
                 coord,
                 masked,
                 infected,
                 stationary,
                 improper,
                 stats,
                 infection_r,
                 mask_e,
                 prob_q):
        self.env = env
        self.coord = coord
        self.masked = masked
        self.infected = infected
        self.stationary = stationary
        self.improper = improper
        self.stats = stats
        self.infection_r = infection_r
        self.mask_e = mask_e
        self.prob_q = prob_q
        self.quarantined = False

    def move(self):
        if not self.stationary:
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
                rate = self.infection_r / (self.mask_e ** 2)
                rate += rate * self.improper
                if random.random() < rate:
                    self.infected = True
                    self.stats.infected_doves += 1
                    self.stats.curr_infected += 1
            elif by_masked and not self.masked:
                if random.random() < self.infection_r / self.mask_e:
                    self.infected = True
                    self.stats.infected_hawks += 1
                    self.stats.curr_infected += 1
            elif not by_masked and self.masked:
                rate = self.infection_r / self.mask_e
                rate += rate * self.improper
                if random.random() < rate:
                    self.infected = True
                    self.stats.infected_doves += 1
                    self.stats.curr_infected += 1
            else:
                if random.random() < self.infection_r:
                    self.infected = True
                    self.stats.infected_hawks += 1
                    self.stats.curr_infected += 1

        # Widespread testing causing quarantine
        if self.infected:
            if random.random() < self.prob_q:
                self.quarantined = True
                self.stats.curr_infected -= 1


