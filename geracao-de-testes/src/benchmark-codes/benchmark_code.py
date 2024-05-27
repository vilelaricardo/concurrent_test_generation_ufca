# exemplo simples de um código de Benchmark em Python
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def benchmark_bubble_sort():
    start_time = time.time()

    test_data = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(test_data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Bubble sort took {elapsed_time:.6f} seconds.")


if __name__ == "__main__":
    benchmark_bubble_sort()
