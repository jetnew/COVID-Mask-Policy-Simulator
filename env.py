import numpy as np
from agents import *


class Env:
    def __init__(self,
                 num_hawks,
                 num_doves,
                 num_hawks_infected,
                 num_doves_infected,
                 stats,
                 infection_rate,
                 mask_effectiveness,
                 percent_stationary,
                 improper_mask_usage_severity,
                 percent_improper_mask_usage,
                 probability_quarantined,
                 size=(100,100)):
        self.num_hawks = num_hawks
        self.num_doves = num_doves
        self.num_hawks_infected = num_hawks_infected
        self.num_doves_infected = num_doves_infected
        self.x , self.y = size
        self.state = np.zeros(shape=(size[0], size[1], 3))
        self.agents = []
        self.stats = stats
        self.stats.infected_hawks = num_hawks_infected
        self.stats.infected_doves = num_doves_infected
        self.infection_rate = infection_rate
        self.mask_effectiveness = mask_effectiveness
        self.percent_stationary = percent_stationary
        self.improper_mask_usage_severity = improper_mask_usage_severity
        self.percent_improper_mask_usage = percent_improper_mask_usage
        self.probability_quarantined = probability_quarantined
        self.populate()
        self.t = 0

    def play(self):
        while not self.done():
            self.step()
    def done(self):
        return self.stats.infected_doves == self.num_doves and \
               self.stats.infected_hawks == self.num_hawks \
                or (not any([a.quarantined for a in self.agents]) \
                and self.stats.curr_infected == 0)
    def step(self):
        # Contact Tracer = {location_name: {(x,y): [Agent]}}
        contact_tracer = {}

        # Agent takes a step
        for agent in self.agents:
            self.state[agent.coord] = 0
            agent.move()

            self.trace(agent, contact_tracer)

        # If any contact is infected, risk infection.
        for coord, contacts in contact_tracer.items():
            if len(contacts) > 1:
                for agent in contacts:
                    if agent.infected:
                        for contact in contacts:
                            contact.risk_infection(by_masked=agent.masked)

        # # Remove quarantined people
        self.agents = [a for a in self.agents if not a.quarantined]

        # Update agent colour
        for agent in self.agents:
            if agent.masked and not agent.infected:
                self.state[agent.coord] = (1,1,1)  # white
            elif agent.masked and agent.infected:
                self.state[agent.coord] = (0,0.5,1)  # orange
            elif not agent.masked and not agent.infected:
                self.state[agent.coord] = (0,1,1)  # yellow
            else:
                self.state[agent.coord] = (0,0,1)  # red

        # Count no. of currently infected people
        self.num_curr_infected = len([agent for agent in self.agents if agent.infected])

        # Update statistics
        self.stats.update(self.t)
        self.t += 1

    def trace(self, agent, tracer):
        if agent.coord not in tracer:
            tracer[agent.coord] = []
        tracer[agent.coord].append(agent)

    def populate(self):
        for i in range(self.num_hawks):
            rand_coord = (np.random.randint(0, self.x), np.random.randint(0, self.y))
            infected = i < self.num_hawks_infected
            stationary = i < self.num_hawks * self.percent_stationary
            self.agents.append(Agent(self,
                                     rand_coord,
                                     masked=False,
                                     infected=infected,
                                     stationary=stationary,
                                     improper=0,
                                     stats=self.stats,
                                     infection_r=self.infection_rate,
                                     mask_e=self.mask_effectiveness,
                                     prob_q=self.probability_quarantined))

        for i in range(self.num_doves):
            rand_coord = (np.random.randint(0, self.x), np.random.randint(0, self.y))
            infected = i < self.num_doves_infected
            stationary = i < self.num_doves * self.percent_stationary
            improper = self.improper_mask_usage_severity \
                if i < self.num_doves * self.percent_improper_mask_usage \
                else 0
            self.agents.append(Agent(self,
                                     rand_coord,
                                     masked=True,
                                     infected=infected,
                                     stationary=stationary,
                                     improper=improper,
                                     stats=self.stats,
                                     infection_r=self.infection_rate,
                                     mask_e=self.mask_effectiveness,
                                     prob_q=self.probability_quarantined))