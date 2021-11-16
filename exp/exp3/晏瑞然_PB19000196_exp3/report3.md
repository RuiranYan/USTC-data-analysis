

# 实验三

**PB19000196 晏瑞然**

## 实验要求：

给定一个数据集和预测任务，需要分析数据以及抽取特征。

## 实验过程：

### 导入模块：

主要导入三个python数据分析重要的库：numpy, pandas, matplotlib.

### 读取数据：

用pandans库中read_csv读取实验所给的exp3.csv文件，将文件中的数据存储成pandas库中的dataframe的格式。打印前5条数据观察数据大致的格式如下：

![image-20210419204049609](/home/yanruiran/.config/Typora/typora-user-images/image-20210419204049609.png)

可以大致看到各个特征与数据的结构，再打印出总表的大小，得到其表规格为80000×80，即80000条数据，每条数据80个特征。

## 数据分析与特征抽取：

### 1.比赛特征
**主要工作：** 分析每次比赛的地图、队列、赛季特征。



首先，查看mapId,queueId,seasonId的数据分布，可以看出mapId有两种11和12，其中11个数有70001次，12有999次。 queueId有7中，各自频率如下。 seasonId只有一种取值13,故该特征可直接去除。

![image-20210419204436426](/home/yanruiran/.config/Typora/typora-user-images/image-20210419204436426.png)

同时发现有map为12的个数与queue为450的数据个数相同，故猜测queue为450与map为12等价。 下面进行验证：

![image-20210419204612220](/home/yanruiran/.config/Typora/typora-user-images/image-20210419204612220.png)

结果与我们的猜想相同，故mapId也没有意义，可以去掉。

再来看看queueId与胜负的关系，得到如下crosstab：

![image-20210419204736757](/home/yanruiran/.config/Typora/typora-user-images/image-20210419204736757.png)

可以看出大多数情况的queueId都在420,430之间且基本胜率接近50%，故也可以认为其与胜负关系无关，可以删除。


### 2.队伍特征
**主要任务：** 通过每个队伍的每个选手的数据，组合成队伍的特征(整体经济、整体人头数)，如根据每个人的经济得到队伍经济。



#### 2.1队伍经济分析

1. 获取每个队伍的经济及经济差，并将得到的数据加入到特征表中。画出经济散点图如下图所示，其中绿色代表team1赢，红色代表team2赢。

![image-20210419205342360](/home/yanruiran/.config/Typora/typora-user-images/image-20210419205342360.png)

2. 画出经济差正负与胜负关系的列联表，其中eco_gap=True代表经济差(team1-team2)大于0,eco_gap=False反之。根据列联表检验，可以认为游戏胜负与经济是否领先相关。

![image-20210419205550154](/home/yanruiran/.config/Typora/typora-user-images/image-20210419205550154.png)

3. 得到胜方与负方经济差分布图及各个统计量，可以看出胜负方经济差大致符合一个正态分布，其均值在8763左右。

   ![image-20210419205809802](/home/yanruiran/.config/Typora/typora-user-images/image-20210419205809802.png)

   ![image-20210419205842014](/home/yanruiran/.config/Typora/typora-user-images/image-20210419205842014.png)

**结论：**

   - 经济是否领先与胜负相关，且经济高的一方更容易获胜，这也很符合常理。
   - 游戏结束时的胜负方经济差大概符合一个均值为8763的正态分布，其各统计量如上图所示。

#### 2.2队伍杀敌数分析

1. 得到每个队伍的杀敌数及杀敌数差，将其加入特征表。因杀敌数相对经济更加集中所以没必要画散点图。
2. 画出人头差正负与胜负关系的列联表，其中kills_gap=True代表经济差(team1-team2)大于0,kills_gap=False反之。根据列联表检验，可以认为游戏胜负与经济是否领先相关。

![image-20210419210303009](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210303009.png)

3. 得到胜负各方的杀敌数分布图及各个统计量，可以看出胜负方人头差大致符合一个正态分布，其均值在12左右。

![image-20210419210350481](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210350481.png)

![image-20210419210403910](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210403910.png)

**结论：**

- 人头数是否领先与胜负相关，且经济高的一方更容易获胜，这也很符合常理。
- 游戏结束时的胜负方人头差大概符合一个均值为12的正态分布，其各统计量如上图所示。

### 3. 地图资源特征

**主要任务：** 分析各个地图资源(如1塔，1龙等)特征对胜负的影响，用曼哈顿距离度量两者距离(相关度)，曼哈顿距离即为team1拿了该资源却输了和未拿该资源却赢了的比赛总和。



#### 3.0 数据预处理

进行分析前首先进行数据类型转换，将TRUE，FALSE字符类型转换成0，1的int型。

#### 3.1 一血

查看是否拿一血与胜负的关系列联表：

![image-20210419210704354](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210704354.png)

计算曼哈顿距离及拿了该资源后的胜率：

![image-20210419210744947](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210744947.png)

#### 3.2 一塔

查看是否拿一塔与胜负的关系列联表：

![image-20210419210900132](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210900132.png)

计算曼哈顿距离及拿了该资源后的胜率：

![image-20210419210931387](/home/yanruiran/.config/Typora/typora-user-images/image-20210419210931387.png)

#### 3.3 一先锋

查看是否拿一先锋与胜负的关系列联表：

![image-20210419211005942](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211005942.png)

计算曼哈顿距离及拿了该资源后的胜率：

![image-20210419211020896](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211020896.png)

#### 3.4 一男爵

查看是否拿一男爵与胜负的关系列联表：

![image-20210419211053323](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211053323.png)

计算曼哈顿距离及拿了该资源后的胜率：

![image-20210419211107199](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211107199.png)

#### 3.5 一龙

查看是否拿一龙与胜负的关系列联表：

![image-20210419211136624](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211136624.png)

计算曼哈顿距离及拿了该资源后的胜率：

![image-20210419211158685](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211158685.png)

#### 3.6 一水晶

查看是否拿一水晶与胜负的关系列联表：

![image-20210419211226638](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211226638.png)

计算曼哈顿距离及拿了该资源后的胜率：

![image-20210419211250480](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211250480.png)


#### 分析：
可以看出拿了地图资源胜率会提高，这在实际中也是显然的。同时也可以发现这些数据中一些有趣的性质。
首先一血、一塔的矩阵正反对角线上的数基本相同，但其他资源的对应矩阵明显有左上大于右下，左下大于右上的性质。
难道team1和team2拿这些资源的胜率有偏差？显然不是，经分析，出现该种状态的原因是**有很多比赛两边都没拿该资源就结束了！！！**
所以左侧数据大于右侧。这时计算拿了该资源后的胜率就比较有意义，现实中lol比赛分析也都如此，会分析拿了某项资源后的胜率。
数据中也有一些反直觉的地方，比如拿了一先锋后的胜率比一大龙的胜率还高，理论上越偏向后期的资源应该对胜率影响越大，**推测比赛数据可能有一定偏差，取的是结束时间较早的数据**，所以先锋作为前期的重要资源对胜负影响就很大，而两边可能都没打大龙游戏就结束了，所以大龙对胜负的影响就较小。

最后，根据曼哈顿距离分析，资源与胜负相关度从高到底排序为(距离近的相关度高)：一先锋 > 一塔 > 一男爵 > 一龙 > 一水晶 > 一血。


### 4.英雄及阵容特征
**主要任务：** 分析各英雄与阵容数据，如英雄胜率、英雄常见位置、阵容胜率等。



#### 4.0 数据预处理

由于只分析英雄相关数据，故把所有玩家有关英雄的数据合在一张表中，得到championData。

![image-20210419211718900](/home/yanruiran/.config/Typora/typora-user-images/image-20210419211718900.png)

其中统计的是每场比赛中每个player使用的英雄的各项数据，每场比赛10个player，故有800000条数据。

#### 4.1英雄胜率分析

生成英雄胜率表并找到其中的胜率最大最小值：

![image-20210419212448635](/home/yanruiran/.config/Typora/typora-user-images/image-20210419212448635.png)

可以看出胜率最高为54%，最低为45%。 由此可见英雄对胜率的影响不算很大，在5%以内，该游戏还算比较平衡。

#### 4.2 lane与role的分析

画出所有的lane与role的关系表：

![image-20210419212545346](/home/yanruiran/.config/Typora/typora-user-images/image-20210419212545346.png)

可以看出,role中所有的None的都来自打野选手，而lane中的none有各个角色。 故作出判断role中none是指打野选手并没有具体的角色而lane中的none是因为数据缺失造成的，要进行数据填补，而填补方式是用该英雄大的最多的lane来替换none。 

接下来进行数据填补，同时得到每个英雄对应最常见lane的字典champion_lane_dict，再通过得到的字典，对原data表进行补全，补全过程及得到的字典见代码。


#### 4.3 类型转换

将英雄，lane，role这些字符串类型特征转换为onehot编码，具体转换过程见代码，打印转换后的表格shape，可以看出已经转换完成。

![image-20210419213058794](/home/yanruiran/.config/Typora/typora-user-images/image-20210419213058794.png)

#### 4.4 得到英雄数据表
对各个英雄数据进行分析，算出登场率，场均人头，场均助攻等场均数据得到一张表，可以用该表衡量英雄各个方面的能力。

![image-20210419213229742](/home/yanruiran/.config/Typora/typora-user-images/image-20210419213229742.png)

## 数据存储：

将更改后的特征表存到exp3Data.csv中，得到的英雄数据表存到exp3ChampionData.csv中(见附带文件中的exp3ChampionData.csv文件)。

## 数据问题分析：

1. 有许多不合理的阵容存在，如有些比赛一个队有3个上路，这显然式不符合真实游戏情况的。
2. 有许多player_lane缺失的数据所有的player_role都为DUO_SUPPORT，这可能是获取的数据已经进行了填补，如再通过上述方式填补会有很多英雄的role都偏向DUO_SUPPORT，造成误差。
3. 如地图资源分析中所述，第一只先锋对游戏胜负影响最大这显然也不太符合常理，故游戏数据可能有一定偏差，如可能都是一些结束时间较早的数据。

