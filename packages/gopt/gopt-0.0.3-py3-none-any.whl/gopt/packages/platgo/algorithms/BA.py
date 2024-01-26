import numpy as np

from gopt.packages.platgo import utils

from ...common.commons import AlgoMode
from .. import GeneticAlgorithm, Population


class BA(GeneticAlgorithm):
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
        simulation_request_callback,
        max_fe=10000,
        name="BA",
        show_bar=False,
        sim_req_cb=None,
        algo_mode=AlgoMode.ACADEMIC,
        debug=False
    ):
        """
        pop_size: 种群大小
        optimization_problem: 优化问题
        e.g.
            optimization_problem = {
                "inputs": [
                    {"param": "x1", "min":0, "max": 1},
                    {"param": "x2", "min":0, "max": 1},
                    {"param": "x3", "min":0, "max": 1}
                ],
                "outputs": ["f1"],
                "variables": [],
                "objectives": [
                    {"objective": "f1", "option": "MinimizeValue"}
                    ],
                "constraints": []
            }
        options: 算法参数
        simulation_request_callback: 仿真回调函数
        maxiter: 最大迭代次数
        name: 名称
        show_bar: 是否显示进度条
        """
        super(BA, self).__init__(
            pop_size,
            options,
            optimization_problem,
            simulation_request_callback,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            algo_mode=algo_mode,
            debug=debug
        )
        self.maxiter = int(self._max_fe/self.problem.pop_size)
        self.r = np.array(np.zeros(self.maxiter))
        self.gamma = 0.9
        self.beta = np.random.random()
        self.alpha = 0.9
        self.A = np.array(np.ones(self.maxiter))
        self.fmin = 0
        self.fmax = 100
        self.gen = int(self._gen/self.problem.pop_size)

    def run_algorithm(self):
        while(self.r[0] == 0):
            self.r[0] = np.random.uniform(0, 0.1)
        for i in range(1, self.maxiter):
            self.r[i] = self.r[0] * (1 - np.exp(-self.gamma * self.gen))
            self.A[i] = self.A[i-1] * self.alpha
        Pop = self.problem.init_pop()
        self.cal_obj(Pop)
        Pbest = Pop.copy()
        best = np.argmin(utils.fitness_single(Pbest))
        Gbest = Pbest[np.array([best])]
        while self.not_terminal(Pop):
            off = self.OperatorBA(Pop, Pbest, Gbest)
            replace = utils.fitness_single(Pop) > utils.fitness_single(off)
            Pop[replace] = off[replace]
            replace = utils.fitness_single(Pbest) > utils.fitness_single(Pop)
            Pbest[replace] = Pop[replace]
            best = np.argmin(utils.fitness_single(Pbest))
            Gbest = Pbest[np.array([best])]
        return Pop

    def OperatorBA(self, Particle, Pbest, Gbest):
        ParticleDec = Particle.decs
        PbestDec = Pbest.decs
        GbestDec = Gbest.decs
        N, D = ParticleDec.shape
        f = self.fmin + (self.fmax - self.fmin) * self.beta
        ParticleVel = np.zeros((N, D))
        # Particle swarm optimization
        # r1 = np.tile(np.random.random((N, 1)), (1, D))
        # r2 = np.tile(np.random.random((N, 1)), (1, D))
        # OffVel = (
        #     ParticleVel
        #     + f * (PbestDec - ParticleDec)
        #     + r2 * (GbestDec - ParticleDec)
        # )
        OffVel = ParticleVel
        tempr = np.random.random()
        if self.gen >= self.maxiter:
            self.gen = self.maxiter-1
        if tempr > self.r[self.gen]:
            OffVel = (0.4*ParticleVel + f * (PbestDec - ParticleVel))
        if 0.5*np.random.random() < self.A[self.gen]:
            OffVel = OffVel + 0.5*np.random.uniform(-1, 1) * (GbestDec - ParticleDec)  # noqa
        OffDec = ParticleDec + OffVel
        Offspring = Population(decs=OffDec, vel=OffVel)
        self.cal_obj(Offspring)
        return Offspring
