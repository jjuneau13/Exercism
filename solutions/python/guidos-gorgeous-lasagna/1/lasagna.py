"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
preparation_time = 0



#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(minutes):
    """Bake time remaining
    :param minutes: int - the time that has passed
    This takes the amount of time passed and subtracts it from the expected bake time"""
    return EXPECTED_BAKE_TIME - minutes


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(layers):
    """Returns the preparation time in minutes
    Takes the number of layers as an argument and returns prep time."""
    return layers*2
#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(num_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.
    Takes number of layers and elapsed bake time."""
    return preparation_time_in_minutes(num_of_layers) + elapsed_bake_time
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
