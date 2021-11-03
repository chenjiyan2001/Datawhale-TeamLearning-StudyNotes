# Task 06 梯度提升树(上)

### 相关资料

- 课程链接: [DataWhale/machine-learning-toy-code/Part D: 梯度提升树](https://datawhalechina.github.io/machine-learning-toy-code/01_tree_ensemble/04_gbdt.html)

- 视频链接 1: [集成学习：从原理到实现/P8 梯度提升树(上)](https://www.bilibili.com/video/BV1wF411e73j?p=8)
- 视频链接 2: [集成学习：从原理到实现/P8 梯度提升树(中)](https://www.bilibili.com/video/BV1wF411e73j?p=9)

### 练习

- 【练习】对于均方损失函数和绝对值损失函数，请分别求出模型的初始预测$F_0$。

  **解答:** 

  MSE: $F_0=[Mean(y),...Mean(y)]$

  MAE: $F_0=[Median(y),...Median(y)]$ (视频里这样说, 但不是很理解...)

  

- 【练习】给定了上一轮的预测结果$F_{m−1}(X_i)$和样本标签$y_i$，请计算使用平方损失时需要拟合的$w^∗_i$。

  **解答:** 

  $w^*_i=arg\min MSE(y_i, F_{m-1}(X_i)+w^*_i)$

  

- 【练习】当样本$i$计算得到的残差$r_i=0$时，本例中的函数在$w=0$处不可导，请问当前轮应当如何处理模型输出？

  **解答:** 

  残差为0时有$y_i=F_{m-1}(X_i)$, 也就不用继续拟合损失, 令$w_i^*$为0

  

- 【练习】除了梯度下降法之外，还可以使用[牛顿法](https://en.wikipedia.org/wiki/Newton's_method_in_optimization)来逼近最值点。请叙述基于牛顿法的GBDT回归算法。

  **解答:** 

  梯度下降法的学习率是超参数, 牛顿法的学习率是计算求得的参数, 其他都一致.

  牛顿法的迭代$F_m=F_{m-1}+w^*_i*$, 其中为$L$在$w=F_{m-1}(X_i)$处的二阶导

  

- 【练习】请验证多分类负梯度的结果。

  **解答:** 

  

- 【练习】请验证二分类负梯度的结果。

  **解答:** 

  

- 【练习】设二分类数据集中正样本比例为10%，请计算模型的初始参数$F(0)$。

  **解答:** 

  即$[p_0,p_1]=[0.1,0.9]$, 由$[\frac{1}{1+e^{F_{i}^{(0)}}}, \frac{e^{F_i^{(0)}}}{1+e^{F_i^{(0)}}}]$可计算得$F_i^{(0)}=-log9$

#### 代码实现

- GBDTRegressor: 见[这里](./codes/GBDTRegressor.py)
- GBDTClassifier: 见[这里](./codes/GBDTClassifier.py)