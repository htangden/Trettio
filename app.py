from functions import *
import numpy as np

hypercubes = []

for i in range(6):
    hypercubes.append(create_hypercube(6, (i+1)))
xi = backprop(hypercubes, 6)
delta_xi = []
for i in range(6):
    delta_xi.append(xi[i+1]-xi[i])
print(f"xi: {xi} \ndelta_xi: {delta_xi}")

