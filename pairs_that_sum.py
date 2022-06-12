def pairs_that_sum(arr, target_sum):
    """
    Searches a list array for pairs of integers that sum to a target sum.

    Parameters:
        arr (list): a list of integers.
        target_sum (int): the target to search for sum of pairs.

    Returns:
        pairs, unq_pairs, unq_num_pairs (lists): Lists of all pairs, unique pairs, and unique number pairs
            that sum to target_sum.
    """

    # initialize pair list
    pairs = []

    # loop over arr and sum each pair
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n):
            if (target_sum - arr[i]) == arr[j] and i != j:
                pairs.append([arr[i], arr[j]])

    # create list of unique pairs and recast nested tuples to list datatype
    unq_pairs = list(set(tuple(pair) for pair in pairs))
    unq_pairs = sorted([list(pair) for pair in unq_pairs])

    # create list of unique numbered pairs
    unq_num_pairs = list(set(tuple(sorted(pair)) for pair in unq_pairs))
    unq_num_pairs = sorted([list(pair) for pair in unq_num_pairs])

    # Outputs:
    return pairs, unq_pairs, unq_num_pairs


a = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
all_pairs, unique_pairs, unique_num_pairs = pairs_that_sum(a, 10)


print(f'All Pairs: {all_pairs} \n')
print(f'Unique Pairs {unique_pairs} \n')
print(f'Unique Number Pairs {unique_num_pairs}')
