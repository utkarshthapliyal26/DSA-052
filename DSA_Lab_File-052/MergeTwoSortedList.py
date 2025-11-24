def merge_sorted_lists(a, b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


# Example usage
if __name__ == "__main__":
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print("List 1:", list1)
    print("List 2:", list2)
    merged = merge_sorted_lists(list1, list2)
    print("Merged:", merged)
