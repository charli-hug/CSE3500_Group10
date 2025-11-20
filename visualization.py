import numpy as np
import os
import matplotlib.pyplot as plt
import shutil


def sphere(x, y):
    return x**2 + y**2

# THE FOLLOWING WILL GO INSIDE THE TRAINING LOOP - SHOULD WE ADD FOR TESTING ? IF SO SEPERTAE CONDITIONAL STATEMENT

folder_i= "particle_plots_worst"
folder_f="particle_plots_best"
folder_p="particle_plots_present"
os.makedirs(folder_p, exist_ok=True)
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

present_best=1000000
present_worst=0
time=10 #INFO TAKEN IN
iteration=1
maxiter = 20

if iteration==1:
    plt.contour(X, Y, Z, levels=20)
    
    # Plot particle points
    plt.scatter(points[:,0], points[:,1], color="black")
    
    filename = os.path.join(folder_p, f"present_iter={iteration}.png") # instead ofiteration we can add the run number
    
    plt.savefig(filename, dpi=300) # saving to current dir
    
    plt.show()

else if iteration==maxiter/2:

    plt.contour(X, Y, Z, levels=20)
    
    # Plot particle points
    plt.scatter(points[:,0], points[:,1], color="black")
    
    filename = os.path.join(folder_p, f"present_iter={iteration}.png") # instead ofiteration we can add the run number
    
    plt.savefig(filename, dpi=300) # saving to current dir
    
    plt.show()

else if iteration==maxiter:

    plt.contour(X, Y, Z, levels=20)
        
    # Plot particle points
    plt.scatter(points[:,0], points[:,1], color="black")
    
    filename = os.path.join(folder_p, f"present_iter={iteration}.png") # instead ofiteration we can add the run number
    
    plt.savefig(filename, dpi=300) # saving to current dir
    
    plt.show()



    if present_best>time:
        
        for filename in os.listdir(source_folder):
        # Path to the source image
            source_path = "particle_plots_present/filename"
            
            # Path to the destination folder
            destination_folder = f"particle_plots_best/filename"
            
            # Copy the image
            shutil.copy(source_path, destination_folder)
                
        if os.path.exists(image_path):
            for filename in os.listdir(source_folder):
    
                image_path="particle_plots_present/present.png"
                os.remove(image_path)
        present_best= time
    
    if present_worst<time:
        
        for filename in os.listdir(source_folder):
        # Path to the source image
            source_path = "particle_plots_present/filename"
            
            # Path to the destination folder
            destination_folder = f"particle_plots_best/filename"
            
            # Copy the image
            shutil.copy(source_path, destination_folder)
                
        if os.path.exists(image_path):
            for filename in os.listdir(source_folder):
    
                image_path="particle_plots_present/present.png"
                os.remove(image_path)
        present_worst=time

    else:
                    
        if os.path.exists(image_path):
            for filename in os.listdir(source_folder):
    
                image_path="particle_plots_present/present.png"
                os.remove(image_path)

    
         

 

