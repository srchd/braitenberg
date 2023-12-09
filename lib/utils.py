import numpy as np

def create_multi_dimensional_fading_array(size, center_value, min_value):
    # Create a 3x3 array with zeros
    array = np.zeros((size, size), dtype=int)

    # Calculate the center position
    center_position = size // 2

    # Set the center value
    array[center_position, center_position] = center_value

    # Calculate the step size for evenly spaced values
    step_size = (center_value - min_value) / center_position

    # Populate the array with evenly spaced values from the center
    # for i in range(center_position + 1):
    #     value = int(center_value - i * step_size)

    #     # Update the values in the four quadrants
    #     array[center_position - i: center_position + i + 1, :] = value
    #     array[:, center_position - i: center_position + i + 1] = value


    # for i in range(center_position + 1):
    #     value = int(center_value - i * step_size)

    #     # Update the values in the four quadrants
    #     array[center_position - i: center_position + i + 1, center_position - i: center_position + i + 1] = value
    #     array[center_position - i: center_position + i + 1, center_position - i: center_position + i + 1] = value

    # for i in range(center_position + 1):
    #     value = int(center_value - i * step_size)
    #     array[center_position - i: center_position + i + 1, center_position - i: center_position + i + 1] = value

    # for i in range(center_position):
    #     array[center_position - i - 1, center_position] = int(center_value - (i + 1) * step_size)  # left
    #     array[center_position + i + 1, center_position] = int(center_value - (i + 1) * step_size)  # right
    #     array[center_position, center_position - i - 1] = int(center_value - (i + 1) * step_size)  # up
    #     array[center_position, center_position + i + 1] = int(center_value - (i + 1) * step_size)  # down
    #     array[center_position - i - 1, center_position - i - 1] = int(center_value - (i + 1) * step_size)
    #     array[center_position - i - 1, center_position + i + 1] = int(center_value - (i + 1) * step_size)
    #     array[center_position + i + 1, center_position - i - 1] = int(center_value - (i + 1) * step_size)
    #     array[center_position + i + 1, center_position + i + 1] = int(center_value - (i + 1) * step_size)

    for x in range(center_position):
        for y in range(center_position):
            array[center_position - x - 1, center_position] = int(center_value - (x + 1) * step_size)  # left
            array[center_position + x + 1, center_position] = int(center_value - (x + 1) * step_size)  # right
            array[center_position, center_position - y - 1] = int(center_value - (y + 1) * step_size)  # up
            array[center_position, center_position + y + 1] = int(center_value - (y + 1) * step_size)  # down
            array[center_position - x - 1, center_position - y - 1] = int(center_value - (x + y + 1) * step_size)
            array[center_position - x - 1, center_position + y + 1] = int(center_value - (x + y + 1) * step_size)
            array[center_position + x + 1, center_position - y - 1] = int(center_value - (x + y + 1) * step_size)
            array[center_position + x + 1, center_position + y + 1] = int(center_value - (x + y + 1) * step_size)

    return array