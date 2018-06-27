#! /usr/bin/env python
# coding=utf-8
import random
import numpy as np
import matplotlib.pyplot as plt

# 用遗传算法求解f(x) = x^2 + x + 3 在[0, 32）上的最大值
mutation_rate = 0.01
gen_num = 20


def init_population(num=4):
    # 初始化种群，种群数目为4
    p = range(32)
    population = random.sample(p, num)
    return population


def encode(num):
    # 个体的编码，即染色体
    chromosome = bin(num)[2:]
    if len(chromosome) != 5:
        filling_bit = 5 - len(chromosome)
        chromosome = "0" * filling_bit + chromosome
    return chromosome


def decode(chromosome):
    # 染色体解码为数字
    return int("0b" + chromosome, 2)


def fit(num):
    # 适应度函数
    return num * num + num + 3


def max_dic(dic):
    max_num = -10000000
    for i in dic:
        if i > max_num:
            max_num = i

    return max_num


def selection(args):
    # 选择函数
    args = list(args)
    fit_list = []
    pair_list = []
    for i in args:
        fit_list.append(fit(i))
    # print("种群中个体适应度", end=":")
    # print(fit_list)
    n = 0
    while n < len(args):
        m = n + 1
        while m < len(args):
            if fit_list[n] < fit_list[m]:
                tmp1 = fit_list[n]
                fit_list[n] = fit_list[m]
                fit_list[m] = tmp1
                tmp2 = args[n]
                args[n] = args[m]
                args[m] = tmp2
            m += 1
        n += 1
    pair_list.append(args[0])
    pair_list.extend(args[0:len(args) - 1])
    # print("选出的配对个体", end=":")
    # print(pair_list)
    return pair_list


def cross(num1, num2, point):
    # 交叉操作
    n1 = encode(num1)
    n2 = encode(num2)
    # # print(n1)
    # # print(n2)
    tmp = n1[point:]
    n1 = n1[0:point] + n2[point:]
    n2 = n2[0:point] + tmp
    # # print(n1)
    # # print(n2)
    return [decode(n1), decode(n2)]


def crossover(parents_list, pair_list, num):
    # 交叉函数
    p = range(num)
    s = int(num / 2)
    pair = random.sample(p, s)
    next_popolution = []
    for i in range(s):
        cross_point = random.randrange(0, 5)
        # print("第" + str(i) + "个交叉点为", end=":")
        # print(cross_point)
        next_popolution.extend(cross(parents_list[i], pair_list[pair[i]], cross_point))

    return next_popolution


def GA(num):
    gen = 0
    population = init_population(num=num)
    while gen < gen_num:
        population.sort()
        population.reverse()
        # print("第" + str(gen) + "代种群：", end=":")
        # print(population)
        pair_list = selection(population)
        population = crossover(population, pair_list, len(population))
        # print("子代为", end=":")
        # print(population)
        gen += 1
        # print("\n\n\n\n")
    return population[0]


def plot_(i):
    y = get_data(100, 22)
    x = range(i)
    plt.plot(x, y)
    plt.show()


def get_data(n, num):
    data = []
    for i in range(n):
        data.append(GA(num))

    return data


def cal_rate(data):
    num_16 = 0
    num_20 = 0
    num_30 = 0
    num_31 = 0
    for i in data:
        if i >= 16:
            num_16 += 1
        if i >= 20:
            num_20 += 1
        if i >= 30:
            num_30 += 1
        if i == 31:
            num_31 += 1
    rate_16 = float(num_16) / len(data)
    rate_20 = float(num_20) / len(data)
    rate_31 = float(num_31) / len(data)

    print("{0:<10} {1:<10} {2:<10} {3:<10}".format(rate_16, rate_20, rate_31, num_31))
    return rate_31


if __name__ == "__main__":
    # plot_(100)
    # GA(10)
    # cal_rate(get_data(10, 10))
    # cal_rate(get_data(100, 10))
    # cal_rate(get_data(1000, 10))
    # cal_rate(get_data(10000, 10))
    # cal_rate(get_data(100000, 10))
    # for
    # cal_rate(get_data(100000, 12))
    x = range(4, 24, 2)
    y = []
    for i in x:
        y.append(cal_rate(get_data(10000, i)))
        print(y)
    plt.plot(x, y)
    plt.show()
