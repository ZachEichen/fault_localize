# Authors Zachary Eichenberger, Ananya Sharma
from typing import Tuple, List
from subprocess import run
import sys

total_calls = 0 


def gen_arg_str(in_set:set) -> List[str]: 
	# assumes that whatever type in in_set has built in to_str method
	return  [str(val) for val in in_set]

def is_interesting(desired_set:set,command:str)->bool :
	call = command.split(' ') + gen_arg_str(desired_set)
	result = run(call).returncode
	globals()['total_calls']= globals()['total_calls'] +1  
	return int(result) ==1 

def partition(in_set:set)-> Tuple[set,set]:
	half_len = len(in_set)//2
	set_list = list(in_set)
	return set(set_list[:half_len]), set(set_list[half_len:])


def delta(target:set, extras:set,command:str):
	# assumptions: the target + extras subset is interesting 
	# 			    target is non-empty 
	# base case, target is len 1 
	if len(target) <= 1: 
		return target 

	# otherwise, partition to recurse
	p1,p2 = partition(target)

	# check t1 subest
	if is_interesting(p1 | extras, command): 
		return delta(p1,extras,command)

	# check t2 subset 
	elif is_interesting(p2 | extras,command):
		return delta(p2,extras,command)

	# if  neither is interesting alone, we have interference 
	else: 
		d1 = delta(p1,p2,command)
		d2 = delta(p2,p1,command)
		return d1 | d2


def handle_io():
	n = int(sys.argv[1])
	use_set = set(range(n))
	command = sys.argv[2]
	return use_set,command

def main(): 
	base_set,command = handle_io()
	out_set = delta(base_set,set(),command)
	out_list = list(out_set)
	print("total calls is {}".format(globals()['total_calls']))
	print("total_corrs is {}".format(globals()['total_corrs']))

	print(out_list)


if __name__ == "__main__": 
	globals()['total_calls'] = 0 
	globals()['total_corrs'] = 0

	main()