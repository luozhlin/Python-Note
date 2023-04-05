import random
import time

def FindMin1(numlist):  # O(n^2)
    overallmin = numlist[0]
    for i in numlist:
        isSmallest = True
        for j in numlist:
            if i>j:
                isSmallest = False
        if isSmallest:
            overallmin = i
    return overallmin

def FindMin2(numlist):  # O(n)
    overallmean = numlist[0]
    for i in numlist:
        if overallmean > i:
            overallmean = i
    return overallmean


if __name__ == "__main__":
    num =[-1,4,3,2,5,31,2,1,6,0]
    print(FindMin2(num))

    for listSize in range(1000,10001,1000):
        num = [random.randrange(10000) for x in range(listSize)]
        start = time.time()
        print(FindMin1(num))
        end = time.time()
        print("Size: %d Time: %f" % (listSize, end-start))

    for listSize in range(1000,10001,1000):
        num = [random.randrange(10000) for x in range(listSize)]
        start = time.time()
        print(FindMin2(num))
        end = time.time()
        print("Size: %d Time: %f" % (listSize, end-start))
