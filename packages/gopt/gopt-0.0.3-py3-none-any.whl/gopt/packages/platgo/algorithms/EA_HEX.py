import numpy as np

from .. import Population
from .. import GeneticAlgorithm


class Group(object):
    """置换群类"""

    def __init__(self, p):
        """给定排序，转为置换群"""
        if isinstance(p, dict):
            self.g = p.copy()
        else:
            group = dict()
            for i in range(len(p) - 1):
                group[p[i]] = p[i + 1]
            group[p[-1]] = p[0]
            self.g = group
            # self.g = {key: group[key] for key in sorted(group.keys())}
        self.cycle = None

    def inverse(self):
        inv_g = dict(zip(self.g.values(), self.g.keys()))
        inv_g = Group(inv_g)
        return inv_g

    def combine(self, m_g):
        new_g = dict()
        for k in self.g.keys():
            new_g[k] = m_g.g[self.g[k]]
        new_g = Group(new_g)
        return new_g

    def equal(self, m_g):
        for k in self.g.keys():
            if self.g[k] != m_g.g[k]:
                return False
        return True

    def to_permute(self, start=1):
        element = start
        permute = [element]
        for _ in range(len(self.g) - 1):
            element = self.g[element]
            if element in permute:
                return [-1]
            else:
                permute.append(element)
        return permute

    def to_permutes(self):
        permutes = []
        cycle = {key: 0 for key in self.g.keys()}
        element = self._get_zero_key(cycle)
        mark = 1
        while element != -1:
            permute = [element]
            for i in range(len(self.g)):
                cycle[element] = mark
                element = self.g[element]
                if element == permute[0]:
                    break
                else:
                    permute.append(element)
            permutes.append(permute)
            element = self._get_zero_key(cycle)
            mark += 1
        return permutes

    def create_cycle(self):
        """创建循环位置"""
        cycle = {key: 0 for key in self.g.keys()}
        element = self._get_zero_key(cycle)
        mark = 1
        while element != -1:
            permute = [element]
            for _ in range(len(self.g)):
                if element == self.g[element]:
                    cycle[element] = -1
                    mark -= 1
                    break
                cycle[element] = mark
                element = self.g[element]
                if element in permute:
                    break
                else:
                    permute.append(element)
            element = self._get_zero_key(cycle)
            mark += 1
        self.cycle = np.array(list(cycle.values()))

    def to_dist(self, group):
        """返回与另一个的不同性指标(不同边的个数)"""
        dist = 0
        for k in self.g.keys():
            if self.g[k] != group.g[k]:
                dist += 1
        return dist

    @staticmethod
    def _get_zero_key(dic):
        """获取该字典中value中第一个为0的key"""
        for key in dic.keys():
            if dic[key] == 0:
                return key
        return -1


class EA_HEX(GeneticAlgorithm):

    type = {
        "n_obj": "single",
        "encoding": {"real", "binary", "permutation"},
        "special": {"large/none", "constrained/none"},
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="EAX_HX",
        show_bar=False,
        sim_req_cb=None,
        ext_opt_prob_cb=None,
        debug=False,
        mode=0,
    ) -> None:

        super(EA_HEX, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            ext_opt_prob_cb=ext_opt_prob_cb,
            debug=debug,
        )
        self.mode = mode  # 修复模式, 0:启发式学习修复, 1:随机修复
        self.num_MAX = 2  # 交叉产生最大子代数量
        self.Q = 10
        self.rho = 0.3
        self.prob_mat = np.ones((self.problem.n_var, self.problem.n_var))

    def run_algorithm(self):
        # 初始化种群
        pop = self.problem.init_pop()
        # 计算目标值
        self.cal_obj(pop)
        while self.not_terminal(pop):
            # 对种群随机排序
            random_index = list(range(self.problem.pop_size))
            np.random.shuffle(random_index)
            pop.decs = pop.decs[random_index]
            pop.objv = pop.objv[random_index]

            for j in range(self.problem.pop_size):

                if j == self.problem.pop_size - 1:  # 最后一个和第一个个体交叉
                    pA, pB = pop.decs[-1], pop.decs[0]
                    pA_fv, pB_fv = pop.objv[-1], pop.objv[0]
                else:  # 相邻两个个体交叉
                    pA, pB = pop.decs[j], pop.decs[j + 1]
                    pA_fv, pB_fv = pop.objv[j], pop.objv[j + 1]

                # 交叉产生子代
                offspring = self.crossover(pA, pB, self.num_MAX)
                # 选择最优个体和其目标值
                c_best, best_fv = self.select_best(offspring)

                # 若子代最优解比父代A更优，则考虑加入种群
                if best_fv[0] < pA_fv[0]:
                    # 若子代最优解跟父代A更相似，则替换A，否则替换B
                    if self.get_dist(c_best, pA) < self.get_dist(c_best, pB):
                        if j == self.problem.pop_size - 1:
                            pop.decs[-1] = c_best
                            pop.objv[-1] = best_fv
                        else:
                            pop.decs[j] = c_best
                            pop.objv[j] = best_fv
                    # 若子代最优解跟父代B更相似，且比父代B更优，则替换B
                    elif (
                        self.get_dist(c_best, pA) > self.get_dist(c_best, pB)
                        and best_fv[0] < pB_fv[0]
                    ):
                        if j == self.problem.pop_size - 1:
                            pop.decs[0] = c_best
                            pop.objv[0] = best_fv
                        else:
                            pop.decs[j + 1] = c_best
                            pop.objv[j + 1] = best_fv

            # 更新概率表
            if self.mode == 0:
                self.update_prob_mat(pop.decs, pop.objv)
        return pop

    def update_prob_mat(self, decs, fvs):
        Delta_prob = np.zeros((decs.shape[1], decs.shape[1]))
        for i in range(decs.shape[1] - 1):
            Delta_prob[decs[:, i], decs[:, i + 1]] += self.Q / fvs.flatten()
        self.prob_mat = (1 - self.rho) * self.prob_mat + Delta_prob

    def get_dist(self, a, b):
        Ea = Group(a)
        Eb = Group(b)
        return Ea.to_dist(Eb)

    def select_best(self, offspring):
        pop = Population(pop_size=len(offspring), decs=offspring)
        self.cal_obj(pop)
        best_index = np.argmin(pop.objv[:, 0])
        best = offspring[best_index]
        best_fv = pop.objv[best_index]
        return best, best_fv

    def crossover(self, a, b, N_MAX=30):
        """交叉过程"""
        if (a == b).all():
            return np.array([a, b])
        Ea = Group(a)
        Eb = Group(b)
        inv_Eb = Eb.inverse()
        offspring = []  # 保存后代
        # 记录已选的边
        mark_a = np.zeros((len(a)), dtype=int)
        # 最多生成N_MAX个子代
        for _ in range(N_MAX):
            choice_index = np.where(mark_a == 0)[0]
            if len(choice_index) == 0:
                break
            element = np.random.choice(choice_index, 1)[0]
            new_Ea = Group(Ea.g)
            permute = [element]
            while True:
                if len(permute) > 1 and element == permute[0]:
                    break
                mark_a[element] = 1
                element = Ea.g[element]
                permute.append(element)
                new_Ea.g[inv_Eb.g[element]] = element
                element = inv_Eb.g[element]
                permute.append(element)
            new_a = new_Ea.to_permutes()
            # 若不能还原为完整序列，则需要启发式修复
            if len(new_a) > 1:
                if self.mode == 1:
                    new_a = self.random_repair(new_a)
                else:
                    new_a = self.heuristic_repair(new_a, self.prob_mat)
            else:
                new_a = new_a[0]
            offspring.append(new_a)
        offspring = np.array(offspring)
        return offspring

    @staticmethod
    def random_repair(permute_list):
        """随机方法修复序列"""
        np.random.shuffle(permute_list)
        permute = []
        for p in permute_list:
            permute.extend(p)
        return permute

    @staticmethod
    def heuristic_repair(permutes, prob_mat):
        """启发式方法修复序列"""
        np.random.shuffle(permutes)
        permute = []
        permute.extend(permutes[0])
        while len(permutes) > 1:
            prob = np.zeros(len(permutes))
            for i in range(1, len(permutes)):
                prob[i] = prob_mat[permutes[0][-1], permutes[i][0]]
            prob = prob / sum(prob)
            e_greed = 0.1  # 以一定概率随机探索
            if np.random.random() < e_greed:
                prob[1:] = np.ones(len(permutes) - 1) / (len(permutes) - 1)
            choice = np.random.choice(list(range(len(prob))), 1, p=prob)[0]
            permute.extend(permutes.pop(choice))
        return permute
