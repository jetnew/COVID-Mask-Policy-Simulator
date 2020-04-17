import numpy as np
from agents import *


class Env:
    def __init__(self,
                 num_hawks,
                 num_doves,
                 num_hawks_infected,
                 num_doves_infected,
                 stats,
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
        self.populate()

    def play(self):
        while not self.done():
            self.step()
    def done(self):
        return self.stats.infected_doves == self.num_doves and \
               self.stats.infected_hawks == self.num_hawks
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

        # Update statistics
        self.stats.update()

    def trace(self, agent, tracer):
        if agent.coord not in tracer:
            tracer[agent.coord] = []
        tracer[agent.coord].append(agent)

    def populate(self):
        for i in range(self.num_hawks):
            rand_coord = (np.random.randint(0, self.x), np.random.randint(0, self.y))
            infected = i < self.num_hawks_infected
            self.agents.append(Agent(self, rand_coord, masked=False, infected=infected, stats=self.stats))

        for i in range(self.num_doves):
            rand_coord = (np.random.randint(0, self.x), np.random.randint(0, self.y))
            infected = i < self.num_doves_infected
            self.agents.append(Agent(self, rand_coord, masked=True, infected=infected, stats=self.stats))