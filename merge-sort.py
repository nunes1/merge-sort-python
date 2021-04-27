#!/usr/bin/python3

import sys
import time


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    return alist


def readFile(lines):
    arrayTemp = []
    f = open("numeros.txt").read().splitlines()
    # print(f)
    for x in range(0, lines):
        arrayTemp.append(int(f[x]))
    return arrayTemp


start_time = time.time()
print("Number of lines:", '{0:,}'.format(int(sys.argv[1])).replace(',', '.'))
lines = int(sys.argv[1])
array = []

array = readFile(lines)
print(array)

array = mergeSort(array)
print(array)

print("Runtime: %s seconds" % (time.time() - start_time))
