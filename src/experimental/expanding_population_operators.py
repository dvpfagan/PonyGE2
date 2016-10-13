from algorithm.parameters import params
from random import sample
from copy import copy

def dave_selection(population):
    """Given an entire population, draw <tournament_size> competitors
    randomly and return the best."""

    tournament_size = params['TOURNAMENT_SIZE']
    winners = []
    gen_size = len(population)
    if params['INVALID_SELECTION']:
        available = population
    else:
        available = [i for i in population if not i.invalid]
    while len(winners) < gen_size:
        competitors = sample(available, tournament_size)
        competitors.sort(reverse=True)
        winners.append(competitors[0])
    return winners

#Will need to add stuff to operators etc to build this.
def dave_replacement(new_pop, individuals):
    """Return new pop. The ELITE_SIZE best individuals are appended
    to new pop if they are better than the worst individuals in new
    pop"""

    if (len(individuals)+len(new_pop)) > 10000:
        for ind in individuals:
            new_pop.append(copy(ind))
        new_pop.sort(reverse=True)
        #Need diversity measure here for pop
        print("Population is now reset to 500")
        return new_pop[:500]
    else:
        print(len(individuals), " inds ", len(new_pop), "new pop")
        for ind in individuals:
            new_pop.append(copy(ind))
        new_pop.sort(reverse=True)
        print("Population is now ", len(new_pop))
        return new_pop