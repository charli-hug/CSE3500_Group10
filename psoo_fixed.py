
"""psoo_fixed.py

Clean, consistently-indented version of psoo. I left the original
`psoo.py` untouched; this file demonstrates the corrected indentation and
behavior. If you'd like, I can replace the original file with this version.
"""

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


if __name__ == "__main__":
    main()
