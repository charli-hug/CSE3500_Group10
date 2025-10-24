from random import uniform
from random import random
import numpy as np

class Particle:
    def __init__(self):
        self.position_i=np.random.uniform(size=2)      # particle position
        self.velocity_i=np.random.uniform(-1,1,2)      # particle velocity
        self.pos_best_i=[]      # best position individual
        self.err_best_i=-1      # best error individual
        self.err_i=-1           # error individual

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.position_i)
        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i
                        

    def update_velocity(self,pos_best_g, c1, c2):
        # update new particle velocity
        r1= random()
        r2= random()
        w=0.5       # constant inertia weight (how much to weigh the previous velocity
        for i in range(0,2):
            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    def update_position(self,bounds):
        # updates the particle position based off new velocity updates
        pass

    def sorted(data_pool, key = lambda item: item[0]):
        # this is the sorted function that is called in line 41 of the psoo algorithm
        pass
        w=0.5       # constant inertia weight (how much to weigh the previous velocity
        c1=1        # cognative constant (not sure what this means)
        c2=2        # social constant (also not sure what this means)

