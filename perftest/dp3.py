#!/bin/python
import itertools as it
import argparse as ap
import time as t

#Argument parsing
b = ap.ArgumentParser()
b.add_argument("-N", type=int, help="This is the large N parameter")
b.add_argument("-n",type=int,help="This is the small n parameter")
b.add_argument("-f",type=str,help="This is the small n parameter")
b = b.parse_args()

N = b.N
n = b.n


#Given sequence of numbers
#split sequence into single elements 
#reassemble in pairs x,y such that x<=y ---> x[-1]<=y[0],
#return this list of pairs
N=[i+1 for i in range(N)]


delta_3 = t.time()
def check_increasing(seq, n=1):
    if seq[0] < n:
        return False
    if seq[0] >= n:
        n = seq[0]
        if len(seq[1:]) < 1:
            return True
        else:
            return check_increasing(seq[1:],n)

output = list()
for i in it.combinations_with_replacement(N,n):
    if check_increasing(i):
        output.append(i)

delta_3 = t.time() - delta_3

print("Combinations + filter time : " + str(delta_3))
print("Combinations + filter results : " + str(len(output)))
'''
output = [str(k) for k in it.product(output, output)]
print(len(output))

print("Length of output is : " + str(len(output)))
with open(b.f+".txt",'w') as f:
    f.write("\n".join([i for i in output]))
'''
