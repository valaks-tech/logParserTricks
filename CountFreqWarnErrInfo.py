from collections import Counter

"""
2020-02-03 11:03:23 WARN My warning message repeated 3 times
2020-02-03 11:03:23 ERR oops, error message repeated 8 times
2020-02-03 11:03:26 ERR this is my error message repeated 1 times
2020-02-03 11:03:26 WARN MY warning , so scary, repeated 1 times
2020-02-03 11:03:26 WARN cpu utilization high, repeated 1 times
2020-02-03 11:03:29 INFO this is for test repeated 2 times

# Expected Output (group by level)
===
WARN: 3
ERR: 2
INFO: 1

"""
import sys, collections
from collections import defaultdict
def logreader(logfile):
    freq = collections.defaultdict(int)
    list_of_strs = ['WARN','ERR','INFO']

    with open(logfile) as f:
        for line in f:
            data = line.strip()
            if any((match1 := search_str) in data for search_str in list_of_strs):
                freq[match1] += 1
    
    print(freq)

if __name__== "__main__":
    logfile="C:\\Users\\shail\\mylogfile.txt"
    logreader(logfile)
