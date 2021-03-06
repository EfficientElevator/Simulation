import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import math
from src.Person import Person
from src.Visualization.visualization import Visualization
from src.simulator import *
from src.building import *
from src.elevator import *
from src.PersonScheduler import *

"""
# Simulation window parameters
xMin = 0
xMax = 100
yMin = 0
yMax = 11  # num_floors + 1
xDelta = xMax - xMin
yDelta = yMax - yMin  # rectangle dimensions
areaTotal = xDelta * yDelta

# Point process parameters
lambda0 = 1  # intensity (ie mean density) of the Poisson process; lambda=1 is mean 1 per second

# Simulate Poisson point process
np.random.seed(seed=1)
numbPoints = scipy.stats.poisson(lambda0 * xDelta).rvs()  # Poisson number of points; areaTotal replaced by xDelta
xx = xDelta * scipy.stats.uniform.rvs(0, 1, (numbPoints, 1)) + xMin  # x-coors of Poisson points
yy = yDelta * scipy.stats.uniform.rvs(0, 1, (numbPoints, 1)) + yMin  # y-coor: starting floor
zz = yDelta * scipy.stats.uniform.rvs(0, 1, (numbPoints, 1)) + yMin  # z-coor: destination floor

for val_arr in yy:
    val_arr[0] = int(math.floor(val_arr[0]))
for val_arr in zz:
    val_arr[0] = int(math.floor(val_arr[0]))

print(yy)
# Plotting
plt.scatter(xx, yy, edgecolor='b', facecolor='none', alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.scatter(xx, zz, edgecolor='b', facecolor='none', alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
"""
sim = Simulator('test', step_func=realistic_physics_step_func)
elevators = [Elevator(1)]
building = Building(name=1, elevators=elevators, n_floors=10)
sim.init_building(building)

ps = PersonScheduler(building)  # , seconds_to_schedule=50)
print(ps.people_spawning[:20])
print(ps.get_time_and_people_of_next_addition(20))

