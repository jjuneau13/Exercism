"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
preparation_time = 0





def bake_time_remaining(minutes):
    """Bake time remaining
    :param minutes: int - the time that has passed
    This takes the amount of time passed and subtracts it from the expected bake time"""
    return EXPECTED_BAKE_TIME - minutes



def preparation_time_in_minutes(layers):
    """Returns the preparation time in minutes
    Takes the number of layers as an argument and returns prep time."""
    return layers*2


def elapsed_time_in_minutes(num_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.
    Takes number of layers and elapsed bake time."""
    return preparation_time_in_minutes(num_of_layers) + elapsed_bake_time

