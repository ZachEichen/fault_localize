import os 
import sys
from typing import List, Union
import subprocess 

TEST_FILE_DIR = "../test_cases"

def test_file_list(filenames:List[str]):
	os.system('rm *.gcda pngout.png') 
	for file in filenames: 
		os.system('./pngtest {}  > /dev/null 2> /dev/null'.format(file))
	os.system('gcov *.c > ../temp.txt 2> /dev/null')

	with open('../temp.txt', 'r') as file: 
		for temp in file.readlines(): 
			text = temp
	# print(text)

	perc = float(text.split('%')[0].split(':')[1])
	return perc

def get_file_name(file_num:Union[str,int])->str: 
	filename = "{}.png".format(file_num)
	return os.path.join(TEST_FILE_DIR,filename)

def test_list(testlist,targ=37.97):
	test_filenames  = [get_file_name(val) for val in testlist]
	perc = test_file_list(test_filenames)
	print("suite with {} files had coverage: {}%".format(len(testlist),perc))
	return abs(perc - targ) <= 0.001

def main(): 
	targ_list = [val for val in sys.argv[1:]]
	if len(targ_list) == 0: 
		targ_list = list(range(1639))
	os.chdir('libpng')
	# print('Running with targets: ')
	# print(targ_list)
	if test_list(targ_list):
		print("interesting!!")
		exit(1) 
	else:
		exit(0)


if __name__ == '__main__': 
	main()
