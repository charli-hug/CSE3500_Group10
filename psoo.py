"""This file is called psoo, for particle swarm optimization optimization, as it optimizes
the c1 and c2 values. This file fixes indentation issues and keeps the original logic.
"""

import pso
import random


# unsure where this is coming in in the actual pso.py file

# need x0 and bounds as inputs for pso.py functions
x0 = [5, 5]   # initial starting location [x1,x2]
bounds = [(-10,10), (-10,10)]  # input bounds [(x1_min,x1_max), (x2_min,x2_max)]
print("Version 2.3")

# This will hold all of our data in tuples that stores the c1, c2, and finish time values
# Finish time will be the amount of iterations our program takes in a specific runthrough
data_pool = []

# This is for the sorted version of our data
sorted_data_pool = []

# Gives a range of values from 0.00 to 1.00, and gives associated weights
c1_values = []
c1_weights = []
c2_values = []
c2_weights = []
for i in range(101):
	c1_values.append(i / 100)
	c1_weights.append(5)
	c2_values.append(i / 100)
	c2_weights.append(5)

# These values gather the best c1 and c2 to be used as the final values,
# as well as the best and worst finish times to compare
best_c1 = 0
best_c2 = 0
# initialize best/worst so comparisons work on first run
best_finish_time = float('inf')
worst_finish_time = float('-inf')

# 0 is a placeholder for how similar best and worst may be
max_time_difference = 0

# If repeat is 0, then the code will run again. If repeat is 1, the code will end
repeat = 0

while True:
	for i in range(100):
		# Run PSO file and store the c1, c2, and finish time in data pool
		# This gives random values for c1 and c2 that are based on the weights
		# This assumes that the function in pso.py is called `run` (can be changed later)
		num_particles = 20
		pso_c1 = random.choices(c1_values, weights=c1_weights, k=1)[0]
		pso_c2 = random.choices(c2_values, weights=c2_weights, k=1)[0]
		data_pool.append(pso.run(num_particles, pso_c1, pso_c2))

	# This assumes the time will be the first item in the tuple
	sorted_data_pool = sorted(data_pool, key=lambda item: item[0])

	# enumerate returns (index, item)
	for index, tup in enumerate(sorted_data_pool):
		# The first (index 0) is the best (smallest finish time) after sorting
		if index == 0:
			best_finish_time = tup[0]
			best_c1 = tup[1]
			best_c2 = tup[2]
		elif index == 99:
			worst_finish_time = tup[0]

		# Increase weight slightly for top 10, decrease for bottom ~11
		if index < 10:
			c1_weights[c1_values.index(tup[1])] += 1
			c2_weights[c2_values.index(tup[2])] += 1
		elif index > 88:
			c1_weights[c1_values.index(tup[1])] -= 1
			c2_weights[c2_values.index(tup[2])] -= 1

	# If the finish times are similar enough then the program is over
	if ((worst_finish_time - best_finish_time) <= max_time_difference):
		print(f"Best c1: {best_c1}\nBest c2: {best_c2}")
		repeat = 1
	# If too many weights dropped, ask the user whether to repeat or quit
	elif (len(c1_values) < 10) and (len(c2_values) < 10):
		r_or_q = input("A best c1 and c2 value could not be found. Press 'R' to repeat. Press 'Q' to stop.")
		while True:
			if (r_or_q == "R") or (r_or_q == "r"):
				break
			elif (r_or_q == "Q") or (r_or_q == "q"):
				repeat = 1
				break
			else:
				r_or_q = input("Invalid input. Press 'R' to repeat. Press 'Q' to stop.")
	else:
		data_pool.clear()
		sorted_data_pool.clear()

	if repeat == 1:
		break
