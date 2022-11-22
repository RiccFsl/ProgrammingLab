def sum_csv(nome_file):
  values = []
  my_file = open(nome_file, 'r')
  for line in my_file:
    element = line.split(',')
    if element[0] != 'Date':
      value = element[1]
      values.append(float(value))
  my_file.close()
  if (len(values) == 0):
    return None
  else:
    return sum(values)
