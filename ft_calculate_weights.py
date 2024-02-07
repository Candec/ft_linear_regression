import sys
import string
from libft import csv_list


def w0(data :list):
	total :float

	for i in data:
		E_price = float(i[0]) - float(i[1])
		total = 0
		total = total + E_price
	return (total)

def w1(data :list):
	total :float

	for i in data:
		E_price = (float(i[0]) - float(i[1])) * float(i[0])
		total = 0
		total = total + E_price
	return (total)


def ft_calculate_weights(path :string):
	if (len(sys.argv) != 2):
		print("Error: Wrong number of arguments")
		exit(1)

	data = csv_list(path)

	if len(data) == 0:
		print ("Error: Importing data")
		return ([0, 0])
	
	if (data[0][0] != "km" and data[0][1] != "price"):
		print ("Error: Invalid format")
		return ([0, 0])
	
	del data[0]
	
	alpha = 3				# Learning rate
	m = len(data) - 1		# Sample size
	intersective :float		# Starting point of f(x)
	step :float				# Stepeness of f(x)

	tetha0 = 0
	tetha1 = 0
	tetha0 = alpha * (1 / m) * w0(data)
	tetha1 = alpha * (1 / m) * w1(data)

	return ([tetha0, tetha1])
	