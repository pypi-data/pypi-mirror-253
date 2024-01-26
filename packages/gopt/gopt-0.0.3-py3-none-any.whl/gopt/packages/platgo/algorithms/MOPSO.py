import numpy as np

from .. import GeneticAlgorithm, utils, operators


class MOPSO(GeneticAlgorithm):
    type = {"n_obj": "multi", "encoding": "real", "special": ""}

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=40000,
        div=10,
        name="MOPSO",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(MOPSO, self).__init__(
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
        self.div = div

    def run_algorithm(self):
        # Generate random population
        Pop = self.problem.init_pop()
        self.cal_obj(Pop)
        Archive = self.UpdateArchive(Pop, self.problem.pop_size, self.div)
        Pbest = Pop.copy()

        while self.not_terminal(Archive):
            REP = self.REPSelection(Archive.objv, Pop.pop_size, self.div)
            Pop = operators.OperatorPSO(Pop, Pbest, Archive[REP])
            self.cal_obj(Pop)
            Archive = self.UpdateArchive(Archive + Pop, Pop.pop_size, self.div)
            Pbest = self.UpdatePbest(Pbest, Pop)
        return Pop

    def UpdateArchive(self, Archive, N, div):
        # Find the non-dominated solutions
        frontno, _ = utils.nd_sort(Archive.objv, 1)
        Archive = Archive[frontno == 1]

        # Grid-based retention
        if len(Archive) > N:
            Del = self.Delete(Archive.objv, len(Archive) - N, div)
            np.delete(Archive, Del, None)
        return Archive

    def Delete(self, PopObj, K, div):
        N = PopObj.shape[0]

        # Calculate the grid location of each solution
        fmax = PopObj.max(0)
        fmin = PopObj.min(0)
        d = (fmax - fmin) / div
        GLoc = np.floor((PopObj - np.tile(fmin, (N, 1))) / np.tile(d, (N, 1)))
        GLoc[GLoc >= div] = div - 1
        GLoc[np.isnan(GLoc)] = 0

        # Calculate the crowding degree of each grid
        _, _, Site = np.unique(
            GLoc, return_index=True, return_inverse=True, axis=0
        )
        CrowdG, _ = np.histogram(Site, bins=np.arange(np.max(Site) + 2))
        # Delete K solutions
        Del = np.zeros(N, dtype=bool)
        while np.sum(Del) < K:
            # Select the most crowded grid
            maxGrid = np.argwhere(CrowdG == max(CrowdG)).flatten()
            Temp = np.random.randint(0, high=len(maxGrid))
            Grid = maxGrid[Temp]
            # And delete one solution randomly from the grid
            InGrid = np.argwhere(Site == Grid).flatten()
            Temp = np.random.randint(0, high=len(InGrid))
            p = InGrid[Temp]
            Del[p] = True
            Site = Site.astype(float)
            Site[p] = np.nan
            CrowdG[Grid] = CrowdG[Grid] - 1

        return Del

    def REPSelection(self, PopObj, N, div):
        NoP = PopObj.shape[0]
        # Calculate the grid location of each solution
        fmax = PopObj.max(0)
        fmin = PopObj.min(0)
        d = (fmax - fmin) / div
        fmin = np.tile(fmin, (NoP, 1))
        d = np.tile(d, (NoP, 1))
        GLoc = np.floor((PopObj - fmin) / d)
        GLoc[GLoc >= div] = div - 1
        GLoc[np.isnan(GLoc)] = 0
        # Detect the grid of each solution belongs to
        _, _, Site = np.unique(
            GLoc, return_index=True, return_inverse=True, axis=0
        )

        # Calculate the crowd degree of each grid
        CrowdG, _ = np.histogram(Site, bins=np.arange(np.max(Site) + 2))

        # Roulette-wheel selection
        TheGrid = utils.roulette_wheel_selection(N, None, CrowdG)
        REP = np.zeros((N), dtype=np.int64)
        for i in range(len(REP)):
            InGrid = np.argwhere(Site == TheGrid[i]).flatten()
            Temp = np.random.randint(len(InGrid))
            REP[i] = InGrid[Temp]
        return REP

    def UpdatePbest(self, Pbest, Pop):
        temp = Pbest.objv - Pop.objv
        Dominate = np.any(temp < 0, axis=1).astype(np.int64) - np.any(
            temp > 0, axis=1
        ).astype(np.int64)
        Pbest[Dominate == -1] = Pop[Dominate == -1]
        temp = np.random.random(len(Dominate))
        Pbest[np.logical_and(Dominate == 0, temp < 0.5)] = Pop[
            np.logical_and(Dominate == 0, temp < 0.5)
        ]
        return Pbest
