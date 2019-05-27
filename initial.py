class Population:
    """Class of population that includes all the individuals

    Attributes:
        connection_matrix (2d list): The connection matrix that represents the network. Must be square matrix.
        source (int): The index(zero-based numbering) indicate the starting point of the path.
        dest (int): The index(zero-based numbering) indicate the ending point of the path.
        iddfs_depth (int): The maximum depth of IDDFS.
        population_size (int): How many individuals should the function return.
        max_individual_size (int): The path should not be larger than this value.
    """

    def __init__(self, connection_matrix, source, dest, iddfs_depth, population_size, max_individual_size):
        self.connection_matrix = connection_matrix
        self.source = source
        self.dest = dest
        self.iddfs_depth = iddfs_depth
        self.population_size = population_size
        self.max_individual_size = max_individual_size

        # Populate each individaul
        for i in range(self.population_size):
            Individual(connection_matrix, source, dest, max_individual_size)

class Individual:
    """Class of individual that initialize using run iddfs and random search

    Attributes:
        connection_matrix (2d list): The connection matrix that represents the network. Must be square matrix.
        source (int): The index(zero-based numbering) indicate the starting point of the path.
        dest (int): The index(zero-based numbering) indicate the ending point of the path.
        max_individual_size (int): The path should not be larger than this value.
    """

    def __init__(self, connection_matrix, source, dest, max_individual_size):
        # Set variables
        self.source = source
        self.dest = dest
        self.max_individual_size = max_individual_size

    def random_search(self):
        pass

def initial(connection_matrix, source, dest, iddfs_depth, population_size, max_individual_size):
    """Initialize the population with given network and return in 2d list

    The path return will not contain cycle
Args: connection_matrix (2d list): The connection matrix that represents the network. Must be square matrix.
        source (int): The index(zero-based numbering) indicate the starting point of the path.
        dest (int): The index(zero-based numbering) indicate the ending point of the path.
        iddfs_depth (int): The maximum depth of IDDFS.
        population_size (int): How many individuals should the function return.
        max_individual_size (int): The path should not be larger than this value.

    Returns:
        2d list: Each element is a variable lengthed path.

    """

    return Population(connection_matrix, source, dest, iddfs_depth, population_size, max_individual_size)

