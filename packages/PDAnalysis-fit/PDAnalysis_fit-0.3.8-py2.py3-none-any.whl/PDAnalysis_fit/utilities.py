import numpy as np

def get_voltage_index(data, desired_voltage):
    array = np.asarray(data)
    index = (np.abs(array - desired_voltage)).argmin() # find closest index to desired_voltage
    return index

def get_voltage_values(data):
    voltage_array = list(dict.fromkeys(data)) # save only one of each voltage value
    index_array = [list(data).index(x) for x in voltage_array] # find the first index for each voltage value 
    index_array.append(len(data)) # adding the final data point index
    return voltage_array, index_array