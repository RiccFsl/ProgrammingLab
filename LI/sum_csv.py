def sum_csv(nome_file):
  values = []
  my_file = open(nome_file, 'r')
  for line in my_file:
    element = line.split(',')
    if element[0] != 'Date':
      value = element[1]
      values.append(float(value))
  my_file.close()
  return sum(values)
