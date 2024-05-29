import matplotlib.pyplot as plt
from Aufgabe_1 import *

def test_sorting_algorithms():
    ns = [10, 100, 500, 1000, 2000, 3000, 6000]  # replace with desired values of n
    selection_times = []
    insertion_times = []
    bubble_times = []

    for n in ns:
        random.seed(42)
        arr = [random.randint(1, 1000) for _ in range(n)]

        start_time = time.time()
        selection_sort(arr)
        end_time = time.time()
        selection_times.append(end_time - start_time)

        start_time = time.time()
        insertion_sort(arr)
        end_time = time.time()
        insertion_times.append(end_time - start_time)

        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        bubble_times.append(end_time - start_time)

    plt.plot(ns, selection_times, label='Selection Sort')
    plt.plot(ns, insertion_times, label='Insertion Sort')
    plt.plot(ns, bubble_times, label='Bubble Sort')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()

test_sorting_algorithms()