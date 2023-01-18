def sum_csv(file_name):
    list = []
    for line in file_name:
        element = line.split(',')
        if (element[0] != 'Date'):
            value = (element[1])
            list.append(float(value))
    return sum(list)