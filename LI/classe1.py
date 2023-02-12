class CSVFile:
	def __init__(self, name):
		self.name = name
		self.my_file = open(self.name, "r")
		
	def get_data (self):
		dati = []
		next(self.my_file)
		for line in self.my_file:
			element = line.split(",")
			Data = element[0]
			Value = element[1]
			dati.append((Data, Value))
		return dati
