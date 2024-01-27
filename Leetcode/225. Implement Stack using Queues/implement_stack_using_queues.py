from collections import deque

# Note
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.

# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


class MyStack:
    """
    In This approach we try to maintain the stack on insertion
    """

    def __init__(self):
        # we have stack like [2,1] where 2 is the top
        self._queue = deque()

    def push(self, x: int) -> None:
        # we have appended 3 so stack [2,1,3] but it must be [3,2,1]
        self._queue.append(x)
        # so we have popped element before it and appended after that
        for _ in range(len(self._queue)-1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not bool(self._queue)


class MyStackWithTwoQueue:
    """
    In this we dont maintain like stack but make operations according to stack
    """

    def __init__(self):
        # we have stack like [2,1] where 2 is the top
        # concept is simple , we do push and empty from q1
        self._q1 = deque()
        self._q2 = deque()

    def push(self, x: int) -> None:
        # we have appended 3 so stack [2,1,3] but it must be [3,2,1]
        self._q1.append(x)

    def pop(self) -> int:
        # we first pop all the elements and add to q2 and swap q1 and q2 except the element to be removed
        while len(self._q1) > 1:
            self._q2.append(self._q1.popleft())
        element = self._q1.popleft()
        self._q1, self._q2 = self._q2, self._q1
        return element

    def top(self) -> int:
        # since we are allowed of pop 0 or can access the first element in queue
        # we will pop and add and swap
        while len(self._q1) > 1:
            self._q2.append(self._q1.popleft())
        element = self._q1[0]
        self._q1, self._q2 = self._q2, self._q1
        return element

    def empty(self) -> bool:
        return not bool(self._q1)


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
# param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_3, param_4)

obj = MyStackWithTwoQueue()
obj.push(1)
obj.push(2)
obj.push(3)
# param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_3, param_4)
