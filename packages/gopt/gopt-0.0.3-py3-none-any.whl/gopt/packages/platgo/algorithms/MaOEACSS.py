
import numpy as np
import random
# from sympy import N
from gopt.packages.platgo.operators import OperatorGA
from scipy.spatial.distance import cdist
from .. import GeneticAlgorithm


class MaOEACSS(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": ""
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="MaOEACSS",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        t=0,
    ):
        super(MaOEACSS, self).__init__(
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
        self.t = t
        # self.xov = operators.XovSbx()  # 模拟二进制交叉
        # self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        Zmin = np.min(pop.objv, axis=0)
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = np.array(self.MatingSelection(pop.objv, Zmin), dtype=int)  # noqa
            offspring = OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            Zmin = np.min(np.vstack((Zmin, offspring.objv)), axis=0)
            temp_pop = offspring + pop  # 合并种群
            pop = self.EnvironmentalSelection(temp_pop, Zmin, self.t, self.problem.pop_size)  # noqa
        return pop

    # def cal_obj(self, pop):
    #     algo_router = AlgorithmRouter()

    #     algo_router.global_design_id += 1
    #     algo_router.add_algo(self)

    #     self.problem.cal_obj(pop)

    #     algo_router.delete_algo(algo_router.global_design_id)

    def MatingSelection(self, PopObj, Zmin):
        N = PopObj.shape[0]
        M = PopObj.shape[1]
        # Calculate the ASF value of each solution
        W = np.maximum(1e-6, PopObj/np.tile(np.sum(PopObj, axis=1),(M, 1)).T)  # noqa
        PopObj = PopObj - Zmin
        ASF = np.max(PopObj/W, axis=1)
        # Obtain the rank value of each solution's ASF value
        rank = np.argsort(ASF)
        ASFRank = np.argsort(rank)
        # Calculate the minimum angle of each solution to others
        cosine = 1 - cdist(PopObj, PopObj, 'cosine')
        Angle = np.arccos(cosine)
        Angle[np.eye(N, dtype=bool)] = np.inf
        Amin = np.min(Angle, axis=1)
        # Binary tournament selection
        matingpool = np.zeros((1, N), dtype=int)
        for i in range(N):
            p = np.random.permutation(N)[:2]
            if ASF[p[0]] < ASF[p[1]] and Amin[p[0]] > Amin[p[1]]:
                p = p[0]
            else:
                p = p[1]
            if random.random() < 1.0002 - ASFRank[p-1]/N:
                matingpool[0, i] = p
            else:
                matingpool[0, i] = random.randint(0, N-1)
        return matingpool

    def EnvironmentalSelection(self, pop, Zmin, t, K):
        # Calculate the distance between each solution to the ideal point
        PopObj = pop.objv - Zmin
        Con = np.sqrt(np.sum(PopObj**2, axis=1))
        # Calculate the angle between each two solutions
        cosine = 1 - cdist(PopObj, PopObj, 'cosine')
        Angle = np.arccos(cosine)
        Angle[np.eye(len(pop), dtype=bool)] = np.inf
        # Eliminate solutions one by one
        Remain = np.array(range(len(pop)))
        while len(Remain) > K:
            sortA = np.sort(Angle[Remain][:, Remain], axis=1)
            rank1 = np.argsort(Angle[Remain][:, Remain], axis=1)
            # rank2 = np.lexsort(np.fliplr(sortA).T)
            rank2 = np.argsort(sortA[:, 0], axis=0)
            A = rank2[0]
            B = rank1[A, 0]
            # Eliminate one of A and B
            if Con[Remain[A]] - Con[Remain[B]] > t:
                # Remain = np.delete(Remain, A-1)
                Remain = np.hstack((Remain[:A], Remain[A+1:]))
            elif Con[Remain[B]] - Con[Remain[A]] > t:
                Remain = np.hstack((Remain[:B], Remain[B+1:]))
            else:
                Remain = np.hstack((Remain[:A], Remain[A+1:]))
        # Population for next generation
        pop = pop[Remain]
        return pop
