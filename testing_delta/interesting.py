import sys


def condition(vals:list):
	return 2 in vals and 7 in vals

def main(): 
	vals = [int(val) for val in  sys.argv[1:]]
	if condition(vals): 
		exit(1)
	else:
		exit(0)


if __name__ == "__main__":
	main()