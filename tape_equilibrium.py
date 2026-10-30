
def tape_equilibrium(A):
    """Return the smallest difference between two nonempty tape halves."""
    total = sum(A)
    left_sum = 0
    smallest_difference = float('inf')

    # Stop at len(A) - 2, so the right side is never empty.
    for index in range(len(A) - 1):
        left_sum += A[index]
        right_sum = total - left_sum
        difference = abs(left_sum - right_sum)

        if difference < smallest_difference:
            smallest_difference = difference

    return smallest_difference

