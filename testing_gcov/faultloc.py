import sys
import re
import math

failed = []
passed = []
passed_dict = {}
failed_dict = {}

def handle_io():
    n = int(len(sys.argv))
    for i in range(n):
        if(sys.argv[i] == f"passed{i}.gcov"):
            passed.append(sys.argv[i])
        
    for i in range(n):
        print(sys.argv[i])
        #for some reason this doesnt work as an f string
        if(sys.argv[i] == "failed1.gcov"):
            failed.append(sys.argv[i])


def process_files():
    for item in passed:
        file = open(item,'r')
        Lines = file.readlines()
        for line in Lines:
            line = line.lstrip()
            if(line.startswith('#####') or line.startswith('=====') or line.startswith('-')):
                continue
            else: 
                line = line.split(":",1)[1]
                number = re.search(r'[0-9]+', line).group()
                if number in passed_dict.keys():
                    passed_dict[number] += 1
                else:
                    passed_dict[number] = [1]
        
    for item in failed:
        file = open(item,'r')
        Lines = file.readlines()
        for line in Lines:
            line = line.lstrip()
            if(line.startswith('#####') or line.startswith('=====') or line.startswith('-')):
                continue
            else: 
                line = line.split(":",1)[1]
                number = re.search(r'[0-9]+', line).group()
                if number in failed_dict.keys():
                    failed_dict[number] += 1
                else:
                    failed_dict[number] = [1]

def sort_tuple(tup_list):
    tup_list.sort(key = lambda x: x[1], reverse=True)
    return tup_list

def calculate_suspicious():
    suspicious = []
    total_failed = len(failed)
    #check case where a line number is both in passed and failed, only in passed, or only in failed
    for itr in passed_dict.keys():
        #in both passed and failed
        if itr in failed_dict.keys():
            suspicious_val = (failed_dict[itr][0] / math.sqrt(total_failed * (failed_dict[itr][0] + passed_dict[itr][0])))
            suspicious.append((itr, suspicious_val))
        #only in passed
        else:
            suspicious.append((itr,0.0))

    #only in failed
    for itr in failed_dict.keys():
        if itr not in passed_dict.keys():
            suspicious_val = (failed_dict[itr][0] / math.sqrt(total_failed * (failed_dict[itr][0])))
            suspicious.append((itr, suspicious_val))

    suspicious = sort_tuple(suspicious)
    if(len(suspicious) >= 100):
        return suspicious[0:100]
    else:
        return suspicious


def main(): 
    handle_io()
    process_files()
    relevant_lines = calculate_suspicious()
    print(relevant_lines)


if __name__ == "__main__": 
	main()
