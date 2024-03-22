class Node:
    def __init__(self, value, priority):
        self.value = value  
        self.priority = priority  

class PriorityQueue:
    def __init__(self):
        self.heap = []  
        
    def insert(self, value, priority):
        node = Node(value, priority) 
        self.heap.append(node)  
        self._heapify_up(len(self.heap) - 1)  

    def remove_max(self):
        if not self.heap: 
            return None 
        max_value = self.heap[0].value  
        last_node = self.heap.pop()  
        if self.heap: 
            self.heap[0] = last_node 
            self._heapify_down(0)  
        return max_value  

    def _heapify_up(self, i):
        parent_i = (i - 1) // 2  
        while i > 0 and self.heap[parent_i].priority < self.heap[i].priority:
            self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
            i = parent_i  
            parent_i = (i - 1) // 2  

    def _heapify_down(self, i):
        left_child_i = 2 * i + 1  
        right_child_i = 2 * i + 2  
        largest_i = i  
        
        if left_child_i < len(self.heap) and self.heap[left_child_i].priority > self.heap[largest_i].priority:
            largest_i = left_child_i
        if right_child_i < len(self.heap) and self.heap[right_child_i].priority > self.heap[largest_i].priority:
            largest_i = right_child_i
        if largest_i != i:  
            self.heap[largest_i], self.heap[i] = self.heap[i], self.heap[largest_i]
            self._heapify_down(largest_i)  
