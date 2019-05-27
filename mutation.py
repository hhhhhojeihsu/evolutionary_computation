def mutation(neighbor_matrix, ind):
    # supposed individual is a list
    position = random.randint(1, len(ind)-2)
    prev_pos = ind[position-1]-1
    next_pos = ind[position+1]-1
    intersection = list(set(neighbor_matrix[prev_pos]) & set(neighbor_matrix[next_pos]))
    ind[position] = random.sample(intersection, 1)[0]+1
    return ind

#mutation(neighbor_matrix, [1, 3, 4])
