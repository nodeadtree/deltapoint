#!/bin/python
# Copyright (c) 2018 Juniper Overbeck
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import itertools as it
import numpy as np
import argparse as ap

#Argument parsing
b = ap.ArgumentParser()
b.add_argument("-N", type=int, help="This is the large N parameter")
b.add_argument("-n",type=int,help="This is the small n parameter")
b.add_argument("-f",type=str,help="This is the small n parameter")
b = b.parse_args()

N = b.N
n = b.n

a = [i+1 for i in range(N)]
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
for i in it.combinations_with_replacement(a,n):
    if check_increasing(i):
        output.append(i)
output = [str(k) for k in it.product(output, output)]
print(len(output))

print("Length of output is : " + str(len(output)))
with open(b.f+".txt",'w') as f:
f.write("\n".join([i for i in output]))
