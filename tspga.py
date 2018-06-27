#! /usr/bin/env python
# coding=utf-8

import random
import math
from math import radians, cos, sin, asin, sqrt


# 计算两点间距离-m
def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = 2 * asin(sqrt(a)) * 6371 * 1000
    return dis


SCORE_NONE = -1


class Life(object):
    """个体类"""

    def __init__(self, aGene=None):
        self.gene = aGene
        self.score = SCORE_NONE


class GA(object):
    """遗传算法类"""

    def __init__(self, aCrossRate, aMutationRage, aLifeCount, aGeneLenght, aMatchFun):
        # lambda作为一个表达式，定义了一个匿名函数
        self.croessRate = aCrossRate  # 交叉概率
        self.mutationRate = aMutationRage  # 突变概率
        self.lifeCount = aLifeCount  # 种群中个体数量
        self.geneLenght = aGeneLenght  # 基因长度
        self.matchFun = aMatchFun  # 适配函数
        self.lives = []  # 种群
        self.best = None  # 保存这一代中最好的个体
        self.generation = 1  # 第几代
        self.crossCount = 0  # 交叉计数
        self.mutationCount = 0  # 变异计数
        self.bounds = 0.0  # 适配值之和，用于选择是计算概率
        self.mean = 1.0  # 适配值平均值
        self.initPopulation()

    def initPopulation(self):
        """初始化种群"""
        self.lives = []
        for i in range(self.lifeCount):
            gene = [x for x in range(self.geneLenght)]
            random.shuffle(gene)  # 用来对一个元素序列进行重新随机排序
            life = Life(gene)
            self.lives.append(life)

    def judge(self):
        """评估，计算每一个个体的适配值"""
        self.bounds = 0.0
        self.best = self.lives[0]
        for life in self.lives:
            life.score = self.matchFun(life)
            self.bounds += life.score
            if self.best.score < life.score:
                self.best = life
        self.mean = self.bounds / self.lifeCount

    def cross(self, parent1, parent2):
        """交叉"""
        n = 0
        while 1:
            newGene = []
            index1 = random.randint(0, self.geneLenght - 1)  # 用于生成一个指定范围内的整数
            index2 = random.randint(index1, self.geneLenght - 1)
            tempGene = parent2.gene[index1:index2]  # 交叉的基因片段
            p1len = 0
            for g in parent1.gene:
                if p1len == index1:
                    newGene.extend(tempGene)  # 插入基因片段
                    p1len += 1
                if g not in tempGene:
                    newGene.append(g)
                    p1len += 1
            if (self.matchFun(Life(newGene)) > max(self.matchFun(parent1), self.matchFun(parent2))):
                self.crossCount += 1
                return newGene
                # else:
            #       rate = random.random()
            #       if rate < math.exp(-100 / math.sqrt(self.generation)):
            #             self.crossCount += 1
            #             return newGene
            if (n > 100):
                self.crossCount += 1
                return newGene
            n += 1

    def mutation(self, egg):
        """突变"""
        index1 = random.randint(0, self.geneLenght - 1)
        index2 = random.randint(0, self.geneLenght - 1)
        newGene = egg.gene[:]  # 产生一个新的基因序列，以免变异的时候影响父种群
        newGene[index1], newGene[index2] = newGene[index2], newGene[index1]
        if self.matchFun(Life(newGene)) > self.matchFun(egg):
            self.mutationCount += 1
            return newGene
        else:
            rate = random.random()
            if rate < math.exp(-10 / math.sqrt(self.generation)):
                self.mutationCount += 1
                return newGene
            return egg.gene

    def getOne(self):
        """选择一个个体"""
        r = random.uniform(0, self.bounds)  # 均匀分布中随机采样
        for life in self.lives:
            r -= life.score
            if r <= 0:
                return life  # 轮盘赌选择方法
        raise Exception("选择错误", self.bounds)

    def newChild(self):
        """产生新后代"""
        parent1 = self.getOne()
        rate = random.random()
        # 按概率交叉
        if rate < self.croessRate:
            # 交叉
            parent2 = self.getOne()
            gene = self.cross(parent1, parent2)
        else:
            gene = parent1.gene

            # 按概率突变
        rate = random.random()
        if rate < self.mutationRate:
            gene = self.mutation(Life(gene))
        return Life(gene)

    def next(self):
        """产生下一代"""
        self.judge()
        newLives = []
        newLives.append(self.best)  # 把最好的个体加入下一代
        while len(newLives) < self.lifeCount:
            newLives.append(self.newChild())
        self.lives = newLives
        self.generation += 1


class TSP(object):
    def __init__(self, aLifeCount=100, ):
        self.initCitys()
        self.lifeCount = aLifeCount
        self.ga = GA(aCrossRate=0.7,
                     aMutationRage=0.02,
                     aLifeCount=self.lifeCount,
                     aGeneLenght=len(self.citys),
                     aMatchFun=self.matchFun())

    def initCitys(self):
        self.citys = []

        # 中国34个省会城市的经纬度坐标
        self.citys.append((116.46, 39.92))
        self.citys.append((117.2, 39.13))
        self.citys.append((121.48, 31.22))
        self.citys.append((106.54, 29.59))
        self.citys.append((91.11, 29.97))
        self.citys.append((87.68, 43.77))
        self.citys.append((106.27, 38.47))
        self.citys.append((111.65, 40.82))
        self.citys.append((108.33, 22.84))
        self.citys.append((126.63, 45.75))
        self.citys.append((125.35, 43.88))
        self.citys.append((123.38, 41.8))
        self.citys.append((114.48, 38.03))
        self.citys.append((112.53, 37.87))
        self.citys.append((101.74, 36.56))
        self.citys.append((117, 36.65))
        self.citys.append((113.6, 34.76))
        self.citys.append((118.78, 32.04))
        self.citys.append((117.27, 31.86))
        self.citys.append((120.19, 30.26))
        self.citys.append((119.3, 26.08))
        self.citys.append((115.89, 28.68))
        self.citys.append((113, 28.21))
        self.citys.append((114.31, 30.52))
        self.citys.append((113.23, 23.16))
        self.citys.append((121.5, 25.05))
        self.citys.append((110.35, 20.02))
        self.citys.append((103.73, 36.03))
        self.citys.append((108.95, 34.27))
        self.citys.append((104.06, 30.67))
        self.citys.append((106.71, 26.57))
        self.citys.append((102.73, 25.04))
        self.citys.append((114.1, 22.2))
        self.citys.append((113.33, 22.13))

    def distance(self, order):
        distance = 0.0
        for i in range(-1, len(self.citys) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance = geodistance(city1[0], city1[1], city2[0], city2[1])
        return distance

    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)

    def run(self, n=0):
        while n > 0:
            self.ga.next()
            distance = self.distance(self.ga.best.gene)
            print(("Generation: %4d \t\t Distance: %f") % (self.ga.generation - 1, distance))  # 输出当前代数和路径长度
            self.ga.best.gene.append(self.ga.best.gene[0])
            print("Path: ", self.ga.best.gene)  # 输出当前最佳路径
            self.ga.best.gene.pop()
            n -= 1


if __name__ == '__main__':
    tsp = TSP()
    tsp.run(100)
