import numpy as np

from gopt.packages.platgo import utils

from .. import GeneticAlgorithm, Population


class SMPSO(GeneticAlgorithm):
    type = {"n_obj": "multi", "encoding": "real", "special": ""}

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="SMPSO",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(SMPSO, self).__init__(
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
        Pop = self.problem.init_pop()
        self.cal_obj(Pop)
        Pbest = Pop
        Gbest, CrowdDis = self.UpdateGbest(Pop, Pop.pop_size)

        while self.not_terminal(Gbest):
            Pop = self.Operator(
                Pop,
                Pbest,
                Gbest[utils.tournament_selection(2, Pop.pop_size, -CrowdDis)],
            )
            Gbest, CrowdDis = self.UpdateGbest(Gbest + Pop, Pop.pop_size)
            Pbest = self.UpdatePbest(Pbest, Pop)
        return Pop

    def UpdateGbest(self, Gbest, N):
        # Update the global best set
        frontno, _ = utils.nd_sort(Gbest.objv, 1)
        Gbest = Gbest[frontno == 1]
        CrowdDis = utils.crowding_distance(Gbest)
        rank = np.argsort(CrowdDis)[::-1]
        Gbest = Gbest[rank[: np.minimum(N, len(Gbest))]]
        CrowdDis = CrowdDis[rank[: np.minimum(N, len(Gbest))]]
        return Gbest, CrowdDis

    def Operator(self, Particle, Pbest, Gbest):
        # Parameter setting
        ParticleDec = Particle.decs
        PbestDec = Pbest.decs
        GbestDec = Gbest.decs
        N, D = ParticleDec.shape
        ParticleVel = np.zeros((N, D))

        # Particle = Population(decs = ParticleDec, vel = ParticleVel)
        # Particle swarm optimization
        W = np.tile(np.random.uniform(0.1, 0.5, size=(N, 1)), (1, D))
        r1 = np.tile(np.random.random((N, 1)), (1, D))
        r2 = np.tile(np.random.random((N, 1)), (1, D))
        C1 = np.tile(np.random.uniform(1.5, 2.5, size=(N, 1)), (1, D))
        C2 = np.tile(np.random.uniform(1.5, 2.5, size=(N, 1)), (1, D))
        OffVel = (
            W * ParticleVel
            + C1 * r1 * (PbestDec - ParticleDec)
            + C2 * r2 * (GbestDec - ParticleDec)
        )
        phi = np.maximum(4, C1 + C2)
        OffVel = OffVel * 2 / np.abs(2 - phi - np.sqrt(phi**2 - 4 * phi))
        delta = np.tile(
            (np.array(self.problem.ub) - np.array(self.problem.lb)) / 2, (N, 1)
        )
        OffVel = np.maximum(np.minimum(OffVel, delta), -delta)
        OffDec = ParticleDec + OffVel
        # Deterministic back
        Lower = np.tile(np.array(self.problem.lb), (N, 1))
        Upper = np.tile(np.array(self.problem.ub), (N, 1))
        repair = np.logical_or(OffDec < Lower, OffDec > Upper)
        OffVel[repair] = 0.001 * OffVel[repair]
        OffDec = np.maximum(np.minimum(OffDec, Upper), Lower)
        # Polynomial mutation
        disM = 20
        Site1 = np.tile(np.random.random((N, 1)) < 0.15, (1, D))
        Site2 = np.random.random((N, D)) < 1 / D
        mu = np.random.random((N, D))
        temp = np.logical_and(np.logical_and(Site1, Site2), mu <= 0.5)
        OffDec[temp] = OffDec[temp] + (Upper[temp] - Lower[temp]) * (
            (
                2 * mu[temp]
                + (1 - 2 * mu[temp])
                * (  # noqa
                    1
                    - (OffDec[temp] - Lower[temp])
                    / (Upper[temp] - Lower[temp])
                )
                ** (disM + 1)
            )
            ** (1 / (disM + 1))
            - 1
        )  # noqa
        temp = np.logical_and(np.logical_and(Site1, Site2), mu > 0.5)
        OffDec[temp] = OffDec[temp] + (Upper[temp] - Lower[temp]) * (
            (
                2 * mu[temp]
                + (1 - 2 * mu[temp])
                * (  # noqa
                    1
                    - (OffDec[temp] - Lower[temp])
                    / (Upper[temp] - Lower[temp])
                )
                ** (disM + 1)
            )
            ** (1 / (disM + 1))
            - 1
        )  # noqa
        Offspring = Population(decs=OffDec, vel=OffVel)
        self.cal_obj(Offspring)

        return Offspring

    def UpdatePbest(self, Pbest, Pop):
        replace = ~np.all(Pop.objv >= Pbest.objv, axis=1)
        Pbest[replace] = Pop[replace]
        return Pbest
