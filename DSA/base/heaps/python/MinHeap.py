class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def get_min(self):
        if not self.heap:
            return None
        
        self.swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self._heapify_down(0)
        return min_value
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break
    
    def _heapify_down(self, index):
        while True:
            left_child 
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        