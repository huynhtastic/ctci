def quick_sort(A, start=0, end=None):
    if len(A) < 2 or start == end:
        return A
    if end == None:
        end = len(A) - 1

    border = start
    for i in range(start, end):
        if A[i] <= A[end]:
            A[i], A[border] = A[border], A[i]
            border += 1
    A[end], A[border] = A[border], A[end]
    A = quick_sort(A, start, max(border-1, 0))
    return quick_sort(A, border, end)
