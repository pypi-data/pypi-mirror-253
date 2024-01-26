'''
------------------------------- Reference --------------------------------
 P. T. Boggs and J. W. Tolle, Sequential quadratic programming
 ActaNumerica, 1995, 4(1): 1-51.  #noqa
'''

import numpy as np

from .. import GeneticAlgorithm, Population


class SQP(GeneticAlgorithm):
    type = {
        "n_obj": "single",
        "encoding": "real",
        "special": {"large/none", "constrained/none"}
    }

    def __init__(
        self,
        pop_size,
        options,
        optimization_problem,
        control_cb,
        max_fe=10000,
        name="SQP",
        show_bar=False,
        sim_req_cb=None,
        debug=False,
    ):
        super(SQP, self).__init__(
            pop_size,
            options,
            optimization_problem,
            control_cb,
            max_fe=max_fe,
            name=name,
            show_bar=show_bar,
            sim_req_cb=sim_req_cb,
            debug=debug
        )
        self.ro = 0.5
        self.gk = None
        self.eta = 0.1
        self.sigma = 0.8

    def run_algorithm(self):
        pop = self.problem.init_pop(1)
        self.cal_obj(pop)
        dfk, Ai = self.FiniteDifference(pop)
        Bk = np.eye(self.problem.n_var)
        lam = np.zeros((1, pop.cv.shape[1]))
        while self.not_terminal(pop):
            _, dk, mu, _ = qpsubp(dfk, Bk, [], [], Ai, -pop.cv.T)
            if mu.size == 0 and lam.size > 0:
                tau = max(0, np.linalg.norm(lam, ord=np.inf))
            elif mu.size > 0 and lam.size == 0:
                tau = max(np.linalg.norm(mu, ord=np.inf), 0)
            elif mu.size == 0 and lam.size == 0:
                tau = 0
            else:
                tau = max(np.linalg.norm(mu, ord=np.inf),
                          np.linalg.norm(lam, ord=np.inf))
            if self.sigma * (tau + 0.05) >= 1:
                self.sigma = 1 / (tau + 2 * 0.05)
            for mk in range(21):
                temp = self.eta * self.ro ** mk * \
                    dphi1(pop, self.sigma, dfk, dk)
                pop1 = Population(decs=(pop.decs + self.ro ** mk * dk.T))
                self.cal_obj(pop1)
                if phi1(pop1, self.sigma) - phi1(pop, self.sigma) < temp:
                    break
            dfk0, Ai0 = dfk, Ai
            dfk, Ai = self.FiniteDifference(pop1)
            Ak = Ai
            lamu = np.dot(np.linalg.pinv(Ak).T, dfk)
            lam = lamu
            sk = (pop1.decs - pop.decs).T
            yk = dlax(dfk, Ai, lam) - dlax(dfk0, Ai0, lam)
            if np.dot(sk.T, yk) > 0.2 * np.dot(np.dot(sk.T, Bk), sk):
                omega = 1
            else:
                omega = 0.8 * np.dot(np.dot(sk.T, Bk), sk) / \
                    (np.dot(np.dot(sk.T, Bk), sk) - np.dot(sk.T, yk))
            zk = omega * yk + (1 - omega) * np.dot(Bk, sk)
            Bk = Bk + np.dot(zk, zk.T) / np.dot(sk.T, zk) - np.dot(np.dot(Bk,
                                                                          sk), np.dot(Bk, sk).T) / np.dot(np.dot(sk.T, Bk), sk)  # noqa
            pop = pop1
            print(np.min(pop.objv))
        return pop

    def FiniteDifference(self, pop: Population) -> np.ndarray:
        # Estimate the gradient of objective by finite difference
        pop1 = Population(decs=pop.decs + np.eye(pop.decs.shape[1]) * 1e-4)
        self.cal_obj(pop1)
        df = (pop1.objv - pop.objv) / 1e-4
        df = df.reshape((len(df), 1))
        dg = -(pop1.cv - np.tile(pop.cv, (len(pop1), 1))).T / 1e-4
        return df, dg


def phi1(pop, sigma):
    p = pop.objv + 1 / sigma * \
        np.linalg.norm(np.where(pop.cv.T > 0, pop.cv.T, 0), ord=1)
    return p


def dphi1(pop, sigma, df, d):
    dp = np.dot(df.T, d) - 1 / sigma * \
        np.linalg.norm(np.where(pop.cv.T > 0, pop.cv.T, 0), ord=1)
    return dp


def dlax(df, Ai, lam):
    dl = df - np.dot(Ai.T, lam)
    return dl


def qpsubp(dfk, Bk, Ae, hk, Ai, gk):
    n = len(dfk)
    l = len(hk)  # noqa
    m = gk.shape[0]
    beta = 0.5
    sigma = 0.2
    epsilon = 1e-6
    gamma = 0.05
    ep0 = 0.05
    d0 = np.ones((n, 1))
    mu0 = 0.05 * np.zeros((l, 1))
    lm0 = 0.05 * np.zeros((m, 1))
    u0 = np.vstack((ep0, np.zeros((n + l + m, 1))))
    z0 = np.vstack((ep0, d0, mu0, lm0))
    z = z0.copy()  # noqa
    ep = ep0
    d = d0.copy()
    mu = mu0
    lm = lm0
    for k in range(150):
        dh = dah(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk)
        if np.linalg.norm(dh) < epsilon:
            break
        A = JacobiH(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk)
        b = psi(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk, gamma) * u0 - dh
        dz = np.dot(np.linalg.inv(A), b)
        de = dz[0]
        dd = dz[1: n + 1]
        if l > 0 and m > 0:
            du = dz[n + 1:n + l + 1]
            dl = dz[n + l + 1:n + m + l + 1]
        elif l == 0:  # noqa
            dl = dz[n + 1:n + m + 1]
        elif m == 0:
            du = dz[n + 1:n + l + 1]
        for mk in range(21):
            t1 = beta ** mk
            if l > 0 and m > 0:
                dh1 = dah(ep + t1 * de, d + t1 * dd, mu + t1 * du,
                          lm + t1 * dl, dfk, Bk, Ae, hk, Ai, gk)
            elif l == 0:  # noqa
                dh1 = dah(ep + t1 * de, d + t1 * dd, mu, lm +
                          t1 * dl, dfk, Bk, Ae, hk, Ai, gk)
            elif m == 0:
                dh1 = dah(ep + t1 * de, d + t1 * dd, mu +
                          t1 * du, lm, dfk, Bk, Ae, hk, Ai, gk)
            if np.linalg.norm(dh1) <= (1 - sigma * (1 - gamma * ep0) * beta ** mk) * np.linalg.norm(dh):  # noqa
                break
        alpha = beta ** mk
        ep = ep + alpha * de
        d = d + alpha * dd
        if l > 0 and m > 0:
            mu = mu + alpha * du
            lm = lm + alpha * dl
        elif l == 0:  # noqa
            lm = lm + alpha * dl
        elif m == 0:
            mu = mu + alpha * du
    return k, d, mu, lm


def phi(ep, a, b):
    p = a + b - np.sqrt(a ** 2 + b ** 2 + 2 * ep ** 2)
    return p


def ddv(ep, d, lm, Ai, gk):
    m = gk.shape[0]
    dd1 = np.zeros((m, m))
    dd2 = np.zeros((m, m))
    v1 = np.zeros((m, 1))
    for i in range(m):
        fm = np.sqrt(lm[i] ** 2 + (gk[i] + np.dot(Ai[i,
                     :].reshape(1, len(Ai[i, :])), d)) ** 2 + 2 * ep ** 2)
        dd1[i][i] = 1 - lm[i] / fm
        dd2[i][i] = 1 - \
            (gk[i] + np.dot(Ai[i, :].reshape(1, len(Ai[i, :])), d)) / fm
        v1[i] = -2 * ep / fm
    return dd1, dd2, v1


def dah(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk):
    n = len(dfk)
    l = len(hk)  # noqa
    m = gk.shape[0]
    dh = np.zeros((n + l + m + 1, 1))
    dh[0] = ep
    if l > 0 and m > 0:
        dh[1: n + 1] = Bk * d - Ae.T * mu - Ai.T * lm + dfk
        dh[n + 1: n + l + 1] = hk + Ae * d
        for i in range(m):
            dh[n + l + 1 + i] = phi(ep, lm[i], gk[i] + Ai[i, :] * d)
    elif l == 0:  # noqa
        dh[1: n + 1] = np.dot(Bk, d) - np.dot(Ai.T, lm) + dfk
        for i in range(m):
            dh[n + 1 + i] = phi(ep, lm[i], gk[i] +
                                np.dot(Ai[i, :].reshape(1, len(Ai[i, :])), d))
    elif m == 0:
        dh[1: n + 1] = Bk * d - Ae.T * mu + dfk
        dh[n + 1: n + l + 1] = hk + Ae * d
    dh = dh.ravel(order='F')
    dh = dh.reshape(dh.shape[0], 1)
    return dh


def psi(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk, gamma):
    dh = dah(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk)
    xi = gamma * np.linalg.norm(dh) * np.min((1.0, np.linalg.norm(dh)))
    return xi


def JacobiH(ep, d, mu, lm, dfk, Bk, Ae, hk, Ai, gk):
    n = len(dfk)
    l = len(hk)  # noqa
    m = gk.shape[0]
    dd1, dd2, v1 = ddv(ep, d, lm, Ai, gk)
    if l > 0 and m > 0:
        A = np.vstack((np.hstack(([[1]], np.zeros((1, n + l + m)))),
                       np.hstack((np.zeros((n, 1)), Bk, -Ae.T, -Ai.T)),
                       np.hstack((np.zeros((l, 1)), Ae, np.zeros((l, l + m)))),
                       np.hstack((v1, np.dot(dd2, Ai), np.zeros((m, l)), dd1))))  # noqa
        return A
    elif l == 0:  # noqa
        A = np.vstack((np.hstack(([[1]], np.zeros((1, n + m)))),
                       np.hstack((np.zeros((n, 1)), Bk, -Ai.T)),
                       np.hstack((v1, np.dot(dd2, Ai), dd1))))
        return A
    elif m == 0:
        A = np.vstack((np.hstack(([[1]], np.zeros((1, n + l)))),
                       np.hstack((np.zeros((n, 1)), Bk, -Ae.T)),
                       np.hstack((np.zeros((l, 1)), Ae, np.zeros((l, l))))))
        return A
