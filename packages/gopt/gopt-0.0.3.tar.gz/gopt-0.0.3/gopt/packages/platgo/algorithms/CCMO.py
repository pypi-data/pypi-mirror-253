import numpy as np

from scipy.spatial.distance import cdist
from ..utils import tournament_selection
from ..operators import OperatorGAhalf, OperatorDE
from ..GeneticAlgorithm import GeneticAlgorithm
from ..Population import Population


class CCMO(GeneticAlgorithm):
    type = {
        "n_obj": "multi",
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": "constrained",
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        simulation_request_callback,
        max_fe=10000,
        name=None,
        show_bar=False,
        sim_req_cb=None,
        debug=False,
        ope=1,
    ):
        super(CCMO, self).__init__(
            pop_size,
            options,
            optimization_problem,
            simulation_request_callback,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug,
        )
        self.ope = ope if ope is not None else 1

    def run_algorithm(self):
        pop1 = self.problem.init_pop()
        self.cal_obj(pop1)
        fitness1 = cal_fitness(pop1.objv, pop1.cv)
        pop2 = self.problem.init_pop()
        self.cal_obj(pop2)
        fitness2 = cal_fitness(pop2.objv)

        while self.not_terminal(pop1):
            if self.ope == 1:
                matingpool1 = tournament_selection(
                    2, pop1.pop_size, fitness1
                )  # noqa
                matingpool2 = tournament_selection(
                    2, pop2.pop_size, fitness2
                )  # noqa
                offspring1 = OperatorGAhalf(pop1[matingpool1], self.problem)
                self.cal_obj(offspring1)
                offspring2 = OperatorGAhalf(pop2[matingpool2], self.problem)
                self.cal_obj(offspring2)

            elif self.ope == 2:
                matingpool1 = tournament_selection(
                    2, 2 * pop1.pop_size, fitness1
                )  # noqa
                matingpool2 = tournament_selection(
                    2, 2 * pop2.pop_size, fitness2
                )  # noqa
                offspring1 = OperatorDE(
                    pop1,
                    pop1[matingpool1[: pop1.pop_size]],
                    pop1[matingpool1[pop1.pop_size:]],
                    self.problem,
                )  # noqa
                self.cal_obj(offspring1)
                offspring2 = OperatorDE(
                    pop2,
                    pop1[matingpool2[: pop2.pop_size]],
                    pop1[matingpool2[pop2.pop_size:]],
                    self.problem,
                )  # noqa
                self.cal_obj(offspring2)

            temp1 = pop1 + offspring1 + offspring2
            pop1, fitness1 = enviromnent_selection(temp1, pop1.pop_size, True)
            temp2 = pop2 + offspring1 + offspring2
            pop2, fitness2 = enviromnent_selection(temp2, pop2.pop_size, False)
        return pop1


def cal_fitness(objv: np.ndarray, cv: np.ndarray = None) -> np.ndarray:
    N = objv.shape[0]
    if cv is None:
        cv = np.zeros((N, 1))
    else:
        cv = np.sum(np.where(cv > 0, cv, 0), axis=1)

    # detect the dominance relation between each two solutions
    dominance = np.zeros((N, N), dtype=bool)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if cv[i] < cv[j]:
                dominance[i][j] = True
            elif cv[i] > cv[j]:
                dominance[j][i] = True
            else:
                k = int(np.any(objv[i] < objv[j])) - int(
                    np.any(objv[i] > objv[j])
                )  # noqa
                if k == 1:
                    dominance[i][j] = True
                elif k == -1:
                    dominance[j][i] = True

    # 计算S(i)
    s = np.sum(dominance, axis=1)
    # 计算R(i)
    r = np.zeros(N)
    for i in range(N):
        r[i] = np.sum(s[dominance[:, i]])
    # 计算D(i)
    distance = cdist(objv, objv)
    distance[np.eye(len(distance), dtype=bool)] = np.inf
    distance = np.sort(distance, axis=1)
    d = 1 / (distance[:, int(np.floor(np.sqrt(N)) - 1)] + 2)
    # 计算fitness
    fitness = r + d

    return fitness


def enviromnent_selection(pop: Population, N: int, is_origin: bool):
    if is_origin:
        fitness = cal_fitness(pop.objv, pop.cv)
    else:
        fitness = cal_fitness(pop.objv)

    # 环境选择
    next = fitness < 1
    if np.sum(next) < N:
        rank = np.argsort(fitness)
        next[rank[:N]] = True
    elif np.sum(next) > N:
        delete = truncation(pop[next].objv, np.sum(next) - N)
        temp = np.argwhere(next)
        next[temp[delete]] = False

    pop = pop[next]
    fitness = fitness[next]

    ind = np.argsort(fitness)
    pop = pop[ind]
    fitness = fitness[ind]

    return pop, fitness


def truncation(objv, K):
    # 截断策略
    distance = cdist(objv, objv)
    distance[np.eye(len(distance), dtype=bool)] = np.inf
    delete = np.zeros(len(objv), dtype=bool)

    while np.sum(delete) < K:
        remain = np.argwhere(~delete).flatten()
        temp = distance[remain]
        temp = temp[:, remain]
        temp = np.sort(temp, axis=1)
        _, rank = np.unique(temp, return_index=True, axis=0)
        delete[remain[rank[0]]] = True

    return delete
