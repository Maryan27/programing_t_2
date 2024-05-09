import csv
import os
from heap_based_priority_queue import PriorityQueue  

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
