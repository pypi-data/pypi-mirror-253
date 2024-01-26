import numpy as np
from scipy.spatial.distance import cdist

from gopt.packages.platgo.operators import OperatorGA
from .. import GeneticAlgorithm, utils


class KnEA(GeneticAlgorithm):
    type = {
        "n_obj": {"many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "constrained/none",
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="KnEA",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        rate=0.5,
    ):
        super(KnEA, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug,
        )
        self.rate = rate
        # self.xov = operators.XovSbx()  # 模拟二进制交叉
        # self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        frontno, _ = utils.nd_sort(pop.objv, pop.cv, np.inf)  # noqa: E501
        KneePoints = np.zeros(self.problem.pop_size, dtype=bool)
        r = -np.ones(2 * self.problem.pop_size)
        t = -np.ones(2 * self.problem.pop_size)
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = self.MatingSelection(pop.objv, frontno, KneePoints)
            offspring = OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            pop = offspring + pop  # 合并种群
            frontno, maxfront = utils.nd_sort(
                pop.objv, pop.cv, self.problem.pop_size
            )  # noqa: E501
            KneePoints, Distance, r, t = self.FindKneePoints(
                pop.objv, frontno, maxfront, r, t, self.rate
            )  # noqa
            pop, frontno, KneePoints = self._environmental_selection(
                pop,
                frontno,
                maxfront,
                KneePoints,
                Distance,
                self.problem.pop_size,
            )  # noqa
        return pop

    def _environmental_selection(
        self, pop, frontno, maxfront, KneePoints, Distance, K
    ):  # noqa
        """
        The environmental selection of KnEA
        """
        # Select the solutions in the first several fronts
        Next = frontno < maxfront
        # Select all the knee points in the last front
        Next[KneePoints] = True
        # Delete or add solutions to make a total of K solutions be chosen in the last front  # noqa
        if np.sum(Next) < K:
            Temp = np.argwhere(
                np.logical_and(frontno == maxfront, KneePoints == False)  # noqa
            ).flatten()  # noqa
            Rank = np.argsort(-Distance[Temp])
            Next[Temp[Rank[0: (K - np.sum(Next))]]] = True  # noqa
        elif np.sum(Next) > K:
            Temp = np.argwhere(
                np.logical_and(frontno == maxfront, KneePoints == True)  # noqa
            ).flatten()  # noqa
            Rank = np.argsort(Distance[Temp])
            Next[Temp[Rank[0: (np.sum(Next) - K)]]] = False  # noqa
        # Population for next generation
        pop = pop[Next]
        frontno = frontno[Next]
        KneePoints = KneePoints[Next]
        return pop, frontno, KneePoints

    def MatingSelection(self, PopObj, frontno, KneePoints):
        # Calculate the weighted distance of each solution
        Dis = cdist(PopObj, PopObj)
        Dis[np.eye(len(Dis), dtype=bool)] = np.inf
        Dis = np.sort(Dis, axis=0)
        temp1 = np.array([3, 2, 1])
        temp2 = np.tile(temp1, (PopObj.shape[0], 1)).T
        Crowd = np.sum(Dis[0:3, :] * temp2, axis=0)
        # Binary tournament selection
        matingpool = utils.tournament_selection(
            2, PopObj.shape[0], frontno, ~KneePoints, -Crowd
        )  # noqa: E501
        return matingpool

    def FindKneePoints(self, PopObj, frontno, maxfront, r, t, rate):
        N = PopObj.shape[0]
        M = PopObj.shape[1]
        KneePoints = np.zeros(N, dtype=bool)
        Distance = np.zeros(N)
        for i in range(1, maxfront + 1):
            Current = np.argwhere(frontno == i).flatten()
            if len(Current) <= M:
                KneePoints[Current] = True
            else:
                # Find the extreme points
                Rank = np.argsort(-PopObj[Current, :], axis=0)
                Extreme = np.zeros(M, dtype=int)
                Extreme[0] = Rank[0, 0]
                for j in range(1, len(Extreme)):
                    k = 0
                    Extreme[j] = Rank[k, j]
                    while Extreme[j] in Extreme[0:j]:
                        k = k + 1
                        Extreme[j] = Rank[k, j]
                # Calculate the hyperplane
                temp = PopObj[Current[Extreme], :]
                try:
                    Hyperplane = np.linalg.solve(temp, np.ones((len(Extreme), 1)))  # noqa
                except:  # noqa
                    print("警告: 矩阵接近奇异值，或者缩放错误。结果可能不准确")
                    Hyperplane = np.dot(np.linalg.pinv(temp), np.ones((len(Extreme), 1)))  # noqa
                # Calculate the distance of each solution to the hyperplane
                temp1 = (np.dot(PopObj[Current, :], Hyperplane) - 1).flatten()
                temp2 = np.sqrt(np.sum(Hyperplane ** 2))
                Distance[Current] = -temp1 / temp2
                # Update the range of neighbourhood
                Fmax = np.max(PopObj[Current, :], axis=0)
                Fmin = np.min(PopObj[Current, :], axis=0)
                if t[i - 1] == -1:
                    r[i - 1] = 1
                else:
                    r[i - 1] = r[i - 1] / np.exp((1 - t[i - 1] / rate) / M)
                R = (Fmax - Fmin) * r[i - 1]
                # Select the knee points
                Rank = np.argsort(-Distance[Current])
                Choose = np.zeros(len(Rank))
                Remain = np.ones(len(Rank))
                for j in Rank:
                    if Remain[j]:
                        for k in range(len(Current)):
                            if np.all(
                                np.abs(
                                    PopObj[Current[j], :]
                                    - PopObj[Current[k], :]
                                )
                                <= R
                            ):  # noqa
                                Remain[k] = 0
                        Choose[j] = 1
                t[i - 1] = np.sum(Choose) / len(Current)
                temp3 = np.argwhere(Choose[Rank] == 1).flatten()[-1]
                Choose[Rank[temp3]] = 0
                KneePoints[Current[Choose == 1]] = True
        return KneePoints, Distance, r, t


def is_invertible(a):
    return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]
