"""
Author: Daniel Nichols
"""
from src.ElevatorState import ElevatorState


class Elevator:
    """
    Elevator class.
    """

    def __init__(self, name, max_velocity=2.5, max_acc=1, jerk=0, speed=0, avg_boarding_time=5, max_riders=10,
                 init_position=0):
        """
        inits the elevator.

        Parameters:
        name -- name of this elevator
        speed -- elevator speed in floors/sec
        avg_boarding_time -- average time spent at each floor (factors in door closing/opening)
        max_velocity -- maximum elevator velocity
        max_acc -- max elevator acceleration
        jerk -- elevator jerk (derivative of acceleration)
        max_riders -- maximum personnel allowed on elevator
        position -- distance (in meters) above the base of floor 1; used by simulation for positioning
        """
        self.name = name
        self.speed = speed
        self.avg_boarding_time = avg_boarding_time
        self.max_velocity = max_velocity
        self.max_acc = max_acc
        self.jerk = jerk
        self.max_riders = max_riders
        self.position = init_position
        self.state = ElevatorState.NO_ACTION

        self.riders = []

    def add_rider(self, rider):
        '''
        Adds a rider to the elevator cart.
        Returns -1 and does nothing if rider is None.
        Returns rider index otherwise.
        '''
        if rider is None:
            return -1

        self.riders.append(rider)
        return len(self.riders)-1

    def remove_rider(self, rider):
        '''
        Removes the rider from the rider list.
        Returns the new size of the rider list.
        '''
        if rider is None:
            return -1

        if rider in self.riders:
            self.riders.remove(rider)

    def get_num_riders(self):
        '''
        Get the number of riders.
        '''
        return len(self.riders)
    

