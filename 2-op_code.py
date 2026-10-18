import time
import numpy as np
import csv
from python_tsp.heuristics import solve_tsp_local_search
from python_tsp.distances import euclidean_distance_matrix

with open("two_opt_results3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "seconds", "distance"])
    n = 2
    while True:

        rng = np.random.default_rng(2026)                # fixed seed
        cities = rng.uniform(0, 100, size=(n, 2))       # 10 random (x, y) points
        d = euclidean_distance_matrix(cities)            # 10 x 10 distances
        startTime = time.time()

        permutation, distance = solve_tsp_local_search(d)

        elapsedTime = time.time() - startTime

        writer.writerow([n, elapsedTime, distance, permutation])    # one row per n
        f.flush()                                      # save it now
        
        print(f"Trip with {n} cities has been completed!")
        print(f">>> Distance: {distance:.2f}")
        print(f">>> Time taken: {elapsedTime:.6f} seconds")
        print("-------------------------")

        if elapsedTime > 600:
            print(f"Computation that took longer that 600 seconds (10minutes) has been found. ({n, distance})")
            break
        else:
            n= n*n
            




