import numpy as np

from .. import GeneticAlgorithm, utils, operators


class g_NSGA2(GeneticAlgorithm):
    type = {
        "n_obj": "multi",
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "preference"
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="g_NSGA2",
        show_bar=False,
        debug=False,
        Point=None,
        sim_req_cb=None,
    ):
        super(g_NSGA2, self).__init__(
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
        if Point is None:
            self.Point = np.zeros((1, self.problem.n_obj)) + 0.5
        else:
            self.Point = np.array([eval(Point)])

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        FrontNo, _ = utils.nd_sort(Evaluate(pop.objv, self.Point), len(pop))
        CrowdDis = utils.crowding_distance(pop, FrontNo)
        while self.not_terminal(pop):
            matingpool = utils.tournament_selection(
                2, pop.pop_size, FrontNo, -CrowdDis
            )
            OffSpring = operators.OperatorGA(pop[matingpool], self.problem)
            self.cal_obj(OffSpring)
            pop, frontno, cd = self.environmental_selection(pop + OffSpring)
        return pop

    def environmental_selection(self, pop):
        PopObj = Evaluate(pop.objv, self.Point)
        FrontNo, MaxFNo = utils.nd_sort(PopObj, self.problem.pop_size)
        Next = FrontNo < MaxFNo
        CrowdDis = utils.crowding_distance(PopObj, FrontNo)
        last = np.argwhere(FrontNo == MaxFNo)
        rank = np.argsort(-CrowdDis[last], axis=0)
        Next[last[rank[0: (self.problem.pop_size - np.sum(Next))]]] = True
        pop = pop[Next]
        FrontNo = FrontNo[Next]  # 选取这些解的前沿
        CrowdDis = CrowdDis[Next]
        return pop, FrontNo, CrowdDis


def Evaluate(PopObj, Point):
    Point = np.tile(Point, (PopObj.shape[0], 1))
    Falg = np.logical_or(
        np.all(PopObj <= Point, axis=1), np.all(PopObj >= Point, axis=1)
    )
    Falg = np.tile(Falg, (PopObj.shape[1], 1))
    PopObj[~(Falg.T)] = PopObj[~(Falg.T)] + (1e10)
    return PopObj
