import json
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold



# 加载数据集合
print('加载数据...')
data = pd.read_csv('exp3.csv')
label = pd.read_csv('label.csv')
# 除去index
data = data.iloc[:, 1:]
label = label.iloc[:,1:]

# 设定训练集和测试集
y_train = label.values
X_train = data.iloc[20000:, :].values
X_test = data.iloc[:20000, :].values

classfeats = (0,1,2,3,4,5,6,7,8,9,10,15,16,17,22,23,24,29,30,31,36,37,38,43,44,45,50,51,52,57,58,59,64,65,66,71,72,73,78,79,80,85,86)

# for col in classfeats:
#     X_train.iloc[col] = X_train.iloc[col].astype('category')
#     X_test.iloc[col] = X_train.iloc[col].astype('category')
# 敲定好一组参数
params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'rmse',
    'max_depth': 15,
    'num_leaves': 20,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0,
    'categorical_features':classfeats
}

# 训练
print('开始训练...')
# 交叉验证
kf = KFold(n_splits=5)
scores = []
for train_index,test_index in kf.split(X_train):
    # 构建lgb中的Dataset格式
    lgb_train = lgb.Dataset(X_train.iloc[train_index], y_train.iloc[train_index])
    lgb_eval = lgb.Dataset(X_train.iloc[test_index], y_train.iloc[test_index], reference=lgb_train)

    gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=300,
                    valid_sets=lgb_eval,
                    early_stopping_rounds=30)

    y_pred = gbm.predict(X_train[test_index], num_iteration=gbm.best_iteration)
    print(mean_squared_error(y_train[test_index], y_pred) ** 0.5)


# # 保存模型
# print('保存模型...')
# # 保存模型到文件中
# gbm.save_model('../../tmp/model.txt')
#
# print('开始预测...')
# # 预测
# y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
# # 评估
# print('预估结果的rmse为:')
# print(mean_squared_error(y_test, y_pred) ** 0.5)