import math
from Task import Task

class Heap:
    def __init__(self, key, max=math.inf):
        self.data = []
        self.max = max

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self):
        return str(self.data)

    @staticmethod
    def _compare(task1:Task, task2:Task, key="r"):
        if key == "r":
            return task1.r < task2.r
        if key == "q":
            return task1.q < task2.q

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _leftChild(i):
        return 2 * i + 1

    @staticmethod
    def _rightChild(i):
        return 2 * i + 2

    def insert(self, el):
        self.data.append(el)
        index = len(self.data) - 1
        if index > 0 and self._compare(self.data[index], self.data[self._parent(index)]):
            parent = self._parent(index)
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def _heapify(self, index: int):
        left_index = self._leftChild(index)
        right_index = self._rightChild(index)
        greatest_elem_index = index
        if left_index < len(self) and self._compare(self.data[left_index], self.data[index]):
            greatest_elem_index = left_index
        if right_index < len(self) and self._compare(self.data[right_index], self.data[greatest_elem_index]):
            greatest_elem_index = right_index
        if greatest_elem_index != index:
            self.data[greatest_elem_index], self.data[index] = self.data[index], self.data[greatest_elem_index]
            self._heapify(greatest_elem_index)

