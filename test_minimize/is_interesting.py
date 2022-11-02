import os 
import sys
from typing import List, Union
import subprocess 

TEST_FILE_DIR = "../test_cases"

def test_file_list(filenames:List[str]):
	# takes a list of files, and runs them through gcov 

	# clear gcov files from previous runs
	os.system('rm *.gcda pngout.png') 
	# run the instrumented program on each test file 
	for file in filenames: 
		os.system('./pngtest {}  > /dev/null 2> /dev/null'.format(file))
	# then run gcov, and print results to temp.txt
	os.system('gcov *.c > ../temp.txt 2> /dev/null')

	# finally, read in the report from temp.txt, 
	with open('../temp.txt', 'r') as file: 
		for temp in file.readlines(): 
			text = temp
	
	# convert output and return 
	perc = float(text.split('%')[0].split(':')[1])
	return perc

def get_file_name(file_num:Union[str,int])->str: 
	# converts file number to name according to format string 
	filename = "{}.png".format(file_num)
	return os.path.join(TEST_FILE_DIR,filename)

def test_list(testlist,targ=37.97) -> bool:
	# tests a specific list of file numbers, 
	# and returns wheter they achieve the target coverage

	# convert from file number to file name
	test_filenames  = [get_file_name(val) for val in testlist]
	# call handy dandy subset coverage tester on file names
	perc = test_file_list(test_filenames)
	print("suite with {} files had coverage: {}%".format(len(testlist),perc))
	# return whether coverage is within an epsilon of target 
	return abs(perc - targ) <= 0.001

def main(): 
	# ingest inputs fromo sys.argv
	targ_list = [val for val in sys.argv[1:]]
	if len(targ_list) == 0: 
		targ_list = list(range(1639))
	# move into libpng directory (important for subsequent operations)
	os.chdir('libpng')
	# test and exit 1 or 0 according to result 
	if test_list(targ_list):
		print("interesting!!")
		exit(1) 
	else:
		exit(0)

if __name__ == '__main__': 
	main()
