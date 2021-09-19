课程链接: [DataWhale/wonderful-sql](https://github.com/datawhalechina/wonderful-sql)

### 1 视图

视图并不是数据库真实存储的数据表，它可以看作是一个窗口，通过这个窗口我们可以看到数据库表中真实存在的数据。

#### 1.1 创建

语法:

```mysql
CREATE VIEW <视图名称>(<列名1>,<列名2>,...) AS <SELECT语句>
```

例子:

```mysql
CREATE VIEW productsum (product_type, cnt_product)
	AS
        SELECT product_type, COUNT(*)
          FROM product
         GROUP BY product_type ;
```

#### 1.2 修改

语法:

```mysql
ALTER VIEW <视图名> AS <SELECT语句>
```

例子:

```mysql
ALTER VIEW productSum
    AS
        SELECT product_type, sale_price
          FROM Product
         WHERE regist_date > '2009-09-11';
```

#### 1.3 更新

因为视图是一个虚拟表，所以对视图的操作就是对底层基础表的操作，所以在修改时只有满足底层基本表的定义才能成功修改。修改视图也会修改原表。

对于一个视图来说，如果包含以下结构的任意一种都是不可以被更新的：

- 聚合函数 SUM()、MIN()、MAX()、COUNT() 等。
- DISTINCT 关键字。
- GROUP BY 子句。
- HAVING 子句。
- UNION 或 UNION ALL 运算符。
- FROM 子句中包含多个表。

语法:

```mysql
UPDATE <视图>
   SET <列名> = <值>
 WHERE <条件表达式>;
```

#### 1.4 删除

语法:

```mysql
DROP VIEW <视图名1> [ , <视图名2> …]
```

例子:

```mysql
DROP VIEW productSum;
```

### 2 子查询

子查询指一个查询语句嵌套在另一个查询语句内部的查询。子查询也可以嵌套使用，但应当尽量避免。

例子:

```mysql
SELECT stu_name
FROM (
         SELECT stu_name, COUNT(*) AS stu_cnt
          FROM students_info
          GROUP BY stu_age) AS studentSum;
```

#### 2.1 标量子查询

执行的SQL语句只能返回一个值，也就是要返回表中具体的**某一行的某一列**。标量子查询能够使用常数或者列名的地方，无论是 WHERE子句、SELECT 子句、GROUP BY 子句、HAVING 子句，还是 ORDER BY 子句，几乎所有的地方都可以使用。

例子:

- 查询出销售单价高于平均销售单价的商品

  ```mysql
  SELECT product_id, product_name, sale_price
    FROM product
   WHERE sale_price > (SELECT AVG(sale_price) FROM product);
  ```

- 查询出平均销售价格

  ```mysql
  SELECT product_id,
         product_name,
         sale_price,
         (SELECT AVG(sale_price)
            FROM product) AS avg_price
    FROM product;
  ```

#### 2.2 关联子查询

通过WHERE语句连接两个查询

例子:

```mysql
SELECT product_type, product_name, sale_price
  FROM product AS p1
 WHERE sale_price > (SELECT AVG(sale_price)
                       FROM product AS p2
                      WHERE p1.product_type =p2.product_type
                   GROUP BY product_type);
```

### 3 函数

#### 3.1 算数函数

- ABS -- 绝对值

  语法:`ABS( 数值 ) `

  ABS 函数用于计算一个数字的绝对值，表示一个数到原点的距离。

  当 ABS 函数的参数为`NULL`时，返回值也是`NULL`。

- MOD -- 求余数

  语法：`MOD( 被除数，除数 )`

  MOD 是计算除法余数（求余）的函数，是 modulo 的缩写。小数没有余数的概念，只能对整数列求余数。

  注意：主流的 DBMS 都支持 MOD 函数，只有SQL Server 不支持该函数，其使用`%`符号来计算余数。

- ROUND -- 四舍五入

  语法：`ROUND( 对象数值，保留小数的位数 )`

  ROUND 函数用来进行四舍五入操作。

  注意：当参数 **保留小数的位数** 为变量时，可能会遇到错误，请谨慎使用变量。

#### 3.2 字符串函数

- CONCAT -- 拼接

  语法：`CONCAT(str1, str2, str3)`

  MySQL中使用 CONCAT 函数进行拼接。

- LENGTH -- 字符串长度

  语法：`LENGTH( 字符串 )`

- LOWER -- 小写转换

  LOWER 函数只能针对英文字母使用，它会将参数中的字符串全都转换为小写。该函数不适用于英文字母以外的场合，不影响原本就是小写的字符。

  类似的， UPPER 函数用于大写转换。

- REPLACE -- 字符串的替换

  语法：`REPLACE( 对象字符串，替换前的字符串，替换后的字符串 )`

- SUBSTRING -- 字符串的截取

  语法：`SUBSTRING （对象字符串 FROM 截取的起始位置 FOR 截取的字符数）`

  使用 SUBSTRING 函数 可以截取出字符串中的一部分字符串。截取的起始位置从字符串最左侧开始计算，索引值起始为1。

- SUBSTRING_INDEX -- 字符串按索引截取

  语法：`SUBSTRING_INDEX (原始字符串， 分隔符，n)`

  该函数用来获取原始字符串按照分隔符分割后，第 n 个分隔符之前（或之后）的子字符串，支持正向和反向索引，索引起始值分别为 1 和 -1。

#### 3.3 日期函数

- CURRENT_DATE -- 获取当前日期

- CURRENT_TIME -- 当前时间

- CURRENT_TIMESTAMP -- 当前日期和时间

- EXTRACT -- 截取日期元素

  语法：`EXTRACT(日期元素 FROM 日期)`

  使用 EXTRACT 函数可以截取出日期数据中的一部分，例如“年”，“月”，或者“小时”“秒”等。该函数的返回值并不是日期类型而是数值类型

  例子:

  ```mysql
  SELECT CURRENT_TIMESTAMP as now,
  EXTRACT(YEAR   FROM CURRENT_TIMESTAMP) AS year;
  ```

#### 3.4 转换函数

- CAST -- 类型转换

  语法：`CAST（转换前的值 AS 想要转换的数据类型）`

  例子:

  ```mysql
  SELECT CAST('0001' AS SIGNED INTEGER) AS int_col;
  ```

  

- COALESCE -- 将NULL转换为其他值

  语法：`COALESCE(数据1，数据2，数据3……)`

  COALESCE 是 SQL 特有的函数。该函数会返回可变参数 A 中左侧开始第 1个不是NULL的值。参数个数是可变的，因此可以根据需要无限增加。

  在 SQL 语句中将 NULL 转换为其他值时就会用到转换函数。

  ```mysql
  SELECT COALESCE(NULL, 11) AS col_1,
  COALESCE(NULL, 'hello world', NULL) AS col_2,
  COALESCE(NULL, NULL, '2020-11-01') AS col_3;
  +-------+-------------+------------+
  | col_1 | col_2       | col_3      |
  +-------+-------------+------------+
  |    11 | hello world | 2020-11-01 |
  +-------+-------------+------------+
  1 row in set (0.00 sec)
  ```

### 4 谓词

谓词就是返回值为真值的函数。包括`TRUE / FALSE / UNKNOWN`。

谓词主要有以下几个：

- LIKE
- BETWEEN
- IS NULL、IS NOT NULL
- IN
- EXISTS

#### 4.1 LIKE

当需要进行字符串的部分一致查询时需要使用该谓词。

部分一致大体可以分为前方一致、中间一致和后方一致三种类型。

语法:

```
<列名> LIKE <字符串>;
```

例子:

```mysql
-- 中间一致, %代表零或多个任意字符, _代表一个任意字符
SELECT *
FROM samplelike
WHERE strcol LIKE '%ddd%';
```

#### 4.2 BETWEEN

BETWEEN的结果包含上下界，也就是闭区间。开区间使用<和>。

语法:

```mysql
<列名> BETWEEN <下界> AND <上界>;
```

#### 4.3 IS NULL、IS NOT NULL

用于判断是否为NULL。

#### 4.4 IN

语法:

```mysql
<列名> IN <值1, 值2,...>
```

例子:

- 常规用法

  ```mysql
  SELECT product_name, purchase_price
  FROM product
  WHERE purchase_price IN (320, 500, 5000);
  ```

- 子查询作为参数

  ```mysql
  SELECT product_name, sale_price
    FROM product
   WHERE product_id NOT IN (SELECT product_id
                              FROM shopproduct
                             WHERE shop_id = '000A');
  ```

#### 4.5 EXIST

判断是否存在某种条件的记录，并返回这些记录。一般右接子查询。

例子:

```mysql
SELECT product_name, sale_price
  FROM product AS p
 WHERE EXISTS (SELECT * -- 无论为何都不会影响结果
                 FROM shopproduct AS sp
                WHERE sp.shop_id = '000C'
                  AND sp.product_id = p.product_id);
```

### 5 CASE

语法:

```mysql
CASE WHEN <求值表达式> THEN <表达式>
     WHEN <求值表达式> THEN <表达式>
     WHEN <求值表达式> THEN <表达式>
     .
     .
     .
ELSE <表达式>
END  
```

例子:

- **应用场景1：根据不同分支得到不同列值**

  ```mysql
  SELECT  product_name,
          CASE WHEN product_type = '衣服' THEN CONCAT('A ： ',product_type)
               WHEN product_type = '办公用品'  THEN CONCAT('B ： ',product_type)
               WHEN product_type = '厨房用具'  THEN CONCAT('C ： ',product_type)
               ELSE NULL
          END AS abc_product_type
    FROM  product;
  ```

- **应用场景2：实现列方向上的聚合**

  ```mysql
  -- 对按照商品种类计算出的销售单价合计值进行行列转换
  SELECT SUM(CASE WHEN product_type = '衣服' THEN sale_price ELSE 0 END) AS sum_price_clothes,
         SUM(CASE WHEN product_type = '厨房用具' THEN sale_price ELSE 0 END) AS sum_price_kitchen,
         SUM(CASE WHEN product_type = '办公用品' THEN sale_price ELSE 0 END) AS sum_price_office
    FROM product;
  ```

### 练习题

1. 创建出满足下述三个条件的视图（视图名称为 ViewPractice5_1）。使用 product（商品）表作为参照表，假设表中包含初始状态的 8 行数据。

   - 条件 1：销售单价大于等于 1000 日元。

   - 条件 2：登记日期是 2009 年 9 月 20 日。
   - 条件 3：包含商品名称、销售单价和登记日期三列。

   对该视图执行 SELECT 语句的结果如下所示。

   ```MYSQL
   SELECT * FROM ViewPractice5_1;
   ```

   执行结果

   ```MYSQL
   product_name | sale_price | regist_date
   --------------+------------+------------
   T恤衫         | 　 1000    | 2009-09-20
   菜刀          |    3000    | 2009-09-20
   ```

   ```mysql
   -- t1代码
   CREATE VIEW  ViewPractice5_1 (product_name, sale_price, regist_date)
   	AS
   		SELECT product_name, sale_price, regist_date
   		FROM 	product
   		WHERE regist_date = '2009-09-20' AND sale_price>=1000;
   ```

2. 向习题一中创建的视图 ViewPractice5_1 中插入如下数据，会得到什么样的结果呢？

   ```mysql
   INSERT INTO ViewPractice5_1 VALUES (' 刀子 ', 300, '2009-11-02');
   ```

   会报错: Field of view 'shop.viewpractice5_1' underlying table doesn't have a default value.

   原因是向视图中插入数据时，也会向原表插入数据，但原表有多个字段不允许为空，因此无法插入。

3. 请根据如下结果编写 SELECT 语句，其中 sale_price_all 列为全部商品的平均销售单价。

   ```mysql
   product_id | product_name | product_type | sale_price | sale_price_all
   ------------+-------------+--------------+------------+---------------------
   0001       | T恤衫         | 衣服         | 1000       | 2097.5000000000000000
   0002       | 打孔器        | 办公用品      | 500        | 2097.5000000000000000
   0003       | 运动T恤       | 衣服          | 4000      | 2097.5000000000000000
   0004       | 菜刀          | 厨房用具      | 3000       | 2097.5000000000000000
   0005       | 高压锅        | 厨房用具      | 6800       | 2097.5000000000000000
   0006       | 叉子          | 厨房用具      | 500        | 2097.5000000000000000
   0007       | 擦菜板        | 厨房用具       | 880       | 2097.5000000000000000
   0008       | 圆珠笔        | 办公用品       | 100       | 2097.5000000000000000
   ```

   ```mysql
   -- t3代码
   SELECT product_id, product_name, product_type, sale_price, 
   (SELECT AVG(sale_price) AS sale_price_all FROM product)
   FROM product
   ```

4. 请根据习题一中的条件编写一条 SQL 语句，创建一幅包含如下数据的视图（名称为AvgPriceByType）

   ```mysql
   product_id | product_name | product_type | sale_price | avg_sale_price
   ------------+-------------+--------------+------------+---------------------
   0001       | T恤衫         | 衣服         | 1000       |2500.0000000000000000
   0002       | 打孔器         | 办公用品     | 500        | 300.0000000000000000
   0003       | 运动T恤        | 衣服        | 4000        |2500.0000000000000000
   0004       | 菜刀          | 厨房用具      | 3000        |2795.0000000000000000
   0005       | 高压锅         | 厨房用具     | 6800        |2795.0000000000000000
   0006       | 叉子          | 厨房用具      | 500         |2795.0000000000000000
   0007       | 擦菜板         | 厨房用具     | 880         |2795.0000000000000000
   0008       | 圆珠笔         | 办公用品     | 100         | 300.0000000000000000
   ```

   提示：其中的关键是 avg_sale_price 列。与习题三不同，这里需要计算出的 是各商品种类的平均销售单价。这与使用关联子查询所得到的结果相同。 也就是说，该列可以使用关联子查询进行创建。问题就是应该在什么地方使用这个关联子查询。

   ```mysql
   -- t4代码
   CREATE VIEW AvgPriceByType
   	AS 
   		SELECT product_id, product_name, product_type, sale_price, 
   					(SELECT	AVG(sale_price) 
   					FROM product AS p2 
   					WHERE p1.product_type = p2.product_type 
   					GROUP BY p1.product_type) AS avg_sale_price 
   		FROM product AS p1;
   ```

5. 运算或者函数中含有 NULL 时，结果全都会变为NULL ？（判断题）

   谓词函数的结果不会变为NULL。

6. 对本章中使用的 product（商品）表执行如下 2 条 SELECT 语句，能够得到什么样的结果呢？

   ①

   ```mysql
   SELECT product_name, purchase_price
     FROM product
    WHERE purchase_price NOT IN (500, 2800, 5000);
   ```

   ②

   ```mysql
   SELECT product_name, purchase_price
     FROM product
    WHERE purchase_price NOT IN (500, 2800, 5000, NULL);
   ```

   ①

   ```
   -- 结果
   prouduct_name	purchase_price
   打孔器	          320
   擦菜板	          790
   ```

   ②

   ```mysql
   prouduct_name	purchase_price
   NULL            NULL
   ```

7. 按照销售单价（ sale_price）对练习 3.6 中的 product（商品）表中的商品进行如下分类。

   - 低档商品：销售单价在1000日元以下（T恤衫、办公用品、叉子、擦菜板、 圆珠笔）
   - 中档商品：销售单价在1001日元以上3000日元以下（菜刀）
   - 高档商品：销售单价在3001日元以上（运动T恤、高压锅）

   请编写出统计上述商品种类中所包含的商品数量的 SELECT 语句，结果如下所示。

   执行结果

   ```mysql
   low_price | mid_price | high_price
   ----------+-----------+------------
           5 |         1 |         2
   ```

   ```mysql
   -- t7代码
   SELECT
   	SUM( CASE WHEN sale_price <= 1000 THEN 1 ELSE 0 END) AS low_price,
   	SUM( CASE WHEN sale_price BETWEEN 1001 AND 3000 THEN 1 ELSE 0 END) AS mid_price,
   	SUM( CASE WHEN sale_price >= 3001 THEN 1 ELSE 0 END) AS high_price 
   FROM
   	product;
   ```

   
