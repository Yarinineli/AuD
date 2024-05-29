def binary_search(arr, target, low=0, high=None):
    
    if high is None:
        high = len(arr)-1
    
    """
    Führt eine binäre Suche auf einem sortierten Array durch, um den Index eines Zielwerts zu finden.

    Parameter:
    arr (list): Das sortierte Array, in dem gesucht werden soll.
    target (int): Der Wert, nach dem gesucht werden soll.
    low (int): Der untere Rand des Suchbereichs (Standardwert: 0).
    high (int): Der obere Rand des Suchbereichs (Standardwert: Länge des Arrays - 1).

    Rückgabe:
    int: Der Index des Zielwerts im Array oder -1, wenn er nicht gefunden wurde.
    """
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

arr = [1, 3, 5, 7, 9]
target = 9

result = binary_search(arr, target)

if result != -1:
    print(f"Target value {target} found at index {result}")
else:
    print(f"Target value {target} not found in the array")