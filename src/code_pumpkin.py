def generate_matrix(cov, rov):
    matrix = []
    for j in range(cov):
        if j % 2 == 0:
            for i in range(rov):
                matrix.append((j, i))
        else:
            for i in range(rov - 1, -1, -1):
                matrix.append((j, i))
    return matrix

def calculate_seeds_to_plant(cov, rov,  pumpkin_counts):
    matrix = generate_matrix(cov, rov)
    seeds_to_plant = []
    for pos in matrix:
        j, i = pos
        seeds_to_plant.append(pumpkin_counts[j][i])
    return seeds_to_plant
