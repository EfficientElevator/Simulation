"""
Author: Austin Day
PersonScheduler.py
"""
import numpy as np


class PersonScheduler:
    """
    PersonScheduler class
    Defines the scheduling for arrival and destinations of elevator passengers
    """

    def __init__(self, building, step_time_scale, expected_destinations=None):
        """
        Creates a PersonScheduler object.

        Arguments:
        building -- The building object for the simulation
        step_time_scale -- The amount of time elapsed between each simulation step (in ms)
        expected_destinations --    A dictionary keyed on ints representing days of the week (-1 = default, 0-6 = monday-sunday) 
                                    each key storing a dict keyed on timestamps representing the time of day this 'schedule' starts (military time)
                                    each timestamp key holding a list representing hourly rates of button presses on each floor. It's complicated.
        """

        self.building = building
        self.step_time_scale = step_time_scale
        self.expected_destinations = expected_destinations  # Expect 1 button press per floor every hour
        if expected_destinations is None:
            self.expected_destinations = {-1: {"0000": [1 for i in range(building.n_floors)]}}
            # By default, expect 1 button press per floor every hour.
        return

    def set_expected_destinations(self, val=None, weekdays=None, timestamp=None, floors=None):
        """
        Sets the expected values for button presses in the building per hour starting at a specified time

        Arguments:
        val -- The value to insert into the expected_destinations dict at the location specified by the other args. Can be a full dict, a list, or just a value. 
        weekdays -- Optional, list of days of the week this schedule is being applied to. If unspecified, sets the default value (Used for all weekdays that arent already set)
        timestamp -- Optional, the time of day this schedule begins at. If left blank, clears all other times and sets new one to start at "0000" (active all day) 
        floors -- Optional, list of floors to apply the new hourly rate to. If left blank, applies to all floors.
        """
        return

    def get_current_expected_val(self, timestamp):
        """
        Based on the current time, finds the current time block it falls into from the expected_destinations table and returns the expected hourly presses list

        Arguments:
        timestamp -- a time to compare to the timetable stored in expected_destination
        """
        return

    # Returns the absolute time and list of people (or one person) that will need to be spawned next
    # relative to the current_timestamp
    def get_time_and_people_of_next_addition(self, current_timestamp):
        # This is what needs to be accessed by the RL step function to determine when to call the ML/when to add
        # people to the system
        # TODO *******
        return 0.0, []

    # Triggers button presses on floors by spawning people in
    def spawn_people(self, timestamp, people):
        self.building.last_floor_button_pressed = timestamp  # needed for rl step func v1
        for person in people:
            self.building.add_waiting_person(person)

