# from random import random
import numpy as np
from scipy.spatial.distance import cdist
# from regex import R
from gopt.packages.platgo.operators import OperatorGA, OperatorGAhalf
from gopt.packages.platgo.utils.selections.tournament_selection import tournament_selection  # noqa

from .. import GeneticAlgorithm, utils


class BCEIBEA(GeneticAlgorithm):
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
        max_fe=40000,
        name="BCEIBEA",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        kappa=0.05
    ):
        super(BCEIBEA, self).__init__(
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
        self.kappa = kappa

    def run_algorithm(self):
        N = self.problem.pop_size
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        # NPC = pop
        PC, nND = self.PCSelection(pop, N)
        while self.not_terminal(PC):
            newpc = self.Exploration(PC, pop, nND, N)
            if newpc is not None:
                self.cal_obj(newpc)
                temp_pop = pop + newpc
                pop = self.EnvironmentalSelection(temp_pop, N, self.kappa)  # noqa
                matingpool = tournament_selection(2, N, -self.CalFitness(pop.objv, self.kappa)[0])  # noqa
                # NewNPC = off
                offspring = OperatorGA(pop[matingpool], self.problem)
                self.cal_obj(offspring)
                temp_pop = offspring + pop
                pop = self.EnvironmentalSelection(temp_pop, N, self.kappa)
                temp_pop1 = PC + offspring + newpc
                PC, nND = self.PCSelection(temp_pop1, N)
            else:
                temp_pop = pop
                pop = self.EnvironmentalSelection(temp_pop, N, self.kappa)  # noqa
                matingpool = tournament_selection(2, N, -self.CalFitness(pop.objv, self.kappa)[0])  # noqa
                # NewNPC = off
                offspring = OperatorGA(pop[matingpool], self.problem)
                self.cal_obj(offspring)
                temp_pop = offspring + pop
                pop = self.EnvironmentalSelection(temp_pop, N, self.kappa)
                temp_pop1 = PC + offspring
                PC, nND = self.PCSelection(temp_pop1, N)
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
            # temp3 = np.hstack((S, MatingPool))
            # temp4 = PC[temp3]
            Offspring = OperatorGAhalf(PC[np.hstack((S, MatingPool))], self.problem)  # noqa
            # self.cal_obj(Offspring)
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
                r = np.delete(r, worst, 0)
                r = np.delete(r, worst, 1)
        return PC, nND

    def EnvironmentalSelection(self, pop, N, kappa):
        Next = np.array(np.arange(len(pop))).flatten()
        Fitness, Ia, C = self.CalFitness(pop.objv, kappa)
        while len(Next) > N:
            x = np.argmin(Fitness[Next]).flatten()
            Fitness = Fitness + np.exp(-Ia[Next[x], :]/C[Next[x]]/kappa).flatten()  # noqa
            Next = np.delete(Next, x)
        pop = pop[Next]
        return pop

    def CalFitness(self, PopObj, kappa):
        N = PopObj.shape[0]
        tempmin = np.min(PopObj, axis=0)
        tempmax = np.max(PopObj, axis=0)
        PopObj = (PopObj - tempmin)/(tempmax - tempmin)
        Ia = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                Ia[i, j] = np.max(PopObj[i, :] - PopObj[j, :])
        C = np.max(np.abs(Ia), axis=0)
        Fitness = (np.sum(-np.exp(-Ia/C/kappa), axis=0) + 1).flatten()
        return Fitness, Ia, C
