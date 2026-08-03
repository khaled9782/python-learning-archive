import numpy as np

array = np.array([[0, 1, -1, -1], [0, 0, 1, -1]])
bool_array = np.array(array, dtype=bool)
print(array)
np_to_list = array.tolist()
print()
print(np_to_list)
