"""
------------------------------- Reference -----------------------------
 K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, A fast and elitist
 multiobjective genetic algorithm: NSGA-II, IEEE Transactions on
 Evolutionary Computation, 2002, 6(2): 182-197.
"""

# from math import ceil, gamma
from operator import mod

# from argon2 import Parameters
# from matplotlib.pyplot import axis
import numpy as np

# from sklearn.model_selection import ParameterSampler
# from sympy import CoercionFailed
# from gopt.packages.platgo.Problem import Problem
from gopt.packages.platgo.operators import OperatorGA
from scipy.spatial.distance import cdist
from .. import GeneticAlgorithm, utils


class RVEAa(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": {"constrained/none"}
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="RVEAa",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        alpha=2,
        fr=0.1,
    ):
        super(RVEAa, self).__init__(
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
        self.alpha = alpha
        self.fr = fr
        # self.xov = operators.XovSbx()  # 模拟二进制交叉
        # self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        # Generate the reference points and random population
        [V0, N] = utils.uniform_point(
            self.problem.pop_size, self.problem.n_obj
        )  # noqa: E501
        V0 = np.where(V0 != 0, V0, 1e-6)
        pop = self.problem.init_pop(N)
        self.cal_obj(pop)
        temp = np.random.random((N, self.problem.n_obj))
        V1 = np.vstack((V0, temp))
        V = V1.copy()
        # Optimization
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = np.random.randint(0, len(pop), (1, N))
            offspring = OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            temp_pop = offspring + pop  # 合并种群
            pop = self.EnvironmentalSelection(
                temp_pop, V, (self._gen / self._max_fe) ** self.alpha
            )  # noqa
            tempa = int(np.ceil(self._gen / N))
            tempb = int(np.ceil(self.fr * self._max_fe / N))
            if not mod(tempa, tempb):
                V[0:N, :] = self.ReferenceVectorAdaptation(pop.objv, V0)  # noqa
            V[N+1:, :] = self.ReferenceVectorRegeneration(pop.objv, V[N+1:, :])  # noqa
            if self._gen >= self._max_fe:
                pop = self.Truncation(pop, N)
        return pop

    def EnvironmentalSelection(self, Pop, V, theta):
        # self.cal_obj(Pop)
        PopObj = Pop.objv
        N, M = PopObj.shape
        NV = V.shape[0]

        """Translate the Pop"""
        PopObj = PopObj - np.tile(np.min(PopObj, axis=0), (N, 1))

        """Calculate the degree of violation of each solution"""
        CV = np.sum(np.maximum(0, Pop.cv), axis=1)

        """Calculate the smallest angle value between each vector and others"""
        cosine = 1 - cdist(V, V, "cosine")
        cosine[np.eye(len(cosine), dtype=bool)] = 0
        gamma = np.min(np.arccos(cosine), axis=1)

        """Associate each solution to a reference vector"""
        Angle = np.arccos(1 - cdist(PopObj, V, "cosine"))
        associate = np.argmin(Angle, axis=1).flatten()

        """Select one solution for each reference vector"""
        Next = np.zeros(NV, dtype=int)
        for i in np.unique(associate):
            current1 = np.argwhere(np.logical_and(associate == i, CV == 0)).flatten()  # noqa
            current2 = np.argwhere(np.logical_and(associate == i, CV != 0)).flatten()  # noqa
            if len(current1) != 0:
                # Calculate the APD value of each solution
                APD = (
                    1 + M * theta * Angle[current1, i] / (gamma[i] + 1e-6)  # noqa
                ) * np.sqrt(np.sum(PopObj[current1, :] ** 2, axis=1))
                # Select the one with the minimum APD value
                best = np.argmin(APD).flatten()
                Next[i] = current1[best]
            elif len(current2) != 0:
                # Select the one with the minimum CV value
                best = np.argmin(CV[current2]).flatten()
                Next[i] = current2[best]
        # Pop for next generation
        Pop = Pop[Next[Next != 0]]
        return Pop

    def ReferenceVectorAdaptation(self, PopObj, V):
        temp = np.max(PopObj, axis=0) - np.min(PopObj, axis=0)
        # tempa = np.tile(temp, (V.shape[0], 1))
        V = V * temp
        return V

    def ReferenceVectorRegeneration(self, PopObj, V):
        PopObj = PopObj - np.min(PopObj, axis=0)
        tempa = 1 - cdist(PopObj, V, "cosine")
        associate = np.argmax(tempa, axis=1).flatten()
        inValid = np.setdiff1d(np.array(range(V.shape[0])), associate)
        tempb = np.random.random((len(inValid), V.shape[1]))
        V[inValid-1, :] = tempb * np.max(PopObj, axis=0)
        return V

    def Truncation(self, pop, N):
        # self.cal_obj(pop)
        Choose = np.ones(len(pop), dtype=bool)
        cos = 1-cdist(pop.objv, pop.objv, "cosine")
        cos1 = np.eye(len(cos), dtype=bool)
        cos[cos1] = 0
        while sum(Choose) > N:
            Remain = np.argwhere(Choose).flatten()
            temp = np.sort(-cos[Remain][:, Remain], axis=1)
            Rank = np.lexsort(np.fliplr(temp).T)
            # Rank = np.argsort(temp1, axis=1).flatten()
            Choose[Remain[Rank[1]]] = False
        pop = pop[Choose]
        return pop
