import numpy as np
from ...common.commons import AlgoMode
from .. import GeneticAlgorithm
from ..Population import Population
from ..utils.fitness_single import fitness_single
# import os
# import scipy.io as sio


class CSO(GeneticAlgorithm):
    type = {
        "n_obj": "single",
        "encoding": "real",
        "special": {"constrained/none", "large/none"},
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="CSO",
        show_bar=False,
        sim_req_cb=None,
        algo_mode=AlgoMode.ACADEMIC,
        debug=False,
    ):
        super(CSO, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            algo_mode=algo_mode,
            debug=debug,
        )
        self.phi = 0.1

    def run_algorithm(self):
        # load_fn = os.path.join(
        #     os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        #     "algorithms/matlab.mat",
        # )
        # load_data = sio.loadmat(load_fn)
        # R = load_data["R"]
        """
         main function for Different Evolution
         if population is None, generate a new population with N
        :param N: population size
        :param population: population to be optimized
        :return:
        """
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        self.adds = np.zeros((self.problem.pop_size, self.problem.n_var))
        his = self.problem.init_pop(0)
        while self.not_terminal(pop):
            rank = np.random.permutation(pop.pop_size)
            loser = rank[0: pop.pop_size // 2]
            winner = rank[pop.pop_size // 2: pop.pop_size]
            # replace = self.fitness_single(pop[loser]) < self.fitness_single(
            #     pop[winner]
            # )
            replace = fitness_single(pop[loser]) < fitness_single(pop[winner])
            # temp = loser[replace[0]]
            # loser[replace[0]] = winner[replace[0]]
            # winner[replace[0]] = temp
            temp = loser[replace]
            loser[replace] = winner[replace]
            winner[replace] = temp

            LoserDec = pop[loser].decs

            WinnerDec = pop[winner].decs
            LoserVel = self.adds[loser]
            R1 = np.tile(
                np.random.rand(pop.pop_size // 2, 1), (1, self.problem.n_var)
            )
            R2 = np.tile(
                np.random.rand(pop.pop_size // 2, 1), (1, self.problem.n_var)
            )
            R3 = np.tile(
                np.random.rand(pop.pop_size // 2, 1), (1, self.problem.n_var)
            )

            # LoserVel = load_data["LoserVel"]
            # WinnerDec = load_data["WinnerDec"]
            # LoserDec = load_data["LoserDec"]
            # R1 = load_data["R1"]
            # R2 = load_data["R2"]
            # R3 = load_data["R3"]
            # popdecs = load_data["popdecs"]
            # LoserVel = (
            #     R1 * LoserVel
            #     + R2 * (WinnerDec - LoserDec)
            #     + self.phi
            #     * R3
            #     * (
            #         np.tile(np.mean(popdecs, axis=0), (pop.pop_size // 2, 1))
            #         - LoserDec
            #     )
            # )
            LoserVel = (
                R1 * LoserVel
                + R2 * (WinnerDec - LoserDec)
                + self.phi
                * R3
                * (
                    np.tile(np.mean(pop.decs, axis=0), (pop.pop_size // 2, 1))
                    - LoserDec
                )
            )
            LoserDec = LoserDec + LoserVel
            pop[loser] = Population(decs=LoserDec)
            self.cal_obj(pop)
            self.adds[loser] = LoserVel
            bestindex = np.argmin(pop.objv)
            if his.pop_size == 0:
                his = pop[np.int(bestindex)]
            else:
                if his.objv > np.min(pop.objv):
                    his = pop[np.int(bestindex)]
                else:
                    rand = np.int(np.random.rand(1) * self.problem.pop_size)
                    pop[rand] = his
            # if self._gen > 9900:
            #     CSO = 1
        return pop

    # def fitness_single(self, pop: Population):
    #     pop_con = np.sum(np.where(pop.cv < 0, 0, pop.cv), axis=1)
    #     feasible = pop_con <= 0
    #     fitness = feasible * pop.objv + ~feasible * np.all(pop_con + 1e10)
    #     return fitness
