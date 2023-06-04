import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    swaps = []
    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swaps.append(list(arr))
    end_time = time.time()
    execution_time = end_time - start_time
    return arr, swaps, execution_time

# Contoh penggunaan:
arr = [23, 12, 8, 32, 85]
sorted_arr, swaps, execution_time = bubble_sort(arr)
print("Hasil Bubble Sort (Versi Lambat):", sorted_arr)
print("Pertukaran yang terjadi:")
for i, swap in enumerate(swaps):
    print("Iterasi ke-", i+1, ":", swap)
print("Waktu eksekusi:", execution_time, "detik")
