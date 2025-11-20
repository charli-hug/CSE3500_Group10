import unittest
#from pso import pso_simple
#from pso.cost_functions import sphere
# from pso.cost_functions import ackley
# from pso.cost_functions import cigar
# from pso.cost_functions import rosenbrock
import time
import math
import pso 
import psoo
#ALL OF THIS WILL BE ADDED AS A FUNC INTO PSO.PY CODE 

#DIFFERENT COST FUNCTIONS CODE
# def sphere(x):
#     total=0
#     for i in range(len(x)):
#         total+=x[i]**2
#     return total
   


# def ackley(x):

#     a = 20
#     b = 0.2
#     c = 2 * math.pi
#     n = len(x)

#     if n == 0:
#         return 0  # Define ackley(0D) as 0

#     sum_sq = sum(xi**2 for xi in x)
#     sum_cos = sum(math.cos(c * xi) for xi in x)

#     term1 = -a * math.exp(-b * math.sqrt(sum_sq / n))
#     term2 = -math.exp(sum_cos / n)

#     return term1 + term2 + a + math.e


# def cigar(x):
#     n = len(x)

#     if n == 0:
#         return 0  # Define cigar(0D) as 0

#     # Cigar function: f(x) = x1^2 + 1e6 * sum_{i=2}^n (xi^2)
#     if n == 1:
#         return x[0] ** 2  # 1D case

#     return x[0]**2 + 1e6 * sum(xi**2 for xi in x[1:])


# def rosenbrock(x):

#     n = len(x)

#     if n == 0:
#         return 0  # Define rosenbrock(0D) as 0

#     # Rosenbrock function: f(x) = sum_{i=1}^{n-1} [100*(x_{i+1} - x_i^2)^2 + (x_i - 1)^2]
#     total = 0
#     for i in range(n - 1):
#         total += 100 * (x[i+1] - x[i]**2)**2 + (x[i] - 1)**2

#     return total


#CODE FOR DIMENSIONS TESTING 
def test_everything():
    x0=[5,5]
    bounds=[(-10,10),(-10,10)]
    test_dimensions = [0,1,2,10,50,100,200,500,1000]
    for i in test_dimensions :
        x0=[5,5] * i
        bounds=[(-10,10),(-10,10)] * i
        start = time.time()
        opt = pso.run(x0, bounds, num_particles=15, psoo.best_c1,psoo.best_c2) # MUST TAKE BOUNDS AND X0 NO MATTER WHAT 
        # opt = run(ackley, x0, bounds, num_particles=100, maxiter=100, verbose=False)
        # opt = run(cigar, x0, bounds, num_particles=100, maxiter=100, verbose=False)
        # opt = run(rosenbrock, x0, bounds, num_particles=100, maxiter=100, verbose=False)
        end= time.time()

        time_taken = end - start

        # self.assertLess(sphere(opt[1]), sphere(x0))
        print(opt[0],f" : for dimesnion {i} took {time_taken} seconds")

if __name__=="__main__":
    print("Starting test file...")
    test_everything()
