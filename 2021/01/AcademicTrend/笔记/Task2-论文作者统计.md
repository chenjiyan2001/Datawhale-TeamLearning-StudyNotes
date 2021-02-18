# Task2-论文作者统计

1. str的常用方法及实例：

    详见[官方文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods)

    1. 常规

        `str.upper()`：字母转换为大写，不处理非字母，返回这个结果

        `str.lower()`：字母转换为小写，不处理非字母，返回这个结果

        ```python
        test = 'aBcD-1$'
        test.upper() # Out: 'ABCD-1$'
        test.lower() # Out: 'abcd-1$'
        test # Out: 'aBcD-1$
        ```

        `str.capitalize()`：对该字符串的首字母大写（而不是句首字母大写），返回这个结果

        ```python
        test = 'this is. #a. te$st stRi2ng '
        test.capitalize() # Out: 'This is. #a. te$st stri2ng '
        ```

        `str.startswith(str)`：判断是否以某字符串开始，返回True或False（注意是starts）

        `str.endswith(str)`：判断是否以某字符串结束，返回True或False（注意是ends）

        ```python
        test = 'this is. #a. te$st stRi2ng '
        test.startswith('this') # Out: True
        test.startswith('ths') # Out: False
        test.endswith(' ') # Out: True
        test.endswith('g') # Out: False
        ```

        `str.format()`：格式化输出，非常常用，不多说

        `str.index(str)`：返回子字符串被找到的最小索引，若没找到返回-1

        `str.find(str)`：返回子字符串被找到的最小索引，若没找到会报ValueError

        ```python
        test = 'this is. #a. te$st stRi2ng '
        test.find('2') # Out: 23
        test.find('1') # Out: -1
        test.index('2') # Out: 23
        test.index('1') # Out: ValueError: substring not found
        ```

        `str.isalnum()`：判断是否为**非符号**字符串（可以有**大小写**和**数字**，但不可以有**符号**）

        `str.isalpha()`：判断是否为**纯字母**字符串（可以有**大小写**，但不可以有**数字**和**符号**）

        `str.isdecimal()`：判断是否为**纯数字**的字符串

        `str.isdigit()`：判断是否为**纯数字**的字符串，同isdecimal

        ```python
        # 空格
        test = ' '
        test.isalnum() # Out: False
        test.isalpha() # Out: False
        test.isdecimal() # Out: False
        test.isdigit() # Out: False

        # 浮点数
        test = str(1.23)
        test.isalnum() # Out: False
        test.isalpha() # Out: False
        test.isdecimal() # Out: False
        test.isdigit() # Out: False

        # 整数
        test = str(1)
        test.isalnum() # Out: True
        test.isalpha() # Out: False
        test.isdecimal() # Out: True
        test.isdigit() # Out: True
        ```

        `str.join(str)`：把字符串（常用与列表→字符串的转换）以指定字符串进行相连

        ```python
        # string
        test = 'avn.shf-g'
        '-'.join(test) # Out: 'a-v-n-.-s-h-f---g'

        # python容器
        lst = ['213-','3','4.2','1','4']
        '-'.join(lst) # Out: '213--3-4.2-1-4'

        tup = ('213-','3','4.2','1','4')
        '-'.join(tup) # Out: '213--3-4.2-1-4'

        s = {'213-','3','4.2','1','4'}
        '-'.join(s) # Out: '4-213--4.2-1-3'(乱序)
        ```

        `str.strip()`：去除两边空格（只去**左/右**空格为**lstrip/rstrip**）

        ```python
        test = ' a vn.s hf-g '
        test.strip() # Out: 'a vn.s hf-g'
        ```

    2. 不常用（或许？）

        `str.swapcase()`：交换大小写

        `str.title()`：对字符串中所有单词首字母大写，单词中间的大写全部转换为小写

        ```python
        test = 'This-is a TEST str#ing'
        test.title() # Out: 'This-Is A Test Str#Ing'
        test.swapcase() # Out: 'tHIS-IS A test STR#ING'
        ```

        `str.center(num, sign)`：定义字符串的长度，不足长度时，两边以指定字符串进行填充

        ```python
        test = 'This-is a TEST str#ing'
        test.center(20,'*') # Out: 'This-is a TEST str#ing'
        test.center(30,'*') # Out: '****This-is a TEST str#ing****'
        test.center(31,'*') # Out: '*****This-is a TEST str#ing****'
        ```

        `str.expandtabs()`：默认开头到\t为8个字节，不足以空格填充

        ```python
        test1 = 'dark souls\tFromSoftware'
        test2 = 'wahaatyahoo\tyahoo'
        test3 = 'a\tb'
        test4 = 'cd\tefghijklmn'
        print(test1.expandtabs())
        print(test2.expandtabs())
        print(test3.expandtabs())
        print(test4.expandtabs())

        # Out
        dark souls      FromSoftware
        wahaatyahoo     yahoo
        a       b
        cd      efghijklmn
        ```

2. 列表拼接
    1. 两层列表→一层列表
        1. sum( lst , [] )：简洁但效率较低，并且要求所有元素都是list

            需要注意的是，这种方法只能实现两层列表变为一层，如果结构复杂（多层）则不能实现想要的效果，使用还是有所局限。原因是sum的start参数设为[]，sum会对该序列的所有元素视作列表，并和空列表相加

            ```python
            # sum的测试例：

            # 1：序列分别为list, tuple
            test_lst = [[1,2],[3],[4],[6]]
            test_tup = ([1,2],[3],[4],[6])
            sum(test_lst,[]) # Out: [1, 2, 3, 4, 6]
            sum(test_tup,[]) # Out: [1, 2, 3, 4, 6]

            # 2：多层嵌套
            test_lst = [[1,2],[3],[4],[5,['a',['b','c']]]]
            sum(test_lst,[]) # Out: [1, 2, 3, 4, 5, ['a', ['b', 'c']]]
            ```

        2. 循环实现：根据需要循环实现

    ```python
    test_lst = [[1,2],[3],[4],[6]]

    # 1：sum
    sum(test_lst,[]) 
    # Out: [1, 2, 3, 4, 6]

    # 2：循环
    lst = []
    for num in test_lst:
        lst += num # 这里也可以使用extend
    lst 
    # Out: [1, 2, 3, 4, 6]
    ```
