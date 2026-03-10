def sort_and_count(values):
    if len(values) <= 1:
        return values, 0

    midpoint = len(values) // 2
    left, left_count = sort_and_count(values[:midpoint])
    right, right_count = sort_and_count(values[midpoint:])

    merged = []
    split_count = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            split_count += len(left) - left_index
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged, left_count + right_count + split_count


if __name__ == "__main__":
    sample = [2, 4, 1, 3, 5]
    sorted_values, inversions = sort_and_count(sample)
    print("Original:", sample)
    print("Sorted:", sorted_values)
    print("Inversions:", inversions)
