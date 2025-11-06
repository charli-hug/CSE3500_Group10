from random import uniform, random
import numpy as np


class Particle:
    def __init__(self):
        self.position_i=np.random.uniform(size=2)      # particle position
        self.velocity_i=np.random.uniform(-1,1,2)      # particle velocity
        self.pos_best_i=[]      # best position individual
        self.err_best_i=-1      # best error individual
        self.err_i=-1           # error individual

    # evaluate current fitness
    def evaluate(self):
        total=0      #using sphere formula as fitness evaluation
        for i in range(len(self.position_i)):
            total+=x[i]**2
        self.err_i = total
        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i
                        

    def update_velocity(self,pos_best_g, c1, c2):
        # update new particle velocity
        r1= random()
        r2= random()
        w=0.5       # constant inertia weight (how much to weigh the previous velocity
        for i in range(0,2):    #0-2 range for 2-D 
            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    def update_position(self,bounds):
        # updates the particle position based off new velocity updates
        for i in range(0,2):    #0-2 range for 2-D 
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]
            
            # adjust maximum position if necessary
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i]<bounds[i][0]:
                self.position_i[i]=bounds[i][0]




#to run algorithm --> returning c1, c2, final_time
def run (num_particles, c1, c2):

    err_best_g=-1                   # best error for group
    pos_best_g=[]                   # best position for group
    # establish the swarm
    swarm=[]
    for i in range(0,num_particles):
        swarm.append(Particle())

    # begin optimization loop
    iterations=0
    maxiter = 30
    while i<maxiter:
        # cycle through particles in swarm and evaluate fitness
        for j in range(0,num_particles):
            swarm[j].evaluate()

            # determine if current particle is the best (globally)
            if swarm[j].err_i<err_best_g or err_best_g==-1:
                pos_best_g=list(swarm[j].position_i)
                err_best_g=float(swarm[j].err_i)
        
        # cycle through swarm and update velocities and position
        for j in range(0,num_particles):
            swarm[j].update_velocity(pos_best_g, c1, c2)
            swarm[j].update_position(bounds)
        iterations+=1
    return (c1, c2, iterations)

