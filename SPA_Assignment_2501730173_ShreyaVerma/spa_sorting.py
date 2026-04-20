# -------------------------------
# Sorting Algorithms
# -------------------------------

import time
import random


# -------- Insertion Sort --------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# -------- Merge Sort --------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# -------- Quick Sort --------
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


# -------------------------------
# Timing Function
# -------------------------------

def measure_time(sort_func, arr):
    copy_arr = arr.copy()

    start = time.time()

    if sort_func == quick_sort:
        sort_func(copy_arr, 0, len(copy_arr) - 1)
    else:
        sort_func(copy_arr)

    end = time.time()

    return (end - start) * 1000  # ms


# -------------------------------
# Dataset Generator
# -------------------------------

def generate_datasets(size):
    random.seed(42)

    random_list = [random.randint(1, 100000) for _ in range(size)]
    sorted_list = list(range(size))
    reverse_list = list(range(size, 0, -1))

    return random_list, sorted_list, reverse_list


# -------------------------------
# MAIN
# -------------------------------

if __name__ == "__main__":

    # Correctness Check
    test = [5, 2, 9, 1, 5, 6]
    print("Original:", test)

    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))
    print("Quick:", quick_sort(test.copy(), 0, len(test) - 1))

    print("\n----- PERFORMANCE -----\n")

    sizes = [1000, 5000, 10000]

    for size in sizes:
        rand, sorted_arr, rev = generate_datasets(size)

        print(f"\nSIZE = {size}")

        # Random
        print("Random:")
        print("Insertion:", round(measure_time(insertion_sort, rand), 2), "ms")
        print("Merge:", round(measure_time(merge_sort, rand), 2), "ms")
        print("Quick:", round(measure_time(quick_sort, rand), 2), "ms")

        # Sorted
        print("Sorted:")
        print("Insertion:", round(measure_time(insertion_sort, sorted_arr), 2), "ms")
        print("Merge:", round(measure_time(merge_sort, sorted_arr), 2), "ms")
        print("Quick:", round(measure_time(quick_sort, sorted_arr), 2), "ms")

        # Reverse
        print("Reverse:")
        print("Insertion:", round(measure_time(insertion_sort, rev), 2), "ms")
        print("Merge:", round(measure_time(merge_sort, rev), 2), "ms")
        print("Quick:", round(measure_time(quick_sort, rev), 2), "ms")