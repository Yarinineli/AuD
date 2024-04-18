import timeit

Fiba_max = 50
FibonacciList = [0, 1]

def fibo(FibonacciList):
    next_number = FibonacciList[-1] + FibonacciList[-2]
    FibonacciList.append(next_number)

for i in range(Fiba_max):
    start = timeit.default_timer()
    fibo(FibonacciList)
print(FibonacciList, timeit.default_timer() - start)

