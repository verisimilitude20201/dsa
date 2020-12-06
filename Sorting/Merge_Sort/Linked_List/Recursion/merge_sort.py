def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    S1 = LinkedQueue()
    S2 = LinkedQueue()

    while len(S1) < n // 2:
        S1.enqueue(S.dequeue())

    while not S.is_empty():
        S2.enqueue(S.dequeue())

    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)


def merge(S1, S2, S):
    while not S1.is_empty() and not S2.is_empty():
        if S1.peek() < S2.peek():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())

    while not S1.is_empty():
        S.enqueue(S1.dequeue())

    while not S2.is_empty():
        S.enqueue(S2.dequeue())


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
    merge_sort(myQueue1)
    print(myQueue1.dequeue())