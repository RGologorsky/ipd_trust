def print_matrix(title, matrix):
	print(title)
	print('\n'.join(['\t'.join(["{:.3f}".format(cell) for cell in row]) for row in matrix]))


def print_list(title, lst):
	print(title)
	print('\t'.join(["{:.3f}".format(num) for num in lst]))


def is_close(a, b, precision=10**-8):
	return abs(a-b) < precision