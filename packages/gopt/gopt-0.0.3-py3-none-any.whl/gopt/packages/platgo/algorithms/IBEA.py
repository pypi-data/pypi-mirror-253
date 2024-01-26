import numpy as np

from ..GeneticAlgorithm import GeneticAlgorithm
from .. import utils, operators


class IBEA(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": ""
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        simulation_request_callback,
        max_fe=10000,
        name=None,
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        kappa=0.05
    ):

        super(IBEA, self).__init__(
            pop_size,
            options,
            optimization_problem,
            simulation_request_callback,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug
        )
        self.kappa = kappa

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)

        while self.not_terminal(pop):
            matingpool = utils.tournament_selection(2, self.problem.pop_size, -self._cal_fitness(pop.objv, self.kappa)[0])  # noqa
            off = operators.OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(off)
            pop = self._environmental_selection(pop+off, self.problem.pop_size, self.kappa)  # noqa
        return pop

    def _cal_fitness(self, objv, kappa):
        N = objv.shape[0]
        objv = (objv-np.min(objv, axis=0))/(np.max(objv, axis=0)-np.min(objv, axis=0))  # noqa
        temp = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                temp[i, j] = np.max(objv[i]-objv[j])

        c = np.max(np.abs(temp), axis=0)
        fitness = np.sum(-np.exp(-temp/c/kappa), axis=0) + 1

        return fitness, temp, c

    def _environmental_selection(self, pop, N, kappa):
        next = list(range(len(pop)))
        fitness, temp, c = self._cal_fitness(pop.objv, kappa)
        while len(next) > N:
            x = np.argmin(fitness[next])

            fitness = fitness + np.exp(-temp[next[x]]/c[next[x]]/kappa)
            if x == len(pop)-1:
                next = next[:x]
            else:
                next = next[:x] + next[x+1:]

        pop = pop[next]

        return pop
