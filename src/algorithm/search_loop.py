from algorithm.parameters import params
from fitness.evaluation import evaluate_fitness
from stats.stats import stats, get_stats


def search_loop():
    """
    This is a standard search process for an evolutionary algorithm. Loop over
    a given number of generations.
    
    :return: The final population after the evolutionary process has run for
    the specified number of generations.
    """

    # Initialise population
    individuals = params['INITIALISATION'](params['POPULATION_SIZE'])

    # Evaluate initial population
    individuals = evaluate_fitness(individuals)

    # Generate statistics for run so far
    get_stats(individuals)

    # Traditional GE
    for generation in range(1, (params['GENERATIONS']+1)):
        stats['gen'] = generation

        # New generation
        individuals = params['STEP'](individuals)

        # Generate statistics for run so far
        get_stats(individuals)

    return individuals
