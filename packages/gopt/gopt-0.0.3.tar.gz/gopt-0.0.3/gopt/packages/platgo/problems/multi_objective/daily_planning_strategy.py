import random
import copy
import numpy as np
from gopt.packages.platgo.Problem import Problem
from gopt.packages.platgo import Population


class Daily_Planning_Strategy(Problem):
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
        self.list1 = optimization_problem["list1"]
        super(Daily_Planning_Strategy, self).__init__(
            optimization_problem, debug=debug
        )

    def init_pop(self, N: int = None):
        if N is None:
            N = self.pop_size
        data = self.data[0]
        decs = list()
        list1 = self.list1
        for i in range(N-1):
            # task_list = random.sample(range(1, len(data["scheduling_task"]) + 1), len(data["scheduling_task"]))
            # dec = list()
            # for j in task_list:
            #     dec += [k for k in range((j-1)*30+1, j*30+1)]
            # decs += [dec]
            decs.append(random.sample(range(1, self.n_var + 1), self.n_var))
        # for j in range(int(N*0.2)):
        # for j in range(5):
        decs += [list1]
        decs = np.array(decs)
        return Population(decs=decs)

    def fix_decs(self, pop: Population):
        # 进行修复, 将开始时间早的往前排
        index_task = self.index_task
        fix_list = random.sample([_ for _ in range(len(pop))], k=1)
        for i in fix_list:
            task_id_ = index_task[pop.decs[i][0]]
            list3 = self.fix_seq(task_id_)
            pop.decs[i] = np.array(list3, dtype=np.int32)
        return pop

    def fix_seq(self, task_id_):
        data = copy.deepcopy(self.data[0])
        next_times = 0
        task_info = dict()  # 记录每个任务的信息
        time_window_dict = dict()  # 记录每个任务的时间窗
        task_main_action = dict()  # 记录每个任务做的主动作的个数
        task_start_time = dict()
        index_task = dict()
        for i in range(0, len(data["scheduling_task"])):
            task_id = data["scheduling_task"][i]["task_id"]
            for _ in [k for k in range(i * 30 + 1, (i + 1) * 30 + 1)]:
                index_task[_] = task_id
        index_list = [i for i in range(1, len(data["scheduling_task"]) * 30 + 1, 30)]
        time_window_dict2 = dict()
        index1 = 1
        task_index_dict = dict()
        task_index1_dict = dict()  # 任务与时间窗的正向映射
        index1_task_dict = dict()  # # 任务与时间窗的反向映射
        for i in range(len(data["scheduling_task"])):
            task_index_dict[data["scheduling_task"][i]["task_id"]] = i + 1
            for t_v in data["scheduling_task"][i]["time_window"]:
                time_window_dict2[index1] = t_v
                task_index1_dict[index1] = data["scheduling_task"][i]["task_id"]
                index1_task_dict.setdefault(data["scheduling_task"][i]["task_id"],[]).append(index1)
                index1 += 1
            time_window_dict[data["scheduling_task"][i]["task_id"]] = data["scheduling_task"][i]["time_window"]
            task_info[data["scheduling_task"][i]["task_id"]] = {
                "main_action_num": data["scheduling_task"][i]["main_action_num"],
                "main_action_time": data["scheduling_task"][i]["main_action_time"],
                "end_action": data["scheduling_task"][i]["end_action"],
                "next_action": data["scheduling_task"][i]["next_action"]
            }
            task_main_action[data["scheduling_task"][i]["task_id"]] = 0
        time_window_dict2 = dict(sorted(time_window_dict2.items(), key=lambda x: (x[1][0])))  # 按开始时间进行排序
        time_window_list2 = list()
        for key in time_window_dict2.keys():
            if task_index1_dict[key] not in time_window_list2:
                time_window_list2.append(task_index1_dict[key])
        index_list2 = [int(task_index_dict[i]) - 1 for i in time_window_list2]
        # sorted_tuples = sorted(zip(index_list2, index_list), key=lambda x: x[0])
        # 提取排序后的元素
        index_list = [index_list[i] for i in index_list2]
        index_list_dict = dict(zip(time_window_list2, index_list))
        index_list_dict2 = copy.deepcopy(index_list_dict)
        # index_list = np.array(index_list)[index_list2].tolist()

        index_ = list()
        for key1, value1 in task_index1_dict.items():
            if value1 == task_id_:
                index_.append(key1)
        time_window_dict3 = copy.deepcopy(time_window_dict2)
        r_index_ = random.choice(index_)
        for key2 in time_window_dict2.keys():
            if time_window_dict2[key2] == time_window_dict2[r_index_]:
                break
            else:
                del time_window_dict3[key2]
        start_time = list(time_window_dict3.values())[0][0]
        pre_task = list(time_window_dict3.keys())[0]
        for key, value in time_window_dict3.items():
            main_action_time = task_info[task_index1_dict[key]]["main_action_time"]  # 获取该任务的主动作时长
            end_action = task_info[task_index1_dict[key]]["end_action"]  # 获取该任务的后处理动作时长
            temp_time = float()
            temp = float()
            flag2 = False
            flag3 = True
            if task_index1_dict[pre_task] != task_index1_dict[key]:  # 发生切换
                next_action = task_info[task_index1_dict[pre_task]]["next_action"]  # 获取该任务的切换动作时长集合
                temp_time = max(task_info[task_index1_dict[pre_task]]["end_action"],
                                next_action[task_index_dict[task_index1_dict[key]] - 1])  # 上一个任务切换到该任务的时长
                start_time -= task_info[task_index1_dict[pre_task]]["end_action"]  # 先退回到上一个任务执行主动作完毕
                start_time += temp_time  # 当前任务的开始时间
                if start_time < value[0]:  # 开始时间在该任务时间窗之前
                    temp = value[0] - start_time
                    start_time = value[0]
                    if start_time + main_action_time > value[1]:
                        start_time -= temp
                        start_time -= temp_time
                        start_time += task_info[task_index1_dict[pre_task]]["end_action"]
                        continue  # 切换到当前任务失败，直接跳过该任务
                    else:
                        flag2 = True
                        next_times += 1  # 切换成功，次数加1
                elif value[0] <= start_time <= value[1]:  # 开始时间在窗口集合中间
                    if start_time + main_action_time > value[1]:
                        start_time -= temp_time
                        start_time += task_info[task_index1_dict[pre_task]]["end_action"]
                        continue  # 切换到当前任务失败，直接跳过该任务
                    else:
                        next_times += 1  # 切换成功，次数加1
                elif start_time > value[1]:  # 这里也是切换失败
                    start_time -= temp_time
                    start_time += task_info[task_index1_dict[pre_task]]["end_action"]
                    continue

            else:  # 没有发生切换【可能进行第一次】
                if start_time + main_action_time < value[0] or start_time < value[0]:
                    if start_time + main_action_time > value[1]:
                        continue
                    start_time = value[0]
                    flag3 = False
                    print("=======================")
            if index_list_dict[task_index1_dict[key]] - index_list_dict2[task_index1_dict[key]] >= 30:  # 该窗口对应的任务全部做完
                # index_list_dict[task_index1_dict[key]] = index_list_dict2[task_index1_dict[key]]+29
                if flag2:
                    start_time -= temp
                if flag3:
                    start_time -= temp_time
                    next_times -= 1
                    start_time += task_info[task_index1_dict[pre_task]]["end_action"]
                continue
            while value[0] <= start_time + main_action_time <= value[1]:  # 初始时间加上主动作时长仍然在该任务的窗口内
                task_start_time[index_list_dict[task_index1_dict[key]]] = [start_time]
                task_main_action[task_index1_dict[key]] += 1  # 该任务的主动作次数加1
                start_time += main_action_time  # 加上该任务的主动作时长
                task_start_time[index_list_dict[task_index1_dict[key]]] += [start_time]
                start_time += end_action  # 加上该任务的后处理动作时长
                index_list_dict[task_index1_dict[key]] += 1
                if index_list_dict[task_index1_dict[key]] - index_list_dict2[
                    task_index1_dict[key]] >= 30:  # 该窗口对应的任务全部做完
                    break
            pre_task = key  # 存储为上一个任务
        gantt_dict = dict()
        for key, value in task_start_time.items():
            if key in index_task:
                gantt_dict.setdefault(index_task[key], []).append(
                    value
                )
        obj1 = len(task_start_time)  # 统计总的主动作[最大化]
        obj2 = len(task_start_time) / 30 / len(gantt_dict)  # 每个任务的完成度之和的平均值[最大化]
        obj3 = next_times * 40  # 总的切换时长[最小化]
        list1 = list(task_start_time.keys())
        list2 = [i + 1 for i in range(len(data["scheduling_task"]) * 30)]
        list3 = list(set(list2) - set(list1))
        return list1+list3

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
        task_info = dict()  # 根据数据集统计每个任务的信息
        task_main_action = dict()  # 统计每个任务执行了多少个主动作
        time_main_action = dict()
        task_index = dict()  # 任务id对序列的映射
        index_task = dict()  # 序列对任务id的映射
        task_index2_dict = dict()
        next_times = 0  # 统计切换次数
        for i in range(0, len(data["scheduling_task"])):
            task_id = data["scheduling_task"][i]["task_id"]
            task_index2_dict[task_id] = i + 1
            task_index[task_id] = [k for k in range(i * 30 + 1, (i + 1) * 30 + 1)]
            for _ in [k for k in range(i * 30 + 1, (i + 1) * 30 + 1)]:
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
                    if time_window[t][0] <= start_time + task_info[index_task[int(x[i])]]["main_action_time"] <= \
                            time_window[t][
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
                        # if start_time + task_info[index_task[int(x[i])]]["main_action_time"] < time_window[t][
                        #     0] or start_time < time_window[t][0]:  # 仍然没有到达该任务的开始时间
                        #     if start_time + task_info[index_task[int(x[i])]]["main_action_time"] > time_window[t][1]:
                        #         continue
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
                    temp_time = max(task_info[index_task[int(pre_task)]]["end_action"],
                                    task_info[index_task[int(pre_task)]]["next_action"][
                                        int(task_index2_dict[index_task[int(x[i])]]) - 1])
                    for t in range(len(time_window)):
                        if start_time + temp_time < time_window[t][0]:  # 任务的切换后，仍然没有到达该任务的开始时间
                            if time_window[t][0] + task_info[index_task[int(x[i])]]["main_action_time"] > \
                                    time_window[t][1]:
                                continue
                            task_main_action[index_task[int(x[i])]] += 1  # 该任务的主动作加1
                            time_main_action[x[i]] = [time_window[t][0]]  # 该主动作的开始时间
                            start_time = time_window[t][0] + task_info[index_task[int(x[i])]][
                                "main_action_time"]  # 更新基准开始时间
                            time_main_action[x[i]] += [start_time]  # 该主动作的结束时间
                            start_time += task_info[index_task[int(x[i])]]["end_action"]  # 加上后处理动作的时间
                            next_times += 1  # 切换成功，切换次数加1
                            pre_task = x[i]  # 记录下切换前的任务
                            Flag_window = True  # 可用窗口已找到
                            break
                        elif time_window[t][0] <= start_time + temp_time <= time_window[t][1]:  # 切换后超过该任务的开始时间
                            if time_window[t][0] <= start_time + temp_time + task_info[index_task[int(x[i])]][
                                "main_action_time"] <= time_window[t][
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
        task_main_action_list = list(task_main_action.values())
        gantt_dict = dict()
        for key, value in time_main_action.items():
            if key in index_task:
                gantt_dict.setdefault(self.index_task[key], []).append(
                    value
                )
        # info = self.check_overlap(gantt_dict, self.time_window_dict)
        # 使用filter函数去除值为0的元素
        time_main_action2 = dict()
        for key, value in time_main_action.items():
            time_main_action2[str(key)] = value
        # import json
        # with open("file_jin.txt", "w") as file:
        #     json.dump(time_main_action2, file)
        task_main_action_list = list(filter(lambda x: x != 0, task_main_action_list))
        obj1 = self.n_var - sum(task_main_action_list)  # 统计总的主动作[最大化]->[150-(每个任务的主动作之和)]
        obj2 = 1 - (sum(task_main_action_list) / 30 / len(task_main_action_list))  # 任务的总计完成度[最大化]->[1-每个任务的完成度之和的平均值]
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
