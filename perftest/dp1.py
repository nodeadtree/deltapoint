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

N = [i+1 for i in range(b.N)]
def sequencerb(seq, b, n,front=list(), ):
    if n < 1:
        return
    combos = []
    for j,i in enumerate(seq[b:]):
        f = front + [i]
        s1 = sequencerb(seq,j+b,n-1,f)
        if s1 is not None:
            combos = combos + s1
        if s1 is None:# and s1 is None:
           combos = combos+[f]
    return combos



def sequencermp(seq, n,front=list(),poolsize=4):
    if n < 1:
        return front
    combos = []
    with Pool(poolsize) as p:
        c = [(seq,j,n-1,front+[i]) for j,i in enumerate(seq)]
        out = list()
        for i in range(0,len(c),poolsize):
            b = p.starmap(sequencerb, c[i:i+poolsize])
            out = out + b
        #fin = len(seq)%poolsize
        #print(p.starmap(sequencer, c[-fin:]))
        #out = out + p.starmap(sequencer, c[-fin:])
        return [i for i in it.chain.from_iterable(out)]
delta_2 = t.time()
a = sequencermp(N,n)
delta_2 = t.time()-delta_2



print("Multiprocessing time : " + str(delta_2))
print("Multiprocessing results : " + str(len(a)))

output = [str(k) for k in it.product(a, a)]
print(len(output))

print("Length of output is : " + str(len(output)))
with open(b.f+".txt",'w') as f:
    f.write("\n".join([i for i in output]))
