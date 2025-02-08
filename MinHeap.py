from typing import List


class MinHeap:
    def __init__(self):
        self.minHeap = []
    def __str__(self):
        return ", ".join(str(item) for item in self.minHeap)
    def is_empty(self):
        return len(self.minHeap) == 0
    def get_all_elements(self):
        return self.minHeap
    def insert(self, node):
        self.minHeap.append(node)
        currentIndex = len(self.minHeap) - 1
        while currentIndex > 0:
            parentIndex = (currentIndex - 1) // 2
            parent = self.minHeap[parentIndex]
            if node.compare(parent):
                self.minHeap[currentIndex], self.minHeap[parentIndex] = self.minHeap[parentIndex], node
                currentIndex = parentIndex
            else:
                break
    def get_min(self):
        if len(self.minHeap) == 0:
            return None
        return self.minHeap[0]
    def remove_min(self):
        if len(self.minHeap) == 0:
            return None
        minNode = self.get_min()
        lastNode = self.minHeap.pop()
        if len(self.minHeap) != 0:
            self.minHeap[0] = lastNode
            currentIndex = 0
            while True:
                leftIndex = 2 * currentIndex + 1
                rightIndex = 2 * currentIndex + 2
                if leftIndex >= len(self.minHeap):
                    break
                minChildIndex = leftIndex
                if rightIndex < len(self.minHeap):
                    left = self.minHeap[leftIndex]
                    right = self.minHeap[rightIndex]
                    if left.compare(right):
                        minChildIndex = rightIndex
                minChild = self.minHeap[minChildIndex]
                if lastNode.compare(minChild):
                    self.minHeap[currentIndex], self.minHeap[minChildIndex] = minChild, lastNode
                    currentIndex = minChildIndex
                else:
                    break
        return minNode
    def delete(self, node):
        if len(self.minHeap) == 0:
            return
        try:
            index = self.minHeap.index(node)
        except ValueError:
            return
        lastNode = self.minHeap.pop()
        if index != len(self.minHeap):
            self.minHeap[index] = lastNode
            currentIndex = index
            while True:
                leftIndex = 2 * currentIndex + 1
                rightIndex = 2 * currentIndex + 2
                if leftIndex >= len(self.minHeap):
                    break
                minChildIdx = leftIndex
                if rightIndex < len(self.minHeap):
                    left = self.minHeap[leftIndex]
                    right = self.minHeap[rightIndex]
                    if left.compare(right):
                        minChildIdx = rightIndex
                minChild = self.minHeap[minChildIdx]
                if lastNode.compare(minChild):
                    self.minHeap[currentIndex], self.minHeap[minChildIdx] = minChild, lastNode
                    currentIndex = minChildIdx
                else:
                    break
                parentIndex = (currentIndex - 1) // 2
                if currentIndex > 0 and lastNode.compare(self.minHeap[parentIndex]):
                    while currentIndex > 0:
                        parentIndex = (currentIndex - 1) // 2
                        parent = self.minHeap[parentIndex]
                        if lastNode.compare(parent):
                            self.minHeap[currentIndex], self.minHeap[parentIndex] = parent, lastNode
                            currentIndex = parentIndex
                        else:
                            break
