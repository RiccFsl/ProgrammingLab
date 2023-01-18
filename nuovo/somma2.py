def sum_csv(file_name):
    list = []
    my_file = open('file_name', 'r')
    for line in my_file:
        my_file = line.split(',')
        if (element[0] != 'Date'):
            value = float(element[1])
            list.append(value)
    my_file.close()