
def frog_jmp(X, Y, D):
    """Return the fewest jumps of length D needed to reach at least Y."""
    distance = Y - X
    jumps = distance // D

    if distance % D != 0:
        jumps += 1

    return jumps