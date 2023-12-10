import numpy as np

def create_multi_dimensional_fading_array(size: int, center_value: int, min_value: int) -> list:
    """
    Creates a 2x2 array, where the center has the max value, and the values are evenly lower 'outwards'.

    Parameters:
        size (int): The size of the array.
        center_value (int): Starting value of the fading.
        min_value (int): Minimum value of the fading.

    Returns:
        array (list): 2D fading-from-center array
    """

    # Create a 3x3 array with zeros
    array = np.zeros((size, size), dtype=int)

    # Calculate the center position
    center_position = size // 2

    # Set the center value
    array[center_position, center_position] = center_value

    # Calculate the step size for evenly spaced values
    step_size = (center_value - min_value) / center_position

    # Populate the array with evenly spaced values from the center
    for x in range(center_position):
        for y in range(center_position):
            array[center_position - x - 1, center_position] = int(center_value - (x + 1) * step_size)  # left
            array[center_position + x + 1, center_position] = int(center_value - (x + 1) * step_size)  # right
            array[center_position, center_position - y - 1] = int(center_value - (y + 1) * step_size)  # up
            array[center_position, center_position + y + 1] = int(center_value - (y + 1) * step_size)  # down
            array[center_position - x - 1, center_position - y - 1] = int(center_value - (x + y + 1) * step_size) # left-up
            array[center_position - x - 1, center_position + y + 1] = int(center_value - (x + y + 1) * step_size) # left-down
            array[center_position + x + 1, center_position - y - 1] = int(center_value - (x + y + 1) * step_size) # right-up
            array[center_position + x + 1, center_position + y + 1] = int(center_value - (x + y + 1) * step_size) # right-down

    return array