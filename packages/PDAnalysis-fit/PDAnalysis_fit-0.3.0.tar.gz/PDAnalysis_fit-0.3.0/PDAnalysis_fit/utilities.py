def get_voltage_index(data, desired_voltage):
    temp = 99
    for i in range(len(data)):
        diff =  abs(data[i] - desired_voltage)
        if diff < temp:
            temp = diff
            index = i
    return index

def get_voltage_values(data):
    voltage_array = [0]
    index_array = [0] # adding the starting index as 0
    voltage_array[0] = data[0]
    j = 0
    for i in range(len(data)):
        if data[i] != voltage_array[j]:
            voltage_array.append(data[i])
            index_array.append(i)
            j += 1
    index_array.append(len(data)) # adding the final data point index
    return voltage_array, index_array