import time
import random

n = 10  # replace with the desired length of the array
arr = [random.randint(1, 100) for _ in range(n)]

def selection_sort(arr):
    """
    Sorts the given array using the selection sort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    None. The array is sorted in-place.

    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Selection Sorted array:", arr)
    
    
def insertion_sort(arr):
    """
    Sorts the given array using the insertion sort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    None. The array is sorted in-place.

    """
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Insertion Sorted array:", arr)



def bubble_sort(arr):
    """
    Sorts the given array using the bubble sort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    None. The function modifies the input array in-place.

    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("\nBubble Sorted array:", arr)

