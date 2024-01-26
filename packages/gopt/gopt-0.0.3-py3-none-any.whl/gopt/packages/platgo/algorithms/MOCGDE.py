import numpy as np

from .. import GeneticAlgorithm, utils, Population


class MOCGDE(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "gradient/none"
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="MOCGDE",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):

        super(MOCGDE, self).__init__(
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

    def run_algorithm(self):
        W, subN = utils.uniform_point(10, self.problem.n_obj)
        pop = self.problem.init_pop(subN)
        self.cal_obj(pop)
        Archive = pop
        K = np.zeros((1, subN))
        g0 = [[] for i in range(10)]
        d0 = [[] for i in range(10)]
        while self.not_terminal(Archive):
            K = np.mod(K, self.problem.n_var) + 1
            OffPop = []
            for i in range(subN):
                gk, site = self.FiniteDifference(pop[i], W[i, :])
                if K[0][i] == 1:
                    dk = -gk
                else:
                    beta = np.dot(gk.T, gk) / np.sum(np.array(g0[i]) ** 2)
                    dk = -gk + beta * np.array(d0[i])
                    if np.dot(gk.T, dk) >= 0:
                        dk = -gk
                success = False
                for step in range(10):
                    mu = np.random.rand(1, self.problem.n_var) < (
                        np.inf / np.sum(site))
                    OffDec = pop[i].decs + np.where(site == 0, 1, 0) * 0.5 ** step * dk.T + mu * site * 0.5 ** step * (Archive[np.random.randint(len(Archive))].decs -  # noqa
                         Archive[np.random.randint(len(Archive))].decs)  # noqa
                    Offspring = Population(decs=OffDec)
                    self.problem.fix_decs(Offspring)
                    self.cal_obj(Offspring)
                    if not OffPop:
                        OffPop = Offspring
                    else:
                        OffPop = OffPop + Offspring
                    if (np.sum(np.where(Offspring.cv > 0, Offspring.cv, 0)) < np.sum(np.where(pop[i].cv > 0, pop[i].cv, 0))) \
                            or (np.sum(np.where(Offspring.cv > 0, Offspring.cv, 0)) == np.sum(np.where(pop[i].cv > 0, pop[i].cv, 0))) \
                            and (np.all(Offspring.objv < pop[i].objv)):  # noqa
                        success = True
                        break
                if success:
                    pop[i] = Offspring
                    g0[i] = gk.tolist()
                    d0[i] = dk.tolist()
                else:
                    pop[i] = Archive[np.random.randint(len(Archive))]
                    K[0][i] = 0
            P = Archive + OffPop
            Archive = UpdateArchive(P, self.problem.pop_size)
        print(Archive.objv)
        return Archive

    def FiniteDifference(self, X, W):
        temp = Population(decs=np.tile(
            X.decs, (self.problem.n_var, 1)) + np.eye(self.problem.n_var) * 1e-6)  # noqa
        self.cal_obj(temp)
        if np.any(X.cv > 0):
            df = (temp.objv - np.tile(X.objv, (self.problem.n_var, 1))) / 1e-6
            site = np.zeros((1, self.problem.n_var))
            df = np.sum(df, axis=1)
        else:
            df = (temp.objv - np.tile(X.objv, (self.problem.n_var, 1))) / 1e-6
            # site = np.any(df < 0, axis=1) == np.any(df > 0, axis=1)
            site = [i and j for i, j in zip(
                np.any(df < 0, axis=1), np.any(df > 0, axis=1))]
            df = np.dot(df, W.T)
        return df, np.array(site)


def UpdateArchive(P, N):
    if np.all(P.cv == 0):
        frontno, _ = utils.nd_sort(P.objv, 1)
    else:
        frontno, _ = utils.nd_sort(P.objv, P.cv, 1)
    temp_pop = P[np.argwhere(np.where(frontno == 1, frontno, 0))]
    if len(temp_pop) > N:
        Choose = np.ones((1, len(temp_pop)))
        Dis = np.linalg.norm(
            temp_pop.objv[:, np.newaxis, :] - temp_pop.objv[np.newaxis, :, :], axis=2)  # noqa
        Dis[np.diag_indices_from(Dis)] = np.inf
        while np.sum(Choose) > N:
            Remain = np.where(Choose[0] != 0)[0]
            Temp = np.sort(Dis[Remain], axis=1)
            Rank = np.argsort(Temp.T)[:, :1]
            Choose[0][Remain[Rank[0]]] = 0
        Choose = 1 == Choose
        temp_pop = temp_pop[Choose]
    return temp_pop
