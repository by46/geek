"""
>>> 2+1
3
"""
import doctest
import random
from bisect import insort
from heapq import cmp_lt
from heapq import heapify
from heapq import heappop
from heapq import heappush
from heapq import heappushpop
from itertools import count
from itertools import islice
from itertools import repeat


def simple_demo(iterable):
    """basic usage heapq

    >>> simple_demo([12, 2, 12, 4, 33, 1, 123, 32145, 1])
    [1, 1, 2, 4, 12, 12, 33, 123, 32145]

    :param iterable:
    :return:
    """
    h = []
    for value in iterable:
        heappush(h, value)
    print([heappop(h) for i in range(len(h))])


def simple_demo2():
    import random

    q = []
    for i in range(20):
        heappush(q, random.randint(0, 100))
    print q


REMOVED = object()


class PriorityQueue(object):
    def __init__(self):
        self._tasks = []
        self._knapsack = {}
        self._counter = count()

    def add(self, task, priority=0):
        if task in self._knapsack:
            self.remove(task)

        task_id = next(self._counter)
        entry = [priority, task_id, task]
        self._knapsack[task] = entry
        heappush(self._tasks, entry)

    def remove(self, task):
        entry = self._knapsack.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        while self._tasks:
            priority, task_id, task = heappop(self._tasks)
            if task is not REMOVED:
                del self._knapsack[task]
                return task
        raise KeyError('pop from an empty priority queue')


def priority_demo():
    q = PriorityQueue()
    for task in range(15):
        priority = random.randint(0, 5)
        q.add('Task {0}: priority {1}'.format(task, priority), priority)
    try:
        while True:
            print q.pop()
    except KeyError:
        pass


def nlargest(n, iterable):
    """Find n largest element in iterable

    Equivalent sorted(iterable, reverse=True)[:10]

    Basic Example:
    >>> nlargest(5, [33, 12, 13, 56, 54, 51, 31, 90, 2, 14])
    [90, 56, 54, 51, 33]
    >>> nlargest(0, [1, 2, 3, 4])
    []
    >>> nlargest(10, [])
    []

    :param n:
    :param iterable:
    :return:
    """
    if n <= 0:
        return []
    it = iter(iterable)
    result = list(islice(it, n))
    if not result:
        return []

    heapify(result)
    for item in it:
        heappushpop(result, item)

    result.sort(reverse=True)
    return result


def nsmallest(n, iterable):
    """Find n smallest element in iterable

    Equivalent sorted(iterable)[:n]

    Basic Example:
    >>> nsmallest(5, [33, 12, 13, 56, 54, 51, 31, 90, 2, 14])
    [2, 12, 13, 14, 31]
    >>> nsmallest(0, [33])
    []
    >>> nsmallest(10, [])
    []

    :param n:
    :param iterable:
    :return:
    """
    if n <= 0:
        return []

    if hasattr(iterable, '__len__') and n * 10 <= len(iterable):
        it = iter(iterable)
        result = sorted(islice(it, n))
        if not result:
            return result

        los = result[-1]
        for item in it:
            if cmp_lt(item, los):
                insort(result, item)
                result.pop()
                los = result[-1]
        return result
    h = list(iterable)
    heapify(h)
    return map(heappop, repeat(h, min(n, len(h))))


if __name__ == '__main__':
    priority_demo()
    simple_demo2()

    doctest.testmod()
