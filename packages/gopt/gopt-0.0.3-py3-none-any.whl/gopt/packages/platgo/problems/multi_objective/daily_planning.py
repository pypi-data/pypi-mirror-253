import random
import datetime
import copy
import numpy as np
import pandas as pd

from gopt.packages.platgo.Problem import Problem
from gopt.packages.platgo import Population


class Daily_Planning(Problem):
    """
    type = {"n_obj": "single", "encoding": "real"}
    """

    def __init__(self, in_optimization_problem, debug=True) -> None:
        optimization_problem = {
            "mode": 0,
            "encoding": "permutation",
            "n_obj": 3,
        }

        optimization_problem.update(in_optimization_problem)
        self.index_task = optimization_problem["index_task"]
        self.time_window_dict = optimization_problem["time_window_dict"]
        super(Daily_Planning, self).__init__(
            optimization_problem, debug=debug
        )

    def init_pop(self, N: int = None):
        if N is None:
            N = self.pop_size
        data = self.data[0]
        decs = list()
        for i in range(N):
            decs.append(random.sample(range(1, self.n_var+1), self.n_var))
        decs = np.array(decs)
        return Population(decs=decs)

    # def fix_decs(self, pop: Population):
    #     # 对边界进行修复
    #     for i in range(len(pop)):
    #         for j in range(pop.decs.shape[1]):
    #             if self.lb[j] <= pop.decs[i][j] <= self.ub[j]:
    #                 continue
    #             else:
    #                 pop.decs[i][j] = np.random.uniform(self.lb[j], self.ub[j])
    #     return pop

    def compute(self, pop) -> None:
        objv = np.zeros((pop.decs.shape[0], self.n_obj))
        finalresult = np.empty((pop.decs.shape[0], 1), dtype=np.object)
        print("done")
        for i, x in enumerate(pop.decs):
            objv[i], finalresult[i] = self.main(x)
        pop.objv = objv
        pop.finalresult = finalresult
        pop.cv = np.zeros((pop.pop_size, self.n_constr))

    def main(self, x):
        data = self.data[0]
        # x = [134, 142, 122, 4, 7, 202, 139, 377, 57, 60, 47, 33, 36, 48, 236, 220, 182, 203, 501, 461, 467, 401, 405, 154, 186, 191, 387, 508, 479, 289, 147, 326, 450, 225, 187, 308, 330, 448, 540, 361, 213, 160, 171, 23, 26, 369, 50, 124, 130, 240, 235, 366, 379, 44, 51, 340, 356, 230, 132, 138, 133, 283, 273, 291, 161, 125, 346, 503, 496, 391, 357, 148, 523, 397, 27, 25, 491, 343, 534, 297, 248, 363, 251, 383, 205, 527, 167, 439, 443, 73, 116, 267, 277, 140, 349, 348, 91, 298, 492, 269, 517, 150, 223, 245, 323, 445, 114, 39, 352, 19, 119, 103, 92, 262, 128, 312, 319, 105, 109, 426, 141, 345, 58, 333, 419, 455, 480, 414, 215, 2, 376, 144, 463, 56, 411, 358, 359, 115, 483, 396, 113, 38, 464, 15, 31, 339, 185, 332, 497, 9, 266, 453, 117, 415, 382, 284, 94, 168, 149, 418, 335, 392, 486, 425, 537, 530, 99, 16, 313, 489, 100, 476, 355, 420, 189, 451, 199, 410, 490, 20, 1, 24, 121, 180, 471, 437, 305, 217, 258, 218, 246, 175, 307, 279, 3, 118, 229, 46, 446, 370, 210, 475, 22, 286, 150, 233, 515, 194, 441, 143, 399, 306, 423, 493, 293, 232, 221, 521, 512, 500, 309, 380, 338, 259, 11, 318, 524, 193, 351, 257, 440, 110, 255, 135, 264, 513, 165, 37, 395, 430, 429, 227, 538, 61, 14, 195, 32, 49, 93, 177, 78, 375, 434, 129, 421, 472, 325, 398, 427, 371, 436, 83, 96, 373, 188, 310, 67, 43, 53, 270, 192, 514, 400, 303, 64, 402, 156, 327, 413, 276, 10, 506, 287, 42, 502, 54, 260, 295, 265, 406, 416, 522, 111, 146, 337, 532, 254, 292, 214, 145, 470, 280, 458, 535, 120, 74, 85, 190, 317, 234, 462, 77, 531, 529, 468, 155, 504, 28, 433, 95, 162, 237, 388, 159, 241, 424, 71, 294, 314, 63, 368, 12, 507, 282, 250, 112, 243, 526, 169, 271, 477, 219, 184, 389, 249, 364, 224, 102, 511, 52, 70, 278, 367, 164, 197, 174, 81, 66, 281, 206, 6, 378, 315, 344, 304, 239, 539, 242, 212, 285, 181, 126, 533, 201, 75, 499, 137, 393, 459, 268, 82, 386, 353, 272, 331, 447, 452, 5, 13, 172, 275, 296, 136, 274, 80, 152, 17, 334, 469, 87, 422, 62, 403, 211, 222, 89, 365, 244, 231, 385, 35, 329, 454, 166, 311, 449, 409, 384, 90, 106, 158, 328, 481, 417, 457, 263, 466, 157, 216, 59, 288, 374, 65, 347, 431, 518, 151, 362, 354, 485, 179, 55, 198, 178, 69, 163, 438, 320, 34, 390, 465, 183, 322, 104, 252, 432, 131, 520, 381, 498, 316, 170, 519, 510, 256, 209, 407, 474, 299, 435, 484, 428, 487, 442, 108, 261, 29, 488, 196, 301, 525, 444, 536, 101, 412, 173, 342, 408, 97, 321, 84, 456, 495, 336, 516, 509, 247, 208, 207, 68, 404, 200, 41, 98, 18, 341, 40, 228, 460, 505, 21, 478, 45, 76, 360, 79, 86, 372, 473, 324, 72, 494, 394, 482, 238, 176, 302, 88, 107, 123, 290, 528, 30, 226, 253, 204, 153, 350, 127, 8]
        task_info = dict()  # 根据数据集统计每个任务的信息
        task_main_action = dict()  # 统计每个任务执行了多少个主动作
        time_main_action = dict()
        task_index = dict()  # 任务id对序列的映射
        index_task = dict()  # 序列对任务id的映射
        task_index2_dict = dict()
        next_times = 0  # 统计切换次数
        for i in range(0, len(data["scheduling_task"])):
            task_id = data["scheduling_task"][i]["task_id"]
            task_index2_dict[task_id] = i+1
            task_index[task_id] = [k for k in range(i*30+1, (i+1)*30+1)]
            for _ in [k for k in range(i*30+1, (i+1)*30+1)]:
                index_task[_] = task_id
            task_info[task_id] = {
                                  "time_window": data["scheduling_task"][i]["time_window"],
                                  "main_action_num": data["scheduling_task"][i]["main_action_num"],
                                  "main_action_time": data["scheduling_task"][i]["main_action_time"],
                                  "end_action": data["scheduling_task"][i]["end_action"],
                                  "next_action": data["scheduling_task"][i]["next_action"]
                                  }
            task_main_action[task_id] = 0
        start_time = task_info[index_task[int(x[0])]]["time_window"][0][0]  # 获取基准开始时间
        pre_task = float()  # 前一个动作
        for i in range(0, len(x)):
            time_window = task_info[index_task[int(x[i])]]["time_window"]  # 该任务的可执行窗口集合
            if i == 0:  # 判断第一个动作一般可行，主要进行基准时间的更新
                for t in range(0, len(time_window)):
                    start_time = task_info[index_task[int(x[i])]]["time_window"][t][0]  # 该动作对应任务的第一个执行时间窗口的开始时间
                    if start_time + task_info[index_task[int(x[i])]]["main_action_time"] < time_window[t][
                        0]:  # 仍然没有到达该任务的开始时间

                        task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                        time_main_action[x[i]] = [time_window[t][0]]  # 该主动作的开始时间
                        start_time = time_window[t][0] + task_info[index_task[int(x[i])]][
                            "main_action_time"]  # 更新基准开始时间
                        time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                        start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                        pre_task = x[i]
                        break
                    if time_window[t][0] <= start_time + task_info[index_task[int(x[i])]]["main_action_time"] <= time_window[t][
                        1]:
                        time_main_action[x[i]] = [start_time]  # 该主动作的开始时间
                        task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                        start_time += task_info[index_task[int(x[i])]]["main_action_time"]  # 基准开始时间+主动作时间
                        time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                        start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                        pre_task = x[i]
                        break  # 找到一个可执行的窗口直接跳出
            else:  # 判断第二个及以后的动作
                if index_task[int(pre_task)] == index_task[int(x[i])]:  # 没有发生任务的切换
                    for t in range(0, len(time_window)):  # 进行第二个动作，仍然对该动作对应的任务时间窗口列表进行遍历
                        if start_time + task_info[index_task[int(x[i])]]["main_action_time"] < time_window[t][0]:  # 仍然没有到达该任务的开始时间
                            if time_window[t][0]+task_info[index_task[int(x[i])]]["main_action_time"] > time_window[t][1]:
                                continue
                            task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                            time_main_action[x[i]] = [time_window[t][0]]  # 该主动作的开始时间
                            start_time = time_window[t][0] + task_info[index_task[int(x[i])]][
                                "main_action_time"]  # 更新基准开始时间
                            time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                            start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                            pre_task = x[i]  # 记录下切换前的任务
                            break
                        if time_window[t][0] <= start_time + task_info[index_task[int(x[i])]]["main_action_time"] <= time_window[t][
                            1]:  # 当前任务在可执行的窗口范围为内
                            start_time = max(time_window[t][0], start_time)
                            time_main_action[x[i]] = [start_time]  # 该主动作的开始时间
                            task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                            start_time += task_info[index_task[int(x[i])]]["main_action_time"]  # 基准开始时间+主动作时间
                            time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                            start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                            pre_task = x[i]  # 记录下切换前的任务
                            break  # 找到一个可执行的窗口直接跳出
                else:  # 发生了任务的切换
                    Flag_window = False
                    start_time -= task_info[index_task[int(pre_task)]]["end_action"]  # 需要先减去上一个任务的后处理时间,让上一个任务退回到主动作完成
                    # 上一个任务的切换时长和后处理时长取其中较大的
                    # 1.当切换时长大于后处理时,执行后处理的同时执行切换,后处理执行完毕,仍然执行切换
                    # 2.当后处理时长大于切换时长时,执行后处理的同时执行切换,切换后,后处理未完成仍需要等待后处理完成
                    temp_time = max(task_info[index_task[int(pre_task)]]["end_action"], task_info[index_task[int(pre_task)]]["next_action"][int(task_index2_dict[index_task[int(x[i])]])-1])
                    for t in range(len(time_window)):
                        if start_time + temp_time < time_window[t][0]:  # 任务的切换后，仍然没有到达该任务的开始时间
                            if time_window[t][0] + task_info[index_task[int(x[i])]]["main_action_time"] > time_window[t][1]:
                                continue
                            task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                            time_main_action[x[i]] = [time_window[t][0]]  # 该主动作的开始时间
                            start_time = time_window[t][0] + task_info[index_task[int(x[i])]][
                                "main_action_time"]  # 更新基准开始时间
                            time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                            start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                            next_times += 1  # 切换成功，切换次数加1
                            pre_task = x[i]  # 记录下切换前的任务
                            Flag_window = True   # 可用窗口已找到
                            break
                        elif time_window[t][0] <= start_time + temp_time <= time_window[t][1]:  # 切换后超过该任务的开始时间
                            if time_window[t][0] <= start_time + temp_time + task_info[index_task[int(x[i])]]["main_action_time"] <= time_window[t][
                                1]:  # 当前任务在可执行的窗口范围为内
                                task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                                start_time += temp_time  # 切换成功加上temp_time作为该任务的开始时间
                                time_main_action[x[i]] = [start_time]  # 该主动作的开始时间
                                start_time += task_info[index_task[int(x[i])]]["main_action_time"]  # 基准开始时间+主动作时间
                                time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                                start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                                next_times += 1  # 切换成功，切换次数加1
                                pre_task = x[i]
                                Flag_window = True
                                break
                    if not Flag_window:  # 找不到可用的时间窗口，切换不了，start_time进行还原
                        start_time += task_info[index_task[int(x[i - 1])]]["end_action"]
        gantt_dict = dict()
        for key, value in time_main_action.items():
            if key in index_task:
                gantt_dict.setdefault(self.index_task[key], []).append(
                    value
                )
        info = self.check_overlap(gantt_dict,self.time_window_dict)
        task_main_action_list = list(task_main_action.values())
        # 使用filter函数去除值为0的元素
        time_main_action2 = dict()
        for key, value in time_main_action.items():
            time_main_action2[str(key)] = value
        # import json
        # with open("file_jin.txt", "w") as file:
        #     json.dump(time_main_action2, file)
        task_main_action_list = list(filter(lambda x: x != 0, task_main_action_list))
        obj1 = self.n_var - sum(task_main_action_list)  # 统计总的主动作[最大化]->[150-(每个任务的主动作之和)]
        obj2 = 1-(sum(task_main_action_list)/30/len(task_main_action_list))  # 任务的总计完成度[最大化]->[1-每个任务的完成度之和的平均值]
        obj3 = next_times * 40  # 总的切换时长[最小化]
        # obj2 = 0  # 任务的总计完成度[最大化]->[1-每个任务的完成度之和的平均值]
        # obj3 = 0  # 总的切换时长[最小化]
        return np.array([obj1, obj2, obj3]), f'{time_main_action}'

    def check_overlap(self, gantt_dict, time_window_dict):
        """
        检查优化后的时间窗是否与原时间窗的完全重叠
        :param gantt_dict:
        :param time_window_dict:
        :return:
        """
        info = dict()
        k = 0
        for key, value in gantt_dict.items():
            time_window = time_window_dict[key]
            for i in range(len(value)):
                v_s = value[i][0]  # 优化出的开始时间
                v_e = value[i][1]  # 优化出的结束时间
                for j in range(len(time_window)):
                    t_s = time_window[j][0]  # 原来的开始时间
                    t_e = time_window[j][1]  # 原来的结束时间
                    if (v_s < t_s < v_e and t_s < v_e < t_e) or (t_s < v_s < t_e and v_s < t_e < v_e) or (
                            v_s < t_s and v_e > t_e):
                        info[key] = [v_s, v_e, t_s, t_e]
                    k += 1
        return info
