"""
------------------------------- Reference --------------------------------
 H. Jain and K. Deb, An evolutionary many-objective optimization algorithm
 using reference-point based non-dominated sorting approach, part II:
 Handling constraints and extending to an adaptive approach, IEEE
 Transactions on Evolutionary Computation, 2014, 18(4): 602-622.
"""

import numpy as np

from scipy.spatial.distance import cdist
from .. import GeneticAlgorithm, utils, operators


class C_MOEA_D(GeneticAlgorithm):
    type = {
        "n_obj": {"multi", "many"},
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
        name="C_MOEA_D",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(C_MOEA_D, self).__init__(
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
        # Generate the weight vectors
        W, N = utils.uniform_point(self.problem.pop_size, self.problem.n_obj)
        T = int(np.ceil(N / 10))
        nr = int(np.ceil(N / 100))
        # Detect the neighbours of each solution
        B = cdist(W, W)
        B = np.argsort(B, axis=1)
        B = B[:, :T]
        # Generate random Pop
        Pop = self.problem.init_pop(N)
        self.cal_obj(Pop)
        Z = np.min(Pop.objv, axis=0)

        # Optimization
        while self.not_terminal(Pop):
            # For each solution
            for i in range(N):
                # Choose the parents
                if np.random.random(1) < 0.9:
                    temp = np.arange(B.shape[1])
                    np.random.shuffle(temp)
                    P = B[i, temp].flatten()
                else:
                    P = np.arange(N)
                    np.random.shuffle(P)
                # Generate an offspring
                Offspring = operators.OperatorGAhalf(Pop[P[0:2]], self.problem)
                self.cal_obj(Offspring)
                # Update the ideal point
                Z = np.minimum(Z, Offspring.objv)
                # Calculate the constraint violation of offspring and P
                CVO = np.sum(np.maximum(0, Offspring.cv))
                CVP = np.sum(np.maximum(0, Pop[P].cv), axis=1)
                # Update the solutions in P by PBI approach
                normW = np.sqrt(np.sum(W[P, :] ** 2, axis=1))
                normP = np.sqrt(
                    np.sum(
                        (Pop[P].objv - np.tile(Z, (len(P), 1))) ** 2,
                        axis=1,
                    )
                )
                normO = np.sqrt(np.sum((Offspring.objv - Z) ** 2, axis=1))
                CosineP = (
                    np.sum(
                        (Pop[P].objv - np.tile(Z, (len(P), 1))) * W[P, :],
                        axis=1,
                    )
                    / normW
                    / normP
                )
                CosineO = (
                    np.sum(
                        np.tile(Offspring.objv - Z, (len(P), 1)) * W[P, :],
                        axis=1,
                    )
                    / normW
                    / normO
                )
                g_old = normP * CosineP + 5 * normP * np.sqrt(1 - CosineP**2)
                g_new = normO * CosineO + 5 * normO * np.sqrt(1 - CosineO**2)
                temp3 = np.logical_or(
                    np.logical_and(g_old >= g_new, CVP == CVO), CVP > CVO
                )
                Pop[
                    P[np.argwhere(temp3 == True)[:nr].flatten()]  # noqa
                ] = Offspring
        return Pop
