import numpy as np
from scipy.spatial.distance import cdist
from ..GeneticAlgorithm import GeneticAlgorithm
from .. import utils, operators


class MSEA(GeneticAlgorithm):
    type = {
        "n_obj": "multi",
        "encoding": {"real", "binary", "permutation", "label", "vrp", "two_permutation"}, # noqa
        "special": ""
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
        debug=False
    ):
        super(MSEA, self).__init__(
            pop_size,
            options,
            optimization_problem,
            simulation_request_callback,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug
        )
        self.xov = operators.XovSbx()  # 模拟二进制交叉
        self.mut = operators.MutPol(self.problem)  # 多项式变异

    def run_algorithm(self):
        pop = self.problem.init_pop()
        self.cal_obj(pop)
        front_no, _ = utils.nd_sort(pop.objv, len(pop))

        while self.not_terminal(pop):
            # normalize the pop
            pop_obj = pop.objv
            fmax = np.max(pop_obj[front_no == 1], axis=0)
            fmin = np.min(pop_obj[front_no == 1], axis=0)
            pop_obj = (pop_obj-fmin)/(fmax-fmin)

            dis = cdist(pop_obj, pop_obj)
            dis[np.eye(len(dis), dtype=bool)] = np.inf

            # local search
            for i in range(self.problem.pop_size):
                s_dis = np.sort(dis, axis=1)
                div = s_dis[:, 0] + 0.001 * s_dis[:, 1]
                if np.max(front_no) > 1:
                    mating_pool = utils.tournament_selection(2, 2, front_no, np.sum(pop_obj, axis=1))  # noqa
                elif np.min(div) < np.max(div) / 2:
                    mating_pool1 = np.argmax(div)
                    mating_pool2 = utils.tournament_selection(2, 1, -div)
                    mating_pool = np.hstack((np.array([mating_pool1]), mating_pool2))  # noqa
                else:
                    mating_pool1 = utils.tournament_selection(2, 1, np.sum(pop_obj, axis=1))  # noqa
                    mating_pool2 = utils.tournament_selection(2, 1, -div)
                    mating_pool = np.hstack((mating_pool1, mating_pool2))
                off = operators.OperatorGAhalf(pop[mating_pool], self.problem)  # noqa
                self.cal_obj(off)
                off_obj = (off.objv-fmin) / (fmax-fmin)

                # non-dominated sort
                new_front = self._update_front(np.vstack((pop_obj, off_obj)), front_no)  # noqa
                if new_front[-1] > 1:
                    continue

                # cal the dis
                off_dis = cdist(off_obj, pop_obj)[0]

                if np.max(new_front) > 1:
                    stage = 1
                elif np.min(div) < np.max(div)/2:
                    stage = 2
                else:
                    stage = 3

                # update the pop
                replace = False
                if stage == 1:

                    worse = np.argwhere(new_front == np.max(new_front)).flatten()  # noqa
                    q = np.argmax(np.sum(pop_obj[worse], axis=1))
                    q = worse[q]
                    off_dis[q] = np.inf
                    replace = True
                elif stage == 2:

                    q = np.argmin(div)
                    off_dis[q] = np.inf
                    s_dis = np.sort(off_dis)
                    o_div = s_dis[0] + 0.01 * s_dis[1]
                    if o_div >= div[q]:
                        replace = True
                else:

                    q = np.argmin(off_dis)
                    off_dis[q] = np.inf
                    s_dis = np.sort(off_dis)
                    o_div = s_dis[0] + 0.01 * s_dis[1]
                    if np.sum(off_obj) <= np.sum(pop_obj[q]) and o_div >= div[q]:  # noqa
                        replace = True

                if replace:
                    front_no = self._update_front(np.vstack((pop_obj, off_obj)), new_front, q)  # noqa
                    if q == 0:
                        front_no = np.hstack((np.array([front_no[-1]]), front_no[:-1]))  # noqa
                    else:
                        front_no = np.hstack((front_no[:q], np.array([front_no[-1]]), front_no[q:-1]))  # noqa
                    # update pop
                    pop[q] = off
                    pop_obj[q] = off_obj

                    # update dis
                    dis[q] = off_dis
                    dis[:, q] = off_dis
        return pop

    def _update_front(self, objv, front_no, x=None):
        N, M = objv.shape
        if x is None:
            # add a new solution
            front_no = np.hstack((front_no, np.array([0])))
            move = np.zeros(N, dtype=bool)
            move[-1] = True
            current_f = 1
            while True:
                dominated = False
                for i in range(N-1):
                    if front_no[i] == current_f:
                        m = 0
                        while m < M and objv[i, m] <= objv[-1, m]:
                            m += 1
                        dominated = m + 1 > M
                        if dominated:
                            break
                if ~dominated:
                    break
                else:
                    current_f += 1
            while any(move):
                next_move = np.zeros(N, dtype=bool)
                for i in range(N):
                    if front_no[i] == current_f:
                        dominated = False
                        for j in range(N):
                            if move[j]:
                                m = 0
                                while m < M and objv[j, m] <= objv[i, m]:
                                    m += 1
                                dominated = m+1 > M
                                if dominated:
                                    break
                        next_move[i] = dominated
                front_no[move] = current_f
                current_f += 1
                move = next_move
        else:

            move = np.zeros(N, dtype=bool)
            move[x] = True
            current_f = front_no[x] + 1
            while any(move):
                next_move = np.zeros(N, dtype=bool)
                for i in range(N):
                    if front_no[i] == current_f:
                        dominated = False
                        for j in range(N):
                            if move[j]:
                                m = 0
                                while m < M and objv[j, m] <= objv[i, m]:
                                    m += 1
                                dominated = m+1 > M
                                if dominated:
                                    break
                        next_move[i] = dominated
                for i in range(N):
                    if next_move[i]:
                        dominated = False
                        for j in range(N):
                            if front_no[j] == (current_f - 1) and ~move[j]:
                                m = 0
                                while m < M and objv[j, m] <= objv[i, m]:
                                    m += 1
                                dominated = m+1 > M
                                if dominated:
                                    break
                        next_move[i] = ~dominated
                front_no[move] = current_f - 2
                current_f += 1
                move = next_move
            front_no = np.hstack((front_no[:x], front_no[x+1:]))

        return front_no
