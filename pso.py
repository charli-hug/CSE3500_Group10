    # evaluate current fitness
def evaluate(self,costFunc):
    self.err_i=costFunc(self.position_i)
    # check to see if the current position is an individual best
    if self.err_i<self.err_best_i or self.err_best_i==-1:
        self.pos_best_i=self.position_i.copy()
        self.err_best_i=self.err_i
                    

def update_velocity(self,pos_best_g):
    # update new particle velocity

def update_position(self,bounds):
    # updates the particle position based off new velocity updates

def sorted(data_pool, key = lambda item: item[0]):
    # this is the sorted function that is called in line 41 of the psoo algorithm
    pass
    w=0.5       # constant inertia weight (how much to weigh the previous velocity
    c1=1        # cognative constant (not sure what this means)
    c2=2        # social constant (also not sure what this means)

