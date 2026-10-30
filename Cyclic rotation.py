
def cyclic_rotation(A, K):
    """Return A rotated to the right K times."""
    if len(A) == 0:
        return []

    steps = K % len(A)
    if steps == 0:
        return A[:]

    return A[-steps:] + A[:-steps]