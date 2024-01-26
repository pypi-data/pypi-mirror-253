import numpy as np
from ...common.commons import AlgoMode
from .. import GeneticAlgorithm, operators
from ..Population import Population
from ..utils.fitness_single import fitness_single


class FEP(GeneticAlgorithm):
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
        name="FEP",
        show_bar=False,
        sim_req_cb=None,
        algo_mode=AlgoMode.ACADEMIC,
        debug=False,
    ):
        super(FEP, self).__init__(
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

    def run_algorithm(self):
        """
         main function for Different Evolution
         if population is None, generate a new population with N
        :param N: population size
        :param population: population to be optimized
        :return:
        """
        pop = self.problem.init_pop()
        self.cal_obj(pop)

        while self.not_terminal(pop):
            offspring, OffEta = operators.OperatorFEP(pop)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            pop = offspring + pop
            # Fit = self.fitness_single(temp_pop)
            Fit = fitness_single(pop)
            Win = np.zeros((1, np.shape(pop)[0]))
            for i in range(np.shape(pop)[0]):
                Win[:, i] = np.sum(Fit[i] <= Fit[np.random.permutation(10)])
            rank = np.argsort(-Win)
            poprank = rank[0, 0: self.problem.pop_size]
            pop = pop[poprank]
        return pop

    def fitness_single(self, pop: Population):
        pop_con = np.sum(np.where(pop.cv < 0, 0, pop.cv), axis=1)
        feasible = pop_con <= 0
        fitness = feasible * pop.objv + ~feasible * (pop_con + 1e10)
        return fitness
