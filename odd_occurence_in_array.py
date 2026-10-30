def odd_occurrences_in_array(A):
    """Return the one value that appears an odd number of times."""
    counts = {}

    for number in A:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for number in counts:
        if counts[number] % 2 != 0:
            return number