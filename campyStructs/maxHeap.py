class MaxHeap:
    def __init__(self, items=[]):
        self.heap = []
        for i in items:
            self.heap.append(i)
            self.floatUp(len(self.heap) - 1)

    def push(self, data):
        print(self.heap)
        self.heap.append(data)
        self.floatUp(len(self.heap) -1)
        print(self.heap)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.swap(0, len(self.heap) -1)
            mmax = self.heap.pop()
            self.bubbleDown(0)
        elif len(self.heap) == 2:
            mmax = self.heap.pop()
        else:
            mmax = False
        return mmax

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def floatUp(self, index):
        parent = index//2
        if index <= 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.floatUp(parent)

    def bubbleDown(self, index):
        left = index * 2
        right = (index * 2) +1
        largest = index
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubbleDown(largest)
#m = MaxHeap([95,3,21])
#m.push(10)
#m.push(100)
#print(str(m.heap))
#print(m.pop())
