import numpy as np
import os
import matplotlib.pyplot as plt

def sphere(x, y):
    return x**2 + y**2

# THE FOLLOWING WILL GO INSIDE THE TRAINING LOOP - SHOULD WE ADD FOR TESTING ? IF SO SEPERTAE CONDITIONAL STATEMENT

folder_i= "particle_plots_worst"
folder_f="particle_plots_best"
os.makedirs(folder_i, exist_ok=True)
os.makedirs(folder_f, exist_ok=True)


#positions = np.array([p.position_i for p in swarm])

points = np.array([
    [2, 1],
    [-1, 3],
    [1, -2]
])

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = sphere(X, Y)

iteration=1
maxiter = 2

if iteration is 1 or maxiter: 

  plt.contour(X, Y, Z, levels=20)

  # Plot particle points
  plt.scatter(points[:,0], points[:,1], color="black")

  if iteration == 1 :
    filename = os.path.join(folder_i, f"sphere_contour_iter={iteration}.png") # instead ofiteration we can add the run number

    plt.savefig(filename, dpi=300) # saving to current dir

    plt.show()

  if iteration == maxiter:

    filename = os.path.join(folder_f, f"sphere_contour_iter={iteration}.png")

    plt.savefig(filename, dpi=300) # saving to current dir

    plt.show()

