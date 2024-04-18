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

def dijkstra(graph, start):  
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = PriorityQueue()  
    queue.insert(start, 0)

    while queue.heap:
        current_element = queue.remove_max()
        for neighbor, weight in graph[current_element]:
            distance = distances[current_element] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.insert(neighbor, distance)
                
    return distances

def find_optimal_server_placement(graph, clients):
    min_max_delay = float('inf')
    optimal_server = None

    for vertex in graph:
        if vertex not in clients:
            max_delay = 0
            for client in clients:
                distances = dijkstra(graph, client) 
                max_delay = max(max_delay, distances[vertex])
            if max_delay < min_max_delay:
                min_max_delay = max_delay
                optimal_server = vertex

    return optimal_server, min_max_delay


if __name__ == "__main__":
    with open("C:/Users/Marian/OneDrive/Desktop/laba/gamsrv.in.txt", "r") as infile:
        N, M = map(int, infile.readline().strip().split())
        clients = set(map(int, infile.readline().strip().split()))
        graph = {i: [] for i in range(1, N + 1)}
        for _ in range(M):
            startnode, endnode, latency = map(int, infile.readline().strip().split())
            graph[startnode].append((endnode, latency))
            graph[endnode].append((startnode, latency))
    
    optimal_server, min_max_delay = find_optimal_server_placement(graph, clients)
    
    with open("C:/Users/Marian/OneDrive/Desktop/laba/gamsrv.out.txt", "w") as outfile:
        outfile.write(str(min_max_delay) + "\n")
