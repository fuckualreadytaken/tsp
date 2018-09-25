#! /usr/bin/env python
# coding=utf-8
from math import radians, cos, sin, asin, sqrt

citys = []
citys.append((116.46, 39.92))
citys.append((117.2, 39.13))
citys.append((121.48, 31.22))
citys.append((106.54, 29.59))
citys.append((91.11, 29.97))
citys.append((87.68, 43.77))
citys.append((106.27, 38.47))
citys.append((111.65, 40.82))
citys.append((108.33, 22.84))
citys.append((126.63, 45.75))
citys.append((125.35, 43.88))
citys.append((123.38, 41.8))
citys.append((114.48, 38.03))
citys.append((112.53, 37.87))
citys.append((101.74, 36.56))
citys.append((117, 36.65))
citys.append((113.6, 34.76))
citys.append((118.78, 32.04))
citys.append((117.27, 31.86))
citys.append((120.19, 30.26))
citys.append((119.3, 26.08))
citys.append((115.89, 28.68))
citys.append((113, 28.21))
citys.append((114.31, 30.52))
citys.append((113.23, 23.16))
citys.append((121.5, 25.05))
citys.append((110.35, 20.02))
citys.append((103.73, 36.03))
citys.append((108.95, 34.27))
citys.append((104.06, 30.67))
citys.append((106.71, 26.57))
citys.append((102.73, 25.04))
citys.append((114.1, 22.2))
citys.append((113.33, 22.13))


def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = 2 * asin(sqrt(a)) * 6371 * 1000
    return dis


def distance(order):
    long = 0.0
    for i in range(-1, len(citys) - 1):
        index1, index2 = order[i], order[i + 1]
        print(index1, index2)
        city1, city2 = citys[index1], citys[index2]
        long += geodistance(city1[0], city1[1], city2[0], city2[1])
        print(long)
    return long


if __name__ == "__main__":
    print(geodistance(citys[0][0], citys[0][1], citys[1][0], citys[1][1]))
