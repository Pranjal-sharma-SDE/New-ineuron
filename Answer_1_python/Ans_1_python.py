def search_matrix(matrix, target):
    """
    Perform a binary search on a 2D matrix to find the target value.

    Args:
        matrix: A 2D list of integers representing the matrix.
        target: An integer value to be found in the matrix.

    Returns:
        True if the target value is found in the matrix, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example usage:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = search_matrix(matrix, target)
print(result)  # Output: True

# Example usage:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 2
result = search_matrix(matrix, target)
print(result)  # Output: False
