def sum_csv(file_name):
    list = []
    my_file = open(file_name , 'r')
    for line in my_file:
        element = line.split(',')
        if (element[0] != 'Date'):
            value = (element[1])
            list.append(float(value))
    return sum(list)