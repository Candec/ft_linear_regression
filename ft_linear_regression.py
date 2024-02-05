import sys
import csv

class weights:
	def __init__(self) -> None:
		tetha0 :float = 0.0
		tetha1 :float = 0.0
	
	@classmethod
	def ft_update_weights(data :list):
		weights.tetha0
		weights.tetha1


def csv_list():
	with(open("data.csv", newline='')) as line:
		read = csv.reader(line)
		data = list(read)
	
	return (data)

def ft_update_weights(weights :weights, data :list):
	pass

def ft_linear_regression(tetha0 :float, tetha1 :float):
	tetha2 = tetha0 + tetha1


if __name__ == '__main__':

	weights = weights()
	data = []

	if (sys.argc == 1):
		# linear_regression(weight.tetha0, weights.tetha1)
		# exit(0)
		pass

	if (sys.argc == 2):
		data = csv_list()
	else:
		print ("Wrong number of arguments\n")
		exit(1)

	weights.ft_update_weights(data)

	# linear_regression(weight.tetha0, weights.tetha1)