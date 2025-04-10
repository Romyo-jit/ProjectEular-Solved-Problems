'''
* Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

                    !!!LOOK AT THE Lattice.png!!!

* How many such routes are there through a 20x20 grid?
'''
from functools import lru_cache

@lru_cache
def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)

path = ['right' for _ in range(20)]
for _ in range(20):
    path.append('down')

num_of_routes = fact(40)/(fact(20)*fact(20))
print("Total routes: ", int(num_of_routes))
