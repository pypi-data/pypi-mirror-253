import numpy as np
from ...common.commons import AlgoMode
from .. import GeneticAlgorithm, utils, operators, Population
from scipy.stats import norm
from scipy.spatial.distance import cdist
from pydacefit.corr import corr_gauss
from pydacefit.dace import DACE, regr_linear


class EGO(GeneticAlgorithm):
    type = {
        "n_obj": "single",
        "encoding": "real",
        "special": "expensive"
    }

    def __init__(
            self,
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=500,
            name="EGO",
            show_bar=False,
            sim_req_cb=None,
            IFEs=None,
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
                "outputs": ["f1", "f2"],
                "variables": [],
                "objectives": [
                    {"objective": "f1", "option": "MinimizeValue"},
                    {"objective": "f2", "option": "MinimizeValue"}
                    ],
                "constraints": []
            }
        options: 算法参数
        simulation_request_callback: 仿真回调函数
        max_fe: 最大迭代次数
        name: 名称
        show_bar: 是否显示进度条
        """
        super(EGO, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            algo_mode=algo_mode,
            debug=debug
        )
        self.IFEs = IFEs

    def run_algorithm(self):
        # self._max_fe = self._max_fe * self.problem.pop_size
        IFEs = self.IFEs
        N = 10 * self.problem.n_var
        PopDec, _ = utils.uniform_point(N, self.problem.n_var, 'Latin')

        dec = np.tile(np.array(self.problem.ub) - np.array(self.problem.lb),
                      (N, 1)) * PopDec + np.tile(self.problem.lb, (N, 1))
        pop = Population(decs=dec)
        self.cal_obj(pop)
        # self._gen += len(pop)
        theta = 10 * np.ones(shape=(1, self.problem.n_var))
        print(self._gen)

        while self.not_terminal(pop):
            # self._gen -= 1
            N, D = pop.decs.shape
            if N > 11 * D - 1:
                index = np.argsort(pop.objv, kind='mergesort', axis=0)
                Next = index[0: 11 * D - 1]
            else:
                Next = np.ones(shape=(N, 1))
                Next = Next.astype(bool)
            PDec = pop[Next].decs.copy()
            PObj = pop[Next].objv.copy()

            dacefit_with_ard = DACE(regr=regr_linear, corr=corr_gauss, theta=theta.flatten(), thetaL=(  # noqa
                                                                                                         1e-5) * np.ones(
                shape=(1, D)).flatten(), thetaU=20 * np.ones(shape=(1, D)).flatten())  # noqa
            dacefit_with_ard.fit(pop.decs, pop.objv)

            theta = dacefit_with_ard.model["theta"].copy()
            PopDec = EvolEI(PDec, PObj, dacefit_with_ard, IFEs, self.problem)
            if checkExist(pop.decs, PopDec):
                tmp = Population(decs=np.array([PopDec]))
                self.cal_obj(tmp)
                # self._gen += len(tmp)
                pop = pop + tmp
                print(np.min(pop.objv))
                print(self._gen)
            print(self._gen)
        return pop


def checkExist(AllDec, PopDec):
    notExist = True
    if np.any(cdist(AllDec, np.array([PopDec])) < (1e-12)):
        notExist = False
    return notExist


def EvolEI(Dec, Obj, model, IFEs, problem):
    Off = np.vstack((operators.OperatorGA(Dec[utils.tournament_selection(
        2, Dec.shape[0], Obj.flatten()), :], problem), operators.OperatorGA(Dec, problem, 0, 0, 1, 20)))  # noqa

    N = Off.shape[0]
    EI = np.zeros(shape=(N, 1))
    Gbest = np.min(Obj)
    E0 = np.inf
    while IFEs > 0:
        for i in range(N):
            y, mse = model.predict(np.array([Off[i, :]]), return_mse=True)
            s = np.sqrt(mse)
            EI[i] = -(Gbest - y) * norm.cdf((Gbest - y) / s) - \
                    s * norm.pdf((Gbest - y) / s)
        index = np.argsort(EI.flatten(), kind='mergesort')
        if EI[index[0]] < E0:
            Best = Off[index[0], :]
            E0 = EI[index[0]]
        Parent = Off[index[0: int(np.ceil(N / 2))], :]
        Off = np.vstack((operators.OperatorGA(Parent[utils.tournament_selection(2, Parent.shape[0], EI[  # noqa
            index[0: int(np.ceil(N / 2))]].flatten()), :], problem),
                         operators.OperatorGA(Parent, problem, 0, 0, 1, 20)))
        IFEs -= Off.shape[0]
    PopDec = Best
    return PopDec
