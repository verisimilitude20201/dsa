def quick_sort(A):
    N = len(A)
    if N < 2:
        return

    pivot = A[N - 1]

    G = []
    S = []
    E = []
    for i in range(N):
        if A[i] > pivot:
            G.append(A[i])
        elif A[i] < pivot:
            S.append(A[i])
        else:
            E.append(A[i])

    quick_sort(S)
    quick_sort(G)

    j = 0

    for i in range(len(S)):
        A[j] = S[i]
        j += 1

    for i in range(len(E)):
        A[j] = E[i]
        j += 1

    for i in range(len(G)):
        A[j] = G[i]
        j += 1


A = [20, 19, 22, 4, 5, 3, 3, 4]
quick_sort(A)
print(A)