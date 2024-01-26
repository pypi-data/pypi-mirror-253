"""
------------------------------- Reference -----------------------------
 K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, A fast and elitist
 multiobjective genetic algorithm: NSGA-II, IEEE Transactions on
 Evolutionary Computation, 2002, 6(2): 182-197.
"""

import numpy as np
from scipy.spatial.distance import cdist
from .. import GeneticAlgorithm, utils, operators


class tDEA(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"},  # noqa
        "special": ""
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="tDEA",
        show_bar=False,
        sim_req_cb=None,
        debug=False
    ):
        super(tDEA, self).__init__(
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
        # self.xov = operators.XovSbx()  # 模拟二进制交叉
        # self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        [W, N] = utils.uniform_point(self.problem.pop_size, self.problem.n_obj)  # noqa: E501
        W = np.where(W != 0, W, 1e-6)
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        z = np.min(pop.objv, axis=0)
        znad = np.max(pop.objv, axis=0)
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = np.random.randint(0, pop.pop_size, (1, pop.pop_size))  # noqa
            offspring = operators.OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            temp_pop = offspring + pop  # 合并种群
            pop, z, znad = self._environmental_selection(temp_pop, W, N, z, znad)  # noqa
            # if(self._max_fe == 100):
            #     print(pop.pop_size)
        return pop

    def _environmental_selection(self, pop, W, N, z, znad):
        """
        The environmental selection of theta-DEA
        """
        frontno, maxfront = utils.nd_sort(
                pop.objv, N
            )  # noqa: E501
        st = np.argwhere(frontno <= maxfront).flatten()
        # Normalization
        PopObj, z, znad = self.Normalization(pop[st].objv, z, znad)
        # theta-non-dominated sorting
        tFrontNo = self.tNDSort(PopObj, W)
        # Selection
        temp1, _ = np.histogram(tFrontNo, bins=np.arange(1, np.max(tFrontNo) + 2))  # noqa
        temp2 = np.cumsum(temp1)
        maxfront = np.argwhere(temp2 >= N).flatten()[0]
        LastFront = np.argwhere(tFrontNo == (maxfront+1)).flatten()
        LastFront = LastFront[np.random.permutation(len(LastFront))]
        temp3 = np.sum(tFrontNo <= (maxfront+1)) - N
        # print(temp3)
        if(temp3 > 0):
            temp4 = np.array(range(temp3))
            # tFrontNo = np.array(tFrontNo, dtype=float)
            tFrontNo[LastFront[temp4]] = np.inf
        Next = st[tFrontNo <= (maxfront+1)]
        pop = pop[Next]
        return pop, z, znad

    def Normalization(self, PopObj, z, znad):
        N = PopObj.shape[0]
        M = PopObj.shape[1]
        # Update the ideal point
        z = np.minimum(z, np.min(PopObj, axis=0))
        # # Update the nadir point
        # Identify the extreme points
        W = np.zeros((M, M)) + 1e-6
        W[np.eye(M, dtype=bool)] = 1
        ASF = np.zeros((N, M))
        for i in range(M):
            temp1 = np.abs((PopObj - z)/(znad - z))
            ASF[:, i] = np.max(temp1/W[i, :], axis=1)
        extreme = np.argmin(ASF, axis=0).flatten()
        # Calculate the intercepts
        temp = PopObj[extreme, :] - np.tile(z, (M, 1))
        Hyperplane = np.linalg.solve(temp, np.ones((M, 1)))
        a = (1/Hyperplane).T + z
        if np.any(np.isnan(a)) or np.any(a <= z):
            a = np.max(PopObj, axis=0)
        znad = a
        # Normalize the population
        PopObj = (PopObj - z)/(znad - z)
        return PopObj, z, znad

    def tNDSort(self, PopObj, W):
        N = PopObj.shape[0]
        NW = W.shape[0]
        # Calculate the d1 and d2 values for each solution to each weight
        normP = np.sqrt(np.sum(PopObj**2, axis=1))
        cos = 1 - cdist(PopObj, W, "cosine")
        temp = np.tile(normP, (W.shape[0], 1)).T
        d1 = temp * cos
        d2 = temp * np.sqrt(1 - cos**2)
        # Clustering
        class1 = np.argmin(d2, axis=1)
        # Sort
        theta = (np.zeros((1, NW)) + 5)[0]
        theta[np.sum(W > 1e-4, axis=1) == 1] = 1e6
        # tFrontNo = np.zeros((1, N), dtype=int).flatten()
        tFrontNo = np.zeros((1, N)).flatten()
        for i in range(NW):
            C = np.argwhere(class1 == i).flatten()
            if len(C) != 0:
                tempa = d1[C, i] + theta[i]*d2[C, i]
                rank = np.argsort(tempa, axis=0).flatten()
                tFrontNo[C[rank]] = np.array(range(1, len(C)+1))
        return tFrontNo
