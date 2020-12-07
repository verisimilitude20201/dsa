def quick_sort(S):
    n = len(S)
    if n < 2:
        return
    pivot = S.peek()
    G = LinkedQueue()
    L = LinkedQueue()
    E = LinkedQueue()
    while not S.is_empty():
        if S.peek() > pivot:
            G.enqueue(S.dequeue())
        elif S.peek() < pivot:
            L.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())

    quick_sort(L)
    quick_sort(G)

    while not L.is_empty():
        S.enqueue(L.dequeue())

    while not E.is_empty():
        S.enqueue(E.dequeue())

    while not G.is_empty():
        S.enqueue(G.dequeue())


if __name__ == '__main__':
    myQueue1 = LinkedQueue()
    myQueue1.enqueue(24)
    myQueue1.enqueue(45)
    myQueue1.enqueue(63)
    myQueue1.enqueue(85)
    myQueue1.enqueue(17)
    myQueue1.enqueue(31)
    myQueue1.enqueue(15)
    myQueue1.enqueue(96)
    quick_sort(myQueue1)
