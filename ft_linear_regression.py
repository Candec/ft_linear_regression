import sys
from libft import csv_list
from ft_calculate_weights import ft_calculate_weights



class weights:
	tetha0 :float = 0.0
	tetha1 :float = 0.0
	
	@classmethod
	def ft_update_weights(elmo, path):
		elmo.tetha0, elmo.tetha1 = ft_calculate_weights(path)


def ft_linear_regression(tetha0, tetha1, x):
	return (tetha0 + (tetha1 * float(x)))
	
if __name__ == '__main__':

	if (len(sys.argv) != 2):
		print ("Error: Wrong number of arguments")
		exit(1)

	elmo = weights()
	elmo.ft_update_weights("data.csv")

	print (ft_linear_regression(elmo.tetha0, elmo.tetha1, sys.argv[1]))