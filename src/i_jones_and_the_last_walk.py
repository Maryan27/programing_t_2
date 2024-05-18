import os
from collections import defaultdict

def counting_ways_to_pass_the_corridor(columns, rows, matrix):
    ways_count_matrix = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        ways_count_matrix[row][0] = 1

    for column in range(1, columns):
        sum_of_ways = defaultdict(int)
        
        for row in range(rows):
            sum_of_ways[matrix[row][column]] += ways_count_matrix[row][column - 1]
        
        for plate in range(column + 1, columns):
            if matrix[row][column] == matrix[row][plate]:
                ways_count_matrix[row][column] += ways_count_matrix[row][plate]

            if row > 0 and column < columns - 1 and matrix[row][column] == matrix[row - 1][column + 1]:
                ways_count_matrix[row][column] += ways_count_matrix[row - 1][column + 1]
            
            if row < rows - 1 and column < columns - 1 and matrix[row][column] == matrix[row + 1][column + 1]:
                ways_count_matrix[row][column] += ways_count_matrix[row + 1][column + 1]

        for row in range(rows):
            ways_count_matrix[row][column] = sum_of_ways[matrix[row][column]]

    total_paths = ways_count_matrix[0][columns - 1] + ways_count_matrix[rows - 1][columns - 1]
    return total_paths



def calculate_total_paths_from_file(file_name):
    """
    This function calculates the total number of paths from input file
    """
    file_path = os.path.join(project_root, 'resource', file_name)
    with open(file_path, 'r') as file:
        first_line = file.readline().strip().split()
        columns, rows = int(first_line[0]), int(first_line[1])
        matrix = [list(file.readline().strip()) for _ in range(rows)]
    total_paths = counting_ways_to_pass_the_corridor(columns, rows, matrix)
    return total_paths

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
file_name = os.path.join(project_root, 'resource', 'i.jones.in.txt')
result = calculate_total_paths_from_file(file_name)


file_path = os.path.join(project_root, 'resource', 'i.jones.out.txt')
output_file_path = os.path.join(project_root, 'resource', file_path)
with open(output_file_path, 'w') as output_file:
    output_file.write(str(result))
