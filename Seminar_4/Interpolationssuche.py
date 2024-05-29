def interpolation_search(arr, target):
    """
    Führt eine Interpolationssuche auf einem sortierten Array durch, um den Index eines Zielwerts zu finden.

    Parameter:
    arr (list): Das sortierte Array, in dem gesucht werden soll.
    target (int): Der Wert, nach dem gesucht werden soll.

    Rückgabe:
    int: Der Index des Zielwerts im Array oder -1, wenn er nicht gefunden wurde.
    ____
    
    Die Interpolationssuche basiert auf der Annahme, dass die Werte im Array gleichmäßig verteilt sind.
    In einem solchen Fall kann man den Standort des gesuchten Werts target im Array basierend auf den Werten an den Indizes low und high abschätzen.
    
    """
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Schätzt die Position des Zielwerts
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Beispielnutzung der interpolation_search-Funktion
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
target = 18
result = interpolation_search(arr, target)

if result != -1:
    print(f"Target value {target} found at index {result}")
else:
    print(f"Target value {target} not found in the array")
