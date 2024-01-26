
import numpy as np
from ..GeneticAlgorithm import GeneticAlgorithm
from ..operators.OperatorGAhalf import OperatorGAhalf
from ..utils.uniform_point import uniform_point
from scipy.spatial.distance import cdist


class MOEADDU(GeneticAlgorithm):
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
        simulation_request_callback,
        max_fe=10000,
        delta=0.9,
        K=5,
        name="MOEADDRA",
        show_bar=False,
        sim_req_cb=None,
        debug=False
    ):
        super(MOEADDU, self).__init__(
            pop_size,
            options,
            optimization_problem,
            simulation_request_callback,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug
        )
        self.delta = delta
        self.K = K
        # self.xov = pg.operators.XovSbx(half=True)  # 模拟二进制交叉
        # self.mut = pg.operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        W, N = uniform_point(
            self.problem.pop_size, self.problem.n_obj)
        W = np.where(W != 0, W, 1e-6)
        T = int(np.ceil(N / 10))
        B = cdist(W, W)
        B = np.argsort(B, axis=1)
        B = B[:, :T]
        # Generate random population
        pop = self.problem.init_pop(N)
        self.cal_obj(pop)
        z = np.nanmin(pop.objv, axis=0)
        znad = np.nanmax(pop.objv, axis=0)
        # Optimization
        while self.not_terminal(pop):
            _, z, znad = self.Normalization(pop.objv, z, znad)
            for i in range(N):
                # Choose the parent
                if np.random.random() < self.delta:
                    P = B[i, np.random.randint(B.shape[1])]
                else:
                    P = np.random.randint(N)
                # Generate an offspring
                a = int(i)
                temp = np.hstack((a, P))
                off = OperatorGAhalf(pop[temp], self.problem)
                self.cal_obj(off)
                temp = 1 - cdist(off.objv, W, "cosine")
                rank = np.argsort(-temp).flatten()
                P = rank[:self.K]
                # Update the K nearest parents by modified Tchebycheff approach
                g_old = np.max(np.abs(pop[P].objv - z) / (znad - z) / W[P, :], axis=1).flatten()  # noqa
                g_new = np.max(np.abs(off.objv - z) / (znad - z) / W[P, :], axis=1).flatten()  # noqa
                temp2 = np.argwhere(g_old >= g_new).flatten()[:1]
                pop[P[temp2]] = off
        return pop

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
        extreme = np.argmin(ASF, axis=0)
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
