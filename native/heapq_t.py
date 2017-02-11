import random
from heapq import heappop
from heapq import heappush
from itertools import count


def simple_demo():
    """
    basic usage heapq
    :return:
    """
    iterable = [12, 2, 12, 4, 33, 1, 123, 32145, 1]
    h = []
    for value in iterable:
        heappush(h, value)
    print([heappop(h) for i in range(len(h))])


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


if __name__ == '__main__':
    simple_demo()
    priority_demo()
