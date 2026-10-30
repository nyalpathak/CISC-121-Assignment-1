
def perm_missing_elem(A):
    """Return the missing number from 1 through len(A) + 1."""
    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2
    actual_sum = sum(A)
    return expected_sum - actual_sum