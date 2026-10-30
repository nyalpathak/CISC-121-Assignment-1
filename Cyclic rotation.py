
def cyclic_rotation(A, K):
    """Return A rotated to the right K times."""
    if len(A) == 0:
        return []
    # Calculate the effective number of steps to rotate, as rotating by the length of A results in the same array.
    steps = K % len(A)
    if steps == 0:
        return A[:]

    return A[-steps:] + A[:-steps]