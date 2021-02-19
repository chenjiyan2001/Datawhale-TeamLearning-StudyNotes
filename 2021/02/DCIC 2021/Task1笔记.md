# Copy of Task1-早高峰共享单车潮汐点的群智优化Baseline

1. 下载库
    - geohash

        直接使用pip install geohash会遇到安装成功但调用失败的问题。正确方式为：

        ```bash
        pip install python-geohash
        ```

    - geopy

        安装方式为：

        ```bash
        pip install geopy
        ```

    - hnswlib

        安装方式为：

        ```bash
        pip install hnswlib
        ```

2. Baseline代码分析：
    1. 函数bike_fence_format：

        转换FENCE_LOC字段的格式，由五个列表合并为一个array。方便后续得到每个区域的经纬度范围（使用np.min/np.max可以直接得到，而不用使用复杂的方式）

    2. geohash编码：

        geohash.encode将二维的经纬度转换成字符串，每个字符串代表一个矩形区域。字符串越长对应的区域越精确。

        这么做是为了解决任务一中识别出潮汐现象最突出的40个区域这个任务

    3. 取中心点FENCE_CENTER：

        由于数据中一个封闭区域由五个经纬度（起点和终点相同）来表示，中心点为四个不重复点的平均值。使用np.mean(axis=0)来得到经纬度的平均值。

    4. 使用pad对日期进行补位：

        使用pad将仅有个位数的日期进行补位，如：1→01

    5. 经纬度聚合

        baseline里做了时间-锁状态的数据透视表，我依据此表绘制了热图，可以发现时间上的一些特征和地理上的一些特征，或许之后会对数据的宏观理解有一定帮助。另外基于此表应该也可以做一些分析。baseline对这些数据是取了两个个区域做plot，不知道这两个区域是不是经过选取有代表性的。

        ![Image/bike_inflow_DH_log2.jpg)

        ![Image/bike_outflow_DH_log2.jpg)

        ![Image/bike_inflow_D_log2.jpg)

        ![Image/bike_outflow_D_log2.jpg)

    6. 关于DENSITY

        关于DENSITY的含义还不是特别理解，疑问主要是在map上。该部分内容隔天更新。

    7. 关于hnswlib

        当前还未花时间学习该部分内容，隔天更新。