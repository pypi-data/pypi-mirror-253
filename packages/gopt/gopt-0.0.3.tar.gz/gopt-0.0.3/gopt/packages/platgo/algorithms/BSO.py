import numpy as np
from ...common.commons import AlgoMode
from .. import GeneticAlgorithm
from ..Population import Population


class BSO(GeneticAlgorithm):
    type = {"n_obj": "single", "encoding": "real", "special": ""}

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="BSO",
        show_bar=False,
        sim_req_cb=None,
        algo_mode=AlgoMode.ACADEMIC,
        debug=False,
    ):
        super(BSO, self).__init__(
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

    def run_algorithm(self):
        """
         main function for Different Evolution
         if population is None, generate a new population with N
        :param N: population size
        :param population: population to be optimized
        :return:
        """
        # Problem parameters
        dim = self.problem.n_var
        # BSO-OS hyper-parameters
        maxe = self._max_fe  # max number of evaluation
        num = self.problem.pop_size  # number of sampling
        pe = 0.2  # percentage_elitist
        # pdd = 0.2  # determine whether a dimension is disrupted or not
        pd = 1  # disrupting elitists. one elitis
        # every 5 generations, and only one dimension
        pre = 0.2  # probability for select elitist, not normals,
        # to generate new individual
        po = 0.8  # probability for select one individual, not two,
        # to generate new individual
        ls = maxe / 20  # slope of the s-shape function
        Lambda = 0.5  # decay factor
        nelite = np.round(num * pe)  # number of elitist
        # nnorm = num - nelite  # number of normals
        # Initialization
        step_size = np.ones(dim)  # step size for search
        archi = self.problem.init_pop()  # archieve to store sampling solutions
        self.cal_obj(archi)

        # tem_archi = np.ones((num, dim))  # temporary archieve

        ne = 0  # counter for number of evalution
        bestf = []  # store best fitness for each iteration
        fitness_sol = np.ones(num)  # store
        tem_sol = np.ones(dim)
        while self.not_terminal(archi):
            # start the main loop of the BSO algorithm
            cycle = self._gen
            if cycle > 1:  # do not do disruption for the first iteration
                # disrupt every iteration but for one dim of one solution
                r_1 = np.random.rand()
                if (
                    r_1 < pd
                ):  # decide whether to select one individual to be disrupted
                    idx = int(np.floor(num * np.random.rand()))
                    tem_sol = archi[idx]
                    # tem_sol[int(np.floor(dim * np.random.rand()))] = lbound +
                    #  (ubound - lbound) * np.random.rand()
                    # fv = benchmark_func(tem_sol,index)
                    fv = tem_sol.objv
                    ne += 1
                    archi[idx] = tem_sol
                    fitness_sol[idx] = fv
            # sort solutions in an archieve based on their function value
            idxsort = np.argsort(fitness_sol)
            # record the best function value in each generation
            bestf.append(fitness_sol[idxsort[0]])
            # calculate s-shape function
            mu = self.sigmoid((Lambda * maxe - ne) / ls)

            # generate num new solutions by adding Gaussian random values
            for i in range(0, num):
                r_1 = np.random.rand()
                if r_1 < pre:  # select elitists to generate a new solution
                    r = np.random.rand()
                    ind_one = int(np.floor(nelite * np.random.rand()))
                    ind_two = int(np.floor(nelite * np.random.rand()))
                    while ind_one == ind_two:
                        ind_one = int(np.floor(nelite * np.random.rand()))
                        ind_two = int(np.floor(nelite * np.random.rand()))
                    if r < po:  # use one elitist
                        tem_sol = archi[np.int(idxsort[ind_one])]
                    else:  # use two elitists
                        rat = np.random.rand()
                        tem_soldec = (
                            rat * archi.decs[idxsort[ind_one]]
                            + (1 - rat) * archi.decs[idxsort[ind_two]]
                        )
                        # tem_sol=self.cal_obj(tem_soldec)
                        tem_sol = Population(decs=tem_soldec.reshape(1, -1))
                        self.cal_obj(tem_sol)
                else:  # select normals to generate a new solution
                    r = np.random.rand()
                    ind_one = int(
                        num - 1 - np.floor(nelite * np.random.rand())
                    )
                    ind_two = int(
                        num - 1 - np.floor(nelite * np.random.rand())
                    )
                    while ind_one == ind_two:
                        ind_one = int(
                            num - 1 - np.floor(nelite * np.random.rand())
                        )
                        ind_two = int(
                            num - 1 - np.floor(nelite * np.random.rand())
                        )
                    if r < po:
                        tem_sol = archi[np.int(idxsort[ind_one])]
                    else:
                        rat = np.random.rand()
                        tem_soldec = (
                            rat * archi.decs[idxsort[ind_one]]
                            + (1 - rat) * archi.decs[idxsort[ind_two]]
                        )
                        # tem_sol=self.cal_obj(tem_soldec)
                        tem_sol = Population(decs=tem_soldec.reshape(1, -1))
                        self.cal_obj(tem_sol)

                # add Gaussian disturbance to the tem_sol
                # to generate a new solution
                step_size = mu * np.random.rand(dim)
                tem_soldec = tem_sol.decs + step_size * np.random.normal(
                    0, 1, dim
                )
                tem_sol = Population(decs=tem_soldec)
                self.cal_obj(tem_sol)
                # selection between new one and the old one with
                # the same index in archieve
                fv = tem_sol.objv
                ne += 1
                if fv < fitness_sol[i]:  # reserve the better one
                    fitness_sol[i] = fv
                    archi[i] = tem_sol
        return archi

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
