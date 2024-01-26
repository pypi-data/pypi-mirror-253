import numpy as np
from typing import Union

from ..Population import Population


class XovSbx:
    """
    自适应的模拟二进制交叉
    Reference
    [1] K. Deb, K. Sindhya, and T. Okabe, Self-adaptive simulated binary
    crossover for real-parameter optimization, Proceedings of the 9th Annual
    Conference on Genetic and Evolutionary Computation, 2007, 1187-1194.
    """

    def __init__(self, proC: float = 1, disC: int = 20, half=False) -> None:
        """
        :param proC: the probabilities of doing crossover
        :param disC: the distribution index of simulated binary crossover
        :param half: return half offspring
        """
        self.proC = proC
        self.disC = disC
        self.half = half

    def _sbx(
        self,
        pop: Population,
        p1: Union[np.ndarray, np.int64],
        p2: Union[np.ndarray, np.int64],
    ) -> Population:
        """
        根据索引向量对种群做交叉
        :param pop: 需要交叉的种群
        :param p1: 父代个体索引向量, shape=(n,), 或者对个体交叉,索引是单个数字
        :param p2: 父代个体索引向量
        :return: 返回交叉后的种群
        """
        N = p1.shape[0] if type(p1) == np.ndarray else 1
        D = pop.decs.shape[1]
        mu = np.random.random((N, D))
        beta = (2 - 2 * mu) ** (-1 / (self.disC + 1))
        beta[mu < 0.5] = (2 * mu[mu < 0.5]) ** (1 / (self.disC + 1))
        beta = beta * (-1) ** np.random.randint(0, 2, (N, D))
        beta[np.random.random((N, D)) < 0.5] = 1
        beta[
            np.random.random((N,)) > self.proC
        ] = 1  # noqa: E501 filter some rows by proC
        t1 = (pop.decs[p1] + pop.decs[p2]) / 2
        t2 = (pop.decs[p1] - pop.decs[p2]) / 2
        offdecs1 = t1 + beta * t2
        if self.half:  # only the first half of offspring are returned
            return Population(decs=offdecs1)
        offdecs2 = t1 - beta * t2
        return Population(decs=np.vstack((offdecs1, offdecs2)))

    def __call__(
        self,
        pop: Population,
        p1: Union[np.ndarray, np.int64],
        p2: Union[np.ndarray, np.int64],
    ) -> Population:
        """
        :param pop: 需要交叉的种群
        :param p1: 父代个体索引向量, shape=(n,)
        :param p2: 父代个体索引向量
        :return: 返回交叉后的种群
        """
        assert (
            p1.ndim <= 1 and p2.ndim <= 1
        ), "index vectors (p1,p2) must be one dim"  # noqa: E501
        # assert p1.shape[0] == p2.shape[0], "index vectors (p1,p2) must have the same length"  # noqa: E501
        offspring = self._sbx(pop, p1, p2)
        return offspring


if __name__ == "__main__":
    decs = np.random.rand(4, 4)
    population = Population(decs=decs)
    sbx = XovSbx()
    offspring = sbx(pop=population, p1=np.array([0, 1]), p2=np.array([2, 3]))
    print(population.decs)
    print(offspring.decs)
