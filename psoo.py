"""This file is called psoo, for particle swarm optimization optimization, as it optimizes the c1 and c2 values (dumb placeholder but psoo is whimsical idc)"""

import pso, random
print("Version 2")

#This will hold all of our data in tuples that stores the c1, c2, and finish time values
#Finish time will be the amount of iterations our program takes in a specific runthrough to get x% of y particles in the global best (say 95% of 50 particles, or 48)
data_pool = []

#This is for the sorted version of our data, where we can use this to compare for bugs against the unsorted
sorted_data_pool = []

#Gives a range of values from 0.00 to 1.00, and gives associated weights
c1_values = []
c1_weights = []
c2_values = []
c2_weights = []
for i in range(100):
    c1_values.append(i / 100)
	c1_weights.append(5)
    c2_values.append(i / 100)
    c2_weights.append(5)

#These values gather the best c1 and c2 to be used as the final values, as well as the best and worst finish times to compare
best_c1 = 0
best_c2 = 0
best_finish_time = 0
worst_finish_time = 0

#0 is a placeholder, this will be whatever number we want that determines how different the best and worst is
max_time_difference = 0

while True:
    for i in range(100):
        #Run PSO file and store the c1, c2, and finish time in data pool
        #This gives random values for c1 and c2 that are based on the weights
				#This assumes that the function in pso.py is called run, but can be changed later
        data_pool.append(pso.run((random.choices(c1_values, weights = c1_weights, k = 1)[0]), (random.choices(c1_values, weights = c1_weights, k = 1)[0])))

    #This assumes the time will be the first item in the tuple, but can be changed from 0-2
    sorted_data_pool = sorted(data_pool, key = lambda item: item[0])

    for tuple, index in enumerate(sorted_data_pool):
        #The first and best item has the finish time, c1, and c2 labeled as the best, with the worst finish time grabbed for later comparison
        if index == 0:
            best_finish_time = tuple[0]
            best_c1 = tuple[1]
            best_c2 = tuple[2]
        elif index == 99:
            worst_finish_time = tuple[0]

        #This makes the best 10 c1 and c2 have a slightly higher chance of being picked, with a slightly lower pick for the worst 10 c1 and c2
        if index < 10:
            c1_weights[c1_values.index(tuple[1])] += 1
            c2_weights[c2_values.index(tuple[2])] += 1
        elif index > 88:
            c1_weights[c1_values.index(tuple[1])] -= 1
            c2_weights[c2_values.index(tuple[2])] -= 1

    #If the finish times are similar enough then the program is over
    if ((worst_finish_time - best_finish_time) <= max_time_difference):
        break
	else:
		data_pool.clear()
		sorted_data_pool.clear()

print("Best c1: " + best_c1 + "\nBest c2:" + best_c2)
