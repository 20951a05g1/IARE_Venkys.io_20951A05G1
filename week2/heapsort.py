def heapi(arr, n, i):
    lar = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[lar]:
        lar = l

    if r < n and arr[r] > arr[lar]:
        lar = r

    if lar != i:
        arr[i], arr[lar] = arr[lar], arr[i]
        heapi(arr, n, lar)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapi(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapi(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Sorted array is:")
print(arr)
