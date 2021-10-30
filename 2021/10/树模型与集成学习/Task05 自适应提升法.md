# Task05自适应提升法

#### 相关资料

- 课程链接: [DataWhale/machine-learning-toy-code/Part C](https://datawhalechina.github.io/machine-learning-toy-code/01_tree_ensemble/03_ada.html#)
- 视频链接(上): https://pan.baidu.com/s/1XC7p314-OsvJEWRAJF7ycA 提取码: 8rdn
- 视频链接(下): https://pan.baidu.com/s/16J5jjDxxVP_uSCv1UETosg 提取码:vkix
- [【机器学习】Adaboost多类分类——SAMME算法，SAMME.R算法 - 为什么昵称不能重复](https://blog.csdn.net/weixin_43298886/article/details/110927084)
- [手写adaboost的分类算法—SAMME算法 - 马东什么](https://zhuanlan.zhihu.com/p/82568979)
- [集成学习之Adaboost算法原理小结 - 刘建平Pinard](https://www.cnblogs.com/pinard/p/6133937.html)
- [scikit-learn AdaBoost](https://github.com/scikit-learn/scikit-learn/blob/0d378913b/sklearn/ensemble/_weight_boosting.py#L313)
- [Multi-class AdaBoost](https://web.stanford.edu/~hastie/Papers/samme.pdf)

#### 练习

- 【练习】假设有一个3分类问题，标签类别为第2类，模型输出的类别标签为[-0.1,-0.3,0.4]，请计算对应的指数损失。

  **解答:** 
  $$
  \begin{align*}
  L(y,f) & = exp(-\frac{y^Tf}{K}) \\
  & = exp(-\frac{[-\frac{1}{2},1,-\frac{1}{2}]*[-0.1,-0.3,0.4]^T}{3}) \\
  & = exp(-\frac{3}{20}) \\
  & \approx{1.16}
  \end{align*}
  $$
  

- 【练习】左侧公式的第二个等号是由于当样本分类正确时，$y^Tb=\frac{K}{K−1}$，当样本分类错误时，$y^Tb=−\frac{K}{(K−1)2}$，请说明原因。

  **解答:** 

  - 分类正确:

    假设为第1类, 有$y=b=[1,-\frac{1}{K-1},,-\frac{1}{K-1}...]$

    故$y^Tb=1+\sum_2^K{\frac{1}{(K-1)^2}}=\frac{K}{K-1}$

  - 分类错误:

    假设为第1类, 有$y=[1,-\frac{1}{K-1},,-\frac{1}{K-1}...]$, $b=[-\frac{1}{K-1},...,1,-\frac{1}{K-1},...]$

    故$y^Tb=-\frac{2}{K-2}+\sum_3^K{\frac{1}{(K-1)^2}}=\frac{K}{(K-1)^2}$

    

- 【练习】对公式进行化简，写出$K=2$时的SAMME算法流程，并与李航《统计学习方法》一书中所述的Adaboost二分类算法对比是否一致。

  **解答:** 

  只有第7行不同:
  $$
  \beta^{*(m)}\gets\frac{1}{2}log\frac{1-err^{(m)}}{err^{(m)}}
  $$
  

- 【练习】在sklearn源码中找出算法流程中每一行对应的处理代码。

  **解答:** 

  与函数[_boost_discrete](https://github.com/scikit-learn/scikit-learn/blob/0d378913b/sklearn/ensemble/_weight_boosting.py#L612)对应



- 【练习】算法2第12行中给出了$f$输出的迭代方案，但在sklearn包的实现中使用了$I_{\{G^∗(x)=S(y)\}}$来代替$b^{∗(m)}(x)$。请根据本文的实现，对sklearn包的源码进行修改并构造一个例子来比较它们的输出是否会不同。（提示：修改AdaboostClassifier类中的decision_function函数和staged_decision_function函数）

  **解答:** 

  sklearn的实现:

  ```python
  sample_weight = np.exp(
                  np.log(sample_weight)
                  + estimator_weight * incorrect * (sample_weight > 0)
              )
  ```

  修改:

  ```python
  sample_weight += [1 if y_predict[i] == y[i] else -1/(n_classes-1) for i in range(len(y))]*estimator_weight
  ```

  

- 【练习】请说明左式第三个等号为何成立。

  **解答:** 

  

- 【练习】验证$h^∗_{k′}$的求解结果。

  **解答:** 

  

- 【练习】算法3的第14行给出了$w_i$的更新策略，请说明其合理性。

  **解答:** 

  

- 【练习】请结合加权中位数的定义解决以下问题：

  - 当满足什么条件时，Adaboost.R2的输出结果恰为每个基预测器输出值的中位数？
  - Adaboost.R2模型对测试样本的预测输出值是否一定会属于MM个分类器中的一个输出结果？若是请说明理由，若不一定请给出反例。
  - 设k∈{y1,...,yM}k∈{y1,...,yM}，记kk两侧（即大于或小于kk）的样本集合对应的权重集合为W+W+和W−W−，证明使这两个集合元素之和差值最小的kk就是Adaboost.R2输出的yy。
  - 相对于普通中位数，加权中位数的输出结果鲁棒性更强，请结合公式说明理由。

  **解答:** 

  

#### 知识回顾

1. 二分类问题下，Adaboost算法如何调节样本的权重？

   **解答:** 

   

2. 样本A在当轮分类错误，且样本B在当轮分类正确，请问在权重调整后，样本A的权重一定大于样本B吗？

   **解答:** 

   是的

   

3. 在处理分类问题时，Adaboost的损失函数是什么？请叙述其设计的合理性。

   **解答:** 

   $L(y,f) = exp(-\frac{y^Tf}{K})$

   由于当且仅当y与f一致时损失最小, 因此可做为损失函数. 另外指数形式适合公式推导

   

4. Adaboost如何处理回归问题？

   **解答:** 

   使用Adaboos.R2算法，采用加权中位数作为输出值。

   

5. 用已训练的Adaboost分类模型和回归模型来预测新样本的标签，请分别具体描述样本从输入到标签输出的流程。

   **解答:** 

   

   

6. 观看周志华老师的讲座视频[《Boosting 25年》](https://www.bilibili.com/video/BV1Cs411c7Zt)并谈谈体会。

   **解答:** 

   还没看

   

#### 代码实现

- SAMME: 见[这里](./codes/SAMME_and_SAMME_R.py)
- SAMME.R: 见[这里](./codes/SAMME_and_SAMME_R.py)