"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large
enough buffer at the end to hold B. Write a method to merge B into A in sorted
order.
"""

def sorted_merge(a, b):
    """
    We move backwards in the buffered list and make comparisons starting from
    the greatest value in each list and fill in the buffer and ultimately the
    rest of list A.

    Time: O(a+b) where a and b are the # of elements in lists a and b
    Space: O(1) since we do not use any auxiliary space
    """

    # make pointers for the last element in each list
    idx_a = len(a) - len(b) - 1
    idx_b = len(b) - 1

    # start from the end of a and fill in the list backwards with the largest
    # element
    for i in range(len(a) - 1, -1, -1):
        # if any idx's are negative, it means we've exhausted the elements in
        # that list
        if idx_a == -1:
            a[i] = b[idx_b]
            idx_b -= 1
        elif idx_b == -1:
            a[i] = a[idx_a]
            idx_a -= 1
        # if the largest element in a is bigger than the largest element in b,
        # we write a[idx_a] to the buffer and access the next largest element
        # in b
        elif a[idx_a] >= b[idx_b]:
            a[i] = a[idx_a]
            idx_a -= 1
        # the opposite of the previous case in terms of writing b[idx_b] to a
        else:
            a[i] = b[idx_b]
            idx_b -= 1
    return a
