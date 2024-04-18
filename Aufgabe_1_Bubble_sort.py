import random

randomList = []

for i in range(0,10):
    n = random.randint(1,100)
    randomList.append(n)
print(randomList)

def bubble_sort(randomList):
    n = len(randomList)
    for i in range(n):
        for j in range(0,n-1):
            if randomList[j] > randomList[j+1]:
                randomList[j], randomList[j+1] = randomList[j+1], randomList[j]
    return randomList

sortedList = bubble_sort(randomList)
print(sortedList)



