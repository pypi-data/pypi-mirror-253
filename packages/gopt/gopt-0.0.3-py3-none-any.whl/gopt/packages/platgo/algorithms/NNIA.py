import numpy as np
from ..GeneticAlgorithm import GeneticAlgorithm
from .. import utils, operators


class NNIA(GeneticAlgorithm):
    type = {
        "n_obj": "multi",
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
        nA=20,
        nC=100,
    ):
        super(NNIA, self).__init__(
            pop_size,
            options,
            optimization_problem,
            simulation_request_callback,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug,
        )
        self.nA = nA
        self.nC = nC

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        D = self._update_domi_pop(pop, self.problem.pop_size)

        while self.not_terminal(D):
            # get active pop
            A = D[:min(self.nA, len(D))]
            # get clone pop
            C = self._cloning(A, self.nC)
            idx = np.random.randint(len(A), size=len(C))
            temp_pop = C + A[idx]
            C1 = operators.OperatorGAhalf(temp_pop, self.problem)
            self.cal_obj(C1)
            # [C,A(randi(length(A),1,length(C)))]
            D = self._update_domi_pop(D+C1, self.problem.pop_size)

        return pop

    def _update_domi_pop(self, D, N):
        idx, _ = utils.nd_sort(D.objv, len(D))
        D = D[idx == 1]
        # TODO descend
        rank = np.argsort(-utils.crowding_distance(D))
        D = D[rank[:min(N, len(rank))]]
        return D

    def _cloning(self, A, nC):
        cd = utils.crowding_distance(A)
        if np.all(cd == np.inf):
            cd = np.ones(len(cd))
        else:
            cd[cd == np.inf] = 2 * max(cd[cd != np.inf])
        q = nC*cd//np.sum(cd)
        C = None
        for i in range(len(A)):
            temp_pop = None
            for j in range(int(q[i])):
                if j == 0:
                    temp_pop = A[i]
                else:
                    temp_pop = temp_pop + A[i]
            if temp_pop is None:
                continue
            if C is None:
                C = temp_pop
            else:
                C = C + temp_pop
        return C
