import numpy as np
import random
from ..utils.uniform_point import uniform_point
from .. import GeneticAlgorithm, operators


class I_DBEA(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "constrained/none"
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="I_DBEA",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(I_DBEA, self).__init__(
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

    def run_algorithm(self):
        W, self.problem.pop_size = uniform_point(
            self.problem.pop_size, self.problem.n_obj)
        W = W / np.tile(np.sqrt(np.sum(W ** 2, axis=1,
                        keepdims=True)), (1, W.shape[1]))
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        z = np.min(pop.objv, axis=0)
        a = Intercepts(pop.objv)

        while self.not_terminal(pop):
            for i in range(self.problem.pop_size):
                Offspring = operators.OperatorGAhalf(
                    pop[i] + pop[np.random.randint(self.problem.pop_size)], self.problem)  # noqa
                self.cal_obj(Offspring)
                Feasible = np.all(pop.cv <= 0, axis=1)
                if ~np.all(Feasible) or ~np.any(np.all(pop[Feasible].objv <= np.tile(Offspring.objv, (np.sum(Feasible), 1)), axis=1)):  # noqa
                    List = random.sample(
                        np.arange(self.problem.pop_size).tolist(), self.problem.pop_size)  # noqa
                    List = np.array(List)
                    nPopObj = (pop[List].objv - np.tile(z, (self.problem.pop_size, 1))  # noqa
                               ) / np.tile(a - z, (self.problem.pop_size, 1))
                    nOffObj = (Offspring.objv - z) / (a - z)
                    normP = np.sqrt(np.sum(nPopObj ** 2, axis=1))
                    normO = np.sqrt(np.sum(nOffObj ** 2, axis=1))
                    CosineP = np.sum(nPopObj * W[List, :], axis=1) / normP
                    CosineO = np.sum(
                        np.tile(nOffObj, (self.problem.pop_size, 1)) * W[List, :], axis=1) / normO  # noqa
                    d1_old = normP * CosineP
                    d1_new = normO * CosineO
                    d2_old = normP * np.sqrt(1 - CosineP ** 2)
                    d2_new = normO * np.sqrt(1 - CosineO ** 2)
                    tmp = np.where(Offspring.cv < 0, 0, Offspring.cv)
                    CVO = np.sum(np.max(tmp))
                    tmp = np.where(pop[List].cv < 0, 0, pop[List].cv)
                    CV = np.sum(np.max(tmp, axis=1, keepdims=True), axis=1)
                    tau = np.mean(CV) * np.sum(CV == 0) / len(CV)
                    t1 = np.logical_and(d2_new == d2_old, d1_new < d1_old)
                    t2 = np.logical_or(d2_new < d2_old, t1)
                    t3 = np.logical_and(CVO < tau, CV < tau)
                    t4 = np.logical_or(t3, CVO == CV)
                    t5 = np.logical_and(t2, t4)
                    t6 = np.logical_and(CVO >= tau, CVO < CV)
                    replace = np.logical_or(t5, t6)
                    if len(np.argwhere(replace)) != 0:
                        pop[List[np.argwhere(replace)[0]]] = Offspring
                    a = Intercepts(pop.objv)
                    z = np.where(z < Offspring.objv, z,
                                 Offspring.objv).flatten()
        return pop


def Intercepts(pop_objv):
    N, M = pop_objv.shape
    Choosed = np.argmin(pop_objv, axis=0)
    L2NormABO = np.zeros(shape=(N, M))
    for i in range(M):
        L2NormABO[:, i] = np.sum(pop_objv[:, np.hstack(
            (np.arange(0, i), np.arange(i + 1, M)))] ** 2, axis=1)
    tmp = np.argmin(L2NormABO, axis=0)
    Choosed = np.hstack((Choosed, tmp))
    Extreme = np.argmax(pop_objv[Choosed, :], axis=0)
    Extreme = np.unique(Choosed[Extreme])
    if len(Extreme) < M:
        a = np.max(pop_objv, axis=0)
    else:
        try:
            Hyperplane = np.dot(np.linalg.inv(pop_objv[Extreme, :]), np.ones(shape=(M, 1)))  # noqa
        except:  # noqa
            print("警告: Singular matrix")   # noqa
            Hyperplane = np.dot(np.linalg.pinv(pop_objv[Extreme, :]), np.ones(shape=(M, 1)))  # noqa
        a = 1 / Hyperplane.T
    return a
