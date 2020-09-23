#!/usr/bin/python
# -*- coding: UTF-8 -*-
#whye

import random
from task_2 import crt
#将d的范围限制在pow(key, t)到pow(key, t-1)之间保证满足N>k>M，要求见ppt
def get_range_of_d(key, t):
    min = int(pow(key, 1/t)) + 1
    max = int(pow(key, 1/(t - 1)))
    return [min, max]

def get_d(key, n, t):
    range_of_d = get_range_of_d(key, t)
    while(1):
        d_array = []
        for _i in range(n):
            d_array.append(random.randint(range_of_d[0], range_of_d[1]))
        if each_prime(d_array):
            return d_array

def each_prime(array):
    for i in range(len(array)):
       for j in range(i):
            if not gcd(array[i], array[j]) == 1:
                return False
    return True

def gcd(a, m):
    while(1):
        if m%a == 0:
            return a
        t = a
        a = m%a
        m = t

def get_k(key, d_array):
    k_array = []
    for d in d_array:
        k_array.append(key%d)
    return k_array

def encode(key, n, t):
    d_array = get_d(key, n, t)
    return zip(range(n), d_array, get_k(key, d_array))

def decode(a, m):
    return crt(a, m)

if __name__ == '__main__':
    key = 230489560234897560232346345645374568567852345692345867029589013485701394587
    n = 5
    t = 3
#encode
    enc = list(encode(key, n, t))
    for i,d,k in enc:
        print(str(i+1) + ' d: ' + str(d), end = '')
        print(' k: ' + str(k))
    
#decode
    a = []
    m = []
    for i,d,k in enc:
        if i == t:
            break
        a.append(k)
        m.append(d)
    print(crt(a, m))