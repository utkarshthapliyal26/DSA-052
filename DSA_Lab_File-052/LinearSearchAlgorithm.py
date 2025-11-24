def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            print(f"Element {target} found at index {i}")
            return i
    print(f"Element {target} not found")
    return -1

# Example usage
arr = [7, 2, 5, 3, 9]
linear_search(arr, 5)
linear_search(arr, 10)
