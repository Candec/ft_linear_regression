import csv
import string

def csv_list(path :string):
	with(open(path, newline='')) as line:
		read = csv.reader(line)
		data = list(read)
		
	return (data)