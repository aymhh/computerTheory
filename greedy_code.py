import time
import networkx
import numpy as np
import csv
from python_tsp.distances import euclidean_distance_matrix
from networkx.algorithms.approximation import greedy_tsp

with open("greedy_code.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "seconds", "distance"])

    n = 2
    while True:

        rng = np.random.default_rng(2026)                # fixed seed
        cities = rng.uniform(0, 100, size=(n, 2))       # 10 random (x, y) points
        d = euclidean_distance_matrix(cities)            # 10 x 10 distances
        G = networkx.from_numpy_array(d)

        
        startTime = time.time()

        tour = greedy_tsp(G, source=0)


        elapsedTime = time.time() - startTime
        
        distance = sum(d[a][b] for a, b in zip(tour, tour[1:]))
        writer.writerow([n, elapsedTime, distance])    # one row per n
        f.flush()                                      # save it now
        
        print(f"Trip with {n} cities has been completed!")
        print(f">>> Distance: {distance:.2f}")
        print(f">>> Time taken: {elapsedTime:.6f} seconds")
        print("-------------------------")
        
        if elapsedTime > 600:
            print(f"Computation that took longer that 600 seconds (10minutes) has been found. ({n, distance})")
            break
        else:
            n= n*2




