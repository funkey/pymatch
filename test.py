import pymatch
import munkres
import numpy as np
from time import time

def match(costs):

    start = time()
    m = munkres.Munkres()
    match = m.compute(costs.copy())
    print("Munkres: %fs"%(time()-start))
    print(match)

    start = time()
    match = pymatch.match(costs.copy())
    print("pymatch: %fs"%(time()-start))
    print(match)

if __name__ == "__main__":

    a = np.random.random((100,200))

    # should be empty
    match(a)

    a = -a

    # should have exactly one match per i
    match(a)
