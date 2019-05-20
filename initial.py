

def initial(connection_matrix, source, dest, iddfs_depth, population_size, max_individual_size):
    """Initialize the population with given network and return in 2d list

    The path return will not contain cycle

    Args:
        connection_matrix (2d list): The connection matrix that represents the network. Must be square matrix.
        source (int): The index(zero-based numbering) indicate the starting point of the path.
        dest (int): The index(zero-based numbering) indicate the ending point of the path.
        iddfs_depth (int): The maximum depth of IDDFS.
        population_size (int): How many individuals should the function return.
        max_individual_size (int): The path should not larger than this value.

    Returns:
        2d list: Each element is a variable lengthed path.

    """
    pass
