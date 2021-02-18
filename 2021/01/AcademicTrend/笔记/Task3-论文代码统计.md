# Task3-论文代码统计

1. pandas修改数据时要注意的问题

    参考文章：[https://zhuanlan.zhihu.com/p/41202576](https://zhuanlan.zhihu.com/p/41202576)

    更新变量的值时，一般我们习惯直接将新值直接赋值给变量，但如果我们在pandas里的DataFrame直接更新，会警告：

    ```markdown
    SettingWithCopyWarning:value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    ```

    警告提示你：你的操作可能没有按预期运行，需要检查结果以确保没有出错。

    先说解决方法：

    1. 如果要更改原始数据，请使用单一赋值操作（loc）：

        ```python
        data.loc[data.bidder == 'parakeet2004', 'bidderrate'] = 100
        ```

    2. 如果想要一个副本，请确保强制让 Pandas 创建副本：

        ```python
        winners = data.loc[data.bid == data.price].copy()
        winners.loc[304, 'bidder'] = 'therealname'
        ```

    3. 关闭警告（不推荐）：

        ```python
        pd.set_option('mode.chained_assignment', None)
        ```

    出现问题的原因：Pandas 中的某些操作会返回数据的视图（View），某些操作会返回数据的副本（Copy）

    具体例子及解释：

    ```python
    # 报SettingWithCopyWarning

    # 第1种情况：可能会造成没有实际修改数据
    data[data.bidder == 'parakeet2004']['bidderrate'] = 100
    # 因为data[data.bidder == 'parakeet2004']步骤是返回数据的Copy，而非View，因此修改操作不是原地进行，修改的内容并没有实际修改到数据上

    # 解决方法：使用.loc
    data.loc[data.bidder == 'parakeet2004', 'bidderrate'] = 100

    # 第2种情况：修改的DataFrame会引起其他DataFrame的变化
    winners = data.loc[data.bid == data.price] # 这相当于“引用”，在winners上的修改会同步到data上
    winners.loc[304, 'bidder'] = 'therealname'

    # 解决方法：创建winners时使用data的副本
    winners =  data.loc[data.bid == data.price].copy()
    ```

2. 正则表达式（re.findall 和 Series.str.findall）

    这里不多说明正则表达式的语法，组队学习上有较详细的介绍，语法上更深入的部分可参考↓↓

    参考文章：

    [简要][https://docs.python.org/zh-cn/3/library/re.html?highlight=正则表达式](https://docs.python.org/zh-cn/3/library/re.html?highlight=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F)

    [详细][https://docs.python.org/zh-cn/3/howto/regex.html#regex-howto](https://docs.python.org/zh-cn/3/howto/regex.html#regex-howto)

    这里主要说明re里的re.findall和Pandas里的Series.str.findall：

    `re.findall(pattern, string, flags=0)`

    - **pattern**：正则表达式
    - **string**：需要处理的字符串
    - **flags**：说明匹配模式，如是否大小写re.I

    `Series.str.findall(pat, flags=0)`

    - **pat**：要搜索的子字符串
    - **flags**：可以传递的正则表达式标志(A，S，L，M，I，X)，默认值为0，表示无。对于此正则表达式模块(re)也必须导入。

3. Series.plot常用参数

    `Series.plot(kind='line', figsize=None, title=None, grid=None, legend=False, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, label=None)`

    1. kind：
        - ‘line’:默认值。线性图
        - ‘bar’：垂直条形图
        - ‘barh’：水平条形图
        - ‘hist’：柱状图
        - ‘box’：box plot
        - ‘kde’：核密度估计Kernel Density Estimation(KDE)
        - ‘density’：和’kde’相同
        - ‘area’：面积图
        - ‘pie’：饼图
    2. figsize：图片尺寸。参数类型为一个元组 (width, height)，单位为英寸
    3. fontsize：字体大小
    4. title：图表的标题
    5. grid：是否显示网格（boolean）
    6. legend：是否在图上显示坐标轴说明（False/True/’reverse’）
    7. style：对应matplotlib里的style
    8. logx / logy / loglog：对坐标轴取对数（x：x轴 / y：y轴 / loglog：同时）
    9. xticks / yticks：同matplotlib
    10. xlim / ylim：同matplotlib
    11. rot：rotation，旋转角度（int）
    12. colormap：cmap，渐变色的模式，见matplotlib
