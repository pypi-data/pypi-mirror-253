import numpy as np
from .. import GeneticAlgorithm, Population


class Adam(GeneticAlgorithm):
    type = {
        "n_obj": "single",
        "encoding": "real",
        "special": ""
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="Adam",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        alpha: int = 1,
        beta1: float = 0.9,
        beta2: float = 0.999
    ) -> None:

        super(Adam, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug
        )
        self.gk = None
        self.alpha = alpha
        self.beta1 = beta1
        self.beta2 = beta2

    def run_algorithm(self):
        """
         main function for Different Evolution
         if population is None, generate a new population with N
        :param N: population size
        :param population: population to be optimized
        :return:
        """
        pop = self.problem.init_pop(1)
        self.cal_obj(pop)
        m0 = np.zeros((1, self.problem.n_var))
        v0 = np.zeros((1, self.problem.n_var))
        k = 1
        while self.not_terminal(pop):
            gk = self.FiniteDifference(pop).T
            m = self.beta1 * m0 + (1 - self.beta1) * gk
            v = self.beta2 * v0 + (1 - self.beta2) * gk ** 2
            pop = Population(decs=pop.decs - self.alpha * (
                m / (1 - self.beta1 ** k)) / (np.sqrt(v / (1 - self.beta2 ** k)) + 1e-8))  # noqa
            self.cal_obj(pop)
            k += 1
        print(pop.objv)
        return pop

    def FiniteDifference(self, pop: Population) -> np.ndarray:
        # Estimate the gradient of objective by finite difference
        pop1 = Population(decs=pop.decs + np.eye(pop.decs.shape[1]) * 1e-4)
        self.cal_obj(pop1)
        df = (pop1.objv - pop.objv) / 1e-4
        return df
