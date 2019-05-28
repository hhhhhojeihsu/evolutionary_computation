#!/usr/bin/env python
# coding: utf-8

import random

def fitness(individual, connection_matrix):
    '''
    This function return an integer of the fitness value for individual

        individual (1d list): list of nodes in an individual
        connection_matrix (2d list): The connection matrix that represents the network (square matrix)
    '''
    return min(connection_matrix[individual[i]][individual[i+1]] for i in range(len(individual)-1))

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

def crossover(chosen1, chosen2, cut_point1, cut_point2):
    '''
    This function will return 2 individual after crossover

        chosen1 (int): individual that is chosen as parent 1
        chosen2 (int): individual that is chosen as parent 2
        cut_point1 (int): location for the cut for individual 1
        cut_point2 (int): location for the cut for individual 2

        cut_point will represent the integer of the right of cutting location
        ex: 2
             |
        [0, 1, 2, 3]
    '''
    result1 = chosen1[:cut_point1] + chosen2[cut_point2:]
    result2 = chosen2[:cut_point2] + chosen1[cut_point1:]

    return result1, result2

def random_crossover(individual1, individual2, connection_matrix, ratio=0.9):
    '''
    This function return population after crossover is done

        chosen1 (int): individual that is chosen as parent 1
        chosen2 (int): individual that is chosen as parent 2
        connection_matrix (2d list): The connection matrix that represents the network (square matrix)
        ratio (float): probability of crossover occuring
    '''

    #Calculate all possible cut point
    max_possible = (len(individual1)-1) * (len(individual2)-1)

    if random.random() < ratio:
        #Check if cutting location is valid
        for i in range(100):
            cut_loc = random.randrange(0, max_possible)
            cut_point1 = cut_loc // (len(individual2)-1) + 1
            cut_point2 = cut_loc % (len(individual2)-1) + 1
            #print(max_possible, cut_loc, cut_point1, cut_point2)

            if(connection_matrix[individual1[cut_point1-1]][individual2[cut_point2]] == 0):
                continue
            if(connection_matrix[individual1[cut_point1]][individual2[cut_point2-1]] == 0):
                continue
            individual1, individual2 = crossover(individual1, individual2, cut_point1, cut_point2)
            break

    return individual1, individual2

#fitness([0, 1, 4], crossover_matrix)
#print(population_with_fitness([[0,1], [0,1,4]], crossover_matrix))
#crossover([1, 4], [0, 1, 5, 2], 1, 2)
#print(random_crossover([[1, 4], [0, 1, 5, 2]], crossover_matrix))

