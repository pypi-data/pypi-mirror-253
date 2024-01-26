import numpy as np

from .. import GeneticAlgorithm, utils, operators


class r_NSGA2(GeneticAlgorithm):
    type = {
        "n_obj": "multi",
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"},  # noqa
        "special": "preference"
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="r_NSGA2",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        Point=None,
        W=None,
        delta=0.1
    ):

        super(r_NSGA2, self).__init__(
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
        self.delta = delta
        if Point is None:
            self.Point = np.zeros((1, self.problem.n_obj)) + 0.5
        else:
            self.Point = np.array([eval(Point)])
        if W is None:
            self.W = np.ones((1, self.problem.n_obj))
        else:
            self.W = np.array([eval(W)])

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        FrontNo, _ = NrDSort(pop.objv, np.inf, self.Point, self.W,
                             1 - (1 - self.delta) * (self._gen + 1) / self._max_fe)  # noqa
        CrowdDis = utils.crowding_distance(pop, FrontNo)
        while self.not_terminal(pop):
            MatingPool = utils.tournament_selection(
                2, self.problem.pop_size, FrontNo, -CrowdDis)
            Offspring = operators.OperatorGA(pop[MatingPool], self.problem)
            self.cal_obj(Offspring)
            '''if self._gen == self.maxgen:
                break'''
            '''print((1 - (1 - self.delta) * (self._gen + 1) / self.maxgen) * 0.1)
            print(self._gen)'''
            pop, FrontNo, CrowdDis = EnvironmentalSelection(pop + Offspring, self.problem.pop_size, self.Point, self.W,  # noqa
                                                            (1 - (1 - self.delta) * (self._gen + 1) / self._max_fe))  # noqa

        print(self.delta)
        print(self.Point)
        return pop


def EnvironmentalSelection(pop, N, Points, W, delta):
    FrontNo, MaxFNo = NrDSort(pop.objv, N, Points, W, delta)
    Next = FrontNo < MaxFNo
    CrowDis = utils.crowding_distance(pop, FrontNo)
    # select the soltions in the last front based on their crowding distances
    last = np.argwhere(FrontNo == MaxFNo)
    rank = np.argsort(-CrowDis[last], axis=0)
    # 先计算next（也就是不是最大前沿上的）的总数，让N-sum即为需要在最后一前沿需要挑选的解
    Next[last[rank[0:(N - np.sum(Next))]]] = True
    # 此时选取最后前沿上rank（即依据cd选取的）最好的解，再使其的next变为Ture
    # pop for next generation
    pop = pop[Next]  # 选取next（即选中的解）中的解
    FrontNo = FrontNo[Next]  # 选取这些解的前沿
    CrowDis = CrowDis[Next]
    return pop, FrontNo, CrowDis


def NrDSort(PopObj, nSort, Points, W, delta):
    FrontNo = np.ones((1, PopObj.shape[0]))
    FrontNo[:, :] = np.inf
    for i in range(Points.shape[0]):
        FrontNo = np.min((FrontNo.flatten(), nrdsort(
            PopObj, Points[i, :], W[i, :], delta)), axis=0)
    # print(FrontNo)
    tmp, s = np.histogram(FrontNo, bins=np.arange(1, np.max(FrontNo) + 2))
    MaxFNo = np.argwhere(np.cumsum(tmp) >= np.min(
        (nSort, len(FrontNo)))).flatten()[0]
    FrontNo[FrontNo > (MaxFNo + 1)] = np.inf
    return FrontNo, MaxFNo + 1


def nrdsort(PopObj, g, w, delta):
    '''PopObj = np.array([0.93205362, 0.77620921, 0.7024097 , 0.20493082, 0.56647329,  # noqa
       0.13642473, 0.42021313, 0.77542403, 0.1549694 , 0.69749201,
       0.8333903 , 0.54825   , 0.56587813, 0.83924589, 0.86218135,
       0.81455265, 0.85817559, 0.68866548, 0.43000186, 0.49121216,
       0.30013336, 0.8087789 , 0.02583454, 0.917778  , 0.42666779,
       0.87325529, 0.43655111, 0.27792901, 0.10787786, 0.24747458,
       0.41208312, 0.03201899, 0.42250451, 0.61566795, 0.41970638,
       0.94832243, 0.11042011, 0.100096  , 0.57218768, 0.31160742])
    PopObj = PopObj.reshape(20, 2)'''

    PopObj, Loc = np.unique(PopObj, return_inverse=True, axis=0)
    # PopObj = PopObj[Loc]
    Dist = np.sqrt(np.dot(((PopObj - np.tile(g, (PopObj.shape[0], 1))) / np.tile(  # noqa
        np.max(PopObj, axis=0) - np.min(PopObj, axis=0), (PopObj.shape[0], 1)))
        ** 2, (w / np.sum(w)).reshape(1, len(w)).T))
    DistExtent = np.max(Dist) - np.min(Dist)
    rank = np.argsort(Dist, axis=0).flatten()
    Dist = Dist[rank]
    PopObj = PopObj[rank, :]
    N, M = PopObj.shape
    FrontNo = np.full(N, np.inf)
    MaxFNo = 0
    # PopObj, index, ind = np.unique(PopObj, return_index=True, return_inverse=True, axis=0)  # noqa
    while np.any(FrontNo == np.inf):
        MaxFNo = MaxFNo + 1
        for i in range(N):
            if FrontNo[i] == np.inf:
                Dominated = False
                for j in range(N):
                    if FrontNo[j] >= MaxFNo and j != i:
                        m = 0
                        while m < M and PopObj[i][m] >= PopObj[j][m]:
                            m = m + 1
                        Dominated = m >= M
                        if Dominated:
                            break
                if np.logical_not(Dominated):
                    for j in range(i - 1, -1, -1):
                        if FrontNo[j] == MaxFNo:
                            Dominated = (
                                ((Dist[j] - Dist[i]) / DistExtent) < -delta)
                            if Dominated:
                                break
                if np.logical_not(Dominated):
                    FrontNo[i] = MaxFNo
    a = FrontNo.copy()
    FrontNo[rank] = a
    FrontNo = FrontNo[Loc]
    return FrontNo
