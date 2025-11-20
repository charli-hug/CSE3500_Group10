"""psoo.py

Small driver to search for good c1/c2 values by running `pso.run` many times
and nudging weights for sampled c1/c2 candidates.

This file focuses on consistent spacing/indentation and a minimal, readable
control loop. It expects `pso.run(num_particles, c1, c2)` to return a tuple
containing (c1, c2, iterations) or similar; we reorder that to make the
finish time the first element internally so sorting is straightforward.
"""
<<<<<<< HEAD

import random
import pso
from typing import List, Tuple


def main() -> None:
    # configuration
    num_particles = 20
    samples_per_generation = 100
    max_time_difference = 0  # stop when best/worst are this close

    # prepare search space and weights (0.00 .. 1.00 by 0.01)
    c1_values: List[float] = [i / 100 for i in range(101)]
    c2_values: List[float] = [i / 100 for i in range(101)]
    c1_weights: List[int] = [5 for _ in c1_values]
    c2_weights: List[int] = [5 for _ in c2_values]

    best_finish_time = float("inf")
    worst_finish_time = float("-inf")
    best_c1 = None
    best_c2 = None

    # main optimization loop
    while True:
        data_pool: List[Tuple[int, float, float]] = []

        for _ in range(samples_per_generation):
            pso_c1 = random.choices(c1_values, weights=c1_weights, k=1)[0]
            pso_c2 = random.choices(c2_values, weights=c2_weights, k=1)[0]

            # pso.run is expected to return (c1, c2, iterations) in this repo
            res = pso.run(num_particles, pso_c1, pso_c2)

            # normalize result so we have (iterations, c1, c2)
            try:
                iterations = int(res[2])
                returned_c1 = float(res[0])
                returned_c2 = float(res[1])
            except Exception:
                # fallback: if function returned (iterations, c1, c2)
                iterations = int(res[0])
                returned_c1 = float(res[1])
                returned_c2 = float(res[2])

            data_pool.append((iterations, returned_c1, returned_c2))

        # sort by the finish time (iterations) ascending
        sorted_data_pool = sorted(data_pool, key=lambda item: item[0])

        # update best/worst from this generation
        gen_best = sorted_data_pool[0]
        gen_worst = sorted_data_pool[-1]
        if gen_best[0] < best_finish_time:
            best_finish_time = gen_best[0]
            best_c1 = gen_best[1]
            best_c2 = gen_best[2]
        if gen_worst[0] > worst_finish_time:
            worst_finish_time = gen_worst[0]

        # nudge weights: boost top 10 candidates, reduce bottom 10
        for idx, tup in enumerate(sorted_data_pool):
            iterations, c1_val, c2_val = tup
            if idx < 10:
                # increase weight but cap to avoid runaway
                i1 = c1_values.index(c1_val)
                i2 = c2_values.index(c2_val)
                c1_weights[i1] = min(c1_weights[i1] + 1, 100)
                c2_weights[i2] = min(c2_weights[i2] + 1, 100)
            elif idx >= len(sorted_data_pool) - 10:
                # decrease weight but don't go negative
                i1 = c1_values.index(c1_val)
                i2 = c2_values.index(c2_val)
                c1_weights[i1] = max(c1_weights[i1] - 1, 0)
                c2_weights[i2] = max(c2_weights[i2] - 1, 0)

        # report progress
        print(
            f"Generation best: iterations={gen_best[0]}, c1={gen_best[1]:.2f}, c2={gen_best[2]:.2f} | "
            f"Global best: iterations={best_finish_time}, c1={best_c1}, c2={best_c2}"
        )

        # stopping criterion
        if (worst_finish_time - best_finish_time) <= max_time_difference:
            print(f"Final best c1: {best_c1}, c2: {best_c2} (iterations={best_finish_time})")
            break

        # small safety: if too many weights reached zero, reinitialize
        if sum(1 for w in c1_weights if w == 0) > len(c1_weights) * 0.9:
            print("Weights collapsed; reinitializing weights.")
            c1_weights = [5 for _ in c1_values]
            c2_weights = [5 for _ in c2_values]
=======
import pso, random
print("Version 2.4.3")
x0 = [5, 5]
bounds = [(-10,10), (-10,10)]
>>>>>>> 60c5b615fd800a8cb0b101e51c2393e11e7b3ea5


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
	initialize()
	while True:
	    for i in range(100):
	        #Run PSO file and store the c1, c2, and finish time in data pool
	        #This gives random values for c1 and c2 that are based on the weights
			#This assumes that the function in pso.py is called run, but can be changed later
			pso_c1 = random.choices(c1_values, weights = c1_weights, k = 1)[0]
			pso_c2 = random.choices(c2_values, weights = c2_weights, k = 1)[0]
	        data_pool.append(pso.run(num_particles, pso_c1, pso_c2, best_finish_time, worst_finish_time, x0, bounds))
	
	    #This assumes the time will be the first item in the tuple, but can be changed from 0-2
	    sorted_data_pool = sorted(data_pool, key = lambda item: item[0])
	
	    for tuple, index in enumerate(sorted_data_pool):
	        #The first and best item has the finish time, c1, and c2 labeled as the best, with the worst finish time grabbed for later comparison
	        if index == 0:
	            if tuple[0] < best_finish_time:
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
				#This gets rid of any elements if they no longer have any associated weights (hopefully)
				if c1_weights[c1_values.index(tuple[1])] == 0:
					c1_weights.pop(c1_values.index(tuple[1]))
					c1_values.pop(c1_values.index(tuple[1]))
	            c2_weights[c2_values.index(tuple[2])] -= 1
				if c2_weights[c2_values.index(tuple[2])] == 0:
					c2_weights.pop(c2_values.index(tuple[2]))
					c2_values.pop(c2_values.index(tuple[2]))
	
	    #If the finish times are similar enough then the program is over
	    if ((worst_finish_time - best_finish_time) <= max_time_difference):
	        print("Best c1: " + best_c1 + "\nBest c2:" + best_c2)
			repeat = 1
		#This following is for the circumstance where we don't have a good c1 and c2 pair after running enough times that the weights have mostly 0's
		elif (len(c1_values) < 10) and (len(c2_values) < 10):
			r_or_q = input("A best c1 and c2 value could not be found. Press 'R' to repeat. Press 'Q' to stop.")
			while True:
				if (r_or_q == "R") or (r_or_q == "r"):
					repeat = 2
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
		elif repeat == 2:
			initialize()
>>>>>>> 60c5b615fd800a8cb0b101e51c2393e11e7b3ea5
