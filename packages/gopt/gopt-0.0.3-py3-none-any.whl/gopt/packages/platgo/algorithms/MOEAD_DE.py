import numpy as np
from scipy.spatial.distance import cdist
from ..GeneticAlgorithm import GeneticAlgorithm
from .. import utils, operators


class MOEAD_DE(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": "real",
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
        delta=0.9,
        nr=2,
    ):
        super(MOEAD_DE, self).__init__(
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
        self.delta = delta if delta is not None else 0.9
        self.nr = nr if nr is not None else 2

    def run_algorithm(self):
        W, N = utils.uniform_point(
            self.problem.pop_size, self.problem.n_obj)
        T = max(N//10, 2)
        B = cdist(W, W)
        B = np.argsort(B)
        B = B[:, :T]
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        Z = np.nanmin(pop.objv, axis=0)

        while self.not_terminal(pop):
            px = np.random.random(N)
            for i in range(N):
                if px[i] < self.delta:
                    p = B[i, np.random.permutation(B.shape[1])]
                else:
                    p = np.random.permutation(N)
                off = operators.OperatorDE(pop[i], pop[p][0], pop[p][1], self.problem)  # noqa
                self.cal_obj(off)
                Z = np.fmin(Z, off.objv)
                # Tchebycheff approch
                g_old = np.max(np.abs(pop[p].objv - Z) * W[p], axis=1)
                g_new = np.max(np.abs(off.objv - Z) * W[p], axis=1)
                pop[p[np.where(g_old >= g_new)[:self.nr]]] = off

        return pop
