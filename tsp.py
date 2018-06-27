#! /usr/bin/env python
# coding=utf-8
import random
from math import radians, cos, sin, asin, sqrt

__author__ = "ProofZ"


def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = 2 * asin(sqrt(a)) * 6371 * 1000
    return dis / 1000


def create_life():
    p = list(range(0, 34))
    random.shuffle(p)
    return p


class GA_TSP:
    def __init__(self, mutation_rate, gen_num, population_num):
        self.mutation_rate = mutation_rate
        self.gen_num = gen_num
        self.population = population_num
        self.lives = []
        self.citys = []

    def init_citys(self):
        # 中国34个省会城市的经纬度坐标，每个省会的经纬度为一个元组放在列表里
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

    def init_population(self):
        # 初始化种群
        for i in range(self.population):
            self.lives.append(create_life())

    def cal_distance(self, life):
        # 计算个体中的距离和
        distance = 0
        n = 0
        while n < len(life) - 1:
            distance += geodistance(self.citys[life[n]][0],
                                    self.citys[life[n]][0],
                                    self.citys[life[n + 1]][0],
                                    self.citys[life[n + 1]][0])
            n += 1
        distance += geodistance(self.citys[life[-1]][0],
                                self.citys[life[-1]][1],
                                self.citys[life[0]][0],
                                self.citys[life[0]][1])
        return distance

    def encode(self):
        pass

    def decode(self):
        pass

    def selection(self):
        diss = []
        for i in self.lives:
            diss.append(self.cal_distance(i))

    def crossover(self):
        pass

    def mutation(self):
        pass

    def run(self):
        pass


def unit_test():
    g = GA_TSP(mutation_rate=0.1,
               gen_num=100,
               population_num=10)
    g.init_population()
    g.init_citys()
    print(g.cal_distance(g.lives[0]))


if __name__ == "__main__":
    unit_test()
