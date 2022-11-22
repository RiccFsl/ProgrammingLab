class CSVFile():
  
  def __init__(self, name):
    self.name = name
    
  def get_data(nome_file):
    
    values = []
    my_file = open(nome_file, 'r')
    for line in my_file:
      element = line.split(',')
      if element[0] != 'Date':
        value = element[1]
    my_file.close()
    return values

my_file = CSVFile('shampoo_sales.txt')