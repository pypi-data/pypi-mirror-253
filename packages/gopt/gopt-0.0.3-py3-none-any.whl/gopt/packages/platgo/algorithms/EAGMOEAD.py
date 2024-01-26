
import numpy as np
from scipy.spatial.distance import cdist
from ..GeneticAlgorithm import GeneticAlgorithm
from .. import utils
from ..operators.OperatorGAhalf import OperatorGAhalf


class EAGMOEAD(GeneticAlgorithm):

    type = {
        "n_obj": {"multi", "many"},
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
        debug=False,
        LGs=8
    ):
        super(EAGMOEAD, self).__init__(
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
        self.LGs = LGs

    def run_algorithm(self):
        W, N = utils.uniform_point(
            self.problem.pop_size, self.problem.n_obj, method="MUD")
        T = max(N//10, 2)
        B = cdist(W, W)
        B = np.argsort(B)

        B = B[:, :T]

        pop = self.problem.init_pop()
        self.cal_obj(pop)
        archive = pop
        s = np.zeros((self.problem.pop_size, self.LGs))

        while self.not_terminal(archive):
            matingpool, offspring_loc = self.mating_selection(B, s)
            # offspring = self.xov(pop,matingpool[:len(matingpool)//2], matingpool[len(matingpool)//2:])  # noqa
            # offspring = self.mut(offspring)
            offspring = OperatorGAhalf(pop[matingpool], self.problem)
            self.cal_obj(offspring)
            pop = self.update_pop(pop, offspring, offspring_loc, W, B)
            archive, sucess = self.update_archive(archive, offspring)

            if any(sucess):
                p, _ = np.histogram(offspring_loc[sucess], np.arange(self.problem.pop_size+1))  # noqa
                s[:, np.mod(self._gen, self.LGs)] = p

        return archive

    def mating_selection(self, B, s):
        N, T = B.shape
        s = np.sum(s, 1) + 1e-6
        D = s/sum(s) + 0.002
        offspring_loc = utils.roulette_wheel_selection(N=N, fitness=1/D)

        matingpool = np.zeros(2*N)
        for i in range(N):
            per = np.random.choice(T, 2, replace=False)
            matingpool[i] = B[offspring_loc[i], per[0]]
            matingpool[i+N] = B[offspring_loc[i], per[1]]
        matingpool = matingpool.astype(np.int32)
        return matingpool, offspring_loc

    def update_pop(self, pop, off, loc, W, B):
        for i in range(len(off)):
            g_old = np.sum(pop[B[loc[i]]].objv * W[B[loc[i]]], 1).flatten()
            g_new = np.dot(W[B[loc[i]]], (off[i].objv).T).flatten()
            pop[B[loc[i]][g_old >= g_new]] = off[i]
        return pop

    def update_archive(self, archive, off):
        N = len(archive)
        archive = archive + off
        front_no, max_front = utils.nd_sort(archive.objv, N)
        next = front_no < max_front
        last = np.argwhere(front_no == max_front)
        crowd_dis = utils.crowding_distance(archive[last].objv)
        rank = np.argsort(-crowd_dis, axis=0)
        next[last[rank[:N-np.sum(next)]]] = True

        archive = archive[next]
        sucess = next[N:]

        return archive, sucess
