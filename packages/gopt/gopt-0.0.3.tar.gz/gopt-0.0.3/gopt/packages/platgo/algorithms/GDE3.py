"""------------------------------- Reference --------------------------------
 S. Kukkonen and J. Lampinen, GDE3: The third evolution step of
 generalized differential evolution, Proceedings of the IEEE Congress on
 Evolutionary Computation, 2005, 443-450.
 """

import numpy as np

from .. import GeneticAlgorithm, utils, operators


class GDE3(GeneticAlgorithm):
    type = {
        "n_obj": "multi",
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "constrained/none",
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="GDE3",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(GDE3, self).__init__(
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

    def run_algorithm(self):
        """
         main function for Different Evolution
         if Pop is None, generate a new Pop with N
        :param N: Pop size
        :param Pop: Pop to be optimized
        :return:
        """
        pop = self.problem.init_pop()
        self.cal_obj(pop)

        while self.not_terminal(pop):
            Offspring = operators.OperatorDE(
                pop,
                pop[
                    np.random.randint(
                        self.problem.pop_size, size=(1, self.problem.pop_size)
                    )
                ],
                pop[
                    np.random.randint(
                        self.problem.pop_size, size=(1, self.problem.pop_size)
                    )
                ],
                self.problem,
            )
            self.cal_obj(Offspring)
            pop = self.EnvironmentalSelection(
                pop, Offspring, self.problem.pop_size
            )
        return pop

    def EnvironmentalSelection(self, Pop, Offspring, N):
        """Select by constraint-domination"""
        PopObj = Pop.objv
        PopCon = Pop.cv
        feasibleP = np.all(PopCon <= 0, axis=1)
        OffObj = Offspring.objv
        OffCon = Offspring.cv
        feasibleO = np.all(OffCon <= 0, axis=1)
        # The offsprings which can replace its parent
        updated = np.logical_and(
            np.logical_or(
                np.logical_and(
                    np.logical_or(
                        np.logical_and(~feasibleP, feasibleO),
                        np.logical_and(~feasibleP, ~feasibleO),
                    ),
                    np.all(PopCon >= OffCon, axis=1),
                ),
                np.logical_and(feasibleP, feasibleO),
            ),
            np.all(PopObj >= OffObj, axis=1),
        )
        # The offsprings which can add to the Pop
        selected = np.logical_and(
            np.logical_and(
                np.logical_and(feasibleP, feasibleO),
                np.any(PopObj < OffObj, axis=1),
            ),
            np.any(PopObj > OffObj, axis=1),
        )
        # Update the Pop
        Pop[updated] = Offspring[updated]
        Pop = Pop + Offspring[selected]

        """Select by non-dominated sorting and crowding distance"""
        PopObj = Pop.objv
        PopCon = Pop.cv
        feasible = np.all(PopCon <= 0, axis=1)
        # Non-dominated sorting based on
        # constraint-domination PopObj[feasible, :]
        FrontNo = np.full((Pop.decs.shape[0]), np.inf)  # noqa
        FrontNo[feasible], MaxFNo = utils.nd_sort(
            PopObj[feasible], np.sum(feasible)
        )
        FrontNo[~feasible], _ = utils.nd_sort(
            PopCon[~feasible], np.sum(~feasible)
        )
        FrontNo[~feasible] += MaxFNo

        # Determine the last front
        counts, _ = np.histogram(
            FrontNo, int(np.max(FrontNo)), range=(1, np.max(FrontNo) + 1)
        )
        MaxFNo = np.argwhere(np.cumsum(counts) >= N).flatten()[0] + 1
        lastFront = np.argwhere(FrontNo == MaxFNo).flatten()
        # Eliminate solutions in the last front one by one
        if isinstance(lastFront, np.int64):
            lastFront_len = 1
        else:
            lastFront_len = len(lastFront)

        while lastFront_len > (N - sum(FrontNo < MaxFNo)):
            worst = np.argmin(utils.crowding_distance(PopObj[lastFront], None))
            lastFront = np.delete(lastFront, worst, None)
            lastFront_len = len(lastFront)
        Pop = Pop[
            np.hstack((np.argwhere(FrontNo < MaxFNo).flatten(), lastFront))
        ]
        return Pop
