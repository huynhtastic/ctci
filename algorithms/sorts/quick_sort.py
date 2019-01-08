def quick_sort(A, start=0, end=None):

    # return the array if it's a length of 1 or the bounds of the sort
    # aren't workable (the start == end condition)
    if len(A) < 2 or start == end:
        return A

    # default value for the ending bound of the sort
    if end == None:
        end = len(A) - 1

    # make the border the starting bound of the sort
    border = start

    for i in range(start, end):
        # check if the current item is bigger than the item located at the
        # ending bound (the pivot)
        if A[i] <= A[end]:
            A[i], A[border] = A[border], A[i]
            border += 1

    # swap the pivot with the border
    A[end], A[border] = A[border], A[end]
    # sort the left partition of the list
    A = quick_sort(A, start, max(border-1, 0))
    # return A with the right partition of the list sorted
    return quick_sort(A, border, end)
