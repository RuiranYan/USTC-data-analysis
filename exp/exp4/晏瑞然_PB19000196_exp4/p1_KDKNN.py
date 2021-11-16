import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import math

# 读取数据
all_data = pd.read_csv('exp3Data.csv')
# all_data = all_data[['team1_firstBlood','team1_firstTower','team1_firstInhibitor'
#     ,'team1_firstBaron','team1_firstDragon','team1_firstRiftHerald',
#       'eco_gap','kills_gap','team1_win']].values
all_data = all_data[['eco_gap', 'kills_gap', 'team1_win']].values
# all_data = all_data[['team1_firstBlood','team1_firstTower','team1_firstInhibitor','team1_firstBaron','team1_firstDragon','team1_firstRiftHerald','team1_win']].values
print(all_data.shape)


# 创建二叉树
class binaryTreeNode():
    def __init__(self, data=None, left=None, right=None, split=None):
        self.data = data
        self.left = left
        self.right = right
        self.split = split

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getsplit(self):
        return self.split


class KNNClassfier(object):

    def __init__(self, k=1):
        self.k = k
        self.root = None

    def getroot(self):
        return self.root

    def kd_tree(self, train_X, train_Y):
        # 构造kd树
        if len(train_X) == 0:
            return None
        if len(train_X) == 1:
            return binaryTreeNode((train_X[0], train_Y[0]))
        index = np.argmax(np.var(train_X, axis=0))
        argsort = np.argsort(train_X[:, index])
        left = self.kd_tree(train_X[argsort[0:len(argsort) // 2], :], train_Y[argsort[0:len(argsort) // 2]])
        right = self.kd_tree(train_X[argsort[len(argsort) // 2 + 1:], :], train_Y[argsort[len(argsort) // 2 + 1:]])
        root = binaryTreeNode((train_X[argsort[len(argsort) // 2], :], train_Y[argsort[len(argsort) // 2]]), left,
                              right, index)
        return root

    def inOrder(self, root):
        # 中序遍历kd树
        if root == None:
            return None
        self.inOrder(root.getleft())
        print(root.getdata())
        self.inOrder(root.getright())

    def search_kd_tree(self, x, knn, root, nodelist):

        while len(knn) == 0:
            if root.getleft() == None and root.getright() == None:
                return knn.append(root.getdata())

            if x[root.getsplit()] < root.getdata()[0][root.getsplit()]:
                if root.getleft() != None:
                    nodelist.append(root.getleft())
                    self.search_kd_tree(x, knn, root.getleft(), nodelist)
                else:
                    nodelist.append(root.getright())
                    self.search_kd_tree(x, knn, root.getright(), nodelist)
            else:
                if root.getright() != None:
                    nodelist.append(root.getright())
                    self.search_kd_tree(x, knn, root.getright(), nodelist)
                else:
                    nodelist.append(root.getleft())
                    self.search_kd_tree(x, knn, root.getleft(), nodelist)

        dis = np.linalg.norm(x - knn[0][0], ord=2)

        while len(nodelist) != 0:
            current = nodelist.pop()
            # currentdis = np.linalg.norm(x-current.getdata()[0],ord=2)
            if np.linalg.norm(x - current.getdata()[0], ord=2) < dis:
                knn[0] = current.getdata()
            if current.getleft() != None and np.linalg.norm(x - current.getleft().getdata()[0], ord=2) < dis:
                knn[0] = current.getleft().getdata()
            if current.getright() != None and np.linalg.norm(x - current.getright().getdata()[0], ord=2) < dis:
                knn[0] = current.getright().getdata()

        return knn

    def fit(self, X, Y):
        '''
        X :  [n_samples,shape]
        Y :  [n_samples,1]
        '''
        self.root = self.kd_tree(X, Y)

    def predict(self, X):
        print('   ')
        output = np.zeros((X.shape[0], 1))
        for i in range(X.shape[0]):
            knn = []
            knn = self.search_kd_tree(X[i, :], knn, self.root, [self.root])
            labels = []
            for j in range(len(knn)):
                labels.append(knn[j][1])
            counts = []
            # print('x:',X[i,:],'knn:',knn)
            for label in labels:
                counts.append(labels.count(label))
            output[i] = labels[np.argmax(counts)]
        return output

    def score(self, X, Y):
        pred = self.predict(X)
        err = 0.0
        for i in range(X.shape[0]):
            if pred[i] != Y[i]:
                err = err + 1
        return 1 - float(err / X.shape[0])


def norm(x, minval, maxval):
    x = x.astype('float64')
    for i in range(x.shape[1]):
        x[:, i] = (x[:, i] - minval[i]) / (maxval[i] - minval[i])
    return x


def get_max_min(X):
    maxval = []
    minval = []
    for i in range(X.shape[1]):
        maxval.append(max(X[:, i]))
        minval.append(min(X[:, i]))
    return maxval, minval


result = []
for i in range(5):
    test_set = (all_data[(i * 16000):((i + 1) * 16000), :])
    ra = [r for r in range((i * 16000), ((i + 1) * 16000))]
    train_set = (np.delete(all_data, ra, axis=0))
    test_set_x = test_set[:, :-1]
    test_set_y = test_set[:, -1]
    train_set_x = train_set[:, :-1]
    train_set_y = train_set[:, -1]
    maxval, minval = get_max_min(train_set_x)
    test_set_x = norm(test_set_x, maxval, minval)
    train_set_x = norm(train_set_x, maxval, minval)
    clf = KNNClassfier(k=5)
    clf.fit(train_set_x, train_set_y)
    result.append(clf.score(test_set_x, test_set_y))
    print(str(i) + ' : ' + str(clf.score(test_set_x, test_set_y)))
print('平均准确率：' + str(np.mean(result)))
