
import numpy as np
from .. import GeneticAlgorithm, utils, operators
from scipy.spatial.distance import cdist


class NSGA3(GeneticAlgorithm):
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
        name="NSGA3",
        show_bar=False,
        sim_req_cb=None,
        debug=False
    ):
        super(NSGA3, self).__init__(
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
        [Z, N] = utils.uniform_point(self.problem.pop_size, self.problem.n_obj)  # noqa: E501
        Z = np.where(Z != 0, Z, 1e-6)
        pop = self.problem.init_pop(N)
        self.cal_obj(pop)
        if np.sum(np.all(pop.cv <= 0, axis=1)) != 0:
            Zmin = np.min(pop[np.all(pop.cv <= 0, axis=1)].objv, axis=0)
        else:
            Zmin = []
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = utils.tournament_selection(
                2,
                N,
                np.sum(np.maximum(0, pop.cv), axis=1),  # noqa
            )  # noqa: E501
            offspring = operators.OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            # Zmin = np.min(pop(all(pop.cv <= 0, 2)).objv, [], axis=0)
            if len(Zmin) == 0 or np.sum(np.all(offspring.cv <= 0, axis=1)) == 0:  # noqa
                Zmin = []
            else:
                Zmin = np.min(
                    np.vstack((Zmin, offspring[np.all(offspring.cv <= 0, axis=1)].objv)),  # noqa: E501
                    axis=0,
                )  # noqa
            temp_pop = offspring + pop  # 合并种群
            pop = self._environmental_selection(
                temp_pop, N, Z, Zmin
            )
        return pop

    def _environmental_selection(self, pop, N, Z, Zmin):
        """
        The environmental selection of NSGA-III
        """
        if len(Zmin)==0:  # noqa
            Zmin = np.ones((1, Z.shape[1]))

        FrontNo, MaxFNo = utils.nd_sort(pop.objv, pop.cv, N)
        Next = FrontNo < MaxFNo

        Last = np.argwhere(FrontNo == MaxFNo).flatten()
        Choose = self.lastselection(
            pop[Next].objv, pop[Last].objv, N - np.sum(Next), Z, Zmin
        )
        Next[Last[Choose]] = True

        pop = pop[Next]
        return pop

    def lastselection(self, PopObj1, PopObj2, K, Z, Zmin):
        PopObj = np.vstack((PopObj1, PopObj2)) - Zmin
        N, M = PopObj.shape
        N1 = PopObj1.shape[0]
        N2 = PopObj2.shape[0]
        NZ = Z.shape[0]

        Extreme = np.zeros(M, dtype=int)
        w = np.zeros((M, M)) + 1e-6 + np.eye(M)
        for i in range(M):
            Extreme[i] = np.argmin(np.max(PopObj / w[i, :], axis=1)).flatten()
        if is_invertible(PopObj[Extreme, :]):
            Hyperplane = np.linalg.solve(PopObj[Extreme, :], np.ones((M, 1)))
        else:
            Hyperplane = np.nan
        a = 1 / (Hyperplane + 1e-6)
        if np.any(np.isnan(a)):
            a = np.max(PopObj, axis=0).T
        PopObj = PopObj / (a.T)
        cos = 1-cdist(PopObj, Z, "cosine")
        Distance = np.tile(np.sqrt(np.sum(PopObj ** 2, axis=1)), (NZ, 1)).T * np.sqrt(np.abs(1 - cos ** 2))  # noqa
        d = np.min(Distance.T, 0)
        pi = np.argmin(Distance.T, 0)
        # temp1, _ = np.histogram(tFrontNo, bins=np.arange(1, np.max(tFrontNo) + 2))  # noqa
        # rho = np.zeros(NZ)
        # for i in range(NZ):
        #     rho[i] = np.sum(pi[:N1] == i)
        rho, _ = np.histogram(pi[:N1], bins=np.arange(1, NZ + 2))  # noqa
        choose = np.zeros(N2)
        choose = choose.astype(bool)
        zchoose = np.ones(NZ)
        zchoose = zchoose.astype(bool)
        while np.sum(choose) < K:
            Temp = np.argwhere(zchoose == True).flatten()  # noqa
            Jmin = np.argwhere(rho[Temp] == np.min(rho[Temp])).flatten()
            j = Temp[Jmin[np.random.randint(len(Jmin))]]
            # Ia = np.ravel(np.array(np.where(pi[N1:] == j)))
            Ia = np.argwhere(np.logical_and(choose == False, pi[N1:] == j)).flatten()  # noqa
            # Ia = Ia[choose[Ia] == False]  # noqa
            # Ia = np.argwhere((choose == 0) & (pi[N1:] == j))[:, 0]
            if (Ia.shape[0] != 0):
                if (rho[j] == 0):
                    # if (rho[j] == 0):
                    s = np.argmin(d[N1 + Ia])
                else:
                    s = np.random.randint(Ia.shape[0])
                # a = Ia[s]
                choose[Ia[s]] = True
                rho[j] = rho[j] + 1
            else:
                zchoose[j] = False
        return choose


def is_invertible(a):
    return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]
