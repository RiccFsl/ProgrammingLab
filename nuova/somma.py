def sum_csv(file_name):
    list = []
    for line in my_file:
        my_file = line.split(',')
        if (element[0] != 'Date'):
            value = float(element[1])
            list.append(value)
    return sum(list)