
from operator import mod
import numpy as np
from gopt.packages.platgo.operators import OperatorGA
from scipy.spatial.distance import cdist
from .. import GeneticAlgorithm, utils


class GFMMOEA(GeneticAlgorithm):
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
        name="GFMMOEA",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        theta=0.2,
        fPFE=0.1,
    ):
        super(GFMMOEA, self).__init__(
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
        self.theta = theta
        self.fPFE = fPFE
        # self.xov = operators.XovSbx()  # 模拟二进制交叉
        # self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        # Generate random population
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        frontno, maxfront = utils.nd_sort(pop.objv, np.inf)
        zmin = np.min(pop.objv, axis=0)
        # Calculate the fitness of each solution
        P = np.ones((1, self.problem.n_obj))
        A = P.copy()
        App, Dis = self.CalFitness(pop.objv - zmin, P, A)
        Dis = np.sort(Dis, axis=1)
        Crowd = Dis[:, 0] + 0.1 * Dis[:, 1]
        # Optimization
        while self.not_terminal(pop):
            # TODO 未考虑编码形式
            matingpool = utils.tournament_selection(2, self.problem.pop_size, frontno, -self.theta*App-(1-self.theta)*Crowd)  # noqa
            offspring = OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(offspring)  # 计算子代种群目标函数值
            zmin = np.min(np.vstack((zmin, offspring.objv)), axis=0)
            # temp_pop = offspring + pop  # 合并种群
            tempa = int(np.ceil(self._gen/self.problem.pop_size))
            tempb = int(np.ceil(self.fPFE * np.ceil(self._max_fe/self.problem.pop_size)))  # noqa
            # if mod(tempa, tempb) > 0:
            #     temp = True
            # else:
            #     temp = False
            if not mod(tempa, tempb) or self.fPFE == 0:
                P, A = self.GFM(pop[frontno == 1].objv - np.tile(zmin, (int(np.sum(frontno == 1)), 1)))  # noqa
            pop, frontno, App, Crowd = self.EnvironmentalSelection(pop + offspring, P, A, zmin, self.theta, self.problem.pop_size)  # noqa
        # print(metrics.hv1(pop))
        return pop

    def EnvironmentalSelection(self, pop, P, A, zmin, theta, N):
        # Non-dominated sorting
        # self.cal_obj(pop)
        frontno, maxfront = utils.nd_sort(pop.objv, N)
        Next = np.argwhere(frontno <= maxfront).flatten()
        # Environmental selection
        PopObj = pop[Next].objv - zmin
        App, Dis = self.CalFitness(PopObj, P, A)
        Choose = self.LastSelection(PopObj, frontno[Next], App, Dis, theta, N)
        # Population for next generation
        pop = pop[Next[Choose]]
        frontno = frontno[Next[Choose]]
        App = App[Choose]
        Dis = np.sort(Dis[Choose][:, Choose], axis=1)
        Crowd = Dis[:, 1] + 0.1 * Dis[:, 2]
        return pop, frontno, App, Crowd

    def CalFitness(self, PopObj, P, A):
        N = PopObj.shape[0]
        M = PopObj.shape[1]
        # Calculate the intersections by gradient descent
        A = np.tile(A, (N, 1))
        P = np.tile(P, (N, 1))
        r = np.ones((N, 1)).flatten()
        tempr = np.tile(r, (M, 1)).T
        lamda = (np.zeros((N, 1)) + 0.1).flatten()
        E = np.sum(A * (PopObj*tempr)**P, axis=1) - 1
        for i in range(1000):
            tempr = np.tile(r, (M, 1)).T
            newr = r - lamda * E * np.sum(A * P * PopObj**P * tempr**(P-1), axis=1)  # noqa
            # print((PopObj * np.tile(newr, (M, 1)).T)**P)
            newE = np.sum(A * (PopObj * np.tile(newr, (M, 1)).T)**P, axis=1) - 1  # noqa
            update = np.logical_and(newr > 0, np.sum(newE**2) < np.sum(E**2))
            r[update] = newr[update]
            E[update] = newE[update]
            lamda[update] *= 1.1
            lamda[~update] /= 1.1
        PopObj1 = PopObj * np.tile(r, (PopObj.shape[1], 1)).T
        # Calculate the convergence of each solution
        App = np.sqrt(np.sum(PopObj1**2, axis=1)) - np.sqrt(np.sum(PopObj**2, axis=1))  # noqa
        # Calculate the diversity of each solution
        Dis = cdist(PopObj1, PopObj1)
        Dis[np.eye(len(Dis), dtype=bool)] = np.inf
        return App, Dis

    def GFM(self, X):
        N = X.shape[0]
        M = X.shape[1]
        X = np.maximum(X, 1e-12)
        P = np.ones((1, M))
        A = np.ones((1, M))
        tempP = np.tile(P, (N, 1))
        tempA = np.tile(A, (N, 1))
        lamda = 1
        E = np.sum(tempA * X**tempP, axis=1) - 1
        MSE = np.mean(E**2)
        for epoch in range(1000):
            # Calculate the Jacobian matrix
            tempP = np.tile(P, (N, 1))
            tempA = np.tile(A, (N, 1))
            J = np.hstack((tempA * X**tempP * np.log(X), X**tempP))
            # Update the value of each weight
            while True:
                Delta = -np.dot(np.dot(np.linalg.inv((np.dot(J.T, J) + np.dot(lamda, np.eye(J.shape[1])))), J.T), E)  # noqa
                newP = P + Delta[0: M].T
                newA = A + Delta[M:].T
                newE = np.sum(np.tile(newA, (N, 1)) * X**np.tile(newP, (N, 1)), axis=1) - 1  # noqa
                newMSE = np.mean(newE**2)
                if newMSE < MSE and np.all(newP > 1e-3) and np.all(newA > 1e-3):  # noqa
                    P = newP
                    A = newA
                    E = newE
                    MSE = newMSE
                    lamda /= 1.1
                    break
                elif lamda > 1e8:
                    return P, A
                else:
                    lamda *= 1.1
        return P, A

    def LastSelection(self, PopObj, frontno, App, Dis, theta, N):
        # Select part of the solutions in the last front
        # Identify the extreme solutions
        # frontno = frontno.flatten()
        NDS = np.argwhere(frontno == 1).flatten()
        temp1 = np.tile(np.sqrt(np.sum(PopObj[NDS, :]**2, axis=1)), (PopObj.shape[1], 1)).T  # noqa
        temp2 = 1 - cdist(PopObj[NDS, :], np.eye(PopObj.shape[1]), "cosine")  # noqa
        Extreme = np.argmin(temp1 * np.sqrt(1 - temp2**2), axis=0)
        nonExtreme = np.ones(len(frontno), dtype=bool)
        nonExtreme[NDS[Extreme]] = False
        # Environmental selection
        Last = frontno == np.max(frontno)
        Choose = np.ones(PopObj.shape[0], dtype=bool)
        while(np.sum(Choose)) > N:
            Remain = np.argwhere(np.logical_and(np.logical_and(Choose, Last), nonExtreme)).flatten()  # noqa
            dis = np.sort(Dis[Remain][:, Choose], axis=1)
            dis = dis[:, 0] + 0.1*dis[:, 1]
            fitness = theta*App[Remain] + (1 - theta)*dis
            worst = np.argmin(fitness)
            Choose[Remain[worst]] = False
        return Choose
