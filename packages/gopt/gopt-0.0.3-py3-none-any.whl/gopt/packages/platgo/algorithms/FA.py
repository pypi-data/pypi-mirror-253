import numpy as np
from gopt.packages.platgo import utils
from ...common.commons import AlgoMode
from .. import GeneticAlgorithm, Population


class FA(GeneticAlgorithm):
    type = {
        "n_obj": "single",
        "encoding": "real",
        "special": ""
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="FA",
        show_bar=False,
        sim_req_cb=None,
        algo_mode=AlgoMode.ACADEMIC,
        debug=False,
    ):
        super(FA, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            algo_mode=algo_mode,
            debug=debug,
        )
        self.alpha = 0.5
        self.beta0 = 1
        self.gamma = np.abs(np.random.normal(0, 1))

    def run_algorithm(self):
        W = 0.4
        Pop = self.problem.init_pop()
        self.cal_obj(Pop)
        Pbest = Pop.copy()
        best = np.argmin(utils.fitness_single(Pbest))
        Gbest = Pbest[np.array([best])]
        while self.not_terminal(Pop):
            off = self.OperatorFA(Pop, Pbest, Gbest, W)
            replace = utils.fitness_single(Pop) > utils.fitness_single(off)
            Pop[replace] = off[replace]
            replace = utils.fitness_single(Pbest) > utils.fitness_single(Pop)
            Pbest[replace] = Pop[replace]
            best = np.argmin(utils.fitness_single(Pbest))
            Gbest = Pbest[np.array([best])]
        return Pop

    def OperatorFA(self, Particle, Pbest, Gbest, W):
        ParticleDec = Particle.decs
        PbestDec = Pbest.decs
        GbestDec = Gbest.decs
        N, D = ParticleDec.shape
        ParticleVel = np.zeros((N, D))
        epsilon = np.random.normal(0, 1, (N, D))
        r = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                r[i, j] = np.linalg.norm(ParticleDec[i, :] - ParticleDec[j, :])
        # print(r)
        beta = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                beta[i, j] = self.beta0 * np.exp(- self.gamma * (r[i, j]**2))
        OffVel = (
            W * ParticleVel
            + np.dot(beta, (PbestDec - ParticleDec))
            + self.alpha * epsilon * (GbestDec - ParticleDec)
        )
        OffDec = ParticleDec + OffVel
        Offspring = Population(decs=OffDec, vel=OffVel)
        self.cal_obj(Offspring)
        return Offspring
