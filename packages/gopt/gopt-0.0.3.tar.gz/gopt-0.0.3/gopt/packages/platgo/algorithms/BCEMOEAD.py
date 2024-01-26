# from random import random
import numpy as np
from scipy.spatial.distance import cdist
# from regex import R
from gopt.packages.platgo.operators import OperatorGAhalf

from .. import GeneticAlgorithm, utils


class BCEMOEAD(GeneticAlgorithm):
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
        name="BCEMOEAD",
        show_bar=False,
        sim_req_cb=None,
        debug=False
    ):
        super(BCEMOEAD, self).__init__(
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
        W, N = utils.uniform_point(
            self.problem.pop_size, self.problem.n_obj
        )  # noqa
        W = np.where(W != 0, W, 1e-6)
        T = int(np.ceil(N / 10))
        nr = int(np.ceil(N / 100))
        B = cdist(W, W)
        B = np.argsort(B)
        B = B[:, :T]
        pop = self.problem.init_pop(W.shape[0])
        self.cal_obj(pop)
        Z = np.min(pop.objv, axis=0)
        PC, nND = self.PCSelection(pop, N)

        while self.not_terminal(PC):
            newpc = self.Exploration(PC, pop, nND, N)
            # print("newpc=",newpc)
            if newpc is not None:  # noqa
                for i in range(len(newpc)):
                    tempa = newpc[i].objv
                    tempa = tempa[0]
                    Z = np.minimum(Z, tempa)
                    p = np.random.permutation(len(pop))
                    g_old = np.max(
                        np.abs(pop[p].objv - Z) / W[p, :], axis=1  # noqa
                    )  # noqa
                    g_new = np.max(
                        np.abs(newpc[i].objv - Z) / W[p, :], axis=1  # noqa
                    )  # noqa
                    tempa = np.argwhere(g_old >= g_new).flatten()[:1]
                    pop[p[tempa]] = newpc[i]
                # NPC(pop) evolving
                newpop = self.problem.init_pop(len(pop))
                # self.cal_obj(newpop)
                newpop_objv = np.zeros((len(newpop), self.problem.n_obj))
                for i in range(len(pop)):
                    tempa = np.random.rand()
                    if tempa < 0.9:
                        p = B[i, np.random.permutation(B.shape[1])]
                    else:
                        p = np.random.permutation(len(pop))
                    off = OperatorGAhalf(pop[p.T.flatten()[:2]], self.problem)  # noqa
                    self.cal_obj(off)
                    newpop[i] = off.copy()
                    newpop_objv[i, :] = off.objv.copy()
                    # Update the ideal point
                    Z = np.minimum(Z, off.objv)
                    # Update the solutions in P by modified Tchebycheff approach  # noqa
                    g_old = np.max(
                        np.abs(pop[p].objv - Z) / W[p, :], axis=1  # noqa
                    )  # noqa
                    g_new = np.max(
                        np.abs(off.objv - Z) / W[p, :], axis=1  # noqa
                    )  # noqa
                    tempa = np.argwhere(g_old >= g_new).flatten()[:nr]
                    pop[p[tempa]] = off.copy()
                newpop.objv = newpop_objv.copy()
                newpop.cv = pop.cv.copy()
                PC, nND = self.PCSelection(pop + newpop + newpc, N)
            else:
                newpop = self.problem.init_pop(len(pop))
                # self.cal_obj(newpop)
                # for i in range(len(pop)):
                #     tempa = np.random.rand()
                #     if tempa < 0.9:
                #         p = B[i, np.random.permutation(B.shape[1])]
                #     else:
                #         p = np.random.permutation(len(pop))
                #     # newpop[i] = OperatorGAhalf(
                #     #     pop[p.T.flatten()[:2]], self.problem
                #     # )  # noqa
                #     # self.cal_obj(newpop)
                #     off = OperatorGAhalf(pop[p.T.flatten()[:2]], self.problem)  # noqa
                #     self.cal_obj(off)
                #     newpop[i] = off.copy()
                #     # Update the ideal point
                #     Z = np.minimum(Z, newpop[i].objv)
                #     # Update the solutions in P by modified Tchebycheff approach  # noqa
                #     g_old = np.max(
                #         np.abs(pop[p].objv - Z) / W[p, :], axis=1  # noqa
                #     )  # noqa
                #     g_new = np.max(
                #         np.abs(newpop[i].objv - Z) / W[p, :], axis=1  # noqa
                #     )  # noqa
                #     tempa = np.argwhere(g_old >= g_new).flatten()[:nr]
                #     pop[p[tempa]] = newpop[i].copy()
                # PC, nND = self.PCSelection(pop + newpop, N)
                newpop_objv = np.zeros((len(newpop), self.problem.n_obj))
                for i in range(len(pop)):
                    tempa = np.random.rand()
                    if tempa < 0.9:
                        p = B[i, np.random.permutation(B.shape[1])]
                    else:
                        p = np.random.permutation(len(pop))
                    off = OperatorGAhalf(pop[p.T.flatten()[:2]], self.problem)  # noqa
                    self.cal_obj(off)
                    newpop[i] = off.copy()
                    newpop_objv[i, :] = off.objv.copy()
                    # Update the ideal point
                    Z = np.minimum(Z, off.objv)
                    # Update the solutions in P by modified Tchebycheff approach  # noqa
                    g_old = np.max(
                        np.abs(pop[p].objv - Z) / W[p, :], axis=1  # noqa
                    )  # noqa
                    g_new = np.max(
                        np.abs(off.objv - Z) / W[p, :], axis=1  # noqa
                    )  # noqa
                    tempa = np.argwhere(g_old >= g_new).flatten()[:nr]
                    pop[p[tempa]] = off.copy()
                newpop.objv = newpop_objv.copy()
                newpop.cv = pop.cv.copy()
                PC, nND = self.PCSelection(pop + newpop, N)
        return pop

    def Exploration(self, PC, pop, nND, N):
        PCobj = PC.objv
        popobj = pop.objv
        fmax = np.max(PCobj, axis=0)
        fmin = np.min(PCobj, axis=0)
        PCobj = (PCobj - fmin) / (fmax - fmin)
        popobj = (popobj - fmin) / (fmax - fmin)
        # Determine the size of the niche
        d = cdist(PCobj, PCobj)
        d1 = np.array(np.eye(len(d)), dtype=bool)
        d[d1] = np.inf
        d = np.sort(d, axis=1)
        temp1 = min(3, d.shape[1])
        r0 = np.mean(d[:, temp1-1])
        r = nND / N * r0
        # Detect the solutions in PC to be explored
        d = cdist(PCobj, popobj)
        temp2 = np.sum(d <= r, axis=1)
        S = np.argwhere(temp2 <= 1).flatten()
        # print("S=", S)
        # Generate new solutions
        if len(S) == 0:
            Offspring = None
        else:
            MatingPool = np.random.randint(0, len(PC), len(S))
            temp3 = np.hstack((S, MatingPool))
            # if temp3.shape[0] and temp3.shape[1] !=0:
            #     temp4 = PC[temp3 - 1]
            # else:temp4 = PC[temp3]
            # print("S.T=", S.T)
            # print("MatingPool=", MatingPool)
            # print(temp3)
            Offspring = OperatorGAhalf(PC[temp3], self.problem)
            self.cal_obj(Offspring)
        return Offspring

    def PCSelection(self, PC, N):
        tempa, _ = utils.nd_sort(PC.objv, 1)
        tempb = np.argwhere(tempa == 1)
        PC = PC[tempb]
        PC = PC[np.random.permutation(len(PC))]
        PCobj = PC.objv
        nND = len(PC)
        if len(PC) > N:
            # Normalization
            fmax = np.max(PCobj, axis=0)
            fmin = np.min(PCobj, axis=0)
            PCobj = (PCobj - fmin) / (fmax - fmin)
            # Determine the radius of the niche
            d = cdist(PCobj, PCobj)
            d1 = np.array(np.eye(len(d)), dtype=bool)
            d[d1] = np.inf
            sd = np.sort(d, axis=1)
            temp1 = min(3, sd.shape[1])
            r1 = np.mean(sd[:, temp1-1])
            r = np.minimum((d / r1), 1)
            # Delete solution one by one
            while len(PC) > N:
                # temp = 1 - np.prod(r, axis=1)
                # tempa = np.argwhere(temp == np.max(temp)).flatten()
                # worst = int(np.mean(tempa))
                # PC = np.delete(PC, worst)
                worst = np.argmax(1 - np.prod(r, axis=1), axis=0)
                PC = PC[:worst] + PC[worst+1:]
                r = np.delete(r, worst, axis=0)
                r = np.delete(r, worst, axis=1)
        return PC, nND
