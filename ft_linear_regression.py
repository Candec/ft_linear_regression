import sys
from libft import csv_list
from ft_calculate_weights import *

class weights:
	def __init__(self) -> None:
		tetha0 :float = 0.0
		tetha1 :float = 0.0
	
	@classmethod
	def ft_update_weights():
		weights.tetha0, weights.tetha1 = ft_calculate_weights()


if __name__ == '__main__':
	def ft_linear_regression():
		weights = weights()

		if (sys.argc != 2):
			print ("Wrong number of arguments\n")
			exit(1)

		weights.ft_update_weights("data.csv")

		lr = ft_linear_regression(weights.tetha0, weights.tetha1, sys.argv[1])
		print (lr)
		return (lr)
	
	ft_linear_regression()