from Binäre_suche import binary_search

def exponential_search(arr, target):
    """
    Führt eine exponentielle Suche auf einem sortierten Array durch, um den Index eines Zielwerts zu finden.

    Parameter:
    arr (list): Das sortierte Array, in dem gesucht werden soll.
    target (int): Der Wert, nach dem gesucht werden soll.

    Rückgabe:
    int: Der Index des Zielwerts im Array oder -1, wenn er nicht gefunden wurde.
    """
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2

    # Verwende die binary_search Funktion mit den erweiterten Parametern low und high
    return binary_search(arr, target, i // 2, min(i, n - 1))

# Beispielnutzung der exponential_search-Funktion
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
target = 15
result = exponential_search(arr, target)

if result != -1:
    print(f"Target value {target} found at index {result}")
else:
    print(f"Target value {target} not found in the array")
