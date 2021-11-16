import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import math


# 定义KNN算法类
class KNN():
    # 初始化参数：K值、已知标签的数据集D，要分类的测试集T
    def __init__(self, data_set, test_set, k=9):
        self.k = k
        self.d = np.array(data_set).astype('float64')
        self.t = np.array(test_set).astype('float64')

    # 整体数据归一
    def norm_all(self):
        data_features = self.d[:, :-1]
        test_features = self.t
        all_features = np.r_[data_features, test_features]
        maxvals, minvals = [], []
        for i in range(all_features.shape[1]):
            maxvals.append(max(all_features[:, i]))
            minvals.append(min(all_features[:, i]))
        for i in range(self.t.shape[1]):
            self.d[:, i] = (self.d[:, i] - minvals[i]) / (maxvals[i] - minvals[i])
            self.t[:, i] = (self.t[:, i] - minvals[i]) / (maxvals[i] - minvals[i])

    # 计算向量距离函数，用欧式距离表示
    def distance(self, X, Y):
        sub = X - Y
        return (sum(sub ** 2))

    # 通过少数服从多数，给定最相邻的k个邻居，返回标签
    def find_label(self, nn):
        label_list = []
        for i in nn:
            # 默认label在data的最后一列
            label_list.append(self.d[i][-1])
        return max(label_list, key=label_list.count)

    def get_result(self):
        self.norm_all()
        print('norm finished')
        label = []
        for i, x in enumerate(self.t):
            if i % 100 == 0:
                print(str(i) + " finished!")
            dis_list = []
            for data in self.d:
                features = data[:len(data) - 1]
                dis_list.append(self.distance(x, features))
            # 找到离x最近的k个邻居
            dis_list = np.array(dis_list)
            nearest_neighbor = dis_list.argsort()[:self.k]
            #             nearest_neighbor = []
            #             for k in range(self.k):
            #                 nearest_neighbor.append(dis_list.index(min(dis_list)))
            #                 # 将最小的距离变成inf
            #                 dis_list[dis_list.index(min(dis_list))] = 100
            # 判断x的类别
            x_label = self.find_label(nearest_neighbor)
            label.append(x_label)

        return label


# # 测试
# data = [[45, 2, 9, 1],
#               [21, 17, 5, 1],
#               [54, 9, 11, 1],
#               [39, 0, 31, 1],
#               [5, 2, 57, 2],
#               [3, 2, 65, 2],
#               [2, 3, 55, 2],
#               [6, 4, 21, 2],
#               [7, 46, 4, 3],
#               [9, 39, 8, 3],
#               [9, 38, 2, 3],
#               [8, 34, 17, 3]]
# # test = [[23, 3, 17]]
# test = [[45, 2, 9],
#               [21, 17, 5],
#               [54, 9, 11],
#               [39, 0, 31],
#               [5, 2, 57],
#               [3, 2, 65],
#               [2, 3, 55],
#               [6, 4, 21],
#               [7, 46, 4],
#               [9, 39, 8],
#               [9, 38, 2],
#               [8, 34, 17]]
# k = KNN(data, test, 3)

# 读取数据
all_data = pd.read_csv('exp3Data.csv')
all_data = all_data[['team1_firstBlood','team1_firstTower','team1_firstInhibitor'
    ,'team1_firstBaron','team1_firstDragon','team1_firstRiftHerald',
      'eco_gap','kills_gap','team1_win']].values
print(all_data.shape)
test = all_data[:16000,:8]
data = all_data[16000:80000,:]
# print(test)
# print(data)
k = KNN(data,test,5)
result = k.get_result()
print(result)
result = np.array(result).T
real_result = all_data[:16000,-1]
print(k.distance(result,real_result))
print('准确率为'+str(1-k.distance(result,real_result)/16000))
