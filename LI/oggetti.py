class CSVFile():
  
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return(f'CsvFile: {self.name}')
    
  def get_data(self):
    list = []
    my_file = open(self.name, 'r')
    for line in my_file:
      element = line.split(',')
      if element[0] != 'Data':
        date = element[0]
        value = element[1]
        list.append([date, value])
    my_file.close()
    return list

shampoo = CSVFile ('shampoo_sales.txt')
print(shampoo)
data = shampoo.get_data()
print (data)