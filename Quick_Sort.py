import random

def quick_sort_inplace(arr):
    """Entry point for in-place quicksort."""
    _quicksort(arr, 0, len(arr) - 1)
    return arr


def _quicksort(arr, low, high):
    """Helper function executing recursive in-place partitioning."""
    if low < high:
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

        p_index = _partition(arr, low, high)

        _quicksort(arr, low, p_index - 1)
        _quicksort(arr, p_index + 1, high)


def _partition(arr, low, high):
    """Lomuto partition scheme."""
    pivot = arr[high]
    i = low - 1  

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1