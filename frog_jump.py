
def frog_jmp(X, Y, D):
    """Return the fewest jumps of length D needed to reach at least Y."""
    distance = Y - X
    jumps = distance // D
    # If the distance is not evenly divisible by D, we need one more jump to cover the remaining distance.
    if distance % D != 0:
        jumps += 1

    return jumps