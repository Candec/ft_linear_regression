import sys
import string
from libft import csv_list


def tetha0(data :list):
	total :float

	for i in list:
		E_price = i[0] - i[1]
		total = total + E_price
	return (tetha0)

def tetha1(data :list):
	total :float

	for i in list:
		E_price = (i[0] - i[1]) * i[0]
		total = total + E_price
	return (tetha1)

if __name__ == '__main__':
	def ft_calculate_weights(path :string):
		if (sys.argc != 2):
			print("Wrong number of arguments\n")
			exit(1)

		data = csv_list(path)

		if data.empty():
			print ("Error importing data\n")
			return ([0, 0])
			exit(1)
		
		alpha = 3				# Learning rate
		m = data.size() - 1		# Sample size
		intersective :float		# Starting point of f(x)
		step :float				# Stepeness of f(x)

		tetha0 = alpha * (1 / m) * tetha0()
		tetha1 = alpha * (1 / m) * tetha1()

		return ([tetha0, tetha1])
	