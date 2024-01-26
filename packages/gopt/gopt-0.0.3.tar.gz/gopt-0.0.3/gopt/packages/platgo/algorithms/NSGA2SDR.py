
import numpy as np
from scipy.spatial.distance import cdist
from .. import GeneticAlgorithm, utils, operators


class NSGA2SDR(GeneticAlgorithm):
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
        name="NSGA2SDR",
        show_bar=False,
        sim_req_cb=None,
        debug=False
    ):
        super(NSGA2SDR, self).__init__(
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
        self.xov = operators.XovSbx()  # 模拟二进制交叉
        self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        zmin = np.min(pop.objv, 0)
        zmax = np.max(pop.objv, 0)
        _, frontno, cd = self._EnvironmentalSelection(
            pop, self.problem.pop_size, zmin, zmax
        )  # noqa: E501 第一次用_,接收pop是因为初始种群保留
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = utils.tournament_selection(
                2, pop.pop_size, frontno, -cd
            )  # noqa: E501
            p1, p2 = utils.random_selection(pop[matingpool])
            offspring = self.xov(pop, p1, p2)
            offspring = self.mut(offspring)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            temp_pop = offspring + pop  # 合并种群
            zmin = np.min(offspring.objv, 0)
            zmax = np.max(pop[frontno == 1].objv, 0)
            pop, frontno, cd = self._EnvironmentalSelection(
                temp_pop, self.problem.pop_size, zmin, zmax
            )  # noqa
        return pop

    def _EnvironmentalSelection(self, pop, N, zmin, zmax):
        PopObj = pop.objv - np.tile(zmin, (len(pop), 1))
        range1 = zmax - zmin
        if 0.05 * np.max(range1) < np.min(range1):
            PopObj = PopObj / range1
        _, x = np.unique(
            np.round(PopObj * 1e6) / 1e6, return_index=True, axis=0
        )  # noqa
        PopObj = PopObj[x, :]
        pop = pop[x]
        N = min(N, len(pop))
        frontno, maxfront = self.NDSort_SDR(PopObj, N)
        Next = frontno < maxfront
        cd = utils.crowding_distance(pop, frontno)
        last = np.argwhere(frontno == maxfront)
        rank = np.argsort(-cd[last], axis=0)
        Next[last[rank[0: (self.problem.pop_size - np.sum(Next))]]] = True
        # 先计算next（也就是不是最大前沿上的）的总数，让N-sum即为需要在最后一前沿需要挑选的解
        # 此时选取最后前沿上rank（即依据cd选取的）最好的解，再使其的next变为Ture
        # pop for next generation
        pop = pop[Next]  # 选取next（即选中的解）中的解
        frontno = frontno[Next]  # 选取这些解的前沿
        cd = cd[Next]
        return pop, frontno, cd

    def NDSort_SDR(self, PopObj, nSort):
        N = PopObj.shape[0]
        NormP = np.sum(PopObj, axis=1)
        # cos = pdist(PopObj, PopObj)
        cos = 1-cdist(PopObj, PopObj, 'cosine')
        cos1 = np.array(np.eye(len(cos)), dtype=bool)
        cos[cos1] = 0
        Angle = np.arccos(cos)
        temp1 = np.min(Angle, axis=1)
        temp2 = np.unique(temp1)
        temp = np.sort(temp2, axis=0)
        minA = temp[min(int(np.ceil(N / 2)), len(temp)-1)]
        # a = np.ones(((Angle / minA).shape[0], (Angle / minA).shape[1]))
        theta = np.array(np.maximum(1, (Angle / minA)**1))  # noqa
        dominate = np.array(np.zeros((N, N)), dtype=bool)
        for i in range(0, N - 1):
            for j in range(i, N):
                if (NormP[i] * theta[i, j]) < NormP[j]:
                    dominate[i, j] = True
                elif (NormP[j] * theta[j, i]) < NormP[i]:
                    dominate[j, i] = True
        # tempdom = np.sum(dominate, axis=0)
        # temp_do = np.bool_(tempdom)
        # temp_dosum = np.sum(temp_do)
        frontno = np.ones((1, N))
        for i in range(0, N):
            frontno[0, i] = np.inf
        maxfront = 0
        frontno = frontno[0]
        while np.sum(frontno != np.inf) < min(nSort, N):
            maxfront += 1
            tempa = ~(np.any(dominate, axis=0))
            tempb = frontno == np.inf
            current1 = tempa & tempb
            # tempc = frontno[current1]
            # tempd = dominate[current1]
            frontno[current1] = maxfront
            # tempe = sum(frontno, axis=0)
            dominate[current1] = False
            # tempf = sum(~dominate, axis=0)
        return frontno, maxfront


# 求两个向量矩阵的余弦值,x的列数等于y的列数
def pdist(x, y):
    x0 = x.shape[0]
    y0 = y.shape[0]
    xmy = np.dot(x, y.T)  # x乘以y
    xm = np.array(np.sqrt(np.sum(x ** 2, 1))).reshape(x0, 1)
    ym = np.array(np.sqrt(np.sum(y ** 2, 1))).reshape(1, y0)
    xmmym = np.dot(xm, ym)
    cos = xmy / xmmym
    return cos
