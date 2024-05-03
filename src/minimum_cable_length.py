import csv
import os

def minimum_cable_length(graph):
    vertex = len(graph)
    selected = [0] * vertex
    selected[0] = True
    edge = 0
    total_length = 0

    while edge < vertex - 1:
        minimum = float('inf')
        first_vertex = 0
        second_vertex = 0
        for start_vertex in range(vertex):
            if selected[start_vertex]:
                for end_vertex in range(vertex):
                    if not selected[end_vertex] and graph[start_vertex][end_vertex] and graph[start_vertex][end_vertex] < minimum:
                        minimum = graph[start_vertex][end_vertex]
                        first_vertex = start_vertex
                        second_vertex = end_vertex
        if first_vertex != 0 or second_vertex != 0:
            selected[second_vertex] = True
            total_length += graph[first_vertex][second_vertex]
            edge += 1

    return total_length


def calculate_minimum_cable_length(file_name):   
      with open(file_name, 'r') as file:
        reader = csv.reader(file)
        graph = []
        for row in reader:
            graph.append(list(map(int, row)))

current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_directory, 'Laba_8', 'islands.csv')
result = calculate_minimum_cable_length(file_name)
