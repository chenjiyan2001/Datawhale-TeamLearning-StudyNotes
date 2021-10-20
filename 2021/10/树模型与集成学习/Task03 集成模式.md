# Task03 集成模式

#### 参考

- 课程链接: [DataWhale/machine-learning-toy-code](https://datawhalechina.github.io/machine-learning-toy-code/01_tree_ensemble/02_ensemble.html)
- <集成学习>: [DataWhale/EnsembleLearning](https://github.com/datawhalechina/team-learning-data-mining/tree/master/EnsembleLearning)

#### 练习

- 【练习】式子第四个等号为何成立？
  $$
  \begin{align*}
      L(\hat{f}) &= \mathbb{E}_D(y-\hat{f}_D)^2 \\
      &= \mathbb{E}_D(f+\epsilon-\hat{f}_D+\mathbb{E}_D[\hat{f}_D]-\mathbb{E}_D[\hat{f_D}])^2 \\
      &= \mathbb{E}_D[(f-\mathbb{E}_D[\hat{f}_D])+(\mathbb{E}_D[\hat{f_D}]-\hat{f_D})+\epsilon]^2 \\
      &= \mathbb{E}_D[(f-\mathbb{E}_D[\hat{f}_D]^2)+\mathbb{E}_D[(\mathbb{E}_D[\hat{f_D}]-\hat{f_D})^2]+\mathbb{E}_D[\epsilon^2] \\
      &=[f-\mathbb{E}_D[\hat{f}_D]]^2+\mathbb{E}_D[(\mathbb{E}_D[\hat{f}_D]-\hat{f}_D)^2]+\sigma^2
  \end{align*}
  $$
  **解答:**
  $$
  \mathbb{E}_D[(f-\mathbb{E}_D[\hat{f}_D])+(\mathbb{E}_D[\hat{f_D}]-\hat{f_D})+\epsilon]^2
  $$
  记$f-\mathbb{E}_D[\hat{f}_D]$为A, $\mathbb{E}_D[\hat{f}_D]-\hat{f}_D$为B, $\mathbb{E}_D[\epsilon]$为C, 展开有$A^2+B^2+C^2+2AB+2AC+2BC$

  由$\epsilon$服从$N(0, \sigma)$分布故$AC=BC=0$, 而$AB$为
  $$
  \begin{align*}
      & \mathbb{E}_D[(f-\mathbb{E}_D[\hat{f}_D])(\mathbb{E}_D[\hat{f}_D]-\hat{f}_D)] \\
      =& f\mathbb{E}_D[\hat{f}_D]-\mathbb{E}_D[\hat{f}_D]^2-f\mathbb{E}_D[\hat{f}_D]+\mathbb{E}_D[\hat{f}_D]^2 \\
      =& 0
  \end{align*}
  $$
  可以发现只留下平方项, 即
  $$
  \mathbb{E}_D[(f-\mathbb{E}_D[\hat{f}_D]^2)+\mathbb{E}_D[(\mathbb{E}_D[\hat{f_D}]-\hat{f_D})^2]+\mathbb{E}_D[\epsilon^2]
  $$
  

- 【练习】有人说[Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias–variance_tradeoff)就是指“一个模型要么具有大的偏差，要么具有大的方差”，你认为这种说法对吗？你能否对“偏差-方差权衡”现象做出更准确的表述？

  **解答:**

  不对, 偏差方差是可以权衡的, 总是存在一个偏差方差均较低情况, 此时模型的误差较小

  模型越复杂, 学习到的局部信息就越多, 相应的泛化性能就越差, 方差就越大; 模型越简单, 模型的拟合能力越弱, 偏差就越大. 对于很多模型来说, 模型的超参数就是衡量模型复杂度的方式, 通过调节超参数的过程就是控制模型复杂度的过程, 从而找到一个合适的模型, 控制偏差方差在一个较低的水平, 从而模型的误差较小. 

  

- 【练习】假设总体有100个样本，每轮利用bootstrap抽样从总体中得到10个样本（即可能重复），请求出所有样本都被至少抽出过一次的期望轮数。（通过[本文](https://en.wikipedia.org/wiki/Coupon_collector's_problem)介绍的方法，我们还能得到轮数方差的bound）

  **解答:**

  根据[Coupon collector's problem](https://en.wikipedia.org/wiki/Coupon_collector%27s_problem), 本问题的期望次数为$100*H(100)\approx519$, 即期望轮数为52轮

  

- 【练习】对于stacking和blending集成而言，若m个基模型使用k折交叉验证，此时分别需要进行几次训练和几次预测？

  **解答:**

  - blending

    训练: m+1次

    预测: 2*m+1次

  - stacking

    训练: m*k+1次

    预测: 2\*m\*k+1次

#### 准备部分

```python
from sklearn.model_selection import KFold, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

import numpy as np
import pandas as pd

m1 = KNeighborsRegressor()
m2 = DecisionTreeRegressor()
m3 = LinearRegression()

models = [m1, m2, m3]

final_model = LinearSVR()

k, m = 4, len(models)

X, y = make_regression(n_samples=1000, n_features=8, n_informative=4, random_state=0)
final_X, _ =make_regression(n_samples=500, n_features=8, n_informative=4, random_state=0)

final_train = pd.DataFrame(np.zeros(X.shape[0], m))
final_test = pd.DataFrame(np.zeros(final_X.shapehape[0], m))
```



#### blending

```python
final_train = pd.DataFrame(np.zeros((X.shape[0], m)))
final_test = pd.DataFrame(np.zeros((final_X.shape[0], m)))
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0):
for i in range(m):
    model = models[i]
    
    model.fit(X_train, y_train)
    final_train.iloc[test_idx, i] = model.predict(X_test)
    final_test.iloc[:, i] += model.predict(final_X)
final_test.iloc[:, i] /= m
    
final_model.fit(final_train, y_train)
res = final_model.predict(final_test)
print('MSE：',mean_squared_error(_, res))
print('RMSE：',np.sqrt(mean_squared_error(_, res)))
```

#### stacking

```python
final_train = pd.DataFrame(np.zeros((X.shape[0], m)))
final_test = pd.DataFrame(np.zeros((final_X.shape[0], m)))
kf = KFold(n_splits=4)
for i in range(m):
    model = models[i]
    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        model.fit(X_train, y_train)
        final_train.iloc[test_idx, i] = model.predict(X_test)
        final_test.iloc[:, i] += model.predict(final_X)
    final_test.iloc[:, i] /= k
    
final_model.fit(final_train, y)
res = final_model.predict(final_test)
print('MSE：',mean_squared_error(_, res))
print('RMSE：',np.sqrt(mean_squared_error(_, res)))
```



