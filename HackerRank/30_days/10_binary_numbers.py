#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby
import operator


if __name__ == '__main__':
    n = int(input())
    b = "{0:b}".format(n)
    groups = groupby(b)
    val = [(key, sum(1 for _ in group)) for key, group in groups]
    val = [(num, count) for num, count in val if num == "1"]
    val.sort(key = operator.itemgetter(1), reverse = True)
print(val[0][1])



# nBin = bin(n).lstrip('0b')
# splitted = sorted(nBin.split(sep='0'), reverse=True)
# print(len(splitted[0]))
# #print(max(map(len, splitted)))
#
#
# def calc_binary(number):
#     length = bin(number)[2:].split('0')
#     return max(list(map(len, length)))
