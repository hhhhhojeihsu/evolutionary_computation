def fitness(individual, connection_matrix):
    '''
    This function return an integer of the fitness value for individual

        individual (1d list): list of nodes in an individual
        connection_matrix (2d list): The connection matrix that represents the network (square matrix)
    '''
    return min(connection_matrix[individual[i]-1][individual[i+1]-1] for i in range(len(individual)-1))

def population_with_fitness(population, connection_matrix):
    '''
    This function will return population with each individuals fitness
    Format:
    [
        { 'individual': [], 'fitness': int }, ...
    ]

        population (2d list): population for the given network
        connection_matrix (2d list): The connection matrix that represents the network (square matrix)
    '''
    return list({'individual':individual, 'fitness':fitness(individual, connection_matrix)}
                for individual in population)

def check_cycle(path):
    '''Check path contains cycle or not
    
    Assume source and destination is not the same
    
    Arguments:
        path (list): A list contains all the verticies sequences
    Return:
        cycle (list):
            - A list contains the path without all the loops
            - An empty list if the path does not contain any loop
    '''
    
    # If there's a vertex appear more then one time, there's bound to be a loop
    if(len(path) == len(set(path))):
        return []
    
    # Get rid of cycle
    vertex_dict = {}
    path_ = path
    idx_start = 0
    while(True):
        for idx, vertex in enumerate(path_[idx_start:]):
            idx_ = idx + idx_start
            if(idx_ == len(path_) - 1):
                if path_[-1] == path_[-2]:
                    return path_[:-1]
                return path_
            if vertex not in vertex_dict:
                vertex_dict[vertex] = idx_
            # cycle detected
            else:
                cycle_start = vertex_dict[vertex] + 1
                # Remove vertices in cycle from dict
                for vertex_del in path_[cycle_start:idx_]:
                    del vertex_dict[vertex_del]
                path_ = path_[:cycle_start] + path_[idx_ + 1:]
                idx_start = cycle_start
                break
    