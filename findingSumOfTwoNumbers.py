#Two pointer method
from timeit import default_timer as timer
import random as rand


def mergeSort(listOfElements):
    if (len(listOfElements) > 1):
        mid = len(listOfElements) // 2
        leftElements = listOfElements[:mid]
        rightElements = listOfElements[mid:]

        mergeSort(leftElements)
        mergeSort(rightElements)

        i = j = k = 0

        while (i < len(leftElements) and j < len(rightElements)):

            if leftElements[i] < rightElements[j]:
                listOfElements[k] = leftElements[i]
                i += 1
            else:
                listOfElements[k] = rightElements[j]
                j += 1
            k += 1

        while i < len(leftElements):
            listOfElements[k] = leftElements[i]
            i += 1
            k += 1

        while j < len(rightElements):
            listOfElements[k] = rightElements[j]
            j += 1
            k += 1

    # print(listOfElements)
    return listOfElements


def findSumPairsBrute(x, target):
    start = timer()
    counter =0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] + x [j] == target:
                counter  += 1
                # print(f'{x[i]} {x[j]}')
    end = timer()
    print(f"Total Pairs: {counter}")
    print(f'Time in brute force: {end - start}')

def findSumPairs(x,target):
    start = timer()
    counter = 0
    x.sort(reverse = True)
    # print(x)
    i =0
    j = len(x)-1

    while(i<j):
        if x[i]+x[j] > target : i +=1
        elif x[i]+x[j] < target : j -= 1
        else:
            counter +=1
            # print(f'{x[i]} {x[j]}')
            i +=1
            j -=1
    end = timer()
    print(f"Total Pairs: {counter}")
    print(f'Time in python sort: {end - start}')

def findSumPairsMergeSort(x,target):
    start = timer()
    counter = 0
    x = mergeSort(x)
    # print(x)
    i = 0
    j = len(x) - 1

    while (i < j):
        if x[i] + x[j] < target:
            i += 1
        elif x[i] + x[j] > target:
            j -= 1
        else:
            counter += 1
            # print(f'{x[i]} {x[j]}')
            i += 1
            j -= 1
    end = timer()
    print(f"Total Pairs: {counter}")
    print(f'Time in merge sort: {end - start}')



xList = rand.sample(range(-100000,100000),15000)
# xList = [11, 4, 1 ,5, -2, -1, 8, 10, -3]
# print(xList)
findSumPairs(xList,777)
findSumPairsMergeSort(xList,777)
findSumPairsBrute(xList,777)
