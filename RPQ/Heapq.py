import math
from Task import Task
from io import StringIO


class Heapq:
    def __init__(self, tasks=[], key="r", max=math.inf, reverse=False):
        self.data = []
        self.max = max
        self.key = key
        self.reverse = reverse

        for task in tasks:
            self.insert(task)

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __bool__(self):
        return len(self.data) > 0

    @staticmethod
    def _compare(task1: Task, task2: Task, key, reverse):
        if reverse is True:
            if key == "r":
                return task1.r > task2.r
            if key == "q":
                return task1.q > task2.q
        else:
            if key == "r":
                return task1.r < task2.r
            if key == "q":
                return task1.q < task2.q

    @staticmethod
    def _parent(i):
        return i // 2

    @staticmethod
    def _leftChild(i):
        return 2 * i

    @staticmethod
    def _rightChild(i):
        return 2 * i + 1

    @property
    def top(self):
        return self.data[0]

    def insert(self, el):
        self.data.append(el)
        index = len(self.data) - 1
        while index > 0 and self._compare(self.data[index], self.data[self._parent(index)], self.key, self.reverse):
            self.data[index], self.data[self._parent(index)] = self.data[self._parent(index)], self.data[index]
            index = self._parent(index)

    def _heapify(self, index: int):
        left_index = self._leftChild(index)
        right_index = self._rightChild(index)
        largest = index
        if left_index < len(self.data) and self._compare(self.data[left_index], self.data[index], self.key,
                                                         self.reverse):
            largest = left_index
        if right_index < len(self.data) and self._compare(self.data[right_index], self.data[largest], self.key,
                                                          self.reverse):
            largest = right_index
        if largest != index:
            self.data[largest], self.data[index] = self.data[index], self.data[largest]
            self._heapify(largest)

    def pop(self):
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        last_element = self.data.pop()
        self.data[0] = last_element
        self._heapify(0)
        return root


    def show_tree(self, total_width=220, fill=' '):
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.data):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            if self.key=="r":
                output.write(str(n.r).center(col_width, fill))
            else:
                output.write(str(n.q).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)