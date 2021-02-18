# Task1-论文数据统计

1. **Python文件读写**：

    使用内置函数open**打开文件**，返回一个**文件对象（file对象）**

    使用格式：var = open( [path] [ , [model] ] )

    其中model为可选项，默认为'r'，即**只读**

    如果路径对应的文件不存在，会报IOError，提示文件不存在

    [open的model选项](https://www.notion.so/d9ebf348cbc441b4af8136769165d6c3)

    file 对象方法：

    - **file.read([size])**：size 未指定则返回整个文件，如果文件大小 >2 倍内存则有问题，f.read()读到文件尾时返回""(空字串)。
    - **file.readline()**：返回一行。
    - **file.readlines([size])**：返回包含size行的列表, size 未指定则返回全部行。
    - **for line in f: print line** ：通过迭代器访问。
    - **f.write("hello\n")**：如果要写入字符串以外的数据,先将他转换为字符串。
    - **f.tell()**：返回一个整数,表示当前文件指针的位置(就是到文件头的字节数)。
    - **f.seek(偏移量,[起始位置])**：用来移动文件指针。
        - 偏移量: 单位为字节，可正可负
        - 起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
    - **f.close()** 关闭文件

    with as 语句：

    - 工作原理：with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
    - 过程：紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
    - 读文件使用：with open([path],[model]) as [var]:    [code block]
    - 例子：

    ```python
    data  = [] 
    with open(r'path', 'r') as f:
        for idx,line in enumerate(f):
            if idx>=500000:# limit number
                break
            data.append(json.loads(line))
    ```

    - 注意：with as语句结束自动关闭文件对象（f.close()，此时将修改后的文件保存），不可在with外调用文件对象

    python写文件：

    调用方法f.write()进行写文件，若open()时使用的模式为只读，将被禁止写入。

2. **字典推导式：**

    格式：{ [键表达式] : [值表达式] for [循环语句] }

    例子：

    1. 键值互换

        ```python
        mcase = {'a': 10, 'b': 34}
        mcase_frequency = {v: k for k, v in mcase.items()}
        print mcase_frequency
        # Output: {10: 'a', 34: 'b'}
        ```

    2. 大小写合并

        ```python
        mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
        mcase_frequency = {
          k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
          for k in mcase.keys()
          if k.lower() in ['a','b']
        }
        print mcase_frequency
        # Output: {'a': 17, 'b': 34}
        ```

3. **Pandas的dt接口：**

    参考：[Pandas中文文档](https://www.pypandas.cn/docs/getting_started/basics.html#dt-%E8%AE%BF%E9%97%AE%E5%99%A8)

    `Series` 提供一个可以简单、快捷地返回 `datetime` 属性值的访问器。这个访问器返回的也是 `Series`，索引与现有的 `Series` 一样。

    一些使用例：

    默认创建了一个Series如下：

    ```python
    s = pd.Series(pd.date_range('20130101 09:10:12', periods=4))
    ```

    1. 获取datetime的年/月/天/时/分/秒/周次/周几（返回一个Series）：

        ```python
        s.dt.year # 年
        s.dt.month # 月
        s.dt.day # 天
        s.dt.hour # 时
        s.dt.mintue # 分
        s.dt.second # 秒 
        s.dt.week # 周次
        s.dt.weekday # 周几
        ```

    2. 时区转换：

        ```python
        stz = s.dt.tz_localize('US/Eastern')
        ```

    3. 还可以用 Series.dt.strftime() 把 datetime 的值当成字符串进行格式化，支持与标准 strftime() 同样的格式。

        ```python
        In [275]: s
        Out[275]: 
        0   2013-01-01
        1   2013-01-02
        2   2013-01-03
        3   2013-01-04
        dtype: datetime64[ns]

        In [276]: s.dt.strftime('%Y/%m/%d')
        Out[276]: 
        0    2013/01/01
        1    2013/01/02
        2    2013/01/03
        3    2013/01/04
        dtype: object
        ```

    - **注意**:用这个访问器处理不是 `datetime` 类型的值时，`Series.dt` 会触发 `TypeError` 错误。
