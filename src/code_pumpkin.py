def generate_matrix(cov, rov):
    matrix = []
    for i in range(rov):
        if i % 2 == 0:
            for j in range(cov):
                matrix.append((i, j))
        else:
            for j in range(cov - 1, -1, -1):
                matrix.append((i, j))
    return matrix

def calculate_seeds_to_plant(m, n,  pumpkin_counts):
    matrix = generate_matrix(m, n)
    seeds_to_plant = []
    for pos in matrix:
        i, j = pos
        seeds_to_plant.append(pumpkin_counts[i][j])
    return seeds_to_plant
