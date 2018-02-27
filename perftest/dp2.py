#!/bin/python
import itertools as it
import argparse as ap
import time as t
from multiprocessing import Pool

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

def sequencer(seq, n,front=list(), ):
    if n < 1:
        return
    combos = []
    for j,i in enumerate(seq):
        f = front + [i]
        s1 = sequencer(seq[j:],n-1,f)
        if s1 is not None:
            combos = combos + s1
        if s1 is None:# and s1 is None:
           combos = combos+[f]
    return combos

delta_1 = t.time()
a = sequencer(N,n)
delta_1 = t.time()-delta_1
 
print("Recursive algorithm time : " + str(delta_1))
print("Recursive algorithm results : " + str(len(a)))
'''
output = [str(k) for k in it.product(output, output)]
print(len(output))

print("Length of output is : " + str(len(output)))
with open(b.f+".txt",'w') as f:
    f.write("\n".join([i for i in output]))
'''
