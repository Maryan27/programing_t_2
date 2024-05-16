import csv
import os

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

    def remove_min(self):  
        if not self.heap: 
            return None 
        min_value = self.heap[0].value  
        last_node = self.heap.pop()  
        if self.heap: 
            self.heap[0] = last_node 
            self._heapify_down(0)  
        return min_value  

    def _heapify_up(self, i):
        parent_i = (i - 1) // 2  
        while i > 0 and self.heap[parent_i].priority > self.heap[i].priority:  
            self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
            i = parent_i  
            parent_i = (i - 1) // 2  

    def _heapify_down(self, i):
        left_child_i = 2 * i + 1  
        right_child_i = 2 * i + 2  
        smallest_i = i 
        
        if left_child_i < len(self.heap) and self.heap[left_child_i].priority < self.heap[smallest_i].priority:  
            smallest_i = left_child_i
        if right_child_i < len(self.heap) and self.heap[right_child_i].priority < self.heap[smallest_i].priority:  
            smallest_i = right_child_i
        if smallest_i != i:  
            self.heap[smallest_i], self.heap[i] = self.heap[i], self.heap[smallest_i]
            self._heapify_down(smallest_i) 

def minimum_cable_length(graph):
    """
    This function finds the minimum cable length using the Prime algorithm with a priority queue
    """
    vertex = len(graph)
    selected = [0] * vertex 
    selected[0] = True
    edge = 0
    total_length = 0
    priority_queue = PriorityQueue()


    for end_vertex in range(vertex):
        if graph[0][end_vertex]:
            priority_queue.insert((graph[0][end_vertex], 0, end_vertex), graph[0][end_vertex])

    while edge < vertex - 1 and priority_queue.heap:
        distance, start_vertex, end_vertex = priority_queue.remove_min()
        if not selected[end_vertex]:
            selected[end_vertex] = True
            total_length += distance
            edge += 1
            for new_end_vertex in range(vertex):
                if not selected[new_end_vertex] and graph[end_vertex][new_end_vertex]:
                    priority_queue.insert((graph[end_vertex][new_end_vertex], end_vertex, new_end_vertex),
                              graph[end_vertex][new_end_vertex])

    return total_length



def calculate_minimum_cable_length(file_name):
    """
    This function calculates the minimum cable length
    """
    file_path = os.path.join(project_root, 'resource', file_name)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        graph = []
        for row in reader:
            graph.append(list(map(int, row)))

    result = minimum_cable_length(graph)
    return result

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
file_name = 'islands.csv'
result = calculate_minimum_cable_length(file_name)
