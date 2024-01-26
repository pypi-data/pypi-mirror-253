"""
------------------------------- Reference --------------------------------
 Y. Tian, Y. Zhang, Y. Su, X. Zhang, K. C. Tan, and Y. Jin, Balancing
 objective optimization and constraint satisfaction in constrained
 evolutionary multi-objective optimization, IEEE Transactions on
 Cybernetics, 2020.
"""

import numpy as np
from scipy.spatial.distance import cdist

from .. import GeneticAlgorithm, utils, operators


class CMOEA_MS(GeneticAlgorithm):
    type = {
        "n_obj": {"multi"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "constrained",
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=20000,
        type=1,
        __lambda=0.5,
        name="CMOEA_MS",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(CMOEA_MS, self).__init__(
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
        self.type = type
        self.__lambda = __lambda

    def run_algorithm(self):
        # Generate random Pop
        Pop = self.problem.init_pop()
        self.cal_obj(Pop)
        Fitness = self.CalFitness(
            np.hstack(
                (
                    np.array([self.CalSDE(Pop.objv)]).T,
                    np.array([self.CalCV(Pop.cv)]).T,
                )
            ),
            None,
        )

        # Optimization
        while self.not_terminal(Pop):
            if self.type == 1:
                MatingPool = utils.tournament_selection(
                    2, Pop.pop_size, Fitness
                )
                Offspring = operators.OperatorGA(Pop[MatingPool], self.problem)
                self.cal_obj(Offspring)
            elif self.type == 2:
                Mat1 = utils.tournament_selection(2, Pop.pop_size, Fitness)
                Mat2 = utils.tournament_selection(2, Pop.pop_size, Fitness)
                Offspring = operators.OperatorDE(
                    Pop, Pop[Mat1], Pop[Mat2], self.problem
                )
                self.cal_obj(Offspring)
            Q = Pop + Offspring
            CV = self.CalCV(Q.cv)
            if np.logical_and(
                np.mean(CV <= 0) > self.__lambda,
                self._gen >= 0.1 * self._max_fe,
            ):
                Fitness = self.CalFitness(Q.objv, CV)
            else:
                Fitness = self.CalFitness(
                    np.hstack(
                        (np.array([self.CalSDE(Q.objv)]).T, np.array([CV]).T)
                    ),
                    None,
                )
            Pop, Fitness = self.EnvironmentalSelection(
                Fitness, Q, self.problem.pop_size
            )
        return Pop

    def CalCV(self, CV_Original):
        CV_Original = np.maximum(CV_Original, 0)
        CV = CV_Original / CV_Original.max(0)
        CV[:, np.isnan(CV[1, :])] = 0
        CV = np.mean(CV, axis=1)
        return CV

    def CalFitness(self, PopObj, CV):
        N = PopObj.shape[0]
        if CV is None:
            CV = np.zeros((PopObj.shape[0], 1))

        # Detect the dominance relation between each two solutions
        Dominate = np.zeros((N, N), dtype=bool)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if CV[i] < CV[j]:
                    Dominate[i][j] = True
                elif CV[i] > CV[j]:
                    Dominate[j][i] = True
                else:
                    k = int(np.any(PopObj[i] < PopObj[j])) - int(
                        np.any(PopObj[i] > PopObj[j])
                    )
                    if k == 1:
                        Dominate[i][j] = True
                    elif k == -1:
                        Dominate[j][i] = True
        # Calculate S(i)
        S = np.sum(Dominate, axis=1)

        # Calculate R(i)
        R = np.zeros(N)
        for i in range(N):
            R[i] = np.sum(S[Dominate[:, i]])

        # Calculate D(i)
        Distance = cdist(np.real(PopObj), np.real(PopObj), "cosine")
        Distance[np.eye(len(Distance), dtype=bool)] = np.inf
        Distance = np.sort(Distance, axis=1)
        D = 1 / (Distance[:, int(np.floor(np.sqrt(N)) - 1)] + 2)

        # Calculate the fitnesses
        Fitness = R + D
        return Fitness

    def CalSDE(self, PopObj):
        N = PopObj.shape[0]
        Zmin = PopObj.min(0)
        Zmax = PopObj.max(0)
        PopObj = (PopObj - np.tile(Zmin, (N, 1))) / (
            np.tile(Zmax, (N, 1)) - np.tile(Zmin, (N, 1))
        )
        SDE = np.zeros(N)
        for i in range(N):
            SPopuObj = PopObj.copy()
            Temp = np.tile(PopObj[i, :], (N, 1))
            Shifted = PopObj < Temp
            SPopuObj[Shifted] = Temp[Shifted]
            Distance = cdist(
                np.real(np.array([PopObj[i, :]])), np.real(SPopuObj)
            ).flatten()
            index = np.argsort(Distance)
            Dk = Distance[index[int(np.floor(np.sqrt(N)) - 1) + 1]]
            SDE[i] = 1 / (Dk + 2)
        return SDE

    def EnvironmentalSelection(self, Fitness, Pop, N):
        # Environmental selection
        Next = Fitness < 1
        if np.sum(Next) < N:
            Rank = np.argsort(Fitness)
            Next[Rank[:N]] = True
        elif np.sum(Next) > N:
            Del = self.Truncation(Pop[Next].objv, np.sum(Next) - N)
            Temp = np.argwhere(Next)
            Next[Temp[Del]] = False
        Pop = Pop[Next]
        Fitness = Fitness[Next]
        ind = np.argsort(Fitness)
        Pop = Pop[ind]
        Fitness = Fitness[ind]

        return Pop, Fitness

    def Truncation(self, PopObj, K):
        # Select part of the solutions by truncation
        Distance = cdist(PopObj, PopObj, "cosine")
        Distance[np.eye(len(Distance), dtype=bool)] = np.inf
        Del = np.zeros(len(PopObj), dtype=bool)

        while np.sum(Del) < K:
            Remain = np.argwhere(~Del).flatten()
            Temp = Distance[Remain]
            Temp = Temp[:, Remain]
            Temp = np.sort(Temp, axis=1)
            _, Rank = np.unique(Temp, return_index=True, axis=0)
            Del[Remain[Rank[0]]] = True
        return Del
